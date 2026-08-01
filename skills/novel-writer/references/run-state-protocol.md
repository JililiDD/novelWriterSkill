# Optional Run Record

Use a run record only when ordinary `brief.md`, `candidate.md`, and `audit.md` cannot reliably handle recovery, candidate selection, batch coordination, source conflict, or a complex overwrite.

Chapter procedure and stage ownership belong to `chapter-pipeline.md`. The run record points to those artifacts; it does not duplicate their findings or evidence.

## 1. Creation triggers

Create a run record only for one or more of:

- interruption or recovery;
- multiple viable candidates;
- batch revision across promoted files;
- source conflict or uncertain freshness;
- a promoted-prose overwrite with complex downstream impact;
- explicitly requested durable execution evidence;
- an audit too large to inspect reliably as one file.

Record the trigger in `brief.md` and in the run record.

Do not use run records for Story Kernel, Project Profile, Story Facts, master plans, volume plans, or ordinary planning confirmation.

## 2. Files

Use:

```text
runs/
├── active/
│   └── <run-id>.md
└── archive/
    └── <run-id>.md
```

Run ID:

```text
<work-unit-id>-<YYYYMMDD>-<sequence>
```

Start from `assets/run-state.template.md`.

A work unit normally uses one run record containing all viable candidate paths and one selected candidate. Do not create a separate selection index.

## 3. Record contents

Keep only:

- run ID, trigger reasons, work unit, operation, and revision level;
- paths to brief, candidates, selected candidate, audit, promoted target, and required backup;
- observations for high-risk inputs whose equality matters;
- one status for each seven-stage step;
- one blocking reason and short notes.

Do not copy into the run record:

- review findings;
- Proposed Story Memory Changes;
- Stable Setting Candidates;
- detailed role inputs and outputs;
- Final Verification evidence;
- Promotion Result.

Those belong in `audit.md` and the referenced project artifacts.

## 4. Stage and status model

Fixed stage order:

```text
preflight
draft_writing
content_review
prose_refinement
story_fact_check
final_verification
promotion_state_update
```

Allowed statuses:

```text
pending
active
paused
passed
blocked
stale
cancelled
not_applicable
```

At most one stage may be `active`.

Use `not_applicable` only when the operation genuinely omits a stage:

| Operation | Default stages |
|---|---|
| Generate / Regenerate | all seven |
| Light revision | Preflight, Prose Refinement, Story Fact Check, Final Verification, Promotion |
| Deep revision | Preflight, Content Review, Prose Refinement, Story Fact Check, Final Verification, Promotion; Draft Writing when required |
| Audit | Preflight, Content Review, Final Verification |

Make an omitted stage applicable when the actual change or a triggered risk requires it.

## 5. Resume and stale behavior

Resume from the earliest applicable stage whose status is:

```text
stale | blocked | paused | active | pending
```

When an input or candidate materially changes:

1. mark the earliest affected stage `stale`;
2. mark every downstream applicable stage `stale`;
3. update the referenced candidate or input observation;
4. rerun from the earliest stale stage.

Without a run record, record the same rerun decision in `audit.md`.

## 6. Freshness

Record only high-risk inputs whose equality matters to the trigger, such as Story Memory, the promoted chapter being overwritten, or a candidate awaiting selection.

Evidence may use an explicit revision, SHA-256, or observed modification time. Compare available evidence in that order. If changed, stale affected stages. If unknown and safety depends on equality, perform the full affected recheck or block.

Never invent integrity evidence.

## 7. Candidate selection

- The first and only candidate may be selected automatically.
- Multiple viable candidates require explicit user selection.
- The selected candidate must be listed in the run record before Promotion.
- Recheck freshness after delayed selection.
- Minor corrections to one candidate do not create a parallel-candidate system.

## 8. Promotion safety

Promotion requires:

- the selected candidate when selection applies;
- fresh passing Final Verification in `audit.md`;
- an unambiguous promoted target;
- a completed backup when overwrite triggers it;
- verified Story Memory changes;
- no unconfirmed Stable Setting Candidate scheduled for automatic application.

Promotion uses the exact verified candidate, rereads promoted prose and updated Story Memory, records the result in `audit.md`, then updates the run status.

## 9. Retirement

After successful Promotion:

1. move the record from `runs/active/` to `runs/archive/`;
2. keep it outside ordinary chapter context;
3. delete it when trusted project history already preserves enough recovery evidence and durable execution evidence was not requested.

## 10. Completion

A run record is complete when applicable stages pass, required Promotion succeeds, promoted prose and Story Memory are reread, and no required stage remains active, paused, blocked, stale, or pending.
