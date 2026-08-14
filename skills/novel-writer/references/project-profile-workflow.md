# Project Profile Workflow — 项目级风格、元素与读者体验总控

Use this reference to create or update the project's authoritative style, reader-experience, and Style Lock file:

```text
state/project_profile.md
```

## Contents

- Ownership, creation order, and confirmation
- Project Profile template, Style Lock, and Style Anchors
- Chapter usage, audits, and updates

## Ownership

Project Profile is the sole owner of:

- writing style, prose density, and Style Lock dimensions;
- element mix and implementation rules;
- Tone Lock;
- reader promise;
- Style Anchors and Rejected Drift Notes;
- project-level craft constraints and forbidden tendencies;
- project-level generation and revision boundaries.

It answers:

> What should this book feel like, and what experience must it consistently deliver?

It may reference the confirmed Story Kernel's reader promise, but it does not own protagonist motivation, opposition logic, relationship pressure, or plot choices.

Do not duplicate the full Style Bible or Element Bible inside Story Facts. Story Facts owns stable confirmed facts and each recurring character's Dialogue Profile; it references the approved Project Profile.

## Creation order

Create the Project Profile after confirming:

1. the Story Kernel, including its reader promise and decision status;
2. main and supporting styles;
3. Style Calibration outcome (Style Lock & Narrative Anchor) when calibrated;
4. core and secondary elements;
5. compatibility constraints and Tone Lock;
6. target length and chapter scale.

Use it before master-plan work, Story Facts work, volume planning, chapter preflight, generation, revision, and style-drift audits.

## Confirmation

Show the complete Project Profile draft and obtain explicit confirmation before first creation or any project-level change.

A one-off chapter complaint, experimental rewrite, brainstorming question, or temporary tone request does not authorize a Project Profile update. Use `references/feedback-promotion.md` when upgrading recurring feedback.

## Required template

```markdown
# Project Profile

## Basic
- Title:
- Genre:
- Target length:
- Chapter scale:

## Narrative Style Lock
### Narrative distance
- [e.g. Third-person limited, medium-close; strict sensory radius]

### Cognitive movement
- [e.g. Observe sensory evidence → infer immediate risk → act/decide]

### Sentence rhythm
- [e.g. Mixed sentence lengths; landing sentences only under high pressure]

### Description density
- [e.g. Functional and scene-grounded; 1–2 sharp tactile/spatial cues]

### Psychological explicitness
- [e.g. Restrained by default; show through avoidance, task focus, or physical friction]

### Dialogue floor
- [e.g. Natural modern vernacular; goal-driven; no shared clipped aphorisms]

### Information release
- [e.g. Evidence before explanation; zero summary of what dialogue already revealed]

### Competence display
- [e.g. Shown through questions asked, verification actions, and cost management]

### Visual emphasis for key entrances/scenes
- [e.g. Viewpoint-selected base image for entrances; spatial/sensory anchors for key scenes]

### Forbidden drift
- [e.g. Over-explaining clues, characters sharing clipped syntax, speechifying NPCs]

## Elements
- Core elements:
- Secondary elements:
- Forbidden elements:
- Implementation rules:
- Conflict-handling rules:

## Tone Lock
- Main emotional texture:
- Lower bound:
- Upper bound:
- Must avoid:
- Reader experience target:

## Reader Promise
- Core experience promised:
- Recurring satisfactions:
- Long-term promises:
- What would betray the reader:

## Style Anchors
### Narrative Anchor
- Source chapter/path or approved calibration sample:
- Must-preserve traits:

### Dialogue Anchor
- Source chapter/path or approved short sample:
- Must-preserve traits:

### High-Intensity Anchor
- Required: no
- Source chapter/path or approved short sample:
- Must-preserve traits:

### Rejected Drift Notes
- [Brief reasons for options rejected during Style Calibration or reviews]

### Drift Signals
- Patterns that indicate the prose is moving away from the approved voice:

## Delivery Boundaries
- Drafting must preserve:
- Refinement may change:
- Reviews must check:
- Light revision may:
- Deep revision requires:
- Never change automatically:

## Rolling Audit
- Checkpoint window: 5 promoted chapters by default
- Explicit project override, when approved:
- Additional drift/complexity triggers:
```

## Style Anchors & Style Lock

Style adjectives alone are not reliable for long projects. The Style Lock decomposes style into concrete execution rules.

The Dialogue Anchor defines only the book's shared dialogue floor: era and setting fit, readability, density, punctuation, realism level, and broad conversational texture. It must not impose one cadence, vocabulary, humor style, or politeness strategy on every character. Individual Dialogue Profiles belong in Story Facts (`references/dialogue-engine.md`).

Visual emphasis defines a project-level tendency, not a word quota. Key character entrances and key scenes receive selected detail while remaining viewpoint-bound and action-connected.

An anchor may be:
- a user-approved sample from Style Calibration (`references/style-calibration.md`);
- a precise path plus passage location in a promoted chapter;
- a compact description of observable traits when no sample exists yet.

## Chapter usage

Chapter Preflight copies only constraints relevant to the current work unit:

```markdown
## Project Profile Constraints
- Style Lock constraints:
- Relevant elements:
- Tone bounds:
- Relevant Style Anchors:
- Shared dialogue-floor constraints:
- Forbidden drift & project craft lessons:
- Chapter-specific prose risks:
```

## Update rules

Project-level confirmation is required to change Style Lock dimensions, elements, Tone Lock, reader promise, Style Anchors, or revision boundaries. Use `references/feedback-promotion.md` for project-level lesson promotion.