---
name: novel-writer
description: Plan, develop, write, audit, revise, resume, and maintain standalone fiction and persistent novel projects. Use for adaptive Story Kernel discovery, protagonist and relationship development, compact character Voice Signatures and Recognition Anchors, Project Profiles, master/volume/arc planning, stable Story Facts, active Story Memory, selective hot/warm/cold context loading, key-character and key-scene visual emphasis, chapter briefs/candidates/audits, five-chapter rolling checkpoint audits, natural-voice drafting, narrative humanization, seven-stage prose delivery, optional run records, continuity review, revision, completion records, archive compaction, and long-running fiction maintenance. Apply when the user asks to create, continue, recover, review, rewrite, or manage a novel, chapter, scene, one-shot, serial, or multi-volume project.
---

# Novel Writer

Use this Skill as the control plane for structured fiction work. Load only the references required for the current intent.

## Universal invariants

1. Read actual supplied or project files before claiming project state, chapter status, story facts, or existing prose.
2. Keep manuscripts, plans, state, briefs, candidates, audits, archives, and book-specific lessons inside the novel project, not this reusable Skill.
3. Give each information class one current owner: master/volume plans for future direction, Project Profile for style/reader experience, shared dialogue floor, and visual-emphasis tendency; Story Facts for stable confirmed facts, recurring-character Voice Signatures, and limited stable Recognition Anchors; Story Memory for active current state; and promoted prose for original evidence of happened events.
4. Treat every approved contract, plan obligation, exact phrase, knowledge boundary, promise window, protected fact, and forbidden change as binding.
5. Derive prose from the approved Project Profile, relevant Story Facts, Story Memory, active plan, selected evidence, and work-unit brief. Treat the Dialogue Anchor as a shared floor and recurring-character Voice Signatures as individual sources; use activated Recognition Anchors and Emphasis Targets selectively; do not impose one voice or one entrance formula on the cast.
6. Apply naturalness at source: make prose belong to the current viewpoint and pressure, avoid automatic explanation and over-completion, and never manufacture roughness merely to appear human.
7. Keep logical role inputs and outputs isolated. Ordinary findings may share one audit file only when each check remains separately identifiable.
8. Run Story Fact Check after Narrative Humanizer whenever prose changes.
9. Run Final Verification before Promotion & State Update or before reporting a verified final artifact.
10. Stable-setting and Project Profile changes require explicit project-level confirmation; a chapter audit may propose but not silently apply them.
11. Keep planning, audit, role, and workflow scaffolding out of final prose.
12. Never auto-continue to the next chapter or scene. Stop immediately when the user asks to stop.
13. Back up promoted prose before approved overwrite.
14. Modify this Skill only with explicit user authorization; follow `references/skill-change-protocol.md`.

## Creation paths

Load `references/creation-paths.md` whenever routing work, handling confirmation, selecting persistence, or applying conditional checks.

- **Standalone Creation** — self-contained one-shot, scene, experiment, or bounded rewrite with no continuing project state.
- **Project Creation** — multi-unit, serialized, shared-setting, or existing-project work requiring continuing planning, stable facts, or current state.

Length alone does not select the path. There are no rigor modes. Add checks only when the task touches protected facts, plan boundaries, or file-safety risks.

## Route by intent

All paths below are relative to `references/`.

| User intent | References |
|---|---|
| Start or re-establish a persistent novel | `creation-paths.md`, `startup-workflow.md`; load each style, planning, facts, or continuity owner only when its startup step begins |
| Standalone short story, fanfiction, or scene | `creation-paths.md`, `fanfic-one-shot-mini-gate.md`, `chapter-pipeline.md` |
| Select style, elements, compatibility, or Tone Lock | `style-and-element-selection.md`, `style-library.md`, `element-library.md`, `style-element-compatibility.md` |
| Master, volume, arc, tournament, case, or dynamic-cast planning | `creation-paths.md`, `layered-novel-planning.md`; add current project authorities only when the plan depends on them |
| Custom reusable style or element | `library-expansion-protocol.md` plus the relevant library |
| Esports-specific planning | `esports-novel-planning.md` plus the active startup/planning owner |
| Create or update Project Profile | `creation-paths.md`, `project-profile-workflow.md`, `style-and-element-selection.md` |
| Create or update Story Facts | `creation-paths.md`, `story-facts-workflow.md` |
| Bootstrap, compact, or audit long-term continuity | `long-form-continuity.md`, `continuity-bug-audit.md`; activate Project Profile, Story Facts, planning, or original prose only when evidence requires them |
| Generate, regenerate, or continue chapter/scene prose | `creation-paths.md`, `chapter-pipeline.md`, `long-form-continuity.md`, `continuity-bug-audit.md`, `narrative-humanizer.md`; add `run-state-protocol.md` only when triggered |
| Revise promoted prose | `creation-paths.md`, `chapter-humanizer-revision-workflow.md`, `chapter-pipeline.md`, `long-form-continuity.md`, `continuity-bug-audit.md`, `narrative-humanizer.md`; add `run-state-protocol.md` only when triggered |
| Run rolling checkpoint, cross-range, or publication audit | `long-form-continuity.md`, `continuity-bug-audit.md`, `narrative-humanizer.md`, `layered-novel-planning.md` |
| Maintain this Skill | `skill-change-protocol.md`, `project-notes-policy.md`, `changelog.md` |

Dashboard and audiobook implementation are outside this Skill.

## Project lifecycle

```text
Seed Intake
→ Adaptive Story Discovery
→ Confirmed Story Kernel
→ Style / Elements / Tone Lock
→ Project Profile
→ Master Plan
→ Story Facts
→ Current Volume and Arc
→ Active-only Story Memory
→ Work-Unit Brief
→ Candidate + Combined Audit
→ Seven-Stage Prose Delivery
→ Five-Chapter Rolling Checkpoint
→ Arc/Volume Completion Record and Compaction
```

Use `startup-workflow.md` for setup, `layered-novel-planning.md` for master/volume/arc ownership, `long-form-continuity.md` for context tiers and current state, and `chapter-pipeline.md` for prose delivery.

## Context policy

Default project work loads hot context only: compact master direction, current volume/arc, relevant Project Profile and Story Facts sections, Story Memory, the current brief, the minimum promoted prose needed to establish the starting state, and explicitly activated evidence. Never use a fixed prior-chapter count.

Warm history loads only when triggered. Archive, backups, completed run records, closed audits, superseded plans, old revisions, and historical candidates are cold and excluded by default.

## Ordinary project chapter

An ordinary chapter uses at most three core artifact roles:

```text
work/chapter-XXX/
├── brief.md
├── candidate.md
└── audit.md
```

They are created progressively and loaded by stage, not created or read together by default. Create a run record, backup, split evidence, or impact analysis only when recovery, multiple candidates, batch revision, source conflict, official overwrite, artifact size, or requested auditability requires it.

## Natural voice control

Core and recurring characters use a minimum Voice Signature in Story Facts: default tactic, attention bias, speech baseline, and one pressure or relationship shift. Do not use personality quotas, catchphrases, accents, or verbal gimmicks as substitutes for motive and behavior. Chapter briefs load at most one compact Voice Cue line for each important speaker.

Draft Writing applies compact prevention rules from `narrative-humanizer.md`: viewpoint ownership, restrained explanation, cognition-shaped rhythm, supported incomplete meaning, differentiated character strategy, and no artificial roughness. Prose Stylist must not polish away character-supported hesitation, bias, evasion, asymmetry, interruption, or unfinished thought.

Narrative Humanizer then performs the full diagnostic pass, including a limited speaker-substitution test for meaningful lines. It keeps supported overlap, makes targeted corrections to constructedness or voice convergence, blocks manufactured roughness, and returns motivational or structural falseness upstream. Story Fact Check verifies that the naturalness pass did not change story meaning.

## Selective visual emphasis

Core and recurring characters may keep one to three stable Recognition Anchors in Story Facts. Chapter briefs add Emphasis Targets only for an important first formal appearance, first true observation, meaningful re-entry/transformed state, key-location first appearance, or materially changed familiar setting.

Draft Writing gives activated entrances a small viewpoint-selected combination of appearance or clothing, action/posture, and scene effect, then adds later detail only when it gains new meaning. Activated key scenes establish spatial, sensory, and action-relevant anchors progressively. Reviews flag both missing grounding and descriptive inventory, static tours, repeated entrance formulas, or detail that the viewpoint would not naturally notice.

## Rolling checkpoint audits

Project Creation uses rolling windows of five promoted chapters. Before Preflight for the first chapter of a new window, verify that the previous window has a passing Checkpoint Audit or a merged Arc/Volume Completion Record covering the same chapters.

A Checkpoint fully reviews only the new window, then reads the previous checkpoint's unresolved findings and Carry-Forward Constraints, current Story Memory and planning, and only historical chapters activated by a concrete evidence need. Never re-audit all prior chapters by default.

Checkpoint work is read-only. It may propose prose revisions, Story Memory corrections, planning rebaseline, or Stable Setting Candidates, but it does not apply them. Unresolved **Blocking Before Next Chapter** findings stop drafting of the next window until repaired or explicitly accepted.

## Seven-stage prose delivery

1. Preflight
2. Draft Writing
3. Content Review
4. Prose Refinement
5. Story Fact Check
6. Final Verification
7. Promotion & State Update

Content Review keeps Character Check and Story Fact and Continuity Check separately identifiable. Prose Refinement runs Prose Stylist before Narrative Humanizer.

## Completion boundary

Do not report prose delivery complete until applicable stages and triggered checks pass, required Promotion succeeds, promoted prose and verified Story Memory changes are reread, Stable Setting Candidates remain separate unless confirmed, and no required finding remains blocked or stale.

Stop after the requested work unit. A request for the next chapter authorizes its Preflight, not silent automatic prose generation.