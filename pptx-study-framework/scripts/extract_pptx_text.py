from __future__ import annotations

import argparse
import sys
import zipfile
from pathlib import Path
import xml.etree.ElementTree as ET


NS = {
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
}


def normalize_text(text: str) -> str:
    return " ".join((text or "").split())


def get_slide_parts(zf: zipfile.ZipFile) -> list[str]:
    rels_root = ET.fromstring(zf.read("ppt/_rels/presentation.xml.rels"))
    rels: dict[str, str] = {}
    for rel in rels_root:
        rid = rel.attrib.get("Id")
        target = rel.attrib.get("Target")
        if rid and target:
            rels[rid] = "ppt/" + target.lstrip("/")

    pres_root = ET.fromstring(zf.read("ppt/presentation.xml"))
    sld_id_list = pres_root.find("p:sldIdLst", NS)
    if sld_id_list is None:
        return []

    parts: list[str] = []
    for sld in sld_id_list:
        rid = sld.attrib.get(f"{{{NS['r']}}}id")
        if rid in rels:
            parts.append(rels[rid])
    return parts


def extract_slide(zf: zipfile.ZipFile, part: str) -> tuple[list[str], list[str]]:
    root = ET.fromstring(zf.read(part))
    titles: list[str] = []
    bodies: list[str] = []

    for shape in root.findall(".//p:sp", NS):
        placeholder = shape.find(".//p:ph", NS)
        placeholder_type = placeholder.attrib.get("type") if placeholder is not None else ""
        texts = [normalize_text(t.text or "") for t in shape.findall(".//a:t", NS)]
        texts = [t for t in texts if t]
        if not texts:
            continue
        joined = " ".join(texts)
        if placeholder_type in ("title", "ctrTitle"):
            titles.append(joined)
        else:
            bodies.append(joined)

    return titles, bodies


def render_file(path: Path) -> str:
    lines: list[str] = [f"# {path.name}", ""]
    with zipfile.ZipFile(path) as zf:
        for index, part in enumerate(get_slide_parts(zf), start=1):
            titles, bodies = extract_slide(zf, part)
            lines.append(f"## Slide {index}")
            if titles:
                lines.append(f"- Title: {' | '.join(titles)}")
            else:
                lines.append("- Title: (none)")

            if bodies:
                for body in bodies:
                    lines.append(f"- Body: {body}")
            else:
                lines.append("- Body: (none)")
            lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Extract slide titles and text blocks from PPTX files into Markdown."
    )
    parser.add_argument("pptx", nargs="+", help="One or more PPTX files")
    args = parser.parse_args()

    outputs: list[str] = []
    for raw_path in args.pptx:
        path = Path(raw_path)
        if not path.exists():
            print(f"[error] file not found: {path}", file=sys.stderr)
            return 1
        outputs.append(render_file(path))

    sys.stdout.write("\n\n".join(outputs))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
