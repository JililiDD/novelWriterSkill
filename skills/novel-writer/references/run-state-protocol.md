# Prose Run-State Protocol

Use this reference only for persistence, recovery, freshness, candidate selection, and promotion safety in chapter, scene, and one-shot delivery. Role responsibilities belong to `role-execution-protocol.md`; prose procedure belongs to `chapter-pipeline.md`; long-term dynamic memory belongs to `long-form-continuity.md`.

## Scope and boundary

Supported work units:

```text
chapter
scene
one_shot
```

Supported operations:

```text
generate
regenerate
revise   # revision_level: light | deep
audit    # revision_level: null
```

For non-revise operations set `revision_level` to `null`.

Do not use this state model for premise, Project Profile, System Bible, character/world setup, or outline planning.

Implement through Markdown, JSON templates, and JSON Schema only. Do not imply a CLI, model runner, database, event log, checkpoint engine, lock, transaction, scheduler, background service, generic DAG, or provider adapter.

## Project-local files

Use an established equivalent when documented. Otherwise:

```text
state/runs/
├── index.json
└── <run-id>.json
```

Run ID:

```text
<work-unit-id>-<YYYYMMDD>-<sequence>
```

It is immutable after creation.

Start from:

- `assets/run-state.template.json`
- `assets/run-index.template.json`

Validate against `references/schemas/` when a validator is available.

## Ownership

Only the Orchestrator writes:

- run snapshots and selection index;
- official prose during Promotion;
- verified Story Memory/dynamic-state updates;
- stable canon or Project Profile only after separate project-level confirmation.

Other roles return outputs, evidence, findings, and proposed changes. This is logical ownership, not filesystem concurrency protection.

## Fixed stage order

```text
1. preflight
2. draft_writing
3. content_review
4. prose_refinement
5. story_fact_check
6. final_verification
7. promotion_state_update
```

At most one top-level stage may be `active`. Content Review internal checks may be parallel; Prose Refinement internal passes remain ordered.

## Status model

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

Normal transitions:

```text
pending -> active | cancelled
active -> passed | blocked | paused | cancelled
paused -> active | cancelled
blocked -> active | cancelled
passed -> stale
stale -> active | cancelled
```

Assign `not_applicable` during Preflight with `not_applicable_reason`. Return it to `pending` only after the approved operation/scope changes. Do not reopen a cancelled or successfully promoted run; create a new run.

## Default applicability

| Operation | Applicable stages by default |
|---|---|
| `generate` | all seven |
| `regenerate` | all seven |
| `revise + light` | Preflight, Prose Refinement, Story Fact Check, Final Verification, Promotion |
| `revise + deep` | Preflight, Content Review, Prose Refinement, Story Fact Check, Final Verification, Promotion; Draft Writing when scope requires fresh drafting |
| `audit` | Preflight, Content Review, Final Verification |

Make omitted review/drafting stages applicable whenever actual scope or discovered risk requires them. Never use `not_applicable` to evade a mandatory check.

## Snapshot contents

Store one current snapshot containing:

- schema version;
- immutable run ID;
- created/updated timestamps;
- mode;
- work-unit type/ID;
- operation/revision level;
- seven fixed stage records.

A stage may contain:

- status and timestamps;
- execution batch;
- input/output/evidence artifacts;
- findings;
- blocking/applicability reason;
- notes;
- Content Review checks or Prose Refinement passes.

Do not store derived/history fields:

```text
status
current_stage
resume_from
history
events
```

Git, backups, or an external system own history.

## Derived run view

Derive in this priority:

1. any `blocked` -> blocked;
2. any `paused` -> paused;
3. any `active` -> active;
4. any `stale` -> stale;
5. Final Verification passed + Promotion pending + run not selected -> awaiting selection;
6. every stage passed/not applicable -> completed;
7. every remaining applicable unfinished stage cancelled -> cancelled;
8. otherwise pending.

`awaiting selection` is not stored.

Resume from the earliest applicable stage in fixed order whose status is `stale`, `blocked`, `paused`, `active`, or `pending`.

## Creation and persistence

### Fast

Create run state when any is true:

- interruption/recovery is plausible;
- persistent dynamic state may change;
- multiple logical stages are used;
- the user requests auditability.

### Standard

Create at Preflight start. Persist brief/Context Manifest, necessary evidence, candidate, Proposed Story Memory Delta, Stable Canon Candidates, verification, promotion, and dynamic-state results.

### Production

Create at Preflight start. Persist complete obtainable input snapshots, every internal output, Context Manifest, delta/candidates, blocking findings, backup evidence, and source-to-final traceability.

## Artifact snapshots

```json
{
  "path": "state/story_memory.md",
  "revision": 4,
  "sha256": null,
  "observed_modified_at": "2026-07-29T16:20:00-04:00"
}
```

`path` is required. Other values may be null. Record only obtained evidence; never fabricate hashes, revisions, timestamps, approvals, or files. Production reports incomplete integrity evidence as degraded.

## Freshness

Compare in order:

1. SHA-256 when both sides have it;
2. explicit revision;
3. existence, path, and observed modification time;
4. otherwise unknown.

Results:

- unchanged -> continue from derived resume point;
- changed -> stale affected stage and all downstream applicable stages;
- unknown in Standard -> rerun Final Verification and every earlier check reasonably affected;
- unknown in Production -> block until reliable comparison or full required recheck.

Do not claim equality without supporting evidence.

## Stale propagation

When a stage input/output materially changes:

1. mark that stage `stale`;
2. mark every downstream applicable stage `stale`;
3. preserve prior outputs/evidence;
4. resume from the earliest stale stage.

An internal Content Review or Prose Refinement change stales its parent and downstream applicable stages.

## Candidate selection

`state/runs/index.json` is a selection registry only.

- Auto-select the first and only ordinary run for a work unit.
- A new alternative/parallel run does not replace selection.
- Multiple candidates require explicit user selection to change `selected_run_id`.
- An unselected run may pass Final Verification; Promotion remains pending.
- After later selection, run freshness checks before Promotion.

## Promotion safety

Automatic promotion is allowed only when:

- the run is selected;
- it creates a new official work unit rather than overwriting one;
- no competing candidate needs selection;
- dynamic Story Memory/state delta is normal and verified;
- no unresolved residual risk exists.

Require change summary and confirmation when:

- regenerate or deep revision overwrites official prose;
- selection changes among candidates;
- residual risk is accepted;
- dynamic-state update is abnormal;
- any Stable Canon Candidate would be applied;
- backup is uncertain or missing;
- target differs from the verified plan.

Promotion must use the exact verified candidate, apply only verified dynamic state, leave unconfirmed stable-canon changes pending, reread outputs, record evidence, and stop.

## Completion

A persisted run is complete only when applicable stages pass, selected promotion succeeds where required, official prose and updated dynamic state are reread, no unconfirmed Stable Canon Candidate was applied, and no stage remains active, paused, blocked, stale, or pending.