---
name: pptx-study-framework
description: Extract and reorganize one or more course PPTX files into a progressive study framework, mind-map style outline, and review checklist. Use when the user wants to fully sort lecture slides, generate a learning path, convert PPT content into structured notes, or produce a study framework from PPTX files.
---

# PPTX Study Framework

Use this skill when the user provides one or more `pptx` lecture files and wants:

- a complete knowledge整理
- a递进式学习框架
- a思维导图式大纲
- a复习提纲 / 自测清单
- multiple PPTs merged into one coherent study path

## Goal

Turn raw PPTX slides into a clean learning artifact that is easier to study than the original deck order.

Preferred outputs:

- one Markdown study framework file
- optionally a mind-map style structure
- optionally derived HTML or other presentation formats if the user asks

## Teaching style

This skill should explain like a strong tutor, not like a passive summarizer.

For each important concept, prefer adding:

- one直观例子
- one容易混淆的反例 or 非例
- one最小题型示范 if the PPT content supports it

When the user wants to “彻底学会”, prioritize explanation quality over compression. The output should help the learner understand why a definition is introduced, what problem it solves, and how it is used in typical exercises.

## Workflow

1. Confirm the PPTX paths exist.
2. If paths contain non-ASCII characters and the shell encoding is unreliable, copy them to temporary ASCII filenames inside the workspace.
3. Run `scripts/extract_pptx_text.py` on the working copies to extract slide text.
4. Rebuild the content by knowledge dependency, not by slide order.
5. Organize the final output into this shape:
   - scope and source files
   - one total knowledge map
   - layered learning order
   - core definitions and theorems
   - intuitive examples and counterexamples
   - typical problem patterns
   - review checklist
   - suggested study schedule if useful
6. Save the final artifact in the user workspace unless they specify a different destination.

## Output rules

- Prefer Chinese if the source courseware is Chinese.
- Do not just summarize slide-by-slide.
- Merge repeated content across multiple decks.
- Make the structure progressively layered: concept -> property -> theorem -> example -> problem type.
- Surface prerequisite relations explicitly.
- For abstract algebra topics, explain with concrete examples whenever possible.
- If a concept is easy to confuse, add one counterexample or a “why this is not enough” note.
- If a theorem is used for solving problems, add a short “how to use it in questions” hint.
- If examples in the PPT are partial or formula-heavy, keep the framework stable and avoid inventing unsupported details.

## Extraction

Use the bundled script for deterministic PPTX text extraction:

`python scripts/extract_pptx_text.py <pptx1> <pptx2> ...`

The script prints Markdown with:

- file heading
- slide number
- detected title
- body blocks

If needed, redirect output to a temporary `.md` file and then rewrite it into the final study framework.

## When to create a mind-map style result

If the user asks for:

- 思维导图
- 知识树
- 学习路线图

then include a top-level tree structure. Markdown headings are usually enough. If the environment supports Mermaid and the user would benefit, include one concise Mermaid flowchart near the top.

## Practical notes

- For finite decks, extracted text is often noisy. Clean OCR-like spacing and repeated footers mentally before reorganizing.
- Repeated chapter review pages should be merged into the final checklist rather than preserved as standalone sections.
- Mathematical symbols may not extract perfectly; preserve only what is clear from context.

## Typical user requests this skill should handle

- “完整梳理这几个 PPT，生成学习框架”
- “把这门课的 PPT 整理成思维导图”
- “按从基础到提高的顺序重组这个课件”
- “合并多个章节 PPT，生成复习总纲”
