# Continuity & Story Logic Audit — 事实、状态、来源、章节接口与因果审查

Use this as the canonical factual-quality reference for chapter, scene, revision, and cross-range audits. It checks whether story content is possible, authorized, sourced, causally consistent, and seamlessly interfaced with neighboring chapters.

## Contents

- Sources of truth and audit categories
- Chapter interface continuity
- Audit procedure and severity
- Required output and boundaries

## Sources of truth

Compare candidate prose against relevant approved sources:
1. chapter/scene contract;
2. Story Facts for stable confirmed facts and protected facts;
3. Story Memory for active current state;
4. approved master/volume/arc plan for intended direction;
5. promoted chapters for original evidence;
6. `state/writing_lessons.md` for confirmed project craft constraints.

When sources conflict, report the conflict and block rather than selecting the convenient version.

## Audit categories

### 1. Contract compliance
Check every binding item from the approved brief (events, character presence, reveal boundaries, exact wording obligations, ending state).

### 2. Character state and relationship continuity
Check location, physical condition, immediate goal, active limitations, relationship phase, and emotional aftermath.

### 3. Knowledge and secret boundaries
Check who knows what, how information was acquired, and prevent narrator/private knowledge leakage.

### 4. Object, resource, evidence, and capability state
Track consequential objects, custody, damage, depletion, and evidentiary reliability.

### 5. Timeline, location, and scene feasibility
Check elapsed time, travel duration, physical distance, stamina/healing feasibility, and environmental obstacles.

### 6. Provenance for new named entities
Verify that newly prominent characters, factions, places, or artifacts enter through a plausible story-world route.

### 7. Literal, figurative, uncertain, and subjective information
Ensure metaphors, sensations, rumors, or dreams are not promoted into objective facts without an establishing event.

### 8. Cause and consequence
Verify that injuries, betrayals, resource expenditures, and discoveries produce plausible, tracked consequences.

### 9. Foreshadowing and reader promises
Ensure promises advance within allowed windows, protected secrets stay unrevealed, and resolved threads receive payoffs.

### 10. Workflow and meta leakage
Remove genuine planning, role, audit, or workflow scaffolding from prose.

### 11. Chapter Interface Continuity (跨章接缝检查)
Inspect continuity across chapter boundaries ($N-1 \rightarrow N \rightarrow N+1$):
- **Time**: Time of day and elapsed time align with the previous chapter's ending.
- **Location**: Specific room/spatial position matches preceding arrival/exit.
- **Physical state**: Fatigue, injuries, breath, and attire state carry forward plausibly.
- **Object custody**: Items carried in hands or pockets match the previous scene.
- **Present cast**: Entrances and exits are causally accounted for.
- **Emotional aftermath**: Character attention and mood reflect preceding events.
- **Pending action**: Opening hook connects smoothly to previous unresolved tension.

## Audit procedure

1. Read the approved contract and authoritative state.
2. Run activated audit categories and Chapter Interface Check.
3. Classify severity: **Critical** (blocks), **Major** (blocks if breaking contract/logic), **Minor** (targeted fix), **Info**.
4. Propose minimal targeted corrections and extract Proposed Story Memory Changes.
5. Invalidate downstream checks if substantive edits are required (`references/quality-gate.md`).

## Required output

```markdown
## Continuity & Story Logic Audit

### Sources checked
- Contract:
- Stable story facts:
- Story Memory:
- Original chapter evidence:

### Contract compliance
- [Requirement]: satisfied / partial / missing / contradicted — evidence

### Chapter Interface Check
- Time & Location continuity: Pass / [Finding]
- Physical state & Object custody: Pass / [Finding]
- Emotional aftermath & Pending action: Pass / [Finding]

### Activated categories
- Character/relationship:
- Knowledge/secrets:
- Object/resource/evidence:
- Timeline/location/feasibility:
- Provenance / Cause & Consequence:
- Foreshadowing / Workflow leakage:

### Findings
- [Severity] [Category] — issue, evidence, corrective owner

### Required fixes
- [Minimal targeted correction]

### Proposed Story Memory Changes
- See `long-form-continuity.md` format.

### Stable Setting Candidates
- Proposed durable change, evidence, impact, and confirmation requirement.

Verdict: Pass / Needs Targeted Revision / Regenerate
```