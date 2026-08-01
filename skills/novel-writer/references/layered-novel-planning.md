# Long-Novel Planning — Master Plan, Volumes, Arcs, and Completion Records

Use this as the authoritative planning reference for multi-chapter, multi-volume, multi-arc, tournament, case-based, journey, career, faction, or changing-cast fiction.

## Core principle

Keep the durable whole-book direction compact, plan the active volume and arc precisely, preserve completed history as concise Completion Records, and archive superseded detail outside the default context.

Future plans are intended direction, not happened events. Promoted prose remains the original evidence of what actually occurred.

## Contents

- Planning ownership, Story Kernel, and master plan
- Volume and arc file lifecycle
- Chapter contracts and Completion Records
- Archive policy, rolling expansion, and confirmation

## Planning ownership

Use established project equivalents. New defaults are `plans/master-plan.md` and `plans/volumes/volume-XXX.md`:

```text
plans/
├── master-plan.md
└── volumes/
    ├── volume-001.md
    ├── volume-002.md
    └── volume-003.md
```

Ownership:

- `master-plan.md` — Story Kernel, whole-book spine, volume index, active pointer, full-book constraints, and important rejected directions.
- `volume-XXX.md` — one volume's contract, arc map, active arc detail, completed arc records, and volume completion record.
- chapter brief — current work-unit contract.

Do not keep complete arc detail for every historical and distant-future arc in `master-plan.md`.

## 1. Story Kernel

For a persistent new project, `master-plan.md` begins with the Story Kernel confirmed under `startup-workflow.md`.

It owns the durable story engine:

- core appeal and distinguishing reader promise;
- protagonist external goal, current pressure, and internal contradiction;
- cost-producing method, belief, loyalty, or fear;
- opposition objective or stable pressure logic;
- one to three core relationship pressures or a justified substitute;
- first irreversible choice;
- climactic value-conflict direction;
- Confirmed, Suggested, Open, and Rejected decisions.

Open items remain planning space. Suggested items are not binding. Rejected directions must not quietly return.

A material change to the story engine requires renewed Story Kernel confirmation.

## 2. Master plan

Keep only durable whole-book direction and navigation:

- working title, genre, target scale, and reader promise;
- protagonist full-book growth line;
- central conflict and thematic question;
- volume sequence and final-stage target;
- ending direction when known;
- anchor characters, relationships, factions, locations, or institutions;
- full-book reveal windows and protected promises;
- unacceptable ending directions or rejected solutions;
- a volume index;
- the current volume, arc, and chapter pointer.

The master plan must remain compact enough to load for every project chapter.

### Master-plan pattern

```markdown
# Master Plan

## Story Kernel
### Core Appeal
- Core attraction:
- Distinguishing promise:
- Reader experience:

### Protagonist Engine
- External goal:
- Current pressure / why now:
- Internal contradiction:
- Cost-producing method or belief:
- Change direction:

### Opposition
- Opposing force:
- Independent objective or operating logic:
- Valid reasoning:
- Structural incompatibility:

### Core Relationships
- Relationship:
  - Mutual needs:
  - Important asymmetry:
  - Change or rupture pressure:
  - Plot effect:

### Choice Architecture
- First irreversible choice:
- Climactic value conflict:
- Likely cost direction:

### Decision Status
- Confirmed:
- Suggested:
- Open:
- Rejected:

## Whole-Book Spine
- Reader promise:
- Protagonist growth line:
- Central conflict:
- Volume sequence:
- Final-stage target:
- Full-book constraints:

## Volume Map
| Volume | Status | Core goal/result | Chapter range | File |
|---|---|---|---|---|

## Active Position
- Current volume:
- Current arc:
- Current chapter:

## Protected Promises and Reveal Windows
- Promise/reveal:
- Earliest allowed point:
- Required source:

## Rejected Directions That Must Not Return
- Direction:
- Reason:
```

## 3. Volume file

Create one file when a volume enters meaningful planning. Status moves through:

```text
Planned -> Active -> Completed
```

A volume file owns:

- starting state;
- volume goal and endpoint;
- chapter-count and word-budget range;
- active cast, opposition, locations, institutions, and systems;
- major events and relationship turns;
- which protagonist contradiction or relationship pressure the volume tests;
- promises and reveal boundaries;
- what must be resolved;
- what must remain open;
- expected exit state;
- arc map;
- arc Completion Records;
- final Volume Completion Record.

### Volume pattern

```markdown
# Volume 1

## Status
- Status: Planned | Active | Completed
- Planned chapter range:
- Actual chapter range:
- Started:
- Completed:

## Volume Contract
- Starting state:
- Goal and endpoint:
- Core conflict:
- Active cast and opposition:
- Main locations/institutions/systems:
- Story Kernel pressure tested:
- Major events and relationship turns:
- Must resolve:
- Must remain open:
- Protected reveal boundaries:
- Expected exit state:

## Arc Map
| Arc | Status | Chapters | Core change |
|---|---|---|---|

## Arc 1 — [Name]
### Status
- Planned | Active | Completed

### Plan
- Entry state:
- Objective:
- Opposition or pressure:
- Escalation:
- Relationship movement:
- Required cost:
- Turning point:
- Decisive choice:
- Expected exit state:
- Promises created/advanced/resolved:

### Current Progress
- Completed:
- Remaining:
- Plan deviation:
- Current risk:
- Next step:

### Arc Completion Record
- Actual chapters:
- Actual outcome:
- Character changes:
- Relationship changes:
- Knowledge changes:
- Important object/resource changes:
- Promises resolved:
- Promises carried forward:
- Open consequences:
- Plan deviations:
- Next-arc entry conditions:
- Key source chapters:

### Checkpoint Coverage, when this arc ends a five-chapter window
- Fully reviewed chapters:
- Previous checkpoint:
- Historical chapters reopened and reasons:
- Blocking Before Next Chapter:
- Required During Next Window:
- Watchlist:
- Carry-Forward Constraints:

## Volume Completion Record
- Actual chapter range:
- Major outcome:
- Character end states:
- Relationship end states:
- Knowledge changes:
- Important object/resource states:
- Promises resolved:
- Promises carried forward:
- Open consequences:
- Confirmed stable-setting changes:
- Pending Stable Setting Candidates:
- Plan deviations:
- Next-volume initial conditions:
- Key source chapters:

### Checkpoint Coverage, when this volume ends a five-chapter window
- Fully reviewed chapters:
- Previous checkpoint:
- Historical chapters reopened and reasons:
- Blocking Before Next Chapter:
- Required During Next Window:
- Watchlist:
- Carry-Forward Constraints:
```

Use `Current Progress` only for an active arc. After completion, compact it into the Arc Completion Record and remove obsolete progress detail from the hot context.

## 4. Arc storage and splitting

By default, keep arcs inside their volume file. Do not create one file per arc merely because arcs exist.

Split a volume into a directory only when necessary for reliable reading, such as:

- the volume exceeds roughly 60–80 chapters;
- an arc exceeds roughly 20–30 chapters;
- many parallel viewpoint arcs make the volume file unwieldy;
- the volume file repeatedly loads large irrelevant sections.

Optional complex-volume layout:

```text
plans/volumes/volume-002/
├── volume-plan.md
└── arcs/
    ├── arc-01.md
    └── arc-02.md
```

The volume file or `volume-plan.md` remains the index and authority for arc status.

## 5. Chapter contracts

Translate the active arc into `work/chapter-XXX/brief.md`.

The brief owns:

- starting state;
- required event chain and turning point;
- required/forbidden characters;
- knowledge boundaries;
- allowed promise/reveal movement;
- emotional and relationship movement;
- reserved future events;
- ending boundary;
- target size;
- relevant context sources and conditional checks.

Do not use the master plan as a substitute for a chapter brief.

## 6. Completion and compaction

### Arc completion

When an arc completes:

1. compare the plan with promoted prose;
2. record actual outcome and state changes;
3. carry forward unresolved promises and consequences;
4. identify confirmed stable-setting changes and pending candidates;
5. record key source chapters;
6. create the next-arc entry conditions;
7. compact active Story Memory entries that are now resolved;
8. move obsolete detailed planning to cold storage only when it still has recovery value.

The Completion Record replaces a separate default Arc Audit file.

### Volume completion

When a volume completes:

1. complete all applicable arc records;
2. record volume-level end state and plan deviations;
3. move confirmed durable facts to Story Facts;
4. carry active/open current state into Story Memory;
5. remove resolved Story Memory entries;
6. update the master-plan Volume Map and Active Position;
7. confirm the next volume's starting conditions before detailed planning.

The Volume Completion Record replaces a separate default Volume Audit file.

### Checkpoint merge rule

When a rolling five-chapter Checkpoint boundary coincides with an arc or volume ending, do not create duplicate reports. Use this priority:

```text
Volume Completion Record
> Arc Completion Record
> standalone Checkpoint Audit
```

The selected Completion Record must still fully review the new Checkpoint window and include previous findings, the three action levels, and Carry-Forward Constraints. A planning Completion Record does not bypass blocking continuity findings.

## 7. Archive policy

Planning states:

- **Active** — current authoritative plan under `plans/`.
- **Superseded** — replaced detail that may explain a prior decision; move to `archive/plans/superseded/` when worth retaining.
- **Rejected** — normally discard; retain only high-impact directions that must not return in the master-plan rejection list.

Default chapter context must not load:

- superseded plans;
- completed arcs' original detailed drafts;
- distant-volume speculative detail;
- brainstorming notes;
- archived plan revisions.

Load them only for recovery, comparison, rollback, or decision-history investigation.

## 8. Rolling expansion

Plan future detail only when it affects current decisions.

After an arc or volume:

1. preserve what actually worked;
2. remove or defer unused speculation;
3. update completion records;
4. update only confirmed stable facts;
5. compact current state;
6. then detail the approaching arc or volume.

Do not convert old brainstorming into stable story facts merely because it appears in a planning file.

## 9. Dynamic cast and event density

Define full-book anchors early only when they shape the whole book. Define volume participants when their volume approaches. Define functional participants only when needed.

Before making a new participant recurring, check that they add a distinct story function, decision pressure, relationship strategy, or viewpoint attention. Merge or defer characters who differ only by a surface label. Create or confirm a compact Voice Signature when the character becomes recurring, not during distant speculative planning.

For event-heavy fiction, estimate both set pieces and consequence space. Reduce fully dramatized events or expand scope when the estimate exceeds the target; do not erase recovery, relationships, investigation, travel, or consequences to preserve an arbitrary chapter count.

Escalation in recognition, power, resources, and threat must follow demonstrated causes.

## Confirmation

Confirm the Story Kernel before treating its engine as binding. Confirm the master-plan direction before creating dependent Story Facts. Confirm each new or materially changed volume contract and active arc before chapter planning.

Changing a future plan changes intended direction only. It does not rewrite promoted chapters or stable story facts. A material story-engine change requires renewed Story Kernel confirmation.