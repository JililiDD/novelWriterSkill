# Long-Form Continuity — 动态记忆、章节增量与周期审计

Use this reference for serial, multi-arc, multi-volume, or continuity-heavy fiction. It adds long-term memory without a database, new prose stage, or per-chapter context/delta file.

## Authority map

| Information | Owner |
|---|---|
| Style, elements, Tone Lock, reader promise, Style Anchors | Project Profile |
| Stable characters, world/system rules, durable canon | System Bible |
| Current state, knowledge, objects, promises, open consequences | Story Memory |
| Future intended direction | Whole-book/volume/arc plans |
| Current unit obligations and selected context | Brief |
| Events that occurred | Promoted final prose |
| Candidate findings and proposed changes | Audit |

Do not average conflicting sources. Preflight identifies the conflict, checks original evidence, determines the outdated owner, and blocks until resolved.

## Story Memory

Use an established equivalent or create `state/story_memory.md` from `assets/story-memory.template.md`.

It has exactly six top-level sections and stores only active/open dynamic information.

### 1. Current Position

Latest promoted unit, current volume/arc, story-world time, active locations, central pressure, and confirmed next-direction boundary.

### 2. Active Characters

Only changing state that affects future behavior:

- location and condition;
- active goal/restriction;
- relationship phase;
- promise, duty, debt, fear, or unresolved emotional effect;
- current capability limit;
- source evidence.

Stable background, baseline voice, permanent abilities, and long-term identity remain in System Bible.

### 3. Knowledge & Secrets

Track consequential information with:

```text
knows | suspects | false_belief | unknown
```

Record fact/secret, relevant character, acquisition source/basis, disclosure restriction, and original evidence. Do not build a full matrix for irrelevant characters.

### 4. Important Objects & Resources

Track consequential holder/controller, location, condition, quantity/availability, functional/evidence value, and source. Exclude props with no later constraint.

### 5. Foreshadowing & Promises

Allowed states:

```text
planned | planted | reinforced | partially_revealed | resolved | deferred | abandoned
```

Record ID, surface meaning, protected truth/payoff, first source, latest movement, allowed advancement window, earliest reveal/payoff, intended resolution range, prohibited early actions, and affected characters.

Repetition counts as reinforcement only when it adds meaning, pressure, or reinterpretation.

### 6. Open Consequences

Track unfinished effects of injury, exhaustion, exposure, debt, promise, threat, grief, conflict, legal/social risk, witnessed action, depleted resources, or broken trust. Record expected follow-through or a plausible reason for delay.

## Evidence discipline

High-risk entries need source chapter/path and, when practical, a passage locator or concise evidence note. Recheck original prose when identity, survival, secret knowledge, clue custody, first foreshadowing, major promise, object transfer, rule exception, or relationship turn drives new work.

A summary locates evidence; it does not replace it.

## Context Manifest

Put this inside the existing brief:

```markdown
## Context Manifest
### Always Loaded
- Project Profile path/revision:
- Relevant System Bible sections:
- Story Memory Current Position:
### Current Work Unit
- Whole-book/volume/arc sections:
- Approved contract:
- Recent promoted chapters:
### Triggered Context
- Characters:
- Knowledge/secrets:
- Objects/resources:
- Foreshadowing/promises:
- Open consequences:
### Source Evidence Rechecked
- [high-risk fact] -> [chapter/path/passage]
### Intentionally Excluded
- [area] — [why irrelevant]
```

Normally load relevant Project Profile/System Bible sections, current volume/arc, contract, latest one to three promoted chapters, activated Story Memory entries, and original evidence for high-risk entries.

Old characters, secrets, items, injuries, capabilities, relationship turns, promises, and foreshadowing trigger additional reads. Do not load the whole manuscript by default or omit a relevant source merely to save context.

## Proposed Story Memory Delta

Put this inside the existing audit:

```markdown
## Proposed Story Memory Delta
### Add
- [new active/open entry with source]
### Update
- Entry ID:
- Before:
- After:
- Evidence:
### Close
- Entry ID:
- Resolution/evidence:
### Stable Canon Candidates
- Proposed durable change:
- Reason:
- Affected files/chapters/runs:
- User confirmation required: Yes
### No Project-State Change
- [activated category checked and unchanged]
```

Stage ownership:

| Stage | Continuity responsibility |
|---|---|
| Preflight | Build Context Manifest and recheck high-risk evidence |
| Draft Writing | Obey current state, knowledge, promises, and consequences |
| Content Review | Extract and audit Proposed Delta |
| Prose Refinement | Preserve delta meaning |
| Story Fact Check | Compare prose/delta with approved story |
| Final Verification | Validate completeness, before/after, evidence, and ownership |
| Promotion | Apply verified dynamic delta and reread Story Memory |

Only the Orchestrator writes Story Memory.

## Dynamic state versus stable canon

Verified dynamic changes may update Story Memory: location/injury, acquired knowledge, object/resource movement, supported relationship phase, promise movement, and opened/resolved consequence.

Stable Canon Candidates require explicit project-level confirmation: identity/backstory, world/system rule, permanent capability exception, central antagonist/end direction, Project Profile/Style Anchor, or major outline restructuring.

A chapter run proposes but never automatically applies stable canon. After confirmation, update the correct owner and stale/revise affected work as needed.

## Periodic audits

Use `assets/periodic-audit.template.md`.

### Checkpoint

Default every 10 promoted chapters, on request, or when drift/complexity appears. Check Style Anchors, voice convergence, repeated language/ending patterns, arc progress, inactive chapters, overdue/duplicate promises, Story Memory conflicts/size, open consequences, and accumulated stable candidates.

The interval may change in Project Profile.

### Arc

At arc completion, check objective/exit state, escalation/cost, character/relationship movement, volume/spine impact, promises created/advanced/resolved, subplot displacement, and next-arc entry state.

### Volume rebaseline

At volume completion, record durable facts, end-state characters/knowledge/objects, resolved/unresolved promises, carried consequences, plan deviations, confirmed/pending stable candidates, next-volume initial state, and Story Memory compaction.

Long projects should not disable arc and volume audits.

## Compaction

At volume rebaseline:

1. remove resolved entries that no longer constrain future work;
2. retain history in promoted prose and the volume audit;
3. merge duplicates without losing restrictions;
4. move approved durable facts to System Bible;
5. carry forward active/open information only;
6. verify every retained entry still affects decisions.

Do not remove unresolved obligations merely to shorten the file.

## Existing-project bootstrap

Do not backfill the whole novel. Build minimum useful Story Memory from Project Profile, System Bible, current volume/arc, latest one to three promoted chapters, existing ledgers/state files, and current unresolved obligations. Read older chapters only for activated high-risk evidence.

Record uncertainty honestly; unresolved high-risk conflict blocks dependent prose.

## Remediation

Periodic audits do not directly rewrite prose or stable files:

- prose issue -> new revise/regenerate run;
- dynamic-state correction -> proposed and verified Story Memory update;
- stable canon/Project Profile change -> explicit confirmation;
- planning change -> approved outline/volume/arc update.

## Completion checks

A continuity-sensitive prose unit is not complete until the brief contains selected context, high-risk facts have evidence, the audit contains a Proposed Delta or explicit no-state-change result, Final Verification approves it, Promotion applies/rereads verified dynamic state, and stable canon remains unchanged without confirmation.