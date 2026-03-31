---
name: personal-output-defaults
description: Use when the user wants their personal default file handling preferences applied or remembered, especially default output directories, whether to keep only final files, cleanup behavior for temporary files, and similar persistent workflow defaults.
---

# Personal Output Defaults

Use this skill when the user asks to preserve or apply personal default file-output preferences across tasks.

Current defaults for this user:

- Default output directory: `D:\study`
- Final generated artifacts should be kept in `D:\study`
- Do not leave duplicate result files in `C:`
- If temporary files must be created in the workspace to complete the task, remove them after the final `D:\study` copies are confirmed
- If a task would normally save elsewhere, prefer `D:\study` unless the user explicitly overrides the destination

## Workflow

1. Before generating files, treat `D:\study` as the default destination.
2. Create `D:\study` if needed.
3. If sandbox or tool constraints require a temporary local workspace file, use it only as an intermediate step.
4. After the final file is successfully written to `D:\study`, clean up temporary or duplicate copies from `C:` when safe.
5. If deletion would remove user-authored content or there is ambiguity about whether a file is temporary, ask before deleting.

## Output policy

- Prefer writing final deliverables directly into `D:\study`.
- If both an extracted intermediate file and a final polished file are produced, both may live in `D:\study`.
- Avoid creating extra copies outside `D:\study`.
- When reporting paths back to the user, prefer the `D:\study` paths.

## Override rule

If the user gives a different destination in the current task, that explicit instruction overrides this skill.
