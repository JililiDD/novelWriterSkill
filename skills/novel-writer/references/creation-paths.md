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

Project setup and files are owned by `startup-workflow.md`, `layered-novel-planning.md`, `story-facts-workflow.md`, `long-form-continuity.md`, and `chapter-pipeline.md`.

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
brief.md
candidate.md
audit.md
```

Create and read them progressively under `chapter-pipeline.md`; they are not a mandatory three-file load set. Create an optional run record only when recovery, candidate selection, batch coordination, source conflict, complex overwrite, or explicitly requested execution evidence cannot be handled reliably by those artifacts.

Split evidence only when one combined audit is too large to inspect, a cross-range or publication review requires it, or a source conflict needs an independent record.

## 4. Confirmation rule

Silence is not confirmation. Approval applies only to the named artifact, change, or work unit.

### Standalone Creation

The premise, style, facts, and brief may be confirmed together when the request already supplies enough binding direction. Do not invent a materially different story engine merely to avoid a question.

### Project Creation

Obtain explicit confirmation before first use or material change of:

- Story Kernel;
- Project Profile;
- master-plan direction;
- current volume or arc obligations;
- Story Facts;
- the current work-unit brief.

Also require explicit confirmation for:

- replacing promoted prose;
- choosing among multiple viable candidates;
- accepting unresolved residual risk;
- applying a Stable Setting Candidate.

Reuse prior approval only when the current authority and relevant decision are materially unchanged.

A request for the next unit authorizes its Preflight only. Stop after every requested unit.

## 5. Conflict ownership

When another reference appears to conflict with this file:

1. preserve the universal invariants in `SKILL.md`;
2. let the domain reference own its artifact fields;
3. let this file own path selection, trigger selection, optional persistence, and confirmation renewal;
4. surface any remaining contradiction instead of inventing a compromise.
