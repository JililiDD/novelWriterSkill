# Changelog

## v2.4.0 — Selective Visual Emphasis

- Added one-to-three stable Recognition Anchors for core and recurring characters without creating full appearance dossiers.
- Added optional Emphasis Targets for important first appearances, first true observations, meaningful re-entries, transformed states, key locations, and materially changed familiar settings.
- Required important entrances to establish a viewpoint-selected base image using appearance or clothing, action/posture, and scene effect when natural.
- Required key scenes to establish spatial, sensory, and action-relevant anchors progressively rather than through static tours.
- Separated stable Recognition Anchors from temporary clothing, grooming, disguise, injury presentation, and one-scene visual details.
- Added review checks for under-description, appearance inventories, repeated entrance formulas, floating dialogue, decorative scene tours, and viewpoint-invalid detail.
- Added rolling Checkpoint signals for visual-recognition drift and repeated scene-staging patterns.
- Synchronized plugin metadata and documentation to version `2.4.0`.

## v2.3.0 — Minimal Character Voice Signatures

- Separated the Project Profile Dialogue Anchor into a shared dialogue floor rather than a cast-wide voice template.
- Added a four-field Voice Signature for core and recurring characters: default tactic, attention bias, speech baseline, and one pressure or relationship shift.
- Limited chapter briefs to one compact Voice Cue line per important speaker instead of copying character dossiers.
- Added motive- and relationship-based dialogue generation plus a limited speaker-substitution test for meaningful lines.
- Preserved legitimate shared language from family, institution, class, or subculture and exempted functional short lines from forced uniqueness.
- Blocked personality quotas, mandatory catchphrases, accents, verbal tics, and surface archetype labels as substitutes for character differentiation.
- Added cross-window checks for convergence in tactic, attention, cadence, humor method, explanatory precision, and social strategy.
- Synchronized plugin metadata and documentation to version `2.3.0`.

## v2.2.0 — Natural Voice at Source

- Added compact draft-time naturalness guardrails so prose does not defer all anti-template work to the Humanizer pass.
- Required narration, attention, judgment, and dialogue to belong to the active viewpoint, character, relationship, and pressure.
- Added constructedness, over-completion, voice/thought ownership, cognition-shaped rhythm, emotional-stakes, skeptical-reader, and artificial-roughness diagnostics.
- Prevented Prose Stylist from regularizing supported hesitation, bias, evasion, asymmetry, interruption, and unfinished thought.
- Added keep / targeted correction / return-upstream decisions so language revision does not disguise missing motivation, causality, relationship movement, or scene construction.
- Added cross-window drift checks for repeated over-completion, manufactured depth, converging attention, and formulaic roughness.
- Preserved Story Fact Check after every Humanizer change and synchronized metadata and documentation to version `2.2.0`.

## v2.1.0 — Rolling Checkpoint Audits

- Added a default rolling Checkpoint every five promoted chapters for Project Creation.
- Made the previous window's Checkpoint a read-only prerequisite before Draft Writing the first chapter of the next window.
- Limited each Checkpoint to the new five-chapter window, prior unresolved findings and Carry-Forward Constraints, current authorities, and targeted historical evidence instead of repeated full-manuscript review.
- Added baseline rules for previously unaudited projects, including one Chapters 001–010 baseline when appropriate and bounded current-arc/recent-window baselines for longer projects.
- Added three action levels: Blocking Before Next Chapter, Required During Next Window, and Watchlist.
- Added promise/credibility, Story Memory health, arc/volume capacity, and narrative-pattern checks to the cross-range audit template.
- Added Checkpoint merge priority for coincident Volume and Arc Completion Records and kept audit findings separate from approved repair workflows.
- Synchronized plugin metadata and documentation to version `2.1.0`.

## v2.0.0 — Clean Project Model

- Removed compatibility support for legacy execution modes, System Bible paths, old run schemas, and historical pointer references.
- Renamed the active control references to `creation-paths.md` and `story-facts-workflow.md`.
- Standardized Project Creation on `state/story_facts.md` and the canonical project directory structure.
- Replaced JSON run state, JSON Schema, and the selected-run index with one optional Markdown run record.
- Made `brief.md`, `candidate.md`, and `audit.md` progressive artifact roles instead of a fixed three-file load set, and replaced fixed recent-chapter loading with dependency-driven minimum promoted-prose selection.
- Renamed the cross-range audit asset and excluded obsolete compatibility and companion references from the release package.
- Reduced the release from 38 to 26 canonical Skill files while preserving Story Discovery, planning, seven-stage prose delivery, Story Fact Check, Final Verification, backup-before-overwrite, Promotion, compaction, and no-auto-continue.
- Synchronized plugin metadata and documentation to version `2.0.0`.

## v1.6.0 — Simplified Project Model and Selective Context

- Replaced Fast, Standard, and Production with two user-visible creation paths: Standalone Creation and Project Creation.
- Removed hidden rigor escalation; added explicit Fact Protection, Plan Boundary, and File Safety checks derived from the exact information or operation touched.
- Replaced user-visible canon/System Bible terminology with Story Facts, stable setting, current state, happened events, and future plans while preserving legacy-path compatibility.
- Added `plans/master-plan.md` plus permanent per-volume files with active arc detail, Arc Completion Records, and Volume Completion Records.
- Added hot, warm, and cold context tiers; archive, backups, completed runs, closed audits, superseded plans, old revisions, and historical candidates are excluded by default.
- Simplified ordinary project chapters to `brief.md`, `candidate.md`, and `audit.md`; split evidence, backups, impact analysis, and run state are conditional.
- Made run state optional, added active/archive retirement, and upgraded its lightweight pointer schema/templates to version `1.2` with `creation_path`, trigger reasons, artifact paths, high-risk input observations, candidate selection, and stage statuses.
- Removed the duplicated role protocol from the default loading chain; `chapter-pipeline.md` now solely owns stage responsibility and handoff.
- Reduced the former execution-mode control reference to creation-path routing, conditional triggers, optional persistence, and confirmation renewal.
- Replaced the fixed ten-chapter checkpoint default with request-, signal-, or user-interval-based cross-range audits.
- Simplified Project Profile's role-specific generation fields into compact delivery and revision boundaries.
- Made `chapters/index.md` an optional navigation aid rather than a mandatory project artifact.
- Moved arc/volume rebaseline into their planning Completion Records and reserved periodic audit files for checkpoint, cross-range, and publication issues.
- Synchronized plugin metadata and documentation to version `1.6.0`.

## v1.5.0 — Adaptive Story Discovery

- Added an adaptive Story Discovery Gate before style selection and formal planning for persistent new-story setup.
- Added a compact Story Kernel covering core appeal, protagonist drive, internal contradiction, opposition logic, core relationship pressure, first irreversible choice, and climactic value conflict.
- Limited discovery to high-leverage structural gaps, at most two primary questions per turn, and explicit separation of Confirmed, Suggested, Open, and Rejected material.
- Added Fast, Standard, and Production behavior without creating a new reference, template, state file, schema, run type, or prose stage.
- Made the Story Kernel the first section of the existing whole-book plan and required renewed confirmation for material story-engine changes.
- Prevented System Bible and Project Profile creation from silently promoting assistant suggestions or unresolved Story Kernel decisions into canon.
- Updated plugin metadata and documentation to version `1.5.0`.

## v1.4.0 — Long-form continuity and architecture simplification

- Added one active-only `state/story_memory.md` model for Current Position, Active Characters, Knowledge & Secrets, Important Objects & Resources, Foreshadowing & Promises, and Open Consequences.
- Added source-backed Context Manifest assembly inside existing work-unit briefs and Proposed Story Memory Delta inside existing chapter audits; Final Verification approves the delta before Promotion applies it.
- Added checkpoint, arc, and volume audit behavior plus Story Memory compaction/rebaseline templates without adding a new prose stage, database, CLI, or runtime layer.
- Clarified single ownership: Project Profile owns style/reader experience and Style Anchors, System Bible owns stable canon, Story Memory owns dynamic state, outlines own future intent, and promoted prose owns original event evidence.
- Consolidated duplicate long-novel planning into one canonical layered planning reference and converted overlapping planning, provenance, continuation, and pitfalls files into compatibility pointers.
- Made Continuity & Story Logic Audit the factual-quality owner and Narrative Humanizer the language-quality owner; reduced completed-prose revision guidance to revision-specific policy.
- Replaced the fixed style menu and exhaustive compatibility catalogue with premise-relevant library selection and a compact four-dimension compatibility framework.
- Moved dashboard/mobile-reader and audiobook/TTS implementation out of core routing, retaining only safe companion handoff boundaries without fixed ports, process-kill commands, or time-sensitive model recommendations.
- Preserved the seven-stage prose workflow and run-state schemas while synchronizing version `1.4.0` metadata and distribution.
- Added matching Claude Code and Codex plugin manifests, GitHub marketplace metadata, installation documentation, and an MIT license so the repository can be installed directly as `novel-writer@novel-writer`.

## v1.3.0 — Resumable prose-run state

- Added a pure-Skill run-state protocol for chapter, scene, and one-shot generation, regeneration, revision, and audit work.
- Added one JSON snapshot per run, a small selected-run index, reusable templates, and Draft 2020-12 schemas without adding a CLI, database, runtime adapter, event log, or workflow engine.
- Replaced the nine top-level role sequence with seven stages: Preflight, Draft Writing, Content Review, Prose Refinement, Story Fact Check, Final Verification, and Promotion & State Update.
- Renamed the drafting role to Draft Writer and the post-Humanizer semantic gate to Story Fact Check while preserving all protected plot, clue, knowledge, canon, beat, phrase, foreshadowing, and boundary checks.
- Added pause, block, stale, cancellation, recovery, freshness, applicability, and downstream invalidation rules with Orchestrator-only state ownership.
- Added multiple candidate runs, explicit selected-run switching, verification-before-promotion, risk-based overwrite confirmation, and post-write reread evidence.
- Preserved existing planning workflows and project files without requiring run-state backfill.

## v1.2.0 — Execution modes and control-plane refactor

- Added Fast, Standard, and Production execution modes with Standard as the default and explicit eligibility, persistence, escalation, and shortcut boundaries.
- Added one confirmation-gate matrix covering premise, style and Tone Lock, Project Profile, outline, System Bible, detailed plot outline, current preflight, deep revision or regeneration, and next-unit continuation.
- Added a platform-independent nine-stage role execution protocol supporting inspectable subagents or isolated sequential passes with identical ownership and pass/fail semantics.
- Reduced `SKILL.md` from 263 lines to a compact control plane that routes detailed startup, generation, continuation, revision, dashboard, and TTS workflows to focused references.
- Reconciled startup, one-shot, chapter, continuation, and completed-prose revision references with the shared mode, confirmation, role, correction, and merge policies.
- Preserved existing quality requirements, including project-file inspection, binding briefs, completed-prose backups, continuity severity, forbidden-prose leakage checks, Humanizer boundaries, Fact Lock, Final Verification, and no automatic chapter continuation.

## v1.1.0 — Skill standardization

- Unified the public name as `novel-writer` / “Novel Writer” and corrected the legacy misspelling in manifests and documentation.
- Reduced `SKILL.md` frontmatter to `name` and `description` and replaced the duplicated provider-specific entrypoint with one platform-neutral control plane.
- Replaced provider-specific delegation terminology with available-subagent or isolated sequential-pass guidance.
- Added `agents/openai.yaml` for ChatGPT Skill metadata.
- Moved book-specific notes out of the reusable Skill into repository-level `project-notes/`.
- Generalized project-derived examples, paths, dashboard instructions, and TTS environment assumptions.
- Added validation and standard `skill.zip` packaging.

The sections below preserve the imported workflow's earlier internal history.

## Unreleased

- Chapter preflight now explicitly reads the prior final chapter and prior audit/Fact Lock when available, preventing next-chapter briefs from relying only on memory or the outline.
- Added chapter boundary control for multi-chapter events: preflight must state what must not be resolved yet and the exact hand-off hook.
- Parent verification now checks target length and whether reserved next-chapter events were accidentally resolved early.

## v2.6.2 — Project Profile workflow

- Added `project-profile-workflow.md` for per-book `state/project_profile.md`.
- Startup flow now creates Project Profile after style/element/tone/length confirmation and before outline/System Bible.
- Added an explicit Project Profile draft confirmation gate before writing `state/project_profile.md`.
- Chapter preflight now reads `state/project_profile.md` when available and includes project profile constraints in chapter briefs.
- Completed-chapter revision now preserves project profile style/tone/element logic.
- System Bible workflow now references/summarizes Project Profile without duplicating the whole file.
- Synchronized `SKILL.md` frontmatter version to `2.6.2`.
- Main `SKILL.md` routing/index now includes Project Profile creation/update.

## v2.6.1 — Step 2A style/element library expansion

- Expanded `style-library.md` with richer Chinese novel/web-novel styles: 废土诗意感, 新怪谈感, 克苏鲁低语感, 市井烟火气, 港风江湖, 赛博冷感, 荒诞寓言, 现实主义冷叙事, 短剧强钩子风, 晋江细腻情绪流, 起点升级爽文风, 日式轻小说吐槽流, 民俗志怪感, 权谋厚重感, 治愈温暖感.
- Expanded `element-library.md` with web-novel mechanisms, emotional/relationship elements, suspense/horror elements, and organization/growth elements.
- Added `style-element-compatibility.md` for strong/conditional/high-risk style-element combinations.
- Updated `style-and-element-selection.md` to require compatibility analysis before length/chapter scale.

## v2.6.0 — Modular refactor

- Slimmed main `SKILL.md` into a hard-rule + module index structure.
- Added skill modification safety protocol: discuss first, modify only after explicit user confirmation.
- Added project notes policy: do not embed full novel manuscripts or large project context into universal references.
- Added startup workflow: topic → style → element mix → tone lock → length → outline → system bible → plot outline → chapters.
- Added style and element selection workflow.
- Added built-in style library and element library.
- Added library expansion protocol for user-defined styles/elements.
- Added chapter pipeline reference.
- Added system bible workflow reference.

## v2.5.x — Previous session-learned improvements

- Narrative Humanizer added as a genre-neutral prose integrity pass.
- Continuity Bug Audit generalized into state/knowledge/object/scene/language/cause ledgers.
- Chapter revision workflow added for already-written chapters.
- Dashboard/mobile/audiobook references split out as supporting modules.
