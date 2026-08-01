# Long-Form Continuity — Current State, Context Tiers, and Archive Discipline

Use this reference for serialized, multi-arc, multi-volume, or continuity-heavy fiction. It keeps current context compact without losing recoverable history.

## Authority map

| Information | Owner |
|---|---|
| Story engine and full-book direction | `plans/master-plan.md` |
| One volume, its arcs, and completion records | `plans/volumes/volume-XXX.md` |
| Style, elements, Tone Lock, reader promise, Style Anchors | Project Profile |
| Stable confirmed story facts and protected facts | Story Facts |
| Active/open current state | Story Memory |
| Current work-unit obligations and selected context | Brief |
| Happened events and original evidence | Promoted final prose |
| Candidate findings and proposed changes | Audit |

Future plans are not happened events. A summary locates evidence; it does not replace promoted prose.

Do not average conflicting authorities. Preflight identifies the conflict, checks original evidence, determines which owner is outdated, and blocks dependent work until resolved.

## Contents

- Authority map and hot/warm/cold context
- Story Memory and evidence discipline
- Brief context, change impact, and state changes
- Completion compaction, archive retirement, and audits

## Context tiers

### Hot context

Load by default for a Project Creation chapter:

1. Story Kernel, whole-book constraints, and Active Position from `master-plan.md`;
2. current volume summary and active arc;
3. only relevant Project Profile sections and Style Anchors;
4. only relevant Story Facts sections;
5. current Story Memory;
6. current brief;
7. the minimum promoted prose needed to establish the current starting state;
8. historical evidence explicitly activated by the brief or a risk trigger.

### Minimum promoted-prose selection

Do not use a fixed chapter count.

1. Start with the current brief and Story Memory.
2. When the new unit directly continues an earlier unit, read that immediate predecessor first.
3. Check whether time, location, active characters, knowledge, object custody, relationship state, unfinished action, and scene pressure are sufficiently established.
4. If not, expand only to the additional directly relevant predecessor or source chapter.
5. Use Completion Records or an optional chapter index to locate older evidence instead of reading intervening unrelated chapters.
6. Stop as soon as the current starting state and activated dependencies are clear.

A unit may need no prior full chapter, one direct predecessor, several connected units, or one much older evidence chapter. Never load an arc or volume merely for reassurance.

### Warm context

Load only when activated:

- completed arc or previous-volume Completion Records;
- a returning character, relationship, object, faction, location, ability, or secret;
- an old promise or consequence becoming active again;
- an original chapter needed to verify identity, knowledge, object custody, reveal timing, rule exception, survival, or relationship change;
- an unresolved cross-chapter audit issue.

### Cold context

Do not load by default:

- completed work directories;
- rejected or superseded candidates;
- completed run records;
- closed audits;
- backups;
- superseded plans;
- old Project Profile, Story Facts, or Story Memory revisions;
- completed arcs' detailed original planning;
- early brainstorming and abandoned directions.

Load cold context only for recovery, comparison, rollback, version investigation, or source-evidence research.

## Default archive exclusions

The following directories are outside ordinary chapter context unless explicitly activated:

```text
archive/
backups/
runs/archive/
```

Do not treat a file as current merely because it exists. Each information class must have one active authority.

## Story Memory

Use an established equivalent or create:

```text
state/story_memory.md
```

Start from `assets/story-memory.template.md`.

Story Memory has exactly six top-level sections and stores only active/open information.

### 1. Current Position

Track:

- latest promoted work unit;
- current volume and arc;
- story-world time;
- active locations;
- central pressure;
- confirmed next-direction boundary.

### 2. Active Characters

Track only changing state that affects future decisions:

- location and condition;
- active goal or restriction;
- relationship phase;
- promise, duty, debt, fear, or unresolved emotional effect;
- current capability limit;
- temporary communication, behavior, clothing, grooming, disguise, or visible condition shift when it affects future interaction;
- source evidence;
- activation or sensitivity note when needed.

Stable background, compact Voice Signature, limited stable Recognition Anchors, permanent abilities, and long-term identity belong in Story Facts. Story Memory records only temporary departures caused by current fear, secrecy, grief, fatigue, injury, disguise, role, clothing/presentation change, or relationship state.

### 3. Knowledge & Secrets

Use only consequential states:

```text
knows | suspects | false_belief | unknown
```

Track the fact or secret, relevant character, acquisition source, disclosure restriction, evidence, and sensitivity when reveal timing matters.

### 4. Important Objects & Resources

Track only items that constrain later work:

- holder/controller;
- location;
- condition and quantity;
- functional or evidence value;
- source;
- plot importance when critical.

### 5. Foreshadowing & Promises

Active states:

```text
planned | planted | reinforced | partially_revealed | deferred
```

Track surface meaning, protected truth/payoff, source, latest movement, allowed advancement window, earliest reveal/payoff, intended resolution range, and prohibited early actions.

When resolved or abandoned, remove the entry after recording the outcome in the relevant arc or volume Completion Record.

### 6. Open Consequences

Track unfinished effects of injury, exhaustion, exposure, debt, promise, threat, grief, conflict, legal/social risk, witnessed action, depleted resources, or broken trust.

When a consequence closes, remove it after recording the resolution in the relevant Completion Record and ensuring promoted prose contains the original evidence.

## Evidence discipline

High-impact entries need source chapter/path and, when practical, a passage locator or concise evidence note.

Recheck original prose when identity, survival, secret knowledge, clue custody, first foreshadowing, major promise, object transfer, rule exception, or relationship turn drives new work.

Use `chapters/index.md` to locate likely evidence without loading the whole manuscript. The index is a locator, not an authority.

Suggested index pattern:

```markdown
# Chapter Index

| Chapter | POV | Time/location | Key events | Important state changes |
|---|---|---|---|---|
```

## Context Sources in the brief

Put selected context inside `work/chapter-XXX/brief.md`:

```markdown
## Context Sources
### Hot
- Master plan sections:
- Current volume/arc sections:
- Project Profile sections:
- Story Facts sections:
- Story Memory sections:
- Minimum promoted prose selected:
- Why each selected unit is necessary:
- Stop condition reached:

### Warm Activated
- Historical record/source:
- Activation reason:

### Source Evidence Rechecked
- Fact -> chapter/path/passage:

### Cold Excluded
- Area/path -> reason excluded:
```

Do not paste entire authority files into the brief. Record paths and selected sections.

## Change Impact in the brief

Record the exact conditional triggers:

```markdown
## Change Impact
- Fact protection triggered: Yes / No — reason
- Plan boundary triggered: Yes / No — reason
- File safety triggered: Yes / No — reason
- Additional checks required:
- Additional files required:
```

This replaces any hidden rigor or Production classification.

## Proposed Story Memory Changes

Put state changes inside the existing audit:

```markdown
## Proposed Story Memory Changes
### Add
- New active/open entry with source:

### Update
- Entry ID:
- Before:
- After:
- Evidence:

### Close and Compact
- Entry ID:
- Resolution/evidence:
- Completion Record destination:

### Stable Setting Candidates
- Proposed durable change:
- Reason:
- Affected files/chapters/plans:
- User confirmation required: Yes

### No Current-State Change
- Activated category checked and unchanged:
```

Only Promotion & State Update writes verified Story Memory changes. Stable Setting Candidates never apply automatically.

## Stage responsibilities

| Stage | Continuity responsibility |
|---|---|
| Preflight | Select hot/warm context, exclude cold context, record triggers, recheck required evidence |
| Draft Writing | Obey current state, stable facts, knowledge, promises, and plan boundaries |
| Content Review | Produce source-backed findings and proposed Story Memory changes |
| Prose Refinement | Preserve story meaning and proposed changes |
| Story Fact Check | Compare refined prose and proposed changes with protected sources |
| Final Verification | Validate evidence, ownership, exact target, and applicable conditional checks |
| Promotion | Write exact verified prose, apply verified current-state changes, reread outputs |

## Arc and volume compaction

Arc and volume completion records are owned by `layered-novel-planning.md`, not by separate default audit files.

At arc completion:

1. record actual outcome, character/relationship/knowledge/object changes, promises, consequences, and source chapters;
2. carry forward active/open information;
3. remove closed Story Memory entries;
4. retain detailed history in promoted prose;
5. archive obsolete planning detail only when it has recovery value.

At volume completion:

1. complete the Volume Completion Record;
2. move confirmed durable changes to Story Facts;
3. keep pending Stable Setting Candidates separate;
4. carry only active/open information into Story Memory;
5. update master-plan pointers and volume map;
6. leave historical detail outside default context.

Do not remove unresolved obligations merely to shorten Story Memory.

## Work and audit retirement

After successful Promotion:

- remove the completed chapter work directory from hot context;
- archive it intact or compact it into a short work record;
- do not load historical candidates by default;
- move completed optional run records from `runs/active/` to `runs/archive/`;
- keep only unresolved cross-chapter issues under active `audits/`;
- move closed audits to `archive/audits/closed/`;
- never load backups unless recovery, comparison, or overwrite investigation requires them.

A compact work record may contain:

```markdown
# Chapter Work Record
- Brief revision:
- Final candidate:
- Official chapter:
- Promotion date:
- Story Memory changes:
- Stable Setting Candidates:
- Remaining risks:
```

## Rolling checkpoint audits

Project Creation uses a default rolling window of five promoted chapters:

```text
audits/checkpoint_001_005.md
audits/checkpoint_006_010.md
audits/checkpoint_011_015.md
```

Run the previous window's Checkpoint before Preflight for the first chapter of the next window. A request for Chapter 006 therefore permits a missing Chapters 001–005 Checkpoint as a read-only prerequisite, but it does not permit drafting past unresolved blocking findings.

### Review scope

For a normal Checkpoint:

1. fully read and review the five newly promoted chapters in the window;
2. read the previous Checkpoint's unresolved findings and Carry-Forward Constraints;
3. read current Story Memory, the active volume/arc, and only relevant Story Facts and Project Profile sections;
4. reopen older promoted chapters only when a specific promise, fact, object, knowledge boundary, rule, or relationship turn requires original evidence;
5. stop historical expansion when the activated issue is resolved.

Never re-read or re-audit every earlier chapter merely because the manuscript has grown.

### Baseline exceptions

When a project already has up to ten promoted chapters and no prior Checkpoint, one baseline file may cover Chapters 001–010. After that, resume five-chapter windows.

For a much longer unaudited project, do not backfill the entire manuscript. Establish a baseline from the current arc or the most recent five to ten chapters, current authorities, Completion Records, and targeted historical evidence. Record uncovered historical uncertainty honestly.

### Required checks

Each Checkpoint reviews:

- facts and continuity: time, travel, location, presence, recovery, knowledge, objects, money, resources, quantities, rules, and capability limits;
- promises and character credibility: new, advanced, fulfilled, intentionally violated, silently dropped, or overdue commitments and consequences;
- Story Memory health: missing, outdated, conflicting, or closable active entries;
- arc and volume capacity: actual date/position, used chapters, remaining obligations, pacing pressure, time-jump risk, and repeated plot engines;
- narrative patterns: repeated scene structures, conflict variety, exposition repetition, voice drift, and character participation balance.

### Finding levels

Use exactly three action levels:

- **Blocking Before Next Chapter** — the next window cannot safely begin until repaired or explicitly accepted;
- **Required During Next Window** — continuation is possible, but the item must be handled within the next five chapters;
- **Watchlist** — not currently an error, but continued drift would become actionable.

### Carry-forward constraints

Every Checkpoint records unresolved constraints needed by later windows:

```markdown
## Carry-Forward Constraints
- Constraint:
- Source:
- Activation trigger:
- Resolution condition:
```

The next Checkpoint reads these constraints instead of reloading all historical chapters. Original prose is reopened only when the constraint is activated or disputed.

### Read-only boundary

Checkpoint auditing does not modify promoted prose, Story Memory, Story Facts, Project Profile, or confirmed plans. It may propose corrections and a repair set. Apply approved repairs through the normal revision, Story Fact Check, Final Verification, and Promotion workflow.

Use `assets/cross-range-audit.template.md` for rolling Checkpoints and broader timeline, voice, repetition, promise-health, or publication reviews.

Do not create a separate Checkpoint file when an Arc or Volume Completion Record covers the same ending window and includes the Checkpoint fields required by `layered-novel-planning.md`.

Active `audits/` contains current Checkpoints with unresolved findings and other cross-range work that can affect writing. Closed reports leave hot context.

## Existing-project bootstrap

Do not backfill the whole novel.

1. identify the current sources for style, stable facts, current state, planning, and promoted prose;
2. migrate active information into the canonical Project Profile, Story Facts, Story Memory, master-plan, volume, and chapter owners;
3. archive or delete superseded active files so only one authority remains;
4. build the minimum useful master/current-volume/current-arc view;
5. build active-only Story Memory from current unresolved obligations;
6. create `chapters/index.md` only when historical lookup has become costly;
7. read older chapters only for activated evidence;
8. record uncertainty honestly and block only dependent work.

## Completion checks

A continuity-sensitive work unit is not complete until:

- the brief records selected context and triggered checks;
- required high-impact facts have source evidence;
- the audit records proposed Story Memory changes or an explicit no-change result;
- Stable Setting Candidates remain separate;
- Story Fact Check and Final Verification pass;
- Promotion applies and rereads only verified current-state changes;
- no unconfirmed stable-setting change is written.