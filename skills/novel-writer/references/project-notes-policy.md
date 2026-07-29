# Project Notes Policy — 项目资料不要膨胀成通用 skill

## Principle

The universal `novel-generator` skill should store **methods**, not full project content.

Project-specific novels such as 《雪尽刀还》 may produce useful lessons, but the skill must not embed full chapters, full briefs, full audits, or whole-book canon as reference material.

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
~/Desktop/hermes/jobs/novel-generator/<book-id>/chapters/
~/Desktop/hermes/jobs/novel-generator/<book-id>/state/
~/Desktop/hermes/jobs/novel-generator/<book-id>/audits/
```

When full context is needed, read it from the project directory on demand. Do not copy it into the skill.

## How to abstract lessons

Convert project incidents into reusable rules:

- Bad: “In 《雪尽刀还》第三章, line X said...”
- Good: “If a sensory metaphor implies a physical object, record it as figurative or rewrite it to avoid later state drift.”

- Bad: “柳照水第七章耳伤...”
- Good: “Track state source consistency: if a character’s sensory injury or resource state changes, later references must preserve source/location unless a new event changes it.”
