# Novel Writer

A reusable Skill for structured long-form fiction planning, seven-stage prose delivery, continuity control, revision, recovery, and multi-volume project maintenance.

## Contents

- `skills/novel-writer/SKILL.md` — compact control plane and intent router
- `skills/novel-writer/agents/openai.yaml` — ChatGPT Skill interface metadata
- `skills/novel-writer/references/` — selectively loaded planning, delivery, state, continuity, and quality protocols
- `skills/novel-writer/assets/` — reusable run-state, Story Memory, and periodic-audit templates
- `.codex-plugin/plugin.json` — Codex plugin manifest
- `.claude-plugin/marketplace.json` — local Claude-compatible marketplace manifest
- `project-notes/` — project-specific material excluded from the reusable Skill package
- `dist/` — generated release archive; ignored by Git

## Core architecture

Novel Writer separates project information by authority:

- **Project Profile** — style, elements, Tone Lock, reader promise, Style Anchors
- **System Bible** — stable characters, world/system rules, durable canon
- **Story Memory** — current dynamic state, knowledge, objects/resources, foreshadowing/promises, open consequences
- **Outlines** — future intent
- **Promoted prose** — original evidence of what occurred
- **Chapter brief/audit** — current contract, selected context, findings, and proposed dynamic-state delta

Supported prose delivery uses seven stages:

1. Preflight
2. Draft Writing
3. Content Review
4. Prose Refinement
5. Story Fact Check
6. Final Verification
7. Promotion & State Update

Final Verification happens before official promotion or Story Memory update. Stable canon changes require separate explicit confirmation.

## Long-form continuity

For serial and multi-volume work, `long-form-continuity.md` provides:

- active-only Story Memory;
- source-backed Context Manifest assembly;
- Proposed Story Memory Delta inside existing chapter audits;
- checkpoint, arc, and volume audits;
- volume rebaseline and Story Memory compaction;
- existing-project bootstrap without full historical backfill.

## Companion boundaries

Dashboard/mobile-reader and audiobook/TTS implementation are separate companion workflows. Novel Writer hands off promoted final prose and stable project artifacts but does not hardcode frontend servers, ports, process commands, current TTS products, GPU assumptions, or deployment environments.

## Install in Codex

Using the Codex binary bundled with the ChatGPT desktop application on macOS:

```bash
/Applications/ChatGPT.app/Contents/Resources/codex plugin marketplace add /path/to/novel-writer
/Applications/ChatGPT.app/Contents/Resources/codex plugin add novel-writer
```

Restart or open a new Codex session after installation.

Example requests:

```text
Use novel-writer to set up a multi-volume novel project.
Use novel-writer to prepare chapter 8 Preflight and Context Manifest.
Use novel-writer to audit this arc for continuity, style drift, and unresolved promises.
Use novel-writer to revise chapter 3 without changing Story Memory facts.
```

## Development

Validate the complete Skill before distribution. Generated packages belong in `dist/` and should not be committed. Publish the complete bundle as `dist/skill.zip` with `novel-writer/` as the archive root.