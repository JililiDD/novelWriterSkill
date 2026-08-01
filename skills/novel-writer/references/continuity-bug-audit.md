# Continuity & Story Logic Audit — 事实、状态、来源与因果审查

Use this as the canonical factual-quality reference for chapter, scene, revision, and cross-range audits. It checks whether story content is possible, authorized, sourced, and causally consistent. It does not judge prose elegance; use `narrative-humanizer.md` for language-naturalness issues.

## Contents

- Sources of truth and audit categories
- Audit procedure and severity
- Required output and boundaries

## Sources of truth

Compare candidate prose against the relevant approved sources:

1. chapter/scene contract;
2. Story Facts for stable confirmed facts and protected facts;
3. Story Memory for active current state;
4. approved master/volume/arc plan for intended direction;
5. promoted chapters for original evidence;
6. Project Profile only where style, reader promise, or prohibited elements affect content acceptability.

When sources conflict, report the conflict and block rather than selecting the convenient version.

## Audit categories

Use only categories relevant to the work unit, but never omit a category that the content activates.

### 1. Contract compliance

Check every binding item from the approved brief:

- required event or turning point;
- required/forbidden character presence;
- reveal and non-reveal boundaries;
- callback or foreshadowing obligation;
- emotional turn;
- exact required wording when applicable;
- work-unit ending boundary;
- events reserved for later units.

Mark each item:

```text
satisfied
partial
missing
contradicted
```

A missing or contradicted central event, required character, reveal boundary, or ending condition is blocking.

### 2. Character state and relationship continuity

Check:

- location and physical condition;
- current goal and immediate motivation;
- capabilities and active limitations;
- relationship phase;
- promises, debts, duties, fears, and unresolved emotional consequences;
- whether behavior follows from established pressure rather than author convenience.

A relationship or personality may change, but the causal bridge must appear in prose or approved planning.

### 3. Knowledge and secret boundaries

For each consequential statement or action, ask:

- Does this character know, suspect, misunderstand, or remain unaware?
- How and when was the information acquired?
- Is certainty being confused with rumor, inference, manipulation, or false belief?
- Has private or narrator-only information leaked into dialogue or action?
- Has a secret been revealed before its permitted window?

Impossible knowledge is blocking when it changes plot, evidence, trust, or a major decision.

### 4. Object, resource, evidence, and capability state

Track only consequential entities:

- ownership and location;
- integrity, damage, copy, destruction, or consumption;
- scarcity and available quantity;
- evidentiary reliability and custody;
- cooldown, cost, energy, money, ammunition, authority, reputation, or team capacity;
- whether an entity reappears after being lost, spent, transferred, or disabled.

Do not create a ledger entry for ordinary detail that has no later consequence.

### 5. Timeline, location, and scene feasibility

Check:

- elapsed time and simultaneous events;
- travel, healing, training, investigation, production, and communication time;
- access, visibility, distance, weather, social control, and physical obstacles;
- whether characters can plausibly speak, move, notice, decide, operate equipment, fight, hide, or recover under the scene pressure;
- whether ages, dates, seasons, schedules, and sequence align.

### 6. Provenance for new named entities

For every newly prominent character, faction, artifact, organization, place, ability, or institution, identify at least one valid source:

- approved outline or volume plan;
- Story Facts;
- earlier clue, document, witness, rumor, relationship, journey, or organizational connection;
- natural discovery caused by the current scene.

A new entity does not need advance mention merely to exist, but it must enter through a plausible story-world path. Do not insert a convenient expert, map location, authority, enemy, or artifact with no causal route.

### 7. Literal, figurative, uncertain, and subjective information

Classify descriptions that may later be mistaken for facts:

```text
literal
figurative
perception
inference
rumor
dream/hallucination
uncertain
```

Do not promote a metaphor, sensation, rumor, dream, or character inference into an objective story fact without a later establishing event.

### 8. Cause and consequence

For every meaningful change, ask what follows.

Examples:

- injury affects later action or receives supported treatment;
- betrayal changes trust or requires a reason it does not;
- public exposure creates social or institutional effects;
- resource expenditure limits later options;
- discovered evidence changes investigation or must remain unusable for a stated reason;
- promises and threats remain active until fulfilled, rejected, or made impossible.

A story may suppress or delay a consequence, but the delay must be plausible and tracked as an open consequence.

### 9. Foreshadowing and reader promises

Check relevant Story Memory entries:

- state and source are correct;
- the current chapter advances only what the allowed window permits;
- protected truth is not explained early;
- reinforcement adds meaning rather than repeating the same clue;
- resolved promises receive an actual payoff;
- newly created promises are captured in the proposed state delta.

### 10. Workflow and meta leakage

Remove genuine planning, role, audit, or chapter-production language from final-intended prose. Use contextual judgment: a word such as “scene,” “reader,” or “chapter” may be legitimate inside the story world, but workflow scaffolding is not.

## Audit procedure

1. Read the approved contract and relevant authoritative state.
2. Extract consequential facts and changes from the candidate.
3. Map each change to prior state and source evidence.
4. Run activated audit categories.
5. Classify severity and identify the corrective owner.
6. Propose the smallest correction that restores correctness without inventing unsupported facts.
7. Extract Proposed Story Memory Changes under `long-form-continuity.md`.
8. Recheck affected categories after correction.

## Severity

- **Critical:** changes plot identity, survival, core evidence, stable rules, protected reveal, central relationship decision, or work-unit contract.
- **Major:** state drift, impossible knowledge/action, unsupported entity, missing consequence, timeline break, or promise failure that damages reader trust.
- **Minor:** localized ambiguity or small continuity issue fixable without changing event meaning.
- **Info:** observation that does not require correction.

Critical findings block. Major findings block when they break the approved contract or downstream logic. Do not hide a blocking factual issue behind prose polish.

## Required output

```markdown
## Continuity & Story Logic Audit

### Sources checked
- Contract:
- Stable story facts:
- Story Memory:
- Original chapter evidence:
- Outline/arc context:

### Contract compliance
- [Requirement]: satisfied / partial / missing / contradicted — evidence

### Activated categories
- Character/relationship:
- Knowledge/secrets:
- Object/resource/evidence:
- Timeline/location/feasibility:
- Provenance:
- Literal/figurative:
- Cause/consequence:
- Foreshadowing/promises:
- Workflow leakage:

### Findings
- [Severity] [Category] — issue, evidence, corrective owner

### Required fixes
- [Minimal targeted correction]

### Proposed Story Memory Changes
- See `long-form-continuity.md` format.

### Stable Setting Candidates
- Proposed durable change, evidence, impact, and confirmation requirement.

Verdict: Pass / Needs targeted revision / Regenerate
```

## Boundaries

- Do not rewrite prose merely to make it more stylish.
- Do not invent new stable story facts to repair a contradiction when a smaller correction exists.
- Do not treat all vivid language as literal.
- Do not force every possible ledger category into every chapter.
- Do not update Story Memory directly; return findings and proposed changes to the Orchestrator.