# Changelog

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
