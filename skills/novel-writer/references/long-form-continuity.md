# Long-Form Continuity — Current State, Context Tiers, and Archive Discipline

Use this reference for serialized, multi-arc, multi-volume, or continuity-heavy fiction. It keeps current context compact without losing recoverable history.

## Authority map

| Information | Owner |
|---|---|
| Story engine and full-book direction | `plans/master-plan.md` |
| One volume, its arcs, and completion records | `plans/volumes/volume-XXX.md` |
| Style, elements, Tone Lock, reader promise, Style Lock | Project Profile |
| Stable confirmed story facts, Dialogue Profiles, protected facts | Story Facts |
| Active/open current state only | Story Memory |
| Project craft lessons & failure pattern rules | `state/writing_lessons.md` |
| Current work-unit obligations and selected context | Brief |
| Happened events and original evidence | Promoted final prose |
| Candidate findings, Quality Gate, and proposed changes | Audit |

Future plans are not happened events. Candidate prose has zero authority over Story Memory or future chapters until promoted.

## Context tiers

### Hot context
Load by default for a Project Creation chapter:
1. Story Kernel, whole-book constraints, and Active Position from `master-plan.md`;
2. current volume summary and active arc;
3. relevant Project Profile sections (Style Lock & Narrative Anchor);
4. relevant Story Facts sections (Dialogue Profiles for present characters);
5. active project craft lessons (`state/writing_lessons.md`);
6. current Story Memory;
7. current brief;
8. the minimum promoted prose needed to establish the current starting state;
9. historical evidence explicitly activated by the brief or a risk trigger.

### Minimum promoted-prose selection
Do not use a fixed chapter count.
1. Start with the current brief and Story Memory.
2. Read the immediate predecessor chapter when directly continuing.
3. Check time, location, active characters, knowledge, object custody, relationship state, and unfinished action.
4. Stop as soon as the current starting state and activated dependencies are clear.

### Warm context
Load only when activated:
- completed arc or previous-volume Completion Records;
- returning characters, objects, secrets, promises, or consequences;
- original chapters needed for evidence;
- unresolved cross-chapter issues.

### Cold context
Excluded by default:
- historical candidates, backups, closed audits, superseded plans, old revisions.

## Story Memory Discipline

`state/story_memory.md` tracks only dynamic, open, and unresolved elements:
- Current Position & Timeline
- Active Characters & Immediate Location
- Knowledge & Secrets (Who knows what and when)
- Consequential Objects & Resource Custody
- Active Promises & Foreshadowing
- Open Consequences & Emotional Aftermath

### State Change Isolation
Proposed Story Memory changes remain pending inside `audit.md` throughout Drafting, Review, Humanizing, and Final Verification. They are **never** written to `state/story_memory.md` until the user confirms Promotion in Stage 7 (`PROMOTION & STATE UPDATE`).

## Chapter Interface Check

Continuity requires checking transitions across chapter boundaries:
- Chapter $N-1$ ending $\rightarrow$ Chapter $N$ opening;
- Chapter $N$ ending $\rightarrow$ Chapter $N+1$ opening.

Verify:
1. Elapsed time and time-of-day continuity.
2. Physical location and spatial orientation.
3. Physical state (stamina, injuries, clothing condition).
4. Object custody (carried in hand, packed, consumed).
5. Present characters and entrance/exit plausibility.
6. Emotional aftermath from preceding events.
7. Immediate objective driving the transition.

Use `scripts/chapter_interface_scan.py` for boundary paragraph extraction.

## Rolling Checkpoint Audits

Project Creation defaults to one Checkpoint per five promoted chapters (`audits/checkpoint_001_005.md`).
- Fully reviews only the new 5 chapters in the window.
- Inherits unresolved findings and Carry-Forward Constraints.
- Action levels: **Blocking Before Next Chapter**, **Required During Next Window**, **Watchlist**.
- Merges into Arc/Volume Completion Records when coincident.