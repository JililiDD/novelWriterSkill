# Completed-Prose Revision Policy — 已完成正文修订策略

Use this for already-written chapter or scene prose. This file owns revision-specific policy only. Execute applicable stages through `chapter-pipeline.md`, `role-execution-protocol.md`, and `run-state-protocol.md`.

## Revision types

### Light revision

Use for bounded line/paragraph changes that preserve scene order and event meaning:

- clarity and rhythm;
- repetition and imagery;
- dialogue naturalness;
- small continuity wording corrections;
- removal of AI-like phrasing or workflow leakage.

Draft Writing and full Content Review may be not applicable only when the scope does not affect structure, action, knowledge, relationships, clues, canon, continuity, or evidence.

### Deep revision

Use for substantial pacing, paragraph/scene restructuring, emotional sequencing, or content changes that preserve the approved overall plot contract.

Require an approved revision plan and overwrite confirmation before promotion.

### Regeneration

Use when the user requests a genuinely different realization of the same approved story unit. Create a separate `regenerate` run and return to the complete chapter pipeline.

Do not treat regeneration as a large patch over the old prose. Use the approved outline, stable canon, Story Memory, current contract, and protected boundaries as sources; vary staging, pacing, scene structure, descriptive focus, and emotional texture.

## Scope resolution

Before editing, state:

- operation and revision level;
- exact official files and candidate output paths;
- approved requested changes;
- protected events, facts, clues, knowledge boundaries, promises, exact phrases, and ending boundary;
- relevant Project Profile and Style Anchors;
- required backup and confirmation behavior;
- whether Story Memory or stable canon may be affected.

When the user requested review-first behavior, report findings and proposed fixes before editing.

## Backup and isolation

Back up completed official prose before an approved overwrite in every mode. Production requires durable backup evidence.

Work in a new candidate or isolated patch. Do not edit the official chapter during analysis, review, refinement, Story Fact Check, or Final Verification.

Keep a maintained draft and official final aligned only through the verified Promotion & State Update step.

## Revision-specific checks

Apply the canonical quality owners:

- `continuity-bug-audit.md` for contract, fact, provenance, knowledge, object/resource, timeline, and consequence checks;
- `narrative-humanizer.md` for language-naturalness and Style Anchor checks;
- Story Fact Check for semantic equivalence after prose refinement;
- `long-form-continuity.md` for Context Manifest and Proposed Story Memory Delta.

Light revision should use the smallest correction that fixes the issue. Do not turn a line edit into an unapproved rewrite.

## State effects

A revision may propose dynamic-state corrections, but the audit must show before/after/evidence. Final Verification validates the delta before Promotion applies it.

A proposed change to stable identity, world rules, Project Profile, central outline direction, or other durable canon is a Stable Canon Candidate and requires explicit project-level confirmation.

## Batch revision

For multiple chapters:

1. divide the range into reviewable batches;
2. apply one approved revision contract and Style Anchor set;
3. back up every official file before overwrite;
4. create separate candidates and evidence per chapter;
5. run cross-batch checks for state drift, repeated language patterns, required events, and Story Memory consistency;
6. promote only verified selected candidates;
7. run a checkpoint or arc audit when the batch spans a meaningful story segment.

Do not normalize all chapters into one identical rhythm or voice.

## Completion report

Report:

- revision type and mode;
- files and backup paths;
- approved scope completed;
- continuity and Humanizer findings;
- Story Fact Check result;
- Proposed Story Memory Delta result;
- Final Verification and Promotion evidence;
- remaining accepted risk.

Stop after the requested revision unit. Do not continue to the next chapter automatically.