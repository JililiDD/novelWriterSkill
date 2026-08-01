# Startup Workflow — 新故事立项与项目初始化

Use this when starting a new story or materially re-establishing an existing project.

Load `creation-paths.md` first. It owns Standalone versus Project Creation, confirmation, conditional checks, and persistence triggers. This file owns startup order and the adaptive Story Discovery Gate. `layered-novel-planning.md` owns persisted master/volume/arc planning.

## Route first

- Use **Standalone Creation** for a self-contained one-shot, scene, experiment, or bounded rewrite that needs no continuing project state. Route to `fanfic-one-shot-mini-gate.md`.
- Use **Project Creation** for any multi-unit, serial, volume-based, shared-setting, or existing-project work requiring continuing planning, stable facts, or current state.

Do not classify by word count alone.

## Contents

- Creation-path routing and project order
- Adaptive Story Discovery and Story Kernel
- Project Profile, master plan, Story Facts, and first volume
- Story Memory, existing projects, and startup boundary

## Project Creation order

1. Seed intake and existing-information scan
2. Adaptive Story Discovery Gate
3. Story Kernel confirmation
4. Style and element selection
5. Compatibility Check and Tone Lock
6. Length, chapter, and volume scale
7. Project Profile confirmation
8. Master-plan confirmation
9. Story Facts confirmation
10. Current-volume and current-arc confirmation
11. Active-only Story Memory initialization
12. Current work-unit Preflight
13. Seven-stage prose delivery

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

Check six dimensions.

### Core appeal

- why the reader would continue;
- what distinguishes the story;
- the central suspense, desire, emotional experience, or transformation promised.

### Protagonist drive

- concrete external goal;
- why action is necessary now;
- what delay or refusal costs;
- first irreversible choice.

Broad wishes such as “become stronger” remain directions until paired with current pressure and consequences.

### Internal contradiction

Identify one behavior, belief, loyalty, fear, value conflict, or coping method capable of producing consequences:

```text
what the protagonist wants
+ how they habitually pursue or protect it
+ the cost that method creates
```

Do not force trauma, diagnosis, or a prescribed character-arc model.

### Opposition

The antagonist or pressure system needs:

- an independent objective or stable operating logic;
- reasoning it considers valid;
- incompatibility with the protagonist's goal, values, or method;
- pressure that continues even if the protagonist does nothing.

Opposition may be a person, faction, institution, environment, social rule, historical force, internal compulsion, or combination.

### Core relationships

Develop only one to three relationships that materially affect the main story:

- what each side wants from the other;
- the important asymmetry in power, knowledge, need, loyalty, or risk;
- what could change or break the relationship;
- how that movement affects the plot.

An isolation-centered story may use a social, ethical, memory, identity, or self-relationship substitute.

### Choice architecture

Clarify:

- **Opening Choice** — the first decision preventing a clean return to the old life;
- **Climactic Choice Direction** — values, goals, loyalties, identities, or costs that cannot all be preserved.

The exact middle and ending events may remain open.

## 3. Conversation rules

- Ask at most two primary questions in one turn.
- Do not re-ask supplied or confirmed information.
- Prefer structural leverage over names, appearance, exact ages, minor backstory, place names, or distant-volume trivia.
- When useful, offer two or three meaningfully different options, explain benefit and risk, and recommend one.
- Let the user combine, reject, replace, or delegate a choice.
- “You decide” authorizes a recommendation, not silent confirmation.
- Challenge weak causality or contradictions directly.
- Stop as soon as completion conditions are met.

Ask only when different answers would materially change:

- the main plot;
- protagonist behavior;
- a core relationship;
- climax or ending direction;
- reader promise.

Low-impact missing details do not block startup.

## 4. Story Kernel handoff

Use the Story Kernel structure owned by `layered-novel-planning.md`.

Show the compact draft and obtain explicit confirmation. Store it at the beginning of `plans/master-plan.md`; do not create a separate Story Development file.

### Completion conditions

A persistent new-story setup may pass when:

1. the story has a recognizable core appeal;
2. the protagonist has a concrete external goal and current pressure;
3. the protagonist has an internal contradiction capable of producing consequences;
4. the opposition has an independent objective or stable pressure logic;
5. at least one core relationship has mutual needs and change pressure, or a justified substitute exists;
6. the opening contains an irreversible choice;
7. the climax has a value-conflict direction;
8. Confirmed, Suggested, Open, and Rejected material are distinguished;
9. the user confirms the Story Kernel.

The gate does not require every volume, character, world detail, midpoint event, or exact ending to be fixed.

## 5. Style, scale, and Project Profile

After Story Kernel confirmation:

1. use `style-and-element-selection.md`, `style-library.md`, `element-library.md`, and `style-element-compatibility.md`;
2. confirm styles, element hierarchy, forbidden tendencies, compatibility constraints, and Tone Lock;
3. define target length, chapter scale, volume expectation, and production cadence;
4. create `state/project_profile.md` under `project-profile-workflow.md`.

Style choices should reinforce the story engine rather than substitute for it.

## 6. Master plan, Story Facts, and first volume

Use `layered-novel-planning.md` to create:

```text
plans/master-plan.md
plans/volumes/volume-001.md
```

The master plan owns Story Kernel, whole-book direction, volume map, active pointer, and full-book boundaries.

The first volume file owns the volume contract, arc map, and active arc. Do not fully detail distant volumes before they affect current decisions.

Use `story-facts-workflow.md` to create `state/story_facts.md` from confirmed decisions only. Suggested or Open directions do not become stable facts automatically.

For each core or recurring character now needed by the first volume, define only a minimum Voice Signature: default tactic, attention bias, speech baseline, and one pressure or relationship shift. Do not complete a cast questionnaire, assign personality quotas, or invent verbal gimmicks for characters who are not yet relevant.

## 7. Story Memory and prose delivery

For Project Creation:

1. initialize only active/open current state under `long-form-continuity.md` and `assets/story-memory.template.md`;
2. create `work/chapter-XXX/brief.md` with Context Sources and Change Impact;
3. confirm the current work-unit brief;
4. let `chapter-pipeline.md` create `candidate.md` when drafting begins and `audit.md` when review begins;
5. load `run-state-protocol.md` only when a run trigger applies.

Do not invent dynamic state merely to fill a template.

## Existing projects

Normalize the active project to the canonical structure before continuing:

```text
plans/master-plan.md
plans/volumes/volume-XXX.md
state/project_profile.md
state/story_facts.md
state/story_memory.md
chapters/
work/
```

1. identify the current sources for style, stable facts, current state, planning, and promoted prose;
2. migrate only active information into the canonical owners;
3. reconstruct a draft Story Kernel from approved plans, stable facts, and promoted prose only when useful;
4. ask only about contradictions or missing drivers blocking future work;
5. obtain confirmation before treating a reconstructed Story Kernel as binding;
6. build or refresh the compact master plan and current volume/arc view;
7. bootstrap active-only Story Memory;
8. archive or delete superseded active files so only one authority remains;
9. continue from the next work-unit Preflight.

Do not backfill every historical chapter. Build `chapters/index.md` only when historical lookup has become costly.

## Boundary

Startup completes when a project has a confirmed Story Kernel, enough approved master/current-volume/current-arc direction, relevant Story Facts, and active current state for the first work-unit Preflight.

Completion of startup does not authorize automatic prose generation or continuation beyond the confirmed work unit.