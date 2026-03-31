---
name: codex-cli-commands
description: Explain the available Codex CLI slash commands and present them as a clear Chinese reference table. Use when the user asks what commands are available in the Codex CLI, asks about "/" command menus, wants command translation, wants a grouped slash-command list, or asks what a specific slash command does.
---

# Codex CLI Commands

Use this skill as a reference sheet for Codex CLI slash commands.

## Response rules

- When the user asks "有哪些命令", "slash commands", "/" menu contents, or similar, present the command list directly instead of giving a vague explanation.
- Prefer Chinese.
- Group commands by function so the list is easy to scan.
- If the user asks about one specific command, explain that command first, then mention nearby related commands if useful.
- If the user asks for translation, translate the command descriptions faithfully and keep the original command names unchanged.
- Do not invent commands that are not in the reference table below unless the current session explicitly shows them.

## Reference table

### Session and conversation

- `/new`: start a new chat during a conversation
- `/resume`: resume a saved chat
- `/fork`: fork the current chat
- `/rename`: rename the current thread
- `/compact`: summarize conversation to prevent hitting the context limit
- `/clear`: clear the terminal and start a new chat

### Modes and agents

- `/plan`: switch to Plan mode
- `/collab`: change collaboration mode (experimental)
- `/agent`: switch the active agent thread
- `/subagents`: switch the active agent thread for subagents
- `/fast`: toggle Fast mode to enable fastest inference at 2X plan usage

### Model, permissions, and environment

- `/model`: choose what model and reasoning effort to use
- `/permissions`: choose what Codex is allowed to do
- `/sandbox-add-read-dir <absolute_path>`: let sandbox read a directory
- `/experimental`: toggle experimental features
- `/status`: show current session configuration and token usage
- `/title`: configure which items appear in the terminal title
- `/statusline`: configure which items appear in the status line
- `/theme`: choose a syntax highlighting theme
- `/personality`: choose a communication style for Codex

### Files, code, and workflow

- `/init`: create an AGENTS.md file with instructions for Codex
- `/skills`: use skills to improve how Codex performs specific tasks
- `/review`: review current changes and find issues
- `/diff`: show git diff, including untracked files
- `/mention`: mention a file
- `/copy`: copy the latest Codex output to the clipboard

### Integrations and plugins

- `/mcp`: list configured MCP tools
- `/plugins`: browse plugins

### Process and account

- `/ps`: list background terminals
- `/stop`: stop all background terminals
- `/feedback`: send logs to maintainers
- `/logout`: log out of Codex
- `/exit`: exit Codex

## Preferred Chinese rendering

When the user asks for a translated list, prefer wording like this:

- `/model`: 选择模型和推理强度
- `/fast`: 切换快速模式
- `/permissions`: 设置 Codex 权限
- `/sandbox-add-read-dir`: 给沙箱增加可读目录
- `/experimental`: 切换实验功能
- `/skills`: 使用技能增强任务处理效果
- `/review`: 审查当前改动
- `/rename`: 重命名当前线程
- `/new`: 新建聊天
- `/resume`: 恢复聊天
- `/fork`: 分叉当前聊天
- `/init`: 初始化 `AGENTS.md`
- `/compact`: 压缩当前对话
- `/plan`: 切换到计划模式
- `/collab`: 切换协作模式
- `/agent`: 切换代理线程
- `/subagents`: 切换子代理线程
- `/diff`: 查看代码差异
- `/copy`: 复制上一条输出
- `/mention`: 引用文件
- `/status`: 查看会话状态
- `/title`: 设置标题栏内容
- `/statusline`: 设置状态栏内容
- `/theme`: 切换高亮主题
- `/mcp`: 查看 MCP 工具
- `/plugins`: 浏览插件
- `/logout`: 退出登录
- `/exit`: 退出 Codex
- `/feedback`: 发送反馈日志
- `/ps`: 查看后台终端
- `/stop`: 停止后台终端
- `/clear`: 清屏并新开聊天
- `/personality`: 切换交流风格

## Notes

- If the user seems unsure whether `/plan` exists, answer clearly that it does exist in the command list when it is present in the current menu.
- If the user asks for a "complete list", return the grouped table first and avoid drifting into unrelated CLI flags unless they ask for those separately.
