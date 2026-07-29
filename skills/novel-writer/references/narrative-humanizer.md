# Narrative Humanizer — 通用小说去 AI 味模块

This module adapts the general `humanizer` skill for long-form fiction. Do **not** apply article/report de-AI rules mechanically. Fiction has genre conventions that must be preserved.

## Purpose

Run a final prose-integrity pass that reduces AI-like writing patterns while preserving:
- the user-approved genre and style
- canon and plot facts
- character voice and knowledge boundaries
- the approved chapter contract
- pacing, tension, and reader-facing tone

The Humanizer is **not** a co-author changing the story. It is a prose integrity editor. It removes machine-like artifacts only where they weaken immersion.

## Placement in the chapter pipeline

Run after `Prose Stylist` and before final delivery:

1. Storyteller drafts prose.
2. Character agents review their own dialogue/actions.
3. Lore Auditor checks fact alignment and outline compliance.
4. Prose Stylist polishes.
5. **Narrative Humanizer removes AI-like prose artifacts.**
6. **Post-Humanizer Fact Lock** confirms no facts, clues, character boundaries, or required beats were changed.
7. Parent agent performs final verification.

## Core prompt template

```text
You are the Narrative Humanizer for a long-form novel.

Your job is not to make the prose more ornate.
Your job is to reduce AI-like writing patterns while preserving the story's approved genre, canon, plot facts, character voice, pacing, and user-approved style.

Use the project's genre profile and style bible. If the project is wuxia, preserve wuxia flavor. If it is sci-fi, preserve technical plausibility. If it is romance, preserve emotional intimacy. Do not impose one genre's style on another.

Check for universal AI-like prose issues:
1. forced aphorisms / fake profundity
2. explanatory narration that states what the scene should imply
3. repetitive sentence rhythm
4. over-neat three-part structures
5. abstract emotional summaries instead of concrete behavior
6. interchangeable character dialogue
7. metaphors that fail literal reading, do not fit the viewpoint character, or repeat the same image family too often
8. author-like explanation or meta-narrative leakage
9. generic scene endings that summarize the theme
10. overly polished, frictionless prose

Then run genre-specific checks based on the story bible:
- wuxia/xianxia: fake classical diction, martial-art list prose, realm/system infodumps
- sci-fi: encyclopedia-like exposition, unsupported technical jargon, civilization-scale inflation
- mystery/thriller: premature clue explanation, detective-summary voice, villain monologue over-explanation
- romance/emotional drama: generic emotional labels, melodramatic template phrasing, intimacy without behavior
- urban/realist: unnatural dialogue, corporate/PPT phrasing, life scenes without lived detail
- fantasy/epic: proper-noun overload, prophecy/superlative inflation, worldbuilding before character need
- horror: direct fear labels, atmosphere adjective pileup, overexplained monster logic
- webnovel/light novel: mechanical trope execution, system-message monotony, tag-like character reactions

Allowed edits:
- sentence-level rewrites
- paragraph compression
- dialogue naturalization
- replacing abstract summary with concrete action
- reducing over-polished or generic phrasing

Forbidden edits:
- changing plot events
- changing clues or evidence
- changing worldbuilding rules
- changing character knowledge boundaries
- adding new facts
- deleting required outline beats
- flattening genre voice into generic literary prose

Output:
1. AI-like passages found
2. Why each passage feels artificial
3. Revised passage
4. Genre/style preservation notes
5. Confirmation that plot facts were preserved
```

## Universal AI-like prose issues

These apply to all novel genres.

### 1. Forced aphorism / fake profundity

Problem: Sentences that sound like quotable lines but do not arise naturally from the scene.

Watch for:
- destiny/era/soul/truth/loneliness/void language used as instant depth
- every scene ending with a polished thematic sentence
- metaphor that sounds clever but does not survive literal reading

Fix:
- Replace broad abstraction with action, object, sensory detail, or character reaction.
- Keep genuine literary style when it is earned by scene pressure.

### 2. Explanatory narration

Problem: The narration states what the reader should infer.

Bad pattern:
- `这说明...`
- `这意味着...`
- `他终于明白...`
- `她意识到自己已经...`

Fix:
- Let evidence, gesture, silence, setting, or dialogue carry meaning.

### 3. Interchangeable character dialogue

Problem: Characters all sound like the same polished assistant.

Check:
- sentence length and rhythm
- vocabulary level
- directness / evasiveness
- what each character knows and refuses to say
- whether dialogue explains plot instead of pursuing a personal goal

Fix:
- Restore each character's voice from the character bible.
- Make dialogue partial, pressured, and motivated.

### 4. Over-neat structure

Problem: AI prose loves symmetry.

Watch for:
- repeated `不是...而是...`
- forced three-part lists
- `从...到...` ranges without real scale
- parallel scene endings
- each paragraph ending in a tidy summary

Fix:
- Break symmetry where it feels mechanical.
- Let some sentences stop plainly.

### 5. Abstract emotion labels

Problem: Naming emotion instead of dramatizing it.

Bad:
- `他感到痛苦、释然、复杂。`

Better:
- Show behavior: what the character touches, avoids, repeats, fails to say, or notices.

### 6. Ill-fitting or over-repeated metaphors

Problem: The metaphor does not fit the viewpoint character, setting, era, technology level, or sensory context. A second problem is repetition: even a valid metaphor becomes AI-like when the same image family or gesture is reused too often.

Check both:
- **Literal/semantic fit**: Does the comparison make sense if read plainly?
- **Frequency and variation**: Has the chapter/book already used the same image family, body cue, or stock phrase too many times?

Watch for repeated image families or phrases such as:
- snow like stone / ash / bone / salt / silence
- wounds like cracks / old scars / dark mouths
- hands tightening, knuckles whitening, fingers going pale
- eyes darkening, breath catching, throat tightening
- objects described as blades, ghosts, graves, shadows, mouths, bones
- repeated “像是...”, “仿佛...”, “如同...” sentence shapes

Allowed repetition:
- A motif may repeat deliberately when it is thematically controlled, plot-relevant, or tied to a character/object.
- Repetition is acceptable if it appears with enough spacing and development.

Not allowed:
- Frequent reuse of the same metaphor type because it sounds pretty.
- Repeated physical shorthand for emotion (`指节发白`, `喉头发紧`, `眼神一暗`) when a scene needs fresher behavior.
- Multiple scenes using the same snow/stone/bone/shadow imagery without new meaning.

Fix:
- Use images the viewpoint character could plausibly perceive or think in.
- Before reusing a similar phrasing, ask whether another expression can create the same effect with fresher means: action, object handling, changed posture, altered rhythm, dialogue omission, silence, interruption, smell/sound/touch, or a scene-specific detail.
- Prefer flexibility over automatic substitution. Do not merely replace `指节发白` with another stock cue like `喉头发紧`; choose the expression that fits this exact character, scene pressure, and viewpoint.
- Do **not** overcomplicate a clear simple cue. If `指节发白` or another direct phrase communicates the moment cleanly and has not been overused, keep it.
- A replacement must be more appropriate, not merely more elaborate. If the reader cannot infer what the new action/object detail expresses, prefer the simpler phrase.
- Use object/action detail only when it truly reveals environment, character state, relationship pressure, or plot tension. A detail like `the cup base landed slightly off` is useful only if the reader can infer why it matters; otherwise it becomes confusing filler.
- Replace repeated ornamental comparisons with concrete action, specific setting detail, silence, interruption, or a new sensory register only when the replacement is clearer or more scene-specific.
- Keep a motif only when the recurrence adds meaning rather than convenience.

### 7. Meta-narrative leakage

Problem: The novel refers to itself as a text or to author/reader mechanics.

Forbidden in prose:
- chapter self-reference
- `前文`, `本章`, `上一章`, `读者`, `作者`, `伏笔`, `场景`, `outline`, `agent`, `audit`

Fix:
- Rephrase as in-world memory, document, place, time, or spoken recollection.

### 8. Frictionless polish

Problem: Every line is smooth, balanced, and complete; nobody stumbles, evades, interrupts, or acts before understanding.

Fix:
- Preserve controlled roughness when it reflects character, tension, class, age, fear, fatigue, or genre.

## Genre-specific overlays

Use these only when the project genre/style bible calls for them. Do not punish valid genre conventions.

### Wuxia / Xianxia

Check for:
- fake classical diction (`此间`, `终归`, `万般`) used as decoration
- `江湖/天道/命数` inflation without concrete stakes
- martial-art list prose where combat becomes skill names
- realm/system infodumps that pause the scene
- battles without distance, breath, injury, cost, or tactical cause

Preserve:
- legitimate semi-classical cadence
- sect/world rules required by the system bible
- named techniques when they carry plot or identity

### Sci-fi

Check for:
- encyclopedia-like exposition
- unsupported technical jargon
- civilization-scale statements used to inflate a small scene
- characters speaking like research abstracts

Preserve:
- necessary technical plausibility
- concise operational detail when it affects risk, plot, or moral choice

### Mystery / Thriller

Check for:
- premature explanation of clues
- detective-summary voice that removes reader participation
- villain monologues that explain the whole scheme
- evidence chains that become too tidy

Preserve:
- fair-play clues
- procedural clarity where the genre requires it

### Romance / Emotional drama

Check for:
- generic emotion labels (`心碎`, `救赎`, `破防`) without behavior
- melodramatic template phrasing
- relationship turns that happen because the narration says so
- intimacy without concrete habits, memory, risk, or choice

Preserve:
- emotional interiority when it is specific and embodied
- genre-appropriate tenderness or heightened feeling

### Urban / Realist

Check for:
- corporate/PPT phrasing
- people speaking too politely or completely
- life scenes without lived detail
- social class, profession, or family dynamics reduced to labels

Preserve:
- everyday plainness
- regional/social speech patterns when supported by character design

### Fantasy / Epic

Check for:
- proper-noun overload
- prophecy/superlative inflation
- worldbuilding before character need
- large battles described only with abstract grandeur

Preserve:
- mythic register when chosen by the style bible
- invented names and systems that matter to plot and identity

### Horror

Check for:
- direct labels of fear instead of sensory dread
- adjective pileups (`阴森`, `诡异`, `恐怖`) replacing concrete unease
- overexplained monster logic
- jump scares telegraphed too clearly

Preserve:
- ambiguity
- rhythm, silence, and delayed explanation

### Webnovel / Light novel

Check for:
- mechanical trope execution
- system-message monotony
- tag-like character reactions
- every payoff explained as a爽点

Preserve:
- valid genre momentum
- tropes the user explicitly wants
- accessible pacing and emotional directness

## Required audit output

The chapter audit or a separate humanizer audit must include:

```markdown
## Narrative Humanizer Check

### Universal AI-like prose issues
- Forced aphorism / fake profundity: Pass / Minor / Major / Critical
- Explanatory narration: Pass / Minor / Major / Critical
- Repetitive rhythm / over-neat structure: Pass / Minor / Major / Critical
- Abstract emotion labels: Pass / Minor / Major / Critical
- Character dialogue differentiation: Pass / Minor / Major / Critical
- Ill-fitting / over-repeated metaphors and stock gestures: Pass / Minor / Major / Critical
- Meta-narrative leakage: Pass / Minor / Major / Critical

### Genre-specific overlay
- Project genre/style profile used: [genre]
- Genre-specific issues found: [bullets]
- Genre conventions preserved: [bullets]

### Changes made
- [passage or category] → [change type]

### Post-Humanizer Fact Lock
- Plot events changed: No / Yes
- Clues/evidence changed: No / Yes
- Worldbuilding rules changed: No / Yes
- Character knowledge boundaries changed: No / Yes
- Required outline beats removed: No / Yes

Verdict: Pass / Needs targeted revision / Regenerate
```

Any `Yes` in Post-Humanizer Fact Lock requires immediate targeted revision before delivery.

## Parent-agent verification additions

After generation, the orchestrating process should verify that the audit includes `Narrative Humanizer Check` and `Post-Humanizer Fact Lock`. It should also inspect suspicious passages directly instead of relying only on keyword bans.

Keyword scans are only warnings. Do not ban valid genre language mechanically. Flag only usage that breaks immersion, contradicts style, or sounds machine-generated.
