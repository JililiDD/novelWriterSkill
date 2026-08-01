# Completed-Prose Revision Policy — 已完成正文修订策略

Use this for already-written chapter or scene prose. This file owns revision-specific policy only. Execute applicable stages through `chapter-pipeline.md`; load `run-state-protocol.md` only when its triggers apply.

## Contents

- Revision types and scope
- Backup, isolation, and conditional checks
- State effects, batch revision, and completion

## Revision types

### Light revision

Use for bounded line or paragraph changes that preserve scene order and event meaning:

- clarity and rhythm;
- repetition and imagery;
- dialogue naturalness;
- small continuity wording corrections;
- removal of AI-like phrasing or workflow leakage.

Draft Writing and full Content Review may be not applicable only when the scope does not affect structure, action, knowledge, relationships, clues, stable facts, current state, continuity, or evidence.

### Deep revision

Use for substantial pacing, paragraph/scene restructuring, emotional sequencing, or content changes that preserve the approved overall plot contract.

Require an approved revision plan and exact overwrite confirmation before Promotion.

### Regeneration

Use when the user requests a genuinely different realization of the same approved story unit.

Create a separate candidate. Use an optional run record only when multiple candidates, recovery, or source-conflict tracking requires it.

Do not treat regeneration as a large patch over old prose. Use the approved plan, Story Facts, Story Memory, current contract, and protected boundaries as sources; vary staging, pacing, scene structure, descriptive focus, and emotional texture.

## Scope resolution

Before editing, record in the brief:

- creation path, operation, and revision level;
- exact official source, candidate, audit, backup, and target paths;
- approved requested changes;
- protected events, facts, clues, knowledge boundaries, promises, exact phrases, and ending boundary;
- relevant Project Profile and Style Anchors;
- Fact Protection, Plan Boundary, and File Safety triggers;
- whether Story Memory or Stable Setting Candidates may be affected;
- affected downstream chapters or plans when known.

When the user requested review-first behavior, report findings and proposed fixes before editing.

## Backup and isolation

Back up completed promoted prose before every approved overwrite.

Work in `candidate.md`, an explicitly named alternative candidate, or an isolated patch. Do not edit promoted prose during analysis, review, refinement, Story Fact Check, or Final Verification.

A missing or uncertain required backup blocks overwrite.

Keep maintained drafts and promoted prose aligned only through verified Promotion & State Update.

## Revision-specific checks

Apply:

- `continuity-bug-audit.md` for contract, fact, provenance, knowledge, object/resource, timeline, and consequence checks;
- `narrative-humanizer.md` for language-naturalness and Style Anchor checks;
- Story Fact Check for semantic comparison after refinement;
- `long-form-continuity.md` for Context Sources and Proposed Story Memory Changes.

Light revision should use the smallest correction that fixes the issue. Do not turn a line edit into an unapproved rewrite.

## Conditional checks

### Fact Protection

Trigger when a revision touches:

- stable identity or background;
- world/system rule;
- permanent ability or relationship foundation;
- protected secret or knowledge boundary;
- plot-critical object or evidence;
- survival, death, or other permanent state.

A durable change becomes a Stable Setting Candidate and requires separate confirmation before Story Facts update.

### Plan Boundary

Trigger when the revision changes:

- reveal/payoff timing;
- reserved future events;
- arc or volume obligations;
- Story Kernel or reader promise;
- downstream planned causality.

Record affected plans and later chapters. Do not silently reinterpret them.

### File Safety

Official overwrite always triggers:

- source and target verification;
- backup;
- candidate isolation;
- fresh Final Verification;
- post-write reread.

Multiple candidates, batch revision, interruption/recovery, or source conflict may additionally trigger an optional run record and impact analysis.

## State effects

A revision may propose current-state corrections, but the audit must show before, after, and evidence. Final Verification validates the proposed change before Promotion applies it.

A proposed change to stable identity, world rules, Project Profile, master/volume/arc direction, or other durable fact remains a Stable Setting Candidate until explicitly confirmed and written to the correct authority.

## Batch revision

For multiple chapters:

1. divide the range into reviewable batches;
2. apply one approved revision contract and Style Anchor set;
3. back up every promoted file before overwrite;
4. create separate candidates and combined per-chapter audits;
5. create an optional run record because batch coordination and recovery are active triggers;
6. check cross-batch state, knowledge, promises, plan impact, and repeated language;
7. promote only verified selected candidates;
8. update Story Memory and any existing/needed chapter index from verified results;
9. keep unresolved cross-range issues in active `audits/` and archive closed reports.

Do not normalize all chapters into one identical rhythm or voice.

## Completion report

Report:

- revision type and creation path;
- official, candidate, backup, and target paths;
- approved scope completed;
- Character, Story Fact and Continuity, and Language findings;
- triggered conditional checks;
- Story Fact Check result;
- Proposed Story Memory Changes;
- Stable Setting Candidates;
- Final Verification and Promotion evidence;
- downstream impact and remaining accepted risk.

Stop after the requested revision unit. Do not continue to the next chapter automatically.