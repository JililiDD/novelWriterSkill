# Creation Paths, Triggers, and Confirmation

Use this reference only for:

- choosing Standalone or Project Creation;
- selecting conditional checks and optional artifacts;
- deciding when confirmation must be renewed.

Universal quality rules belong to `SKILL.md`. Project files belong to their domain references. Chapter artifacts and stage procedure belong to `chapter-pipeline.md`.

## 1. Choose the creation path

### Standalone Creation

Use only when the requested unit is self-contained and all are true:

- no later unit depends on its state;
- no project authority must be updated;
- no shared-setting or serial continuity must be preserved;
- one compact brief can govern the work.

Typical examples: a one-shot, isolated scene, experiment, or bounded rewrite supplied in the request.

Use `fanfic-one-shot-mini-gate.md`. Default deliverables are `brief.md`, `candidate.md`, `audit.md`, and `final.md`.

### Project Creation

Use when any are true:

- the work belongs to an existing novel, serial, series, or shared setting;
- later units depend on its characters, relationships, knowledge, objects, promises, or consequences;
- the user is building a multi-chapter or multi-volume project;
- Project Profile, Story Facts, Story Memory, plans, or promoted chapters must be read or updated;
- the unit establishes continuing story truth.

A short chapter in an existing novel is Project Creation. A long one-shot may remain Standalone Creation. Do not classify by word count alone.

Project setup and files are owned by `startup-workflow.md`, `style-calibration.md`, `layered-novel-planning.md`, `story-facts-workflow.md`, `long-form-continuity.md`, and `chapter-pipeline.md`.

## 2. Add only triggered checks

Preflight records only trigger classes that actually apply.

### Fact Protection

Trigger when the work touches:

- stable identity, background, relationship foundation, world rule, or capability limit;
- protected secret or knowledge boundary;
- plot-critical object, resource, or evidence;
- permanent character, relationship, or capability change;
- conflicting claims about happened events.

Add only the relevant comparison: protected fact, who-knows-what, object custody, permanent-change impact, or original promoted-prose evidence.

A proposed stable-setting change remains a **Stable Setting Candidate** until explicitly confirmed.

### Plan Boundary

Trigger when the work touches:

- reveal or payoff windows;
- events reserved for a later unit;
- volume or arc requirements and protected open threads;
- reader promises;
- Story Kernel or climax value-conflict constraints;
- a plan change with downstream impact.

Add only the relevant check: reveal timing, reserved-event preservation, promise movement, current volume/arc compliance, or downstream plan impact.

### File Safety

Trigger when the operation involves:

- overwriting promoted prose;
- multiple viable candidates;
- batch revision;
- interruption or recovery;
- source conflict or uncertain freshness;
- ambiguous source or target paths.

Add only the required safeguard: backup, candidate selection, optional run record, freshness comparison, impact analysis, or post-write reread.

Do not create run records, backups, split evidence, or impact-analysis files without a matching trigger.

## 3. Persistence rule

Ordinary Project Creation uses at most three core artifact roles:

```text
work/chapter-XXX/
├── brief.md
├── candidate.md
└── audit.md
```

Create and read them progressively under `chapter-pipeline.md`. Candidate prose remains isolated and possesses zero authority until officially promoted.

## 4. Confirmation rules

Silence is not confirmation. Approval applies only to the named artifact, change, or work unit.

### Project Creation Confirmation Gates

Obtain explicit confirmation before first use or material change of:

- Story Kernel;
- Project Profile (Style Lock & Narrative Anchor);
- master-plan direction;
- current volume or arc obligations;
- Story Facts and Dialogue Profiles;
- project craft lessons (`state/writing_lessons.md`);
- the current work-unit brief.

### Mandatory Promotion Confirmation Gate

1. Final Verification passing verdict strictly yields **`PROMOTION READY`**, never silent Promotion.
2. Candidate prose and proposed Story Memory changes must **never** be written to official project files (`chapters/chapter-XXX.md`, `state/story_memory.md`) without a fresh, explicit user confirmation in the current turn.
3. **Fresh Confirmation Requirement**: Even if the user stated *"改完直接替换"* at the beginning of the turn, the assistant must still present the `PROMOTION READY` status, quality gate score, and verification summary, and request final promotion confirmation before modifying official project files.
4. **Valid Promotion Authorizations**: *"可以 promote"*, *"就用这版"*, *"正式替换吧"*, *"定为正式章节"*.
5. **Invalid / Insufficient Authorizations**: *"改一下第二章"*, *"润色一下"*, *"给我看看"*, *"继续检查"*, *"做到 9.5 分以上"*.

### Autonomous Batch Mode Delegation (自动化连写授权)

When the user explicitly requests multi-chapter autonomous drafting (e.g. *"自动连写第 5 到 10 章"*, *"按大纲写完第一卷"*, or slash command `/goal`):
1. The user grants **Bounded Batch Promotion Delegation** across the specified range $[M..N]$.
2. Within this bounded scope, the system autonomously executes drafting, dual-pass humanization, quality gate scoring, promotion, and memory updates per `references/autonomous-batch-pipeline.md`.
3. **Circuit Breakers**: If any chapter fails the quality gate ($< 9.5$) after 2 automated repair passes, encounters an unresolvable story fact conflict, or hits a blocking 5-chapter checkpoint audit, the delegation is **immediately suspended**, and the assistant pauses to request human review.

Outside of an explicit Autonomous Batch command, stop after every requested unit.

## 5. Conflict ownership

When another reference appears to conflict with this file:

1. preserve the universal invariants in `SKILL.md`;
2. let the domain reference own its artifact fields;
3. let this file own path selection, trigger selection, optional persistence, and confirmation renewal;
4. surface any remaining contradiction instead of inventing a compromise.
