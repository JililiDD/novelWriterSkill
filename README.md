# Novel Writer

A reusable skill for structured long-form fiction planning, chapter generation, continuity auditing, revision, and project-state management.

## Contents

- `skills/novel-writer/SKILL.md` — skill entrypoint and workflow router
- `skills/novel-writer/agents/openai.yaml` — ChatGPT skill interface metadata
- `skills/novel-writer/references/` — selectively loaded workflow and quality modules
- `.codex-plugin/plugin.json` — Codex plugin manifest
- `.agents/plugins/marketplace.json` — local agent marketplace manifest
- `.claude-plugin/marketplace.json` — local Claude-compatible marketplace manifest
- `project-notes/` — project-specific material excluded from the reusable skill package
- `dist/` — generated release archives; ignored by Git

## Core workflow

Novel Writer supports:

1. premise, style, element, and tone confirmation
2. project profile and System Bible creation
3. detailed and layered novel planning
4. per-chapter preflight confirmation
5. staged drafting, character review, lore audit, styling, and humanization
6. post-humanizer fact locking and project-state updates
7. targeted chapter revision, dashboards, and optional TTS workflows

Project-specific manuscripts, canon, audits, and learned rules must remain in the novel project's own directory rather than in the reusable skill.

## Install in Codex

Using the Codex binary bundled with the ChatGPT desktop application on macOS:

```bash
/Applications/ChatGPT.app/Contents/Resources/codex plugin marketplace add /path/to/novel-writer
/Applications/ChatGPT.app/Contents/Resources/codex plugin add novel-writer
```

Restart or open a new Codex session after installation.

Example requests:

```text
Use novel-writer to set up a new novel project.
Use novel-writer to prepare chapter 8 preflight for /path/to/book.
Use novel-writer to audit chapter 3 for continuity and AI-like prose.
```

## Development

Generated packages belong in `dist/` and should not be committed. Validate the skill before distribution and publish the final ChatGPT-compatible bundle as `skill.zip`.
