---
name: novel-writer
description: Use when planning, writing, auditing, or revising long-form fiction in Codex. Port of the user's Hermes novel-generator workflow with Codex-compatible preflight gates, style/element bibles, chapter pipeline, continuity audit, humanizer pass, and project-scoped state files.
version: 1.0.0
author: JililiDD / Hermes Agent port
license: MIT
metadata:
  tags: [novel, fiction, creative-writing, long-form, codex]
  source_skill: hermes:novel-generator@2.6.2
---

# Novel Writer — Codex-compatible long-form fiction workflow

This is a Codex-importable port of the user's Hermes `novel-generator` skill. It keeps the original novel workflow and reference library, but adds a Codex compatibility layer so it can be used without Hermes-only tools.

## Codex compatibility layer

1. Treat this `SKILL.md` as the routing and hard-rule entrypoint. Load only the reference files needed for the user's current request from `references/`.
2. Hermes-specific references to `delegate_task`, "parent assistant", or multi-agent tool calls mean: run distinct role passes in Codex. If Codex has subagents in the current environment, use them; otherwise simulate the agents sequentially in clearly separated passes: Orchestrator, Storyteller, Character Review, Lore Auditor, Prose Stylist, Narrative Humanizer, Fact Lock, and Final Verification.
3. Do not expose internal role notes, audit scaffolding, or planning markers in final novel prose. Keep working files in the project directory, preferably under `state/`, `drafts/`, `chapters/`, and `audits/`.
4. For filesystem facts, read actual files before deciding. For generated artifacts, verify files exist, are non-empty, and pass the relevant checks before reporting success.
5. If a referenced Hermes tool is unavailable in Codex, use the closest Codex/native equivalent: shell commands for file checks, separate markdown files for handoffs, and explicit sequential review passes for agent separation.
6. Codex does not need to modify this skill during normal novel work. Project-specific rules and learned constraints belong in the novel project's own `state/` files, not in this reusable skill.

## Quick usage in Codex

- New novel: "Use novel-writer to set up a new novel about ..."
- Continue a book: "Use novel-writer; project is /path/to/book; generate chapter 8 preflight."
- Revise prose: "Use novel-writer to review chapter 3 for AI-like prose; propose edits first."
- Dashboard/mobile: "Use novel-writer to create/update a mobile-readable dashboard for /path/to/book."

When the user asks to generate a chapter, start with chapter preflight and wait for explicit confirmation before drafting正文, unless the same conversation already contains that chapter's confirmed preflight.

---

## Imported Hermes workflow


# Novel Generator — Modular Multi-Agent Novel System

This skill helps create, audit, revise, and manage long-form fiction. It is intentionally modular: `SKILL.md` contains only hard rules, routing, and module index. Detailed workflows live in `references/`.

## Non-negotiable hard rules

1. **Never write novel正文 directly in the parent assistant** when generating new chapters. Use `delegate_task` multi-agent workflow.
2. **Every chapter requires preflight confirmation** before prose drafting. `生成第X章` means start preflight, not write正文 immediately, unless the user already confirmed that chapter’s preflight in the same conversation.
3. **Do not auto-continue** to the next chapter. After finishing chapter X, stop and ask whether to continue.
4. **Do not modify this skill without explicit user confirmation.** If the user is discussing improvements, first explain the plan; only edit after the user says `可以改`, `就这么做`, `开始修改`, `确认`, `按这个方案执行`, `可以继续`, or equivalent. See `references/skill-change-protocol.md`.
5. **Do not turn one project’s details into universal rules.** Store methods in universal references; keep full project content in the project directory. See `references/project-notes-policy.md`.
6. **Do not hardcode one prose style or genre.** Derive style from the user-approved Style Bible, Element Bible, Tone Lock, and System Bible.
7. **Humanizer cannot change facts.** After Narrative Humanizer, run Post-Humanizer Fact Lock.
8. **Project-specific writing constraints override generic defaults** when confirmed by the user, but they must stay project-scoped.
9. **After正文 generation begins, project-specific audit findings, book-specific rules, and writing lessons must be stored in that book's project directory (e.g. `state/book_specific_rules.md`) or a separate book-specific skill, not mixed into the universal `novel-generator` skill.** The universal skill may store only the generic routing rule that such project notes must remain project-scoped.
10. **Back up before targeted revision** of completed chapter files.
11. **Use tools for file/system/current-state facts.** Read actual files and verify outputs; do not rely on memory.
12. **Fanfic / one-shot requests still need a mini-lock when this skill is loaded or when a planning workflow was promised.** Do not treat “short fanfic scene” as permission to skip structure after promising a process. Before prose, produce a compact brief and get confirmation: Premise Lock, Style Lock, Element Lock, Tone Lock, Outline, Mini System Bible, and Scene/Chapter Preflight. For short fanfic, this can be concise, but it must happen before drafting unless the user explicitly says to skip planning and write immediately. See `references/fanfic-one-shot-mini-gate.md` for the compact template and pitfalls.

## Mode routing

Load only the references needed for the current task.

| User intent | Required references |
|---|---|
| New novel setup | `startup-workflow.md`, `style-and-element-selection.md`, `style-library.md`, `element-library.md`, `style-element-compatibility.md`, `project-profile-workflow.md`, `layered-novel-planning.md` |
| Short fanfic / one-shot scene with specific emotional constraints | `style-and-element-selection.md`, `style-library.md`, `element-library.md`; use compact Premise/Style/Element/Tone/Outline/Mini Bible/Preflight confirmation before drafting unless user explicitly says to skip planning |
| Long novel / multi-stage cast planning | `layered-novel-planning.md`, plus `system-bible-workflow.md` when creating canon |
| Custom style/element proposal | `library-expansion-protocol.md`, plus relevant library |
| Esports novel planning | `esports-novel-planning.md`, plus startup/style/element references as needed |
| Project profile creation/update | `project-profile-workflow.md`, `startup-workflow.md` |
| System Bible creation | `system-bible-workflow.md` |
| Detailed plot outline | `startup-workflow.md`, `system-bible-workflow.md`; for long multi-volume projects also load `staged-long-novel-planning.md` |
| Multi-volume / staged long-novel planning, tournaments, dynamic rosters/casts | `staged-long-novel-planning.md`, plus `startup-workflow.md` and `system-bible-workflow.md` as needed |
| Generate a chapter | `chapter-pipeline.md`, `continuity-bug-audit.md`, `narrative-humanizer.md`, `new-character-provenance-gate.md`; for already-running serial projects also load `ongoing-serial-chapter-handoff.md` |
| Revise completed chapter | `chapter-humanizer-revision-workflow.md`, `narrative-humanizer.md`, `continuity-bug-audit.md` |
| Dashboard/mobile reading | `mobile-dashboard.md`, `multi-book-dashboard-management.md` |
| Audiobook/TTS | `audiobook-tts.md` |
| Skill maintenance/refactor | `skill-change-protocol.md`, `project-notes-policy.md`, `changelog.md` |
| 《雪尽刀还》 project-specific context | `xuejin-daohuan-generation-notes.md`, `xuejin-daohuan-endgame-notes.md` only when working on that book |

## New novel setup flow

When the user starts a new novel, follow `references/startup-workflow.md`.

For long novels with changing casts, teams, factions, tournaments, or multi-stage careers, also follow `references/layered-novel-planning.md` and `references/staged-long-novel-planning.md`: lock the full-book spine, calculate event/match density when relevant, keep only a small long-foreshadowing ledger globally, then detail the current volume; do not over-plan every later-stage character/team before prose begins unless the user explicitly wants a fully locked long outline.

Required order:

1. Topic / Seed Confirmation
2. Writing Style Selection
3. Trope & Element Mix Selection
4. Compatibility Check + Tone Lock
5. Length / Chapter Scale
6. Project Profile Creation (`state/project_profile.md`)
7. Initial Story Outline Confirmation
8. System Bible Confirmation
9. Detailed Plot Outline Confirmation
10. Per-Chapter Preflight
11. Chapter Generation Pipeline

**Rule:** Do not ask for target word count before style, elements, and tone are locked.

## Confirmation gates

Before generating any prose, obtain explicit confirmations:

1. **Topic / Seed confirmation** — the premise direction is correct.
2. **Style + Element + Tone confirmation** — main style, supporting styles, core elements, forbidden styles/elements, Tone Lock.
3. **Initial Outline confirmation** — world, main characters, chapter structure direction.
4. **System Bible confirmation** — character bible, relationship map, world/system rules, Style Bible, Element Bible.
5. **Detailed Plot Outline confirmation** — per-chapter plot points, turning points, foreshadowing, planned reveals.
6. **Per-chapter preflight confirmation** — before each chapter正文.

Never treat silence or “no objection” as confirmation.

## Style and element system

Use `references/style-and-element-selection.md`.

Principles:
- User chooses one main style and up to two supporting styles.
- User chooses 1–3 core elements and 0–3 secondary elements.
- Run compatibility analysis before deciding length or outline.
- Convert confirmed choices into Style Bible and Element Bible.
- If the user proposes a new reusable style/element that is not in the library, follow `references/library-expansion-protocol.md`: define it, ask whether to save it, then add only after confirmation.

Libraries:
- `references/style-library.md`
- `references/element-library.md`

## System Bible

Use `references/system-bible-workflow.md`.

System Bible must include or reference:
- Project Profile Summary from `state/project_profile.md` when available
- Character Bible
- Relationship Map
- World/System Rules
- Style Bible
- Element Bible

Subagents should receive the final approved System Bible and current state files, not brainstorming history or rejected alternatives.

## Chapter generation pipeline

Use `references/chapter-pipeline.md`. For continuing an already-running serial novel after prior chapters exist, also use `references/ongoing-serial-chapter-handoff.md` to refresh live files, route `继续下一章`-style requests through the preflight gate, and verify delegated outputs before sending files.

### Handling “new version / alternative take” requests for existing chapters

When the user says they want a **new version** of a chapter (e.g. “重新写一个第一章”, “给我一个完全不同的版本”, “不要修改原稿，要忘掉原来的”), treat it as a fresh generation task:

1. Do **not** read or reference the previous chapter prose as a base.
2. Regenerate strictly from the current approved outline, System Bible, character boundaries, and foreshadowing ledger only.
3. Deliberately vary pacing, scene structure, descriptive focus, and emotional texture while still hitting every required plot point and contract item.
4. The goal is a meaningfully different realization of the same story beat, not a polished or reworded version of the prior draft.

Add a short note in the chapter brief when this mode is active so downstream agents know the intent.

Required agent stages:
1. Orchestrator preflight
2. Storyteller draft
3. Character Agents voice/action review
4. Lore Auditor
5. Prose Stylist
6. Narrative Humanizer
7. Post-Humanizer Fact Lock
8. Orchestrator state update
9. Parent verification

### Approved chapter contract gate

Before drafting, Orchestrator must extract the binding chapter contract into `state/chapterXX_brief.md`:
- chapter title
- main plot points
- turning point
- required characters
- new foreshadowing
- callbacks/resolutions
- emotional tone
- style risks
- continuity risks

Missing or contradicted main plot points are Critical Bugs.

### New-character / new-location provenance gate

For every newly prominent named character, faction, artifact, or location, state which prior clues/artifacts/witness statements/outline threads lead there. Avoid sudden NPC/map insertion.

Use `references/new-character-provenance-gate.md`.

## Lore Auditor and continuity

Lore Auditor must:
- extract facts from the draft
- verify them 1:1 against System Bible and approved state
- check outline compliance
- check character voice/knowledge boundaries
- run `references/continuity-bug-audit.md`
- report severity: Critical / Major / Minor

Continuity audit is genre-neutral. Use only ledgers relevant to the current story/chapter:
- character state
- information/knowledge
- object/resource/evidence
- scene feasibility
- literal-vs-figurative language
- cause→consequence

Do not hardcode injury/combat/wound checks unless the chapter actually contains those elements.

## Prose Stylist and Narrative Humanizer

Prose Stylist must apply the approved Style Bible and genre profile.

Checklist:
- remove technical markers
- remove meta/chapter self-reference
- scan metaphor/simile logic and viewpoint fit
- scan over-repeated image families and stock body cues
- reduce forced aphorisms and generic polish
- preserve valid genre conventions

Narrative Humanizer uses `references/narrative-humanizer.md`.

It must reduce AI-like prose artifacts without changing:
- plot events
- clues/evidence
- world rules
- character knowledge boundaries
- required outline beats
- foreshadowing obligations

Any fact drift after Humanizer is a Critical Bug.

## Forbidden prose leaks

Final novel prose must not contain:
- `F-`
- `[伏笔]`
- `agent`
- `audit`
- `outline`
- `scene`
- `场景一`
- `上一章`
- `本章`
- `前文`
- `伏笔`
- `读者`
- `作者`
- other chapter-planning/meta-writing language

Prior events should be referenced as in-world memory, place, object, document, time, or speech.

## Parent-agent post-generation verification

After any chapter-generation `delegate_task`, the parent assistant must independently verify before reporting success:

1. Expected files exist and are non-empty.
2. Final chapter text and audit report are readable.
3. Forbidden/meta terms are absent.
4. Required chapter contract items are present semantically; exact clue phrases must remain exact when required.
5. Audit includes outline compliance, fact alignment, meta leakage check, continuity audit, humanizer check, and fact lock.
6. If dashboard is running, chapter read endpoint returns HTTP 200.
7. If verification fails, patch or request targeted revision before reporting completion.

## Targeted revision of completed chapters

When the user asks to revise existing prose for AI-like writing, repeated metaphors, phrasing, or continuity bugs:

1. Load `references/chapter-humanizer-revision-workflow.md`.
2. If user asks to review first, only review and propose changes.
3. Wait for confirmation before editing.
4. Back up files.
5. Patch final chapter and matching scene draft when appropriate.
6. Verify forbidden terms, required plot/clue terms, and dashboard.

Revision modes:
- **Light revision**: line-level prose, metaphor/repetition, small state clarifications; no plot restructure.
- **Deep revision**: paragraph/scene pacing changes; requires explicit approval.
- **Regeneration**: rewrite chapter; requires explicit approval and chapter pipeline.

## Dashboard and mobile reading

Dashboard/mobile details live in:
- `references/mobile-dashboard.md`
- `references/multi-book-dashboard-management.md`

Project dashboards should bind to `0.0.0.0:8420` for mobile/LAN access when the user wants phone access.

Do not assume legacy `/api/status`; for the multi-book dashboard, verify with `/api/books` and actual `/read/<book-id>/...` URLs.

## Audiobook / TTS

Audiobook notes live in `references/audiobook-tts.md`.

Use TTS only when requested. Keep audiobook workflow separate from core novel generation.

## Project notes policy

Full manuscripts, full chapter briefs, and full audits stay in project directories, not universal references.

Universal references should contain only compact reusable lessons. See `references/project-notes-policy.md`.

## Tool-failure fallback

If file tools fail unexpectedly even though files exist, switch to deterministic Python file I/O for inspection, replacement, and verification:

```bash
python3 - <<'PY'
from pathlib import Path
p = Path('/absolute/path/to/file.md')
text = p.read_text(encoding='utf-8')
# inspect / replace / verify
p.write_text(text, encoding='utf-8')
print(p.exists(), p.stat().st_size, len(text.splitlines()))
PY
```

## Reference index

Core workflow:
- `references/startup-workflow.md`
- `references/style-and-element-selection.md`
- `references/style-library.md`
- `references/element-library.md`
- `references/style-element-compatibility.md`
- `references/library-expansion-protocol.md`
- `references/project-profile-workflow.md`
- `references/layered-novel-planning.md`
- `references/staged-long-novel-planning.md`
- `references/system-bible-workflow.md`
- `references/chapter-pipeline.md`
- `references/ongoing-serial-chapter-handoff.md`
- `references/esports-novel-planning.md`

Quality and revision:
- `references/continuity-bug-audit.md`
- `references/narrative-humanizer.md`
- `references/chapter-humanizer-revision-workflow.md`
- `references/outline-compliance-and-prose-logic.md`
- `references/new-character-provenance-gate.md`

Operations:
- `references/mobile-dashboard.md`
- `references/multi-book-dashboard-management.md`
- `references/audiobook-tts.md`

Maintenance:
- `references/skill-change-protocol.md`
- `references/project-notes-policy.md`
- `references/changelog.md`

Project-specific:
- `references/xuejin-daohuan-generation-notes.md`
- `references/xuejin-daohuan-endgame-notes.md`
