# Startup Workflow — 新小说立项流程

Use this when the user starts a new novel or proposes a new premise.

## Core ordering

Do **not** ask for target word count before style, elements, and tone are locked. Length depends on the complexity of style and element mix.

Recommended order:

1. **Topic / Seed Confirmation**
2. **Writing Style Selection**
3. **Trope & Element Mix Selection**
4. **Compatibility Check + Tone Lock**
5. **Length / Chapter Scale**
6. **Project Profile Creation** (`state/project_profile.md`)
7. **Initial Story Outline Confirmation**
8. **System Bible Confirmation**
9. **Detailed Plot Outline Confirmation**
10. **Per-Chapter Preflight**
11. **Chapter Generation Pipeline**

## Step 1 — Topic / Seed Confirmation

Summarize the user’s idea:
- genre/domain
- protagonist seed
- central conflict
- world direction
- things the user dislikes or forbids

Then ask for confirmation before building the style/element plan.

## Step 2 — Writing Style Selection

Load `references/style-and-element-selection.md` and, when useful, `references/style-library.md`.

Ask the user to choose:
- main style: exactly 1
- supporting styles: up to 2
- styles to avoid
- custom style if none fits

## Step 3 — Trope & Element Mix

Load `references/element-library.md`.

Ask the user to choose:
- core elements: 1–3
- secondary elements: 0–3
- forbidden elements

If the user proposes a new style/element not in the library, follow `references/library-expansion-protocol.md`.

## Step 4 — Compatibility Check + Tone Lock

Before word count or outline, produce:

```markdown
## Compatibility Check
- Works well:
- Potential conflicts:
- Suggested core:
- Suggested weak/optional elements:

## Tone Lock
- Main emotional texture:
- Lower bound:
- Upper bound:
- Must avoid:
- Reader experience target:
```

Wait for user confirmation.

## Step 5 — Length / Chapter Scale

Only after tone is locked, ask:
- total target length
- chapter count / chapter size
- generation cadence
- dashboard requirement

Warn if chosen elements exceed the selected length.

## Step 6 — Project Profile Creation

After style, element mix, Tone Lock, and length/chapter scale are confirmed, create:

```text
state/project_profile.md
```

Use `references/project-profile-workflow.md`.

Before writing the file, present the full Project Profile draft and wait for explicit user confirmation. Do not treat earlier brainstorming or partial choices as permission to create the project-level rule file.

This file preserves the project’s style, element rules, tone, reader promise, and revision boundaries. It should be used by outline generation, System Bible, chapter preflights, and completed-chapter revision.

## Step 7 onward

Proceed to:
- initial outline
- system bible
- detailed plot outline
- per-chapter preflight
- chapter generation

For long novels with many stages, teams, factions, or changing casts, use `references/layered-novel-planning.md`: confirm the full-book spine, then create a detailed bible/outline for the current volume only. Later teams, transfers, rivals, and functional characters can remain placeholders until their volume approaches.

Use the chapter pipeline in `references/chapter-pipeline.md`.
