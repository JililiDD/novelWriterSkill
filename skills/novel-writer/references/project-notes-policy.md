# Project Notes Policy — 项目资料不要膨胀成通用 skill

## Principle

The reusable `novel-writer` skill should store **methods**, not full project content.

Individual novel projects may produce useful lessons, but the skill must not embed full chapters, full briefs, full audits, or whole-book story facts as reference material.

## What belongs in universal references

Allowed:
- reusable workflow rules
- abstracted pitfalls
- compact checklists
- generic examples
- cross-genre audit methods
- style/element selection mechanisms

Examples:
- “Do not let a metaphor become a literal fact later.”
- “New witnesses/locations need provenance from prior clues.”
- “Humanizer must be genre-neutral.”

## What does NOT belong in universal references

Do not store:
- whole chapters
- full novel manuscripts
- full chapter briefs
- full audit reports
- project-specific dialogue
- large excerpts copied from one book
- one book's plot as universal workflow

## Project notes size target

A project-specific note should be a compact summary/checklist, normally under 1,000–2,000 Chinese characters unless the user explicitly asks otherwise.

## Where full project content lives

Full text stays in the project directory, e.g.:

```text
<project-root>/chapters/
<project-root>/state/
<project-root>/audits/
```

When full context is needed, read it from the project directory on demand. Do not copy it into the skill.

## How to abstract lessons

Convert project incidents into reusable rules:

- Bad: “In Project A, chapter 3, line X said...”
- Good: “If a sensory metaphor implies a physical object, record it as figurative or rewrite it to avoid later state drift.”

- Bad: “Character A's ear injury in chapter 7...”
- Good: “Track state-source consistency: if a character's injury or resource state changes, later references must preserve its source and location unless a new event changes it.”
