# Startup Workflow — 新故事立项与项目初始化

Use this when starting a new story or materially re-establishing an existing project.

Load `creation-paths.md` first. It owns Standalone versus Project Creation, confirmation, conditional checks, and persistence triggers. This file owns startup order and the adaptive Story Discovery Gate. `layered-novel-planning.md` owns persisted master/volume/arc planning. `style-calibration.md` owns controlled style calibration.

## Route first

- Use **Standalone Creation** for a self-contained one-shot, scene, experiment, or bounded rewrite that needs no continuing project state. Route to `fanfic-one-shot-mini-gate.md`.
- Use **Project Creation** for any multi-unit, serial, volume-based, shared-setting, or existing-project work requiring continuing planning, stable facts, or current state.

Do not classify by word count alone.

## Contents

- Creation-path routing and project order
- Adaptive Story Discovery and Story Kernel
- Optional Style Calibration and Style Lock
- Project Profile, master plan, Story Facts, and first volume
- Story Memory, existing projects, and startup boundary

## Project Creation order

1. Seed intake and existing-information scan
2. Adaptive Story Discovery Gate
3. Story Kernel confirmation
4. Style and element direction
5. Optional **Style Calibration** (2–4 controlled short-scene variants) $\rightarrow$ Style Lock & Narrative Anchor
6. Compatibility Check and Tone Lock
7. Length, chapter, and volume scale
8. Project Profile confirmation (`state/project_profile.md`)
9. Master-plan confirmation (`plans/master-plan.md`)
10. Story Facts confirmation (`state/story_facts.md` with Dialogue Profiles)
11. Current-volume and current-arc confirmation (`plans/volumes/volume-001.md`)
12. Project craft lessons initialization (`state/writing_lessons.md` when applicable)
13. Active-only Story Memory initialization (`state/story_memory.md`)
14. Current work-unit Preflight
15. Seven-stage prose delivery

Do not move into formal project artifacts until the Story Kernel is confirmed.

## 1. Seed intake

Organize what the user already supplied:

- **Known / User-Supplied** — stated facts, intentions, preferences, and constraints;
- **Suggested** — assistant proposals not yet approved;
- **Open** — unresolved decisions that could materially change the story;
- **Rejected** — declined or prohibited directions.

Never present Suggested material as confirmed planning or stable story facts.

## 2. Adaptive Story Discovery Gate

Explore only gaps whose answers could materially change plot, protagonist behavior, core relationships, climax, ending direction, or reader promise. This is not a character questionnaire.

Check six dimensions:
- **Core appeal**: reader promise, central suspense, core emotional experience;
- **Protagonist drive**: external goal, current urgency, first irreversible choice;
- **Internal contradiction**: habitual coping method vs cost produced;
- **Opposition**: independent operating logic incompatible with protagonist;
- **Core relationships**: mutual needs, asymmetry, breaking conditions (1–3 key bonds);
- **Choice architecture**: opening irreversible choice and climactic value conflict.

## 3. Conversation rules

- Ask at most two primary questions in one turn.
- Do not re-ask supplied or confirmed information.
- Offer 2–3 meaningfully distinct structural options with pros/cons when useful.
- Challenge weak causality or contradictions directly.
- Stop as soon as completion conditions are met.

## 4. Story Kernel handoff

Store the confirmed Story Kernel at the top of `plans/master-plan.md`.

### Completion conditions

A persistent new-story setup may pass when:
1. the story has a recognizable core appeal;
2. the protagonist has a concrete external goal and current pressure;
3. the protagonist has an internal contradiction capable of producing consequences;
4. the opposition has an independent objective or stable pressure logic;
5. at least one core relationship has mutual needs and change pressure;
6. the opening contains an irreversible choice;
7. the climax has a value-conflict direction;
8. Confirmed, Suggested, Open, and Rejected material are distinguished;
9. the user confirms the Story Kernel.

## 5. Style Direction, Optional Style Calibration, and Project Profile

After Story Kernel confirmation:

1. Discuss initial style preferences using `style-and-element-selection.md`, `style-library.md`, and `element-library.md`.
2. **Offer Optional Style Calibration** (`references/style-calibration.md`):
   - When the user gives abstract style keywords or lacks a concrete text anchor, offer to generate 2–4 controlled versions (600–1,500 Chinese characters) of a single short scene.
   - User selects, hybridizes, or adjusts the sample to form the **Style Lock**, **Narrative Anchor**, and **Rejected Drift Notes**.
   - If the user declines or already provides an established text anchor, skip straight to Project Profile confirmation.
3. Confirm styles, element hierarchy, forbidden tendencies, compatibility constraints, and Tone Lock.
4. Define target length, chapter scale, volume expectation, and production cadence.
5. Create `state/project_profile.md` under `project-profile-workflow.md`.

## 6. Master plan, Story Facts, and first volume

Use `layered-novel-planning.md` to create:

```text
plans/master-plan.md
plans/volumes/volume-001.md
```

Use `story-facts-workflow.md` and `dialogue-engine.md` to create `state/story_facts.md` from confirmed decisions only:
- Core and recurring characters receive a **Dialogue Profile** (goal, knowledge baseline, status impact, default tactic, pressure shifts, refusal/request style) and 1–3 stable Recognition Anchors.
- Secondary characters operate under **Functional Character Realism** (partial knowledge, self-preservation stakes, concrete facts).

## 7. Story Memory, Project Lessons, and Prose Delivery

For Project Creation:

1. Initialize `state/writing_lessons.md` when project-level craft lessons or failure pattern constraints have been confirmed (`references/feedback-promotion.md`).
2. Initialize only active/open current state in `state/story_memory.md` under `long-form-continuity.md` and `assets/story-memory.template.md`.
3. Create `work/chapter-XXX/brief.md` with Context Sources, Dialogue Cues, and Change Impact.
4. Confirm the current work-unit brief.
5. Proceed through the seven-stage prose delivery pipeline in `chapter-pipeline.md`.

## Existing projects

Normalize existing projects to canonical layout before continuing:
- `plans/master-plan.md`
- `plans/volumes/volume-XXX.md`
- `state/project_profile.md`
- `state/story_facts.md`
- `state/story_memory.md`
- `state/writing_lessons.md` (optional)
- `chapters/`
- `work/`

Bootstrap active-only Story Memory, archive superseded active files, and continue from the next work-unit Preflight.

## Boundary

Startup completes when a project has a confirmed Story Kernel, Project Profile with Style Lock, approved master/volume direction, Story Facts with Dialogue Profiles, and active current state for the first work-unit Preflight.

Completion of startup does not authorize automatic prose generation.