# Chapter / Scene Delivery Workflow

Use this after planning and current-unit confirmation are satisfied.

Load:

- `execution-modes.md` — confirmation/mode;
- `run-state-protocol.md` — persistence/recovery/selection/promotion eligibility;
- `role-execution-protocol.md` — responsibility and handoff;
- `long-form-continuity.md` — Story Memory, Context Manifest, delta;
- `continuity-bug-audit.md` — factual quality;
- `narrative-humanizer.md` — language quality.

This file owns prose-delivery artifacts and stage application, not the mode/state/role definitions themselves.

## Default project artifacts

Follow project conventions or use:

```text
state/project_profile.md
state/system_bible.md
state/story_memory.md
state/chapterXX_brief.md
state/runs/
drafts/
chapters/
audits/
```

Project Profile owns style/reader experience; System Bible stable canon; Story Memory current dynamic state; outlines future intent; promoted prose original event evidence.

## Work-unit brief

Create/refresh a brief containing:

```markdown
# Work-Unit Brief
## Identity
- Type/ID, operation/revision, mode, POV, title, target size
## Approved Contract
- Starting state
- Required event chain/turning point
- Required/forbidden characters
- Emotional movement
- Callbacks/foreshadowing and allowed secret movement
- Exact wording, reserved future events, ending boundary
- Forbidden changes
## Project Profile Constraints
- Relevant style/elements/Tone Lock/Style Anchors/drift risks
## Continuity Hazards
- Character/relationship, knowledge, objects/resources, timeline/location, provenance, open consequences
## Context Manifest
- Use `long-form-continuity.md`
## Output Plan
- Candidate, audit, official target, backup, verification
```

Apply the current-unit gate. Do not draft until Preflight passes.

## Seven stages

### 1. Preflight

- Resolve project, mode, work unit, operation, candidate/target, selected run, and confirmation.
- Read actual Project Profile, System Bible, Story Memory, current plan, recent promoted prose, and activated evidence.
- Build Context Manifest; recheck original sources for high-risk facts.
- Block on source conflict, missing authority, unclear scope, or unsafe path.
- Set applicability with reasons and initialize state when required.

### 2. Draft Writing

- Draft from the approved contract and selected context.
- Obey current character/knowledge/object/promise/consequence state and Style Anchors.
- Enrich realization without replacing required events or boundaries.
- Save a new candidate; never write directly to official final.
- Keep workflow scaffolding out of prose.

### 3. Content Review

Keep Character Review and Lore & Continuity Audit separately identifiable.

Character Review checks voice, action, motivation, knowledge, relationship/emotional continuity, and required presence.

Lore & Continuity Audit applies `continuity-bug-audit.md`, marks every contract item, assigns severity/owner, separates Stable Canon Candidates, and produces the Proposed Story Memory Delta or explicit no-state-change result.

Blocking corrections create a new candidate and stale this and downstream stages.

### 4. Prose Refinement

Run:

1. Prose Stylist — apply Project Profile/Style Anchors to rhythm, viewpoint, imagery, clarity, and local pacing without semantic change.
2. Narrative Humanizer — apply `narrative-humanizer.md` while preserving facts, contract, and delta meaning.

Keep inputs/outputs traceable; Production persists both.

### 5. Story Fact Check

Compare refined candidate and Proposed Delta with the contract, pre-refinement source, System Bible, Story Memory, and activated evidence.

Block unauthorized changes to event/order, action/intention, presence, knowledge, relationship, clue/evidence/provenance, rules, promises/reveal timing, exact phrases, ending boundary, or delta meaning.

Name compared versions. Corrections return to the owner and rerun affected downstream checks.

### 6. Final Verification

Before any official write, verify:

- candidate/audit/evidence are readable;
- contract and reserved-future boundaries pass;
- length is compliant or exception approved;
- Content Review/Humanizer/Story Fact Check are complete and fresh;
- Context Manifest covers activated authorities/evidence;
- Proposed Delta is complete, source-backed, and dynamic only;
- Stable Canon Candidates are separated from automatic updates;
- candidate/target/backup plan are unambiguous;
- no unrelated state change is proposed.

Record findings only; do not promote or update state.

### 7. Promotion & State Update

For the selected run with fresh passing verification:

- satisfy risk-based confirmation;
- back up official prose before overwrite;
- promote the exact verified candidate without further editing;
- apply only verified dynamic Story Memory/project-state delta;
- leave Stable Canon Candidates pending unless separately confirmed;
- reread official prose and updated state;
- record source, target, backup, changes, and reread evidence.

Unselected verified candidates keep Promotion pending and require freshness after later selection.

## Operations

### Generate

All seven stages for a new official unit.

### Regenerate

Create a separate candidate run. Use approved project truth, not old prose as rewrite base; preserve binding obligations unless changes were approved. Do not replace selection automatically.

### Revise

Use `chapter-humanizer-revision-workflow.md` for light/deep scope, review-first, backup, batching, and overwrite confirmation. Execute applicable stages here.

### Audit

Preflight, Content Review, and Final Verification by default. Do not rewrite prose or state unless the user expands scope into an approved correction.

### One-shot / short scene

Use `fanfic-one-shot-mini-gate.md`. A self-contained Fast unit may use temporary memory; an existing-canon unit still obeys relevant stable/dynamic state.

## Alternative candidates

A genuinely different version uses a separate regenerate run, varies realization rather than merely wording, completes applicable stages, preserves existing selection, and requires explicit candidate/overwrite confirmation before Promotion.

## Completion

Complete only after required Promotion succeeds, official prose and dynamic state are reread, and no required stage remains active, paused, blocked, stale, or pending. Stop after the requested unit; never auto-continue.