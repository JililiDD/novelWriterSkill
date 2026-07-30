---
name: novel-writer
description: Plan, write, audit, revise, resume, and manage long-form fiction and serialized novels. Use for new novel setup, style and element selection, Project Profiles, whole-book and volume planning, System Bibles, dynamic Story Memory, chapter or scene preflight, seven-stage prose delivery, resumable run state, candidate versions, continuity and lore audits, prose revision, narrative humanization, periodic checkpoint/arc/volume audits, and long-running fiction project maintenance. Apply when the user asks to create, continue, recover, review, rewrite, or maintain a novel, chapter, scene, one-shot, serial, or multi-volume fiction project.
---

# Novel Writer

Use this Skill as the control plane for structured long-form fiction work. Load only the references required for the current intent.

## Universal invariants

1. Read actual project files before claiming project state, chapter status, canon, or existing prose.
2. Keep manuscripts, briefs, audits, canon, dynamic memory, and book-specific lessons inside the novel project, not this reusable Skill.
3. Give each information class one authoritative owner: Project Profile for style/reader experience, System Bible for stable canon, Story Memory for current dynamic state, outlines for future intent, and promoted prose for original event evidence.
4. Treat every approved contract, outline obligation, exact phrase, knowledge boundary, promise window, and canon fact as binding.
5. Derive prose from the approved Project Profile, Style Anchors, System Bible, Story Memory, current plan, and work-unit brief; do not impose a universal voice.
6. Keep role inputs and outputs isolated. No role may silently overwrite another role's source.
7. Run Story Fact Check after Narrative Humanizer whenever prose changes.
8. Run Final Verification before Promotion & State Update and before reporting completion.
9. Stable canon and Project Profile rules require explicit project-level confirmation; a chapter run may propose but not silently apply them.
10. Keep planning, audit, role, and workflow scaffolding out of final prose.
11. Never auto-continue to the next chapter or scene. Stop immediately when the user asks to stop.
12. Back up completed prose before approved overwrite.
13. Modify this Skill only with explicit user authorization; follow `references/skill-change-protocol.md`.

## Execution mode

Load `references/execution-modes.md` whenever selecting rigor, handling confirmation, deciding what may be combined or skipped, or responding to a request to move faster.

- **Fast** — bounded, low-risk, self-contained work.
- **Standard** — default for ordinary planning, generation, continuation, and revision.
- **Production** — publication-oriented or maximum-traceability work.

Modes change ceremony, persistence, and pass separation, not quality or canon standards.

## Route by intent

All paths below are relative to `references/`.

| User intent | Canonical references |
|---|---|
| Start or re-establish a novel | `execution-modes.md`, `startup-workflow.md`, `style-and-element-selection.md`, `style-library.md`, `element-library.md`, `style-element-compatibility.md`, `project-profile-workflow.md`, `layered-novel-planning.md`, `system-bible-workflow.md`, `long-form-continuity.md` |
| Short fanfiction or one-shot | `execution-modes.md`, `fanfic-one-shot-mini-gate.md`, `chapter-pipeline.md`; add project/state references when it belongs to an existing canon |
| Whole-book, volume, arc, tournament, case, or dynamic-cast planning | `execution-modes.md`, `layered-novel-planning.md`, `project-profile-workflow.md`, `system-bible-workflow.md`, `long-form-continuity.md` |
| Custom reusable style or element | `library-expansion-protocol.md` plus the relevant library |
| Esports-specific planning | `esports-novel-planning.md` plus canonical startup/planning references |
| Create or update Project Profile | `execution-modes.md`, `project-profile-workflow.md`, `style-and-element-selection.md` |
| Create or update System Bible | `execution-modes.md`, `system-bible-workflow.md` |
| Bootstrap or audit long-term continuity | `long-form-continuity.md`, `continuity-bug-audit.md`, `project-profile-workflow.md`, `system-bible-workflow.md` |
| Generate, regenerate, or continue chapter/scene prose | `execution-modes.md`, `run-state-protocol.md`, `role-execution-protocol.md`, `chapter-pipeline.md`, `long-form-continuity.md`, `continuity-bug-audit.md`, `narrative-humanizer.md` |
| Revise completed prose | `execution-modes.md`, `run-state-protocol.md`, `role-execution-protocol.md`, `chapter-humanizer-revision-workflow.md`, `chapter-pipeline.md`, `long-form-continuity.md`, `continuity-bug-audit.md`, `narrative-humanizer.md` |
| Run checkpoint, arc, or volume audit | `long-form-continuity.md`, `continuity-bug-audit.md`, `narrative-humanizer.md`, `layered-novel-planning.md` |
| Maintain this Skill | `skill-change-protocol.md`, `project-notes-policy.md`, `changelog.md` |

Dashboard and audiobook implementation are separate companion workflows. The compatibility references `mobile-dashboard.md`, `multi-book-dashboard-management.md`, and `audiobook-tts.md` define handoff boundaries only.

## High-level lifecycle

For a persistent long-form project:

```text
Premise
→ Style/Elements/Tone Lock
→ Project Profile
→ Whole-Book Spine
→ System Bible
→ Current Volume/Arc
→ Story Memory
→ Work-Unit Preflight
→ Seven-Stage Prose Delivery
→ Periodic Checkpoint/Arc/Volume Audit
```

Use `startup-workflow.md` for setup, `layered-novel-planning.md` for planning, `long-form-continuity.md` for dynamic memory and periodic audits, and `chapter-pipeline.md` for prose delivery.

## Seven-stage prose delivery

1. Preflight
2. Draft Writing
3. Content Review
4. Prose Refinement
5. Story Fact Check
6. Final Verification
7. Promotion & State Update

Content Review keeps Character Review and Lore & Continuity Audit separately identifiable. Prose Refinement runs Prose Stylist before Narrative Humanizer. Use inspectable subagents when available or the same isolated contracts sequentially.

## Completion boundary

Do not report prose delivery complete until applicable mode requirements are met, blocking findings are resolved, Story Fact Check and Final Verification pass with fresh evidence, the selected candidate is promoted when applicable, the verified dynamic Story Memory delta is applied and reread, and no required stage remains active, paused, blocked, stale, or pending.

Stop after the requested work unit. A request for the next chapter authorizes entry into its Preflight, not silent automatic prose generation.