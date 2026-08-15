# Chapter / Scene Delivery Workflow

Use this after planning and current-unit confirmation are satisfied.

Load:

- `creation-paths.md` — creation-path, confirmation, conditional checks, and persistence triggers;
- `long-form-continuity.md` — context tiers, Story Memory, and proposed state changes;
- `dialogue-engine.md` — dialogue formula, speaker-substitution check, and NPC realism;
- `continuity-bug-audit.md` — factual quality and chapter interface checks;
- `narrative-humanizer.md` — dual-pass structural and surface naturalness;
- `quality-gate.md` — 7-dimension quality scoring, check invalidation, and skeptical reader test;
- `run-state-protocol.md` only when a run-record trigger applies.

This file owns prose-delivery artifacts, the chapter state machine, and seven-stage execution.

## Contents

- Project structure and ordinary work files
- Chapter state machine
- Work-unit brief
- Seven-stage delivery
- Audit structure, operations, and completion

## Project structure

```text
plans/master-plan.md
plans/volumes/volume-XXX.md
state/project_profile.md
state/story_facts.md
state/story_memory.md
state/writing_lessons.md         # optional project craft lessons
chapters/chapter-XXX.md
chapters/index.md                # optional navigation aid
work/chapter-XXX/
├── brief.md
├── candidate.md
└── audit.md
```

Ownership:

- Project Profile — style, reader experience, Style Lock, and shared dialogue floor;
- Global Writing Rules (`~/.novel-writer/global_writing_rules.md`) — universal linguistic invariants, anti-tautology, and cross-project craft standards;
- Story Facts — stable confirmed facts, protected facts, Dialogue Profiles, and Recognition Anchors;
- Story Memory — active/open current state only;
- `state/writing_lessons.md` — confirmed project craft constraints for this novel (`references/feedback-promotion.md`);
- master and volume plans — future intended direction;
- promoted prose — original evidence of happened events;
- brief — current contract and selected context;
- audit — findings, conditional checks, quality gate scores, verification, and promotion record.

Role boundaries:

- the Orchestrator owns Preflight, optional run records, Final Verification, Promotion confirmation requests, official Promotion, and verified Story Memory writes;
- Draft Writing creates candidates and never writes promoted prose;
- review and verification stages write findings/proposals only;
- Prose Stylist and Narrative Humanizer may change expression but not protected story meaning;
- substantive candidate corrections invalidate affected downstream checks (`references/quality-gate.md`).

## Chapter state machine

```text
PRE-FLIGHT
  ↓
DRAFTING
  ↓
CONTENT REVIEW (Character, Continuity, Chapter Interface)
  ↓
STRUCTURAL NATURALNESS PASS
  ↓
PROSE STYLIST
  ↓
SURFACE HUMANIZER PASS
  ↓
STORY FACT CHECK
  ↓
QUALITY GATE (Score >= 9.5 / 10)
  ↓
FINAL VERIFICATION
  ↓
PROMOTION READY (Candidate meets promotion criteria; official text unchanged)
  ↓
USER CONFIRMATION REQUIRED (Fresh confirmation in current turn)
  ↓
PROMOTION & OVERWRITE BACKUP
  ↓
POST-WRITE REREAD
  ↓
STATE UPDATE (Apply Story Memory delta)
  ↓
PROMOTED
```

### Critical State Definitions

- **NOT READY**: Blocking findings exist or Quality Gate $< 9.5$. Promotion cannot be requested.
- **PROMOTION READY**: All checks pass, Quality Gate $\ge 9.5$, Skeptical Reader Test passes. Candidate is eligible for promotion. `chapters/chapter-XXX.md` and `state/story_memory.md` remain strictly unchanged.
- **PROMOTED**: User explicitly approved promotion in the current turn. Formal chapter is written, backup created, reread verified, and Story Memory updated.

## Ordinary artifact roles

```text
work/chapter-XXX/
├── brief.md       # contract and selected context
├── candidate.md   # current prose candidate
└── audit.md       # findings, Quality Gate, verification, and Promotion record
```

Create them progressively:

- Preflight creates or refreshes `brief.md`;
- Draft Writing creates `candidate.md` when prose work begins;
- Content Review creates `audit.md` when findings must be recorded;
- audit-only work may create or refresh `audit.md` without creating a new candidate.

## Work-unit brief

Create or refresh `brief.md`:

```markdown
# Work-Unit Brief

## Identity
- Creation path: Standalone | Project
- Type and ID:
- Operation / revision level:
- POV and title:
- Target size: [Flexible guidance range, e.g. 2,500–4,000 words; dramatic density first]

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
- Style Lock constraints:
- Tone bounds:
- Relevant Style Anchors:
- Shared dialogue-floor constraints:
- Relevant visual-emphasis constraints:
- Forbidden drift & project craft lessons:
- Chapter-specific prose risks:

## Active Character Dialogue Cues
- [Important speaker] — goal now; tactic; knowledge baseline; pressure/relationship shift

## Emphasis Targets
- Important character entrance — character; trigger; reader must retain; POV appearance cue; action/effect
- Key scene establishment — location; spatial anchor; sensory anchor; action-relevant constraint

## Chapter Interface
- Chapter N-1 ending state:
- Target Chapter N ending state:
- Chapter N+1 handoff expectation:

## Context Sources
- Use `long-form-continuity.md` hot/warm/cold structure.

## Change Impact
- Fact protection triggered: Yes / No — reason
- Plan boundary triggered: Yes / No — reason
- File safety triggered: Yes / No — reason
- Additional checks required:

## Output Plan
- Candidate: `work/chapter-XXX/candidate.md`
- Audit: `work/chapter-XXX/audit.md`
- Official target: `chapters/chapter-XXX.md`
```

## Seven stages

### 1. Preflight
- Resolve creation path, work unit, target, confirmation, and any optional run record.
- If first chapter of a new five-chapter window, verify previous Checkpoint.
- Read hot context only (brief, Story Memory, Dialogue Profiles, relevant Story Facts, minimum promoted prose).
- Cascade-load craft rules: Universal rules from `~/.novel-writer/global_writing_rules.md` and active project lessons from `state/writing_lessons.md`.
- Recheck original promoted prose for high-impact facts.

### 2. Draft Writing
- Draft from approved brief and five positive generation principles (`SKILL.md`).
- Generate dialogue via Dialogue Engine (`references/dialogue-engine.md`). Apply Functional Character Realism for NPCs.
- Apply Explanation Budget: evidence and concrete actions before narration.
- Respect narrative density: Conclude the chapter when dramatic beats and emotional shifts are complete. Never force artificial padding to hit an arbitrary word count ceiling.
- Save to `candidate.md`. Never write directly to official chapters.

### 3. Content Review
Record separately in `audit.md`:
- **Character Check**: Dialogue Engine compliance, Speaker-Substitution Check on consequential lines, NPC realism.
- **Story Fact & Continuity Check**: Contract compliance, timeline, knowledge boundaries, object custody (`references/continuity-bug-audit.md`).
- **Chapter Interface Check**: Continuity of time, place, carried objects, emotional aftermath, and pending action across $N-1 \rightarrow N \rightarrow N+1$.
- **Conditional Checks**: Run triggered Fact Protection, Plan Boundary, or File Safety checks.

### 4. Prose Refinement
Execute in strict sequence:
1. **Structural Naturalness Pass**: macro check for smartness inflation, NPC info kiosks, instant comprehension, paragraph symmetry, all-service-to-protagonist scenes (`references/narrative-humanizer.md`).
2. **Prose Stylist**: improve rhythm, viewpoint imagery, clarity, and pacing without regularizing supported hesitation or asymmetry.
3. **Surface Naturalness Pass**: micro check for sentence cadence, AI reaction clichés, unearned aphorisms, over-completion, and **FP-009 Tautological Collisions (e.g. "一豆如豆", "暗自心想", "忍不住不禁")**.

### 5. Story Fact Check
- Compare refined candidate with pre-refinement version and approved brief.
- Verify that naturalness edits did not alter events, knowledge, promises, or state changes.

### 6. Final Verification & Quality Gate
- Score the candidate against the 7-dimension Quality Gate (`references/quality-gate.md`).
- Evaluate the 9-question Skeptical Reader Test (including Artificial Padding Check).
- If Total $\ge 9.5 / 10$ and no critical dimension $< 9.0$: assign verdict **`PROMOTION READY`**.
- Present verification results to the user and request explicit promotion authorization.

### 7. Promotion & State Update
Executed **only after explicit user confirmation in the current turn**:
1. Back up existing official chapter if overwriting.
2. Write exact verified candidate to `chapters/chapter-XXX.md`.
3. Perform post-write reread of the official file.
4. Apply verified Proposed Story Memory Changes to `state/story_memory.md`.
5. Update `chapters/index.md` if present.
6. Record Promotion Result in `audit.md` and set status to **`PROMOTED`**.

## Recommended audit structure

```markdown
# Work-Unit Audit

## Contract Check

## Character Check
- Dialogue Engine compliance:
- Speaker-substitution findings:
- Functional character realism (NPCs):

## Story Fact & Continuity Check

## Chapter Interface Check
- Chapter N-1 to N transition:
- Chapter N to N+1 handoff:

## Structural Naturalness Check

## Prose / Surface Humanizer Check

## Conditional Checks
### [Only triggered checks]

## Quality Gate
- Contract / Continuity: x / 2.0
- Character / Voice: x / 2.0
- Naturalness / Anti-Template: x / 2.0
- Scene / Pacing: x / 1.5
- POV / Cognitive Ownership: x / 1.0
- Prose Precision / Rhythm: x / 1.0
- Chapter Interface: x / 0.5
- Total Score: x / 10.0 (Threshold: >= 9.5)

## Skeptical Reader Test (8 Questions)

## Proposed Story Memory Changes

## Stable Setting Candidates

## Story Fact Check
- Compared versions:

## Final Verification
- Verdict: NOT READY | PROMOTION READY

## Promotion Authorization
- User confirmation: Pending | Confirmed
- Confirmation evidence: [Current-turn explicit authorization quote]

## Promotion Result
- Official target written:
- Backup created:
- Post-write reread: Verified
- Story Memory updated:
- Status: PROMOTED
```

## Completion

Complete only after candidate reaches `PROMOTION READY`, explicit user authorization is obtained, Promotion succeeds, and post-write reread is verified. Stop after the requested work unit. Never auto-continue.