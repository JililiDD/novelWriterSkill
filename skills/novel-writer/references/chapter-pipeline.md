# Chapter / Scene Delivery Workflow

Use this after planning and current-unit confirmation are satisfied.

Load:

- `creation-paths.md` — creation-path, confirmation, conditional checks, and persistence triggers;
- `long-form-continuity.md` — context tiers, Story Memory, and proposed state changes;
- `continuity-bug-audit.md` — factual quality;
- `narrative-humanizer.md` — language quality;
- `run-state-protocol.md` only when a run-record trigger applies.

This file owns prose-delivery artifacts and seven-stage application.

## Contents

- Project structure and ordinary work files
- Work-unit brief
- Seven-stage delivery
- Audit structure, operations, and completion

## Project structure

Use established equivalents or:

```text
plans/master-plan.md
plans/volumes/volume-XXX.md
state/project_profile.md
state/story_facts.md
state/story_memory.md
chapters/chapter-XXX.md
chapters/index.md              # optional navigation aid
work/chapter-XXX/
├── brief.md
├── candidate.md
└── audit.md
```

Ownership:

- Project Profile — style, reader experience, and shared dialogue floor;
- Story Facts — stable confirmed facts, protected facts, and recurring-character Voice Signatures;
- Story Memory — active/open current state;
- master and volume plans — future intended direction;
- promoted prose — original evidence of happened events;
- brief — current contract and selected context;
- audit — findings, conditional checks, proposed state changes, verification, and promotion record.

Role boundaries:

- the Orchestrator owns Preflight, optional run records, Promotion, and verified Story Memory writes;
- Draft Writing creates candidates and never writes promoted prose;
- review and verification stages write findings/proposals only;
- Prose Stylist and Narrative Humanizer may change expression but not protected story meaning;
- corrections create a new candidate version and invalidate affected downstream checks.

Use subagents when useful or execute the same boundaries sequentially.

## Ordinary artifact roles

An ordinary Project Creation chapter or scene uses at most three core artifact roles:

```text
work/chapter-XXX/
├── brief.md       # contract and selected context
├── candidate.md   # current prose candidate
└── audit.md       # findings, verification, and Promotion record
```

These are responsibility boundaries, not a requirement to create or load all three at once.

Create them progressively:

- Preflight creates or refreshes `brief.md`;
- Draft Writing creates `candidate.md` when prose work begins;
- Content Review creates `audit.md` when findings must be recorded;
- audit-only work may create or refresh `audit.md` without creating a new candidate;
- a direct standalone deliverable may keep equivalent content temporarily when no project persistence is required.

Load only the artifacts and sections required by the active stage. Do not load an entire prior audit when one unresolved finding or Promotion result is sufficient. Logical checks remain separately identifiable inside `audit.md`; they do not require separate permanent files.

Add files only when triggered:

- `backups/...` — official overwrite;
- `runs/active/<run-id>.md` — recovery, multiple candidates, batch work, source conflict, or requested auditability;
- `impact-analysis.md` — multi-unit downstream impact too large for the combined audit;
- separate evidence files — publication/cross-range review or source conflict requiring independent inspection.

## Work-unit brief

Create or refresh `brief.md`:

```markdown
# Work-Unit Brief

## Identity
- Creation path: Standalone | Project
- Type and ID:
- Operation / revision level:
- POV and title:
- Target size:

## Approved Contract
- Starting state:
- Required event chain / turning point:
- Required and forbidden characters:
- Emotional and relationship movement:
- Knowledge boundaries:
- Callbacks, promises, and allowed secret movement:
- Exact wording obligations:
- Reserved future events:
- Ending boundary:
- Forbidden changes:

## Project Profile Constraints
- Relevant style and elements:
- Tone bounds:
- Relevant Style Anchors:
- Shared dialogue-floor constraints:
- Relevant visual-emphasis constraints:
- Forbidden drift:
- Chapter-specific prose risks:

## Active Character Voice Cues
- [Important speaker] — current goal; default tactic; speech baseline; current pressure or relationship shift

## Emphasis Targets
- Important character entrance — character; trigger; reader must retain; POV-selected appearance/clothing cue; character-revealing action or scene effect
- Key scene establishment — location; spatial anchor; dominant sensory anchor; action-relevant object or constraint

## Context Sources
- Use `long-form-continuity.md` hot/warm/cold structure.

## Change Impact
- Fact protection triggered: Yes / No — reason
- Plan boundary triggered: Yes / No — reason
- File safety triggered: Yes / No — reason
- Additional checks required:
- Additional files required:

## Output Plan
- Candidate, when prose work begins:
- Audit, when review begins:
- Official target:
- Backup, when triggered:
- Run record, when triggered:
```

Use only fields activated by the work unit; omit empty checklist lines that add no constraint. Include Voice Cues only for characters whose choices or dialogue materially affect this unit; one compact line per character is normally enough. Include Emphasis Targets only for an important first formal appearance, first true observation, meaningful re-entry/transformed state, key location first appearance, or materially changed familiar setting. Apply the current-unit confirmation gate. Do not draft project prose before the brief passes Preflight.

## Stage-based artifact loading

Use the minimum artifact set needed by the active stage:

| Stage | Default work-artifact reads |
|---|---|
| Preflight | current or prior `brief.md`; the previous rolling Checkpoint when starting a new five-chapter window; prior `audit.md` only for recovery, unresolved findings, or an overwrite decision |
| Draft Writing | approved `brief.md`; current `candidate.md` only when continuing or revising an existing candidate |
| Content Review | approved `brief.md`, current `candidate.md`, and the relevant current `audit.md` sections |
| Prose Refinement | approved `brief.md`, current candidate, and only review findings that constrain refinement |
| Story Fact Check | approved `brief.md`, pre-refinement and refined candidate versions, proposed state changes, and activated fact sources |
| Final Verification | approved `brief.md`, final candidate, relevant complete audit sections, and triggered evidence |
| Promotion | exact verified candidate and the verified Promotion/state-update sections of `audit.md` |

A stage may load more only when a specific dependency, recovery need, or conditional trigger requires it.

## Seven stages

### 1. Preflight

- Resolve creation path, project, work unit, operation, candidate/target, confirmation, and any optional run record.
- When the requested chapter is the first chapter after a completed five-chapter window, verify that the previous window has a passing Checkpoint Audit or a merged Arc/Volume Completion Record.
- If that Checkpoint is missing, perform it as a read-only prerequisite using `long-form-continuity.md`; if **Blocking Before Next Chapter** findings remain, stop before Draft Writing.
- Read only hot context plus explicitly activated warm evidence.
- Exclude cold/archive/backup content unless recovery, comparison, rollback, or evidence investigation requires it.
- Record Context Sources and Change Impact.
- Recheck original promoted prose for high-impact facts.
- Block on unresolved source conflict, missing authority, unclear scope, unsafe path, or missing confirmation.

### 2. Draft Writing

- Draft from the approved brief and selected context.
- Obey Story Facts, Story Memory, active volume/arc, knowledge boundaries, object state, promises, consequences, and Style Anchors.
- Apply the compact draft-time guardrails in `narrative-humanizer.md`: make narration and attention belong to the current viewpoint; do not explain what the scene already conveys; let rhythm follow cognition and pressure; allow supported incomplete meaning; never manufacture roughness.
- Generate important dialogue from the speaker's goal, default tactic, attention bias, relationship, and current pressure. Treat the Dialogue Anchor as a shared floor, not a cast-wide voice template. Do not manufacture distinction through catchphrases, accents, or quirks alone.
- For an activated important-character entrance, establish a usable base image through a small viewpoint-selected combination of appearance or clothing, stable Recognition Anchors, posture/action, and effect on the scene. Include at least one appearance or clothing cue when natural, integrate detail into action, and do not pause for a complete inventory.
- For an activated key-scene establishment, orient the reader with a spatial relationship, a dominant sensory cue, and an action-relevant object or constraint. Reveal additional detail progressively as characters move, observe, or conflict; do not provide a static tour.
- Enrich realization without replacing required events or boundaries.
- Save to `candidate.md` or an explicitly named alternative candidate.
- Never write directly to promoted prose.
- Keep workflow scaffolding out of prose.

### 3. Content Review

Record separately identifiable sections in `audit.md`.

#### Character Check

Check voice, action, motivation, knowledge, relationship/emotional continuity, and required presence or absence. For meaningful decisions, conflict lines, and emotional turns, use a limited speaker-substitution test: if another major character could take the line unchanged without losing motive, attention, relationship strategy, or phrasing, inspect for voice convergence. Do not require functional short lines to be unique.

For an activated important entrance, verify that the reader receives a concrete, viewpoint-valid base image; appearance/clothing, behavior, and scene effect are selected rather than inventoried; later detail adds new meaning rather than repeating the introduction. For an activated key scene, verify enough spatial, sensory, and action grounding to understand what follows without turning the passage into a location tour. Treat both missing grounding and excessive descriptive pause as findings.

#### Story Fact and Continuity Check

Apply `continuity-bug-audit.md` to:

- contract obligations;
- stable and current fact alignment;
- knowledge and protected secrets;
- provenance;
- objects and resources;
- timeline and scene feasibility;
- causality;
- promises and reveal timing;
- workflow leakage.

Produce Proposed Story Memory Changes or an explicit no-current-state-change result. Separate Stable Setting Candidates.

#### Conditional Checks

Run only those triggered in the brief:

- protected fact / secret / knowledge check;
- critical object custody check;
- reveal-window or reserved-event check;
- volume/arc promise check;
- downstream plan impact check;
- overwrite/source-target/freshness check;
- other explicitly justified check.

Blocking corrections create a new candidate version and invalidate affected downstream checks.

### 4. Prose Refinement

Run in order:

1. **Prose Stylist** — improve rhythm, viewpoint, imagery, clarity, and local pacing under Project Profile and Style Anchors without regularizing supported hesitation, bias, evasion, asymmetry, interruption, or unfinished thought.
2. **Narrative Humanizer** — diagnose constructedness, voice/thought ownership, cognition-shaped rhythm, emotional over-explanation, skeptical-reader credibility, and artificial roughness; keep supported polish, make targeted corrections, or return structural problems upstream.

The passes may be temporary. Persist separate outputs only when a conditional evidence requirement justifies them.

### 5. Story Fact Check

Compare the refined candidate and Proposed Story Memory Changes with:

- the approved brief;
- the pre-refinement source;
- relevant Story Facts;
- current Story Memory;
- active master/volume/arc boundaries;
- activated promoted-prose evidence.

Block unauthorized changes to event/order, action/intention, presence, knowledge, relationship, clue/evidence, rules, promises/reveal timing, exact phrases, ending boundary, or proposed-state meaning.

Name the compared versions in `audit.md`.

### 6. Final Verification

Before any official write, verify:

- every artifact required by the actual operation and completed stages is readable;
- contract and reserved-future boundaries pass;
- length is compliant or an exception is approved;
- Character Check, Story Fact and Continuity Check, Language Check, and triggered conditional checks are complete and fresh;
- Narrative Humanizer reports no unresolved constructedness, artificial roughness, or return-upstream finding;
- Context Sources cover the activated authorities and evidence;
- Proposed Story Memory Changes are complete, source-backed, and current-state only;
- Stable Setting Candidates are separated from automatic updates;
- candidate, target, and any required backup/run plan are unambiguous;
- no unrelated state or plan change is proposed.

Record findings only. Do not promote or update state during Final Verification.

### 7. Promotion & State Update

After fresh passing verification:

- satisfy any required overwrite or candidate-selection confirmation;
- create the required backup before overwriting promoted prose;
- promote the exact verified candidate without further editing;
- apply only verified Story Memory changes;
- leave Stable Setting Candidates pending unless separately confirmed;
- update `chapters/index.md` only when it already exists or historical lookup has become costly;
- reread promoted prose and every updated active authority;
- record source, target, backup, state changes, and reread evidence in `audit.md` or the optional run record.

After successful Promotion, the work directory leaves hot context. Archive it intact or compact it under `archive/work/` according to `long-form-continuity.md`.

## Recommended audit structure

```markdown
# Work-Unit Audit

## Contract Check
## Character Check
## Story Fact and Continuity Check
## Language Check

## Conditional Checks
### [Only triggered checks]

## Proposed Story Memory Changes
## Stable Setting Candidates
## Story Fact Check
## Final Verification
## Promotion Result
```

Do not add empty conditional sections merely to imitate rigor.

## Operations

### Generate

Use all seven logical stages for a new promoted unit.

### Regenerate

Create a genuinely different candidate. Preserve approved obligations unless changes were confirmed. Use an optional run record only when multiple candidates or recovery require it. Do not replace an existing selection silently.

### Revise

Use `chapter-humanizer-revision-workflow.md`. Always isolate candidate work and back up promoted prose before overwrite.

### Audit

Run Preflight, Content Review, and Final Verification by default. Do not rewrite prose or state unless the user expands scope into an approved correction.

For a rolling Checkpoint, fully review only the new five-chapter window, inherit unresolved findings and Carry-Forward Constraints from the previous Checkpoint, and reopen older chapters only for activated evidence. Use the three finding levels defined in `long-form-continuity.md`.

### Standalone one-shot or scene

Use `fanfic-one-shot-mini-gate.md`. A self-contained unit may use temporary memory. A unit belonging to an existing project follows Project Creation and reads the relevant project authorities regardless of length.

## Alternative candidates

A genuinely different version may use `candidate-a.md`, `candidate-b.md`, and an optional run record. Explicit selection is required before Promotion when more than one viable candidate exists.

Minor corrections to one candidate do not require a new parallel-candidate system.

## Completion

Complete only after applicable stages pass, required Promotion succeeds, promoted prose and verified Story Memory changes are reread, Stable Setting Candidates remain separate unless confirmed, and no required triggered check remains blocked or stale. The first chapter of a new five-chapter window cannot enter Draft Writing while the previous window has unresolved **Blocking Before Next Chapter** findings.

Stop after the requested work unit. Never auto-continue.