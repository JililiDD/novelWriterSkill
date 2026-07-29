---
name: novel-writer
description: Plan, write, audit, revise, and manage long-form fiction and serialized novels. Use for new novel setup, style and trope selection, project profiles, outlines, System Bibles, chapter preflight, chapter drafting, continuity and lore audits, prose revision, narrative humanization, project-state maintenance, multi-volume planning, fanfiction mini-gates, reading dashboards, and audiobook or TTS preparation. Apply when the user asks to create or continue a novel project, generate or rewrite a chapter, review fiction for continuity or AI-like prose, or maintain reusable fiction project files.
---

# Novel Writer

Use this skill as the control plane for structured long-form fiction work. Load only the reference files required for the current request.

## Core rules

1. Read actual project files before making claims about project state, chapter status, canon, or existing prose.
2. Keep full manuscripts, chapter briefs, audits, canon, and book-specific lessons inside the novel project. Do not add them to this reusable skill.
3. Before drafting a new chapter, create or refresh its chapter preflight and obtain explicit user confirmation. A request such as “generate chapter 8” starts preflight unless that chapter's preflight was already confirmed in the current conversation.
4. Do not automatically continue to the next chapter after finishing the current one.
5. Do not modify this skill unless the user explicitly authorizes the change. Follow `references/skill-change-protocol.md`.
6. Derive prose style from the approved Style Bible, Element Bible, Tone Lock, and project-specific rules. Do not impose a universal genre or voice.
7. Treat the approved chapter brief as a binding contract. Missing or contradicted required plot points are Critical bugs.
8. Narrative Humanizer may change expression but must not change facts, clues, world rules, character knowledge, required beats, or foreshadowing obligations. Run Fact Lock after humanization.
9. Back up completed chapter files before targeted revision.
10. Use available subagents for isolated role passes when supported. Otherwise run the same roles sequentially with separate inputs, outputs, and intermediate files.
11. Do not expose role notes, audit scaffolding, planning tags, or workflow terminology in final novel prose.
12. Stop immediately when the user asks to stop. Do not continue drafting or advance to another chapter.

## Route by intent

| User intent | Load these references |
|---|---|
| Start a new novel | `startup-workflow.md`, `style-and-element-selection.md`, `style-library.md`, `element-library.md`, `style-element-compatibility.md`, `project-profile-workflow.md`, `layered-novel-planning.md` |
| Short fanfiction or one-shot | `fanfic-one-shot-mini-gate.md`, `style-and-element-selection.md`, `style-library.md`, `element-library.md` |
| Long or multi-stage novel planning | `layered-novel-planning.md`, `staged-long-novel-planning.md`, `system-bible-workflow.md` |
| Custom reusable style or element | `library-expansion-protocol.md`, plus the relevant library |
| Esports novel planning | `esports-novel-planning.md`, plus startup, style, and element references as needed |
| Create or update project profile | `project-profile-workflow.md`, `startup-workflow.md` |
| Create System Bible | `system-bible-workflow.md` |
| Build detailed plot outline | `startup-workflow.md`, `system-bible-workflow.md`; also load `staged-long-novel-planning.md` for multi-volume projects |
| Generate or regenerate a chapter | `chapter-pipeline.md`, `continuity-bug-audit.md`, `narrative-humanizer.md`, `new-character-provenance-gate.md`; also load `ongoing-serial-chapter-handoff.md` for an existing serial |
| Revise completed prose | `chapter-humanizer-revision-workflow.md`, `narrative-humanizer.md`, `continuity-bug-audit.md` |
| Dashboard or mobile reading | `mobile-dashboard.md`, `multi-book-dashboard-management.md` |
| Audiobook or TTS | `audiobook-tts.md` |
| Maintain this skill | `skill-change-protocol.md`, `project-notes-policy.md`, `changelog.md` |

All reference paths are relative to `references/`.

## New novel setup

Follow `references/startup-workflow.md` in this order:

1. Confirm premise or seed.
2. Select primary and supporting writing styles.
3. Select core and secondary tropes or elements.
4. Run compatibility analysis and lock tone.
5. Decide length and chapter scale.
6. Create `state/project_profile.md`.
7. Confirm the initial story outline.
8. Create and confirm the System Bible.
9. Create and confirm the detailed plot outline.
10. Prepare the first chapter preflight.
11. Run the chapter pipeline only after confirmation.

Do not ask for target word count before style, elements, and tone are sufficiently defined.

## Confirmation gates

Before new prose generation, obtain explicit confirmation for the applicable gates:

1. Premise direction.
2. Style, elements, forbidden tendencies, and Tone Lock.
3. Initial outline.
4. System Bible.
5. Detailed plot outline.
6. Current chapter preflight.

Do not treat silence or lack of objection as confirmation. For short one-shots, use the compact gate in `references/fanfic-one-shot-mini-gate.md` unless the user explicitly asks to skip planning and write immediately.

## Chapter generation

Follow `references/chapter-pipeline.md`.

Before drafting, write the binding chapter contract to `state/chapterXX_brief.md` or the project's established equivalent. Include:

- chapter number and title
- main plot points
- turning point
- required characters
- new foreshadowing
- callbacks and resolutions
- emotional tone
- style risks
- continuity risks
- exact required phrases, when any

Run these role passes:

1. Orchestrator preflight
2. Storyteller draft
3. Character voice and action review
4. Lore and continuity audit
5. Prose Stylist
6. Narrative Humanizer
7. Post-Humanizer Fact Lock
8. Orchestrator state update
9. Final verification

Use separate files or clearly isolated outputs between passes. Do not let multiple roles silently overwrite the same source file without an explicit merge step.

### Alternative version requests

When the user requests a genuinely different version of an existing chapter:

1. Do not use the previous chapter prose as the rewrite base.
2. Use only the approved outline, System Bible, current state, character boundaries, and foreshadowing ledger.
3. Deliberately vary pacing, scene structure, descriptive focus, and emotional texture.
4. Preserve every binding contract item.
5. Mark the chapter brief as an alternative-generation task.

## New entity provenance

For each newly prominent named character, faction, artifact, or location, identify the prior clue, outline thread, witness statement, document, or established cause that leads to it. Follow `references/new-character-provenance-gate.md`.

## Continuity and lore audit

The audit must:

- extract material facts from the draft
- compare them against the approved System Bible and state files
- check chapter-contract compliance
- check character voice and knowledge boundaries
- inspect timeline, objects, resources, evidence, locations, and cause-to-consequence logic when relevant
- classify findings as Critical, Major, or Minor

Do not apply irrelevant genre-specific checks. For example, do not force wound tracking into a chapter with no injury or combat.

## Stylist, Humanizer, and Fact Lock boundaries

### Prose Stylist

Apply the approved style system. Improve rhythm, viewpoint consistency, imagery, genre fit, and scene-level prose without changing story facts.

### Narrative Humanizer

Reduce templated transitions, mechanical symmetry, repeated image families, stock body cues, forced aphorisms, over-explanation, and generic polished phrasing. Preserve all facts and obligations.

### Fact Lock

Compare the humanized version with the approved brief, pre-humanized draft, System Bible, and state. Any changed fact, clue, knowledge boundary, required beat, or foreshadowing obligation is Critical.

## Forbidden prose leakage

Final novel prose must not contain workflow or planning markers such as:

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

Use contextual judgment for words that may occur naturally in the story. The intent is to prevent planning language from leaking into prose, not to ban legitimate in-world vocabulary blindly.

## Final verification

Before reporting a chapter complete, independently verify:

1. Expected files exist and are non-empty.
2. Final chapter and audit files are readable.
3. No planning or workflow markers leaked into prose.
4. All binding chapter-contract items are present semantically.
5. Exact required phrases remain exact when the contract requires exact wording.
6. The audit covers contract compliance, fact alignment, continuity, humanizer review, and Fact Lock.
7. Project state and ledgers were updated where required.
8. Any configured reading endpoint returns successfully when dashboard verification is part of the request.

If verification fails, correct the issue or run a targeted revision before reporting success.

## Revising completed chapters

Follow `references/chapter-humanizer-revision-workflow.md`.

- If the user asks for review first, report findings and proposed changes without editing.
- Obtain approval before changing completed prose when required by the workflow.
- Back up the affected files.
- Patch the final chapter and corresponding working draft when the project maintains both.
- Re-run continuity, required-term, leakage, and Fact Lock checks.

Revision levels:

- Light: line-level prose, repetition, metaphors, and small state clarifications.
- Deep: paragraph or scene pacing changes; require explicit approval.
- Regeneration: fresh chapter generation through the full chapter pipeline.

## Project state

Prefer these project-local directories when the project has no established structure:

```text
state/
drafts/
chapters/
audits/
```

System Bible and current state should contain approved canon, not brainstorming history or rejected alternatives. Subagents and staged role passes should receive only the approved materials needed for their task.

## Optional workflows

Dashboard and mobile-reading guidance:

- `references/mobile-dashboard.md`
- `references/multi-book-dashboard-management.md`

Audiobook and TTS guidance:

- `references/audiobook-tts.md`

Keep these optional workflows separate from core chapter generation unless the user asks for them.

## Reference index

Core planning and generation:

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
- `references/fanfic-one-shot-mini-gate.md`

Quality and revision:

- `references/continuity-bug-audit.md`
- `references/narrative-humanizer.md`
- `references/chapter-humanizer-revision-workflow.md`
- `references/outline-compliance-and-prose-logic.md`
- `references/new-character-provenance-gate.md`
- `references/workflow-pitfalls.md`

Operations:

- `references/mobile-dashboard.md`
- `references/multi-book-dashboard-management.md`
- `references/audiobook-tts.md`

Maintenance:

- `references/skill-change-protocol.md`
- `references/project-notes-policy.md`
- `references/changelog.md`
