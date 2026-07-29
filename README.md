# Noval Writer Skill

Codex-importable package for the user's long-form novel writing workflow.

Path: `/Users/jli/Desktop/programs/novalWriterSkill`

## Contents

- `.codex-plugin/plugin.json` — Codex plugin manifest
- `skills/novel-writer/SKILL.md` — Codex-compatible skill entrypoint
- `skills/novel-writer/references/` — copied reference modules from Hermes `novel-generator`
- `.agents/plugins/marketplace.json` and `.claude-plugin/marketplace.json` — marketplace manifests for local import flows
- `dist/noval-writer-skill-1.0.0.zip` — portable archive

## Install/import in Codex

Using the bundled Codex binary on this Mac:

```bash
/Applications/ChatGPT.app/Contents/Resources/codex plugin marketplace add /Users/jli/Desktop/programs/novalWriterSkill
/Applications/ChatGPT.app/Contents/Resources/codex plugin add noval-writer-skill
```

Then restart/open a new Codex session and invoke:

```text
Use novel-writer to set up a new novel project...
```

## Notes

The original Hermes skill uses `delegate_task`. In Codex, the skill's compatibility layer translates that into separate role passes or Codex subagents if available.
