# Platform-Independent Role Execution Protocol

Use this reference for logical responsibility, input/output isolation, blocking ownership, and handoff. State transitions belong to `run-state-protocol.md`; chapter procedure belongs to `chapter-pipeline.md`; long-term memory belongs to `long-form-continuity.md`.

Roles are contracts, not runtime features. Use inspectable subagents when available or execute the same bounded contracts sequentially.

## Shared contract

Every role/check must have:

- one responsibility;
- approved inputs and allowed reads;
- an isolated output;
- explicit allowed changes and protected content;
- blocking conditions;
- corrective owner/handoff;
- completion evidence.

Shared rules:

- no role silently overwrites another role's source;
- only the Orchestrator writes run/index state;
- only Promotion writes official prose or verified project state;
- later stages cannot hide blocking findings;
- final prose contains no workflow scaffolding;
- at most one top-level stage is active;
- Content Review checks may be parallel;
- Prose Refinement runs Stylist before Humanizer.

## Seven stages

### 1. Preflight — Orchestrator

**Owns:** project/work-unit resolution, mode, operation, confirmation, authoritative inputs, Context Manifest, binding brief, safe output paths, applicability, and run initialization.

**Reads:** user request; approved Project Profile, System Bible, Story Memory, outlines, recent promoted prose, activated original evidence, existing official files, and revision scope.

**Outputs:** approved brief/Context Manifest and run snapshot when persistence applies.

**May change:** routing, brief before approval, applicability, and Orchestrator-owned run fields.

**Must preserve:** approved project files, official prose, user constraints, and mode invariants.

**Blocks on:** unresolved source conflict, missing authority/evidence, missing confirmation, invalid scope, or unsafe/ambiguous paths.

**Pass evidence:** contract, selected context, high-risk evidence, continuity hazards, Style Anchors, operation, outputs, applicability, and verification plan are explicit.

### 2. Draft Writing — Draft Writer

**Owns:** first prose realization of the approved contract.

**Reads:** brief/Context Manifest, relevant Project Profile and Style Anchors, System Bible, Story Memory, activated evidence, arc context, and recent prose when needed.

**Outputs:** new candidate draft, never the official final file.

**May change:** staging, wording, dialogue, pacing, transitions, imagery, and descriptive focus within the contract.

**Must preserve:** events, facts, knowledge, relationships, rules, promises, exact wording obligations, and work-unit boundary.

**Blocks on:** incomplete/contradictory contract or unavailable required source.

**Pass evidence:** readable candidate satisfies every binding item without workflow leakage.

### 3. Content Review

Parent passes only when both applicable checks pass and their findings remain separately identifiable.

#### Character Review

**Owns:** voice, action, motivation, knowledge, relationship, emotional continuity, and required presence/absence.

**Reads:** candidate, brief, relevant System Bible foundations, Story Memory, relationship/knowledge evidence, prior prose, and arc context.

**Outputs:** severity-ranked character findings and correction owner.

**May change:** findings only unless assigned a separate correction.

**Blocks on:** critical character contradiction, impossible knowledge, unsupported relationship turn, broken motivation, or missing required character.

**Pass evidence:** every major character is accounted for across voice, action, knowledge, relationship, and presence.

#### Lore & Continuity Audit

**Owns:** contract compliance, stable/dynamic fact alignment, knowledge, provenance, objects/resources/evidence, timeline/scene feasibility, causality, foreshadowing/promises, leakage, and Proposed Story Memory Delta.

**Reads:** candidate, brief/Context Manifest, System Bible, Story Memory, activated original evidence, arc/outline context, and Character Review when relevant.

**Outputs:** source-backed audit, severity/corrective owner, Proposed Story Memory Delta or explicit no-state-change result, and separated Stable Canon Candidates.

**May change:** findings/proposals only unless assigned a separate correction.

**Blocks on:** critical contradiction, missing contract beat, invalid provenance, impossible state/knowledge, broken rule/timeline/causality, premature reveal, or contract-breaking Major finding.

**Pass evidence:** all activated categories and every contract item are resolved; delta is complete and source-backed.

### 4. Prose Refinement

#### Prose Stylist

**Owns:** rhythm, viewpoint consistency, imagery, clarity, local pacing, and project-style fit.

**Reads:** candidate cleared of blocking review findings, brief, relevant Project Profile/Style Anchors, recent prose for drift, and non-blocking notes.

**Outputs:** new styled candidate.

**May change:** wording, paragraphing, transitions, imagery, and local emphasis.

**Must preserve:** all story meaning and Proposed Story Memory Delta.

**Blocks on:** requested style change would alter contract, facts, or approved Project Profile.

#### Narrative Humanizer

**Owns:** reduction of templated, over-explained, repetitive, generic, or frictionless AI-like expression.

**Reads:** styled candidate, brief, relevant Style Anchors, `narrative-humanizer.md`, recent prose for drift, and the Proposed Delta.

**Outputs:** new humanized candidate plus language findings/drift signals.

**May change:** surface expression and cadence only.

**Must preserve:** events, actions, intentions, knowledge, clues, rules, promises, exact phrases, ending boundary, and delta meaning.

**Blocks on:** language change requires or creates a semantic/state change.

Parent pass evidence: Stylist output feeds Humanizer, both outputs are traceable, and protected meaning remains unchanged.

### 5. Story Fact Check

**Owns:** direct semantic comparison after refinement.

**Reads:** humanized candidate, styled/pre-refinement source, brief, System Bible, Story Memory, activated evidence, and Proposed Delta.

**Outputs:** pass/fail report naming compared versions and differences.

**May change:** findings only.

**Blocks on:** unauthorized change to event/order, action/intention, presence, knowledge, relationship, clue/evidence, rule, promise/reveal, exact phrase, ending boundary, or delta meaning.

**Handoff:** pass to Final Verification; otherwise route to the owning prose/content stage and rerun affected downstream checks.

### 6. Final Verification

**Owns:** independent verification of the complete candidate package before any official write.

**Reads:** candidate, brief/Context Manifest, review evidence, Humanizer result, Story Fact Check, Proposed Delta, Stable Canon Candidates, promotion/backup plan, and authoritative sources.

**Outputs:** pass/fail report, decisive evidence, target paths, and residual risk.

**May change:** findings only.

**Blocks on:** missing/unreadable artifact, incomplete context/review, contract failure, leakage, failed Story Fact Check, unsupported/incomplete delta, stable-canon change scheduled for automatic write, ambiguous target, missing required backup, or unresolved requested verification.

**Pass evidence:** every applicable final check is fresh and the exact promotion/state plan is safe.

### 7. Promotion & State Update — Orchestrator

**Owns:** official promotion and application of already verified dynamic state.

**Reads:** selected run, passing fresh Final Verification, verified candidate/delta, Story Memory, official target, backup plan, and required confirmation.

**Outputs:** official prose, updated verified dynamic state, reread evidence, and promotion record.

**May change:** official artifact, verified Story Memory/dynamic-state fields, explicitly verified ledgers, and Orchestrator-owned run/index state.

**Must preserve:** candidate content, stable canon/Project Profile without separate approval, unrelated state, evidence, backups, and source drafts.

**Blocks on:** unselected run, stale/failed verification, ambiguous source/target, missing confirmation/backup, state conflict, or unconfirmed Stable Canon Candidate.

**Pass evidence:** official output traces to the verified candidate, only verified dynamic delta is applied, stable candidates remain pending unless separately approved, and all written files are reread.

## Correction discipline

1. Record finding and owner.
2. Correct in a new version/isolated output.
3. Stale affected and downstream applicable stages.
4. Rerun the owning role and downstream checks.
5. Promote only the selected candidate with fresh Final Verification.

## Completion

A workflow is complete only after applicable stages pass, selected promotion succeeds where required, verified dynamic state is updated/reread, no stable canon was silently changed, and no stage remains active, paused, blocked, stale, or pending.