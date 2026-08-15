---
name: novel-writer
description: Plan, develop, write, audit, revise, resume, and maintain standalone fiction and persistent novel projects. Use for adaptive Story Kernel discovery, style calibration, protagonist and relationship development, Dialogue Engine and character Voice Signatures, Project Profiles with Style Lock, master/volume/arc planning, stable Story Facts, active Story Memory, project craft lessons, selective hot/warm/cold context loading, dual-pass humanization, seven-dimension chapter quality gates, chapter interface continuity, mandatory promotion confirmation, rolling checkpoints, and long-running fiction maintenance. Apply when the user asks to create, continue, recover, review, rewrite, or manage a novel, chapter, scene, one-shot, serial, or multi-volume project.
---

# Novel Writer

Use this Skill as the control plane for structured fiction work. Load only the references required for the current intent.

## Universal invariants

1. Read actual supplied or project files before claiming project state, chapter status, story facts, or existing prose.
2. Keep manuscripts, plans, state, briefs, candidates, audits, archives, and book-specific lessons (`state/writing_lessons.md`) inside the novel project, not this reusable Skill.
3. Give each information class one current owner: master/volume plans for future direction; Project Profile for style, reader experience, and Style Lock; Story Facts for stable confirmed facts, Dialogue Profiles, and Recognition Anchors; Story Memory for active current state; and promoted prose for original evidence of happened events.
4. Treat every approved contract, plan obligation, exact phrase, knowledge boundary, promise window, protected fact, and forbidden change as binding.
5. Apply the five positive generation principles to all prose:
   - **POV owns the prose**: narration, attention, judgment, and sensory radius belong strictly to the viewpoint character.
   - **Characters speak from motive, knowledge, status, relationship, and pressure**: use the generative Dialogue Engine; never use clipped syntax, pseudo-classical diction, or shared strategic language as generic markers of intelligence.
   - **Evidence precedes interpretation**: present observable behavior, sensory details, and consequences first; do not explain what the reader can already follow.
   - **Competence is behavioral**: establish protagonist competence through observational attention, calculated questions, cost management, and verified actions, never through narrator praise.
   - **Causal closure**: a scene ends after meaningful causal state change, not after thematic summarization or authorial aphorisms.
6. Unpromoted candidate prose has zero authority over happened story events and must never silently alter downstream Story Memory, future chapter assumptions, or official text.
7. Never promote candidate prose into an official chapter or update Story Memory from that candidate without a fresh, explicit user confirmation after Final Verification. Final Verification may produce `PROMOTION READY`; it may not silently produce `PROMOTED`.
8. Substantive candidate changes invalidate dependent downstream checks. Re-run affected Character, Naturalness, Story Fact, Interface, and Final Verification stages before returning to `PROMOTION READY`.
9. Evaluate repeated user feedback about writing defects for project-level promotion into `state/writing_lessons.md`. Do not repeatedly patch single chapters when the underlying generation rule is flawed.
10. Keep logical role inputs and outputs isolated. Ordinary findings share one audit file only when each check remains separately identifiable.
11. Run Story Fact Check after Narrative Humanizer whenever prose changes.
12. Stable-setting, Project Profile, and project craft lesson changes require explicit project-level confirmation; a chapter audit may propose but not silently apply them.
13. Keep planning, audit, role, and workflow scaffolding out of final prose.
14. Never auto-continue to the next chapter or scene unless the user has explicitly authorized Autonomous Batch Mode (`references/autonomous-batch-pipeline.md`). Stop immediately when the user asks to stop or when a circuit breaker trips.
15. Back up promoted prose before approved overwrite.
16. Modify this Skill only with explicit user authorization; follow `references/skill-change-protocol.md`.

## Creation paths

Load `references/creation-paths.md` whenever routing work, handling confirmation, selecting persistence, or applying conditional checks.

- **Standalone Creation** — self-contained one-shot, scene, experiment, or bounded rewrite with no continuing project state.
- **Project Creation** — multi-unit, serialized, shared-setting, or existing-project work requiring continuing planning, stable facts, or current state.

Length alone does not select the path. There are no rigor modes. Add checks only when the task touches protected facts, plan boundaries, or file-safety risks.

## Route by intent

All paths below are relative to `references/`.

| User intent | References |
|---|---|
| Start a novel (Interactive Discovery or Autonomous Genesis) | `creation-paths.md`, `startup-workflow.md`, `style-calibration.md`, `layered-novel-planning.md`, `style-and-element-selection.md` |
| Standalone short story, fanfiction, or scene | `creation-paths.md`, `fanfic-one-shot-mini-gate.md`, `chapter-pipeline.md`, `dialogue-engine.md` |
| Autonomous multi-chapter batch drafting / whole-book generation | `autonomous-batch-pipeline.md`, `creation-paths.md`, `chapter-pipeline.md`, `quality-gate.md`, `long-form-continuity.md` |
| Calibrate or recalibrate narrative style | `style-calibration.md`, `project-profile-workflow.md` |
| Capture recurring feedback / craft lessons | `feedback-promotion.md` |
| Character dialogue design & NPC realism | `dialogue-engine.md`, `story-facts-workflow.md` |
| Select style, elements, compatibility, or Tone Lock | `style-and-element-selection.md`, `style-library.md`, `element-library.md` |
| Master, volume, arc, tournament, case, or dynamic-cast planning | `creation-paths.md`, `layered-novel-planning.md`; add current project authorities only when the plan depends on them |
| Custom reusable style or element | `library-expansion-protocol.md` plus the relevant library |
| Create or update Project Profile | `creation-paths.md`, `project-profile-workflow.md`, `style-calibration.md` |
| Create or update Story Facts | `creation-paths.md`, `story-facts-workflow.md`, `dialogue-engine.md` |
| Bootstrap, compact, or audit long-term continuity | `long-form-continuity.md`, `continuity-bug-audit.md`; activate Project Profile, Story Facts, planning, or original prose only when evidence requires them |
| Generate, regenerate, or continue chapter/scene prose | `creation-paths.md`, `chapter-pipeline.md`, `dialogue-engine.md`, `narrative-humanizer.md`, `quality-gate.md`, `long-form-continuity.md`, `continuity-bug-audit.md`; add `run-state-protocol.md` only when triggered |
| Revise promoted prose | `creation-paths.md`, `chapter-humanizer-revision-workflow.md`, `chapter-pipeline.md`, `dialogue-engine.md`, `narrative-humanizer.md`, `quality-gate.md`, `long-form-continuity.md`, `continuity-bug-audit.md`; add `run-state-protocol.md` only when triggered |
| Run rolling checkpoint, cross-range, or publication audit | `long-form-continuity.md`, `continuity-bug-audit.md`, `narrative-humanizer.md`, `layered-novel-planning.md`, `quality-gate.md` |
| Maintain this Skill | `skill-change-protocol.md`, `changelog.md` |

Dashboard and audiobook implementation are outside this Skill.

## Project lifecycle

```text
Seed Intake
→ Adaptive Story Discovery
→ Confirmed Story Kernel
→ Initial Style Direction & Optional Style Calibration
→ Project Profile & Style Lock
→ Master Plan
→ Story Facts & Dialogue Profiles
→ Current Volume and Arc
→ Active-only Story Memory
→ Work-Unit Brief
→ Candidate + Combined Audit
→ Seven-Stage Prose Delivery
→ Quality Gate (Score >= 9.5)
→ PROMOTION READY
→ Fresh User Confirmation
→ Promotion & State Update (PROMOTED)
→ Five-Chapter Rolling Checkpoint
→ Arc/Volume Completion Record and Compaction
```

Use `startup-workflow.md` for setup, `style-calibration.md` for style lock, `layered-novel-planning.md` for master/volume/arc ownership, `long-form-continuity.md` for context tiers and current state, and `chapter-pipeline.md` for prose delivery.

## Context policy

Default project work loads hot context only: compact master direction, current volume/arc, relevant Project Profile and Story Facts sections, active `state/writing_lessons.md` summaries, Story Memory, the current brief, the minimum promoted prose needed to establish the starting state, and explicitly activated evidence. Never use a fixed prior-chapter count.

Warm history loads only when triggered. Archive, backups, completed run records, closed audits, superseded plans, old revisions, and historical candidates are cold and excluded by default.

## Ordinary project chapter

An ordinary chapter uses at most three core artifact roles:

```text
work/chapter-XXX/
├── brief.md
├── candidate.md
└── audit.md
```

They are created progressively and loaded by stage. Create a run record, backup, split evidence, or impact analysis only when recovery, multiple candidates, batch revision, source conflict, official overwrite, artifact size, or requested auditability requires it.

## Natural voice & dialogue engine

Core and recurring characters use a Dialogue Profile in Story Facts: current goals, knowledge boundaries, status speech impact, default conversational tactic, pressure shifts, and trusted-counterpart shifts (`references/dialogue-engine.md`). Do not use personality quotas, catchphrases, accents, or verbal gimmicks as substitutes for motive and social strategy. Chapter briefs load at most one compact Voice Cue line for each important speaker.

Secondary characters follow **Functional Character Realism**: partial knowledge, immediate self-preservation stakes, concrete examples over abstract summaries, and natural imperfections.

Draft Writing applies compact prevention rules from `narrative-humanizer.md`: viewpoint ownership, explanation budget, cognition-shaped rhythm, supported incomplete meaning, and no artificial roughness. Prose Stylist must not polish away character-supported hesitation, bias, evasion, asymmetry, interruption, or unfinished thought.

Narrative Humanizer executes a **Dual-Pass Model**:
1. **Structural Naturalness Pass**: macro-level check for smartness inflation, NPC information kiosks, cognitive acceleration, all-service-to-protagonist scenes, and symmetrical paragraph structures.
2. **Surface Naturalness Pass**: micro-level check for sentence cadence, cliché reactions, unearned aphorisms, and over-completion.

Story Fact Check verifies that naturalness passes did not alter story facts, knowledge, or promises.

## Chapter quality gate

Every candidate must satisfy the 7-dimension Quality Gate in `references/quality-gate.md` (Total $\ge$ 9.5 / 10 and no critical category $<$ 9.0 / 10) plus the 8-question Skeptical Reader Test before reaching `PROMOTION READY`. Substantive prose changes invalidate dependent checks and require re-execution.

## Seven-stage prose delivery

1. **Preflight**
2. **Draft Writing**
3. **Content Review** (Character Check, Story Fact & Continuity Check, Chapter Interface Check)
4. **Prose Refinement** (Structural Naturalness → Prose Stylist → Surface Humanizer)
5. **Story Fact Check**
6. **Final Verification & Quality Gate** (`PROMOTION READY`)
7. **Promotion & State Update** (`PROMOTED` — requires fresh explicit user confirmation)

## Completion boundary

Do not report prose delivery complete until applicable stages and triggered checks pass, the candidate reaches `PROMOTION READY`, fresh user confirmation is obtained, official Promotion succeeds, promoted prose and verified Story Memory changes are reread, Stable Setting Candidates remain separate unless confirmed, and no required finding remains blocked or stale.

Stop after the requested work unit. A request for the next chapter authorizes its Preflight, not silent automatic prose generation.