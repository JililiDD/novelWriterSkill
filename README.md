# Novel Writer

Novel Writer is a GitHub-installable plugin and reusable Skill for structured long-form fiction planning, seven-stage prose delivery, continuity control, revision, recovery, and multi-volume project maintenance.

## Install from GitHub

The repository is both the marketplace and the plugin source.

### Claude Code

```bash
claude plugin marketplace add JililiDD/novelWriterSkill
claude plugin install novel-writer@novel-writer
```

Restart Claude Code or open a new session after installation.

### Codex

```bash
codex plugin marketplace add JililiDD/novelWriterSkill
codex plugin add novel-writer@novel-writer
```

Restart Codex or open a new session after installation.

## Install from a local checkout

Replace `/absolute/path/to/novelWriterSkill` with this repository's absolute path.

### Claude Code

```bash
claude plugin marketplace add /absolute/path/to/novelWriterSkill
claude plugin install novel-writer@novel-writer
```

### Codex

```bash
codex plugin marketplace add /absolute/path/to/novelWriterSkill
codex plugin add novel-writer@novel-writer
```

## Use the plugin

Skills activate when the request matches their purpose. Example requests:

```text
Use novel-writer to set up a multi-volume novel project.
Use novel-writer to prepare chapter 8 Preflight and Context Manifest.
Use novel-writer to audit this arc for continuity, style drift, and unresolved promises.
Use novel-writer to revise chapter 3 without changing Story Memory facts.
```

## Plugin structure

- `.claude-plugin/marketplace.json` — Claude-compatible GitHub marketplace
- `.claude-plugin/plugin.json` — Claude plugin manifest
- `.codex-plugin/plugin.json` — Codex plugin manifest
- `.agents/plugins/marketplace.json` — Codex marketplace registration metadata
- `skills/novel-writer/SKILL.md` — compact control plane and intent router
- `skills/novel-writer/agents/openai.yaml` — ChatGPT Skill interface metadata
- `skills/novel-writer/references/` — selectively loaded planning, delivery, state, continuity, and quality protocols
- `skills/novel-writer/assets/` — reusable run-state, Story Memory, and periodic-audit templates
- `project-notes/` — project-specific material excluded from the reusable Skill package
- `dist/` — generated release archives; ignored by Git

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

## Development

Validate the complete Skill before distribution. Generated packages belong in `dist/` and should not be committed. Publish the complete bundle as `dist/skill.zip` with `novel-writer/` as the archive root.

## License

MIT
