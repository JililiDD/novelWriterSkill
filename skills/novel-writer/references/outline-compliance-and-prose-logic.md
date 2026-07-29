# Outline Compliance and Prose Logic Pitfalls

Use this reference during chapter preflight, drafting, audit, styling, and revision.

## Pitfall 1: Treating the approved outline as loose inspiration

### Failure mode

A generated chapter keeps the general theme but changes the approved title, location, premise, event chain, turning point, required character, reveal boundary, or ending hook.

### Required control

Before drafting, copy the user-approved chapter requirements into an `Approved Chapter Contract` inside the chapter brief. Role passes may enrich transitions, staging, sensory detail, and dialogue, but may not replace binding contract items.

The audit must mark every contract item as:

- Satisfied
- Partially satisfied
- Missing
- Contradicted

A missing or contradicted main event, turning point, required character, reveal boundary, or foreshadowing obligation is Critical.

## Pitfall 2: Stylish prose with weak literal logic

### Failure mode

A sentence sounds polished or quotable but its literal image is strained, internally inconsistent, or inappropriate to the viewpoint.

### Required control

Run a Prose Logic and Naturalness pass:

1. Read metaphors and similes literally before accepting them.
2. Check whether the viewpoint character could naturally form the comparison.
3. Replace forced aphorisms with concrete action, setting, or dialogue when clearer.
4. Flag sentences that sound clever but do not survive ordinary reading.
5. If awkward constructions are systemic rather than isolated, return the scene for revision instead of applying superficial polish.

Prefer observable evidence such as lowered voices, interrupted gestures, closed doors, changed posture, or a character refusing to answer.

## Pitfall 3: Meta-narrative leakage

### Failure mode

Final prose refers to chapters, outlines, readers, foreshadowing tags, drafting decisions, or audit terminology.

### Required control

Reference prior events from inside the story world: a place, object, document, memory, date, wound, promise, or spoken line.

Flag expressions such as:

- `上一章`
- `本章`
- `前文提到`
- `这个伏笔`
- `读者会发现`
- `此处埋下`
- planning, agent, audit, outline, or scene labels

A genuine workflow leak is at least Major and must be removed before delivery.

## Pitfall 4: Dashboard logic tied to one book

### Failure mode

A reading dashboard hardcodes one project path, title, chapter naming pattern, or state-file layout.

### Required control

A reusable dashboard should:

- discover projects under a configured root
- switch between books without code changes
- support the project's actual chapter and audit naming conventions
- display available setting files such as outlines, character bibles, System Bibles, foreshadowing ledgers, and chapter briefs
- count Chinese characters with a CJK-aware method rather than whitespace splitting
- provide mobile-readable typography and wrapping
- validate generated read URLs and API responses against the running application

Use placeholders such as `<dashboard-root>` and `<project-root>` in reusable documentation. Do not embed one machine's absolute paths.

## Pitfall 5: Hardcoding Humanizer rules to one genre

### Failure mode

A humanization prompt assumes a specific genre and treats valid conventions from other genres as defects.

### Required control

Keep universal checks genre-neutral:

- forced aphorisms
- explanatory narration
- repetitive rhythm
- over-neat structures
- abstract emotion labels
- interchangeable dialogue
- ill-fitting metaphors
- meta-narrative leakage
- frictionless, over-polished phrasing

Apply genre-specific checks only as overlays derived from the approved project profile and Style Bible. Humanization may alter delivery but not plot facts, clues, world rules, knowledge boundaries, or approved beats.

## Pitfall 6: Reusing the same image family or stock gesture

### Failure mode

The prose avoids obviously broken metaphors but repeatedly relies on the same images or shorthand reactions, making scenes and characters feel interchangeable.

### Required control

1. Scan repeated image families, not only exact repeated words.
2. Cross-check recent chapters when a motif may be overused.
3. Preserve repetition when it is intentional, spaced, and gains meaning.
4. Do not mechanically ban common phrases; frequency and context matter.
5. Before substituting synonyms, consider a different expression path: action, posture, silence, interrupted dialogue, object interaction, scene-specific sensation, or sentence rhythm.
6. Use object details only when they reveal environment, character state, relationship pressure, or plot tension.
7. Do not optimize for a target metaphor count.

## Pitfall 7: Weak audits miss state drift and causality

### Failure mode

An audit checks broad canon but misses concrete discontinuities:

- an action or full line does not fit available time or physical pressure
- a metaphor, rumor, dream, or perception later becomes narrator fact
- an important state change has no consequence
- ownership, location, relationship, resource, injury, ability, or knowledge changes without cause

### Required control

Run a genre-neutral continuity audit using only relevant ledgers:

1. Character state: body, emotion, relationships, promises, secrets, abilities, resources, and constraints.
2. Information and knowledge: who knows what, how they learned it, and whether certainty, rumor, and inference remain distinct.
3. Objects, resources, and evidence: ownership, location, damage, consumption, scarcity, and proof value.
4. Scene feasibility: time, pressure, visibility, ability, available pauses, and physical access.
5. Literal versus figurative language: do not promote metaphor, sensation, rumor, dream, hallucination, or subjective perception into objective fact without an event.
6. Cause to consequence: important changes must affect later behavior or be deliberately resolved.
7. Cross-chapter state drift is Major or Critical depending on story impact, not merely stylistic.

See `continuity-bug-audit.md` and `narrative-humanizer.md` for detailed procedures.
