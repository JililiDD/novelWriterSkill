# Narrative Humanizer — 小说语言自然度与去模板化

Use this as the canonical language-quality reference after Prose Stylist. It improves expression while preserving the approved story, Project Profile, Style Anchors, and chapter contract.

Narrative Humanizer is not a continuity auditor, plot editor, or canon writer. Factual defects belong to `continuity-bug-audit.md`; all changed prose must still pass Story Fact Check.

## Inputs

Read only what is needed:

- styled candidate prose;
- relevant Project Profile constraints and Style Anchors;
- character voice constraints;
- chapter contract and protected facts;
- recent promoted prose when checking repetition or drift;
- blocking language findings from prior review.

## Allowed changes

- sentence and paragraph rewrites;
- dialogue naturalization;
- rhythm variation;
- removal of redundant explanation;
- compression of generic or over-polished phrasing;
- replacement of weak, repeated, or viewpoint-inappropriate imagery;
- restoration of genre-appropriate roughness, silence, interruption, or asymmetry.

## Forbidden changes

Do not change:

- plot events or event order;
- character actions, intentions, presence, or knowledge;
- clues, evidence, provenance, or reveal timing;
- world/system rules;
- required beats or exact phrases;
- foreshadowing obligations;
- relationship state;
- work-unit ending boundary;
- proposed Story Memory Delta.

When a language correction would require a factual or structural change, return a finding to the owning stage instead of making it silently.

## Universal checks

### 1. Forced aphorism and manufactured depth

Flag lines that sound quotable but are not earned by scene pressure. Replace broad abstractions with specific behavior, sensory evidence, object interaction, or plain language when stronger.

Do not remove genuine lyricism merely because it is elevated.

### 2. Explanatory narration

Reduce narration that tells the reader what dialogue, silence, or action already shows.

Common symptoms:

- repeated “this meant” or “he finally understood” summaries;
- restating the emotional meaning after a clear scene beat;
- explaining a clue immediately after presenting it;
- narrating the theme at every scene ending.

Preserve explanation required for clarity, genre mechanics, or viewpoint reasoning.

### 3. Repetitive rhythm and over-neat structure

Check for:

- repeated sentence length and cadence;
- mechanically balanced clauses;
- excessive three-part lists;
- repeated contrast frames such as “not X but Y”;
- every paragraph ending in a polished conclusion;
- every scene following the same setup-turn-summary pattern.

Vary only where the repetition feels automatic rather than intentional.

### 4. Abstract emotion instead of behavior

Replace generic emotion labels when a more specific action, avoidance, failed response, bodily choice, or attention shift can carry the moment.

Do not ban interiority. Keep precise thoughts and named emotions when the viewpoint naturally recognizes them.

### 5. Interchangeable dialogue

Check each major speaker for:

- vocabulary and sentence length;
- directness, evasion, politeness, or aggression;
- what they notice and refuse to say;
- social position and relationship-specific address;
- knowledge boundaries;
- how pressure changes their speech.

Dialogue should pursue a character goal, not merely explain the outline.

### 6. Ill-fitting or repeated imagery

Check both literal fit and repetition across recent prose.

Reject imagery that:

- does not fit the viewpoint, era, setting, profession, or sensory context;
- implies an unintended physical fact;
- repeats the same image family without added meaning;
- replaces one stock gesture with another equally generic gesture;
- becomes more elaborate but less clear.

A recurring motif is valid when deliberate, spaced, and meaningfully developed.

### 7. Stock gestures and reaction shorthand

Watch for repeated tightening hands, darkened eyes, caught breath, constricted throat, pale knuckles, frozen steps, and similar shortcuts.

Keep a simple cue when it is accurate and not overused. Otherwise use scene-specific behavior, object handling, silence, interruption, posture, or changed speech rhythm.

### 8. Frictionless polish

AI-like prose often makes every sentence complete, balanced, articulate, and emotionally resolved.

Preserve controlled roughness where character, age, class, fear, exhaustion, intimacy, conflict, or genre calls for fragments, mistakes, evasions, interruptions, or unfinished thought.

### 9. Meta and workflow leakage

Remove genuine references to drafting, agents, audits, outlines, readers, chapter production, or tagged foreshadowing from final-intended prose.

Use contextual judgment. A legitimate in-world chapter, reader, scene, report, or audit is not automatically a workflow leak.

## Genre overlays

Apply only overlays required by the approved Project Profile.

### Wuxia / xianxia

Check decorative pseudo-classical diction, technique-list combat, realm exposition that stops the scene, and grand abstractions without distance, cost, breath, injury, or tactical cause. Preserve legitimate semi-classical cadence and named techniques that matter.

### Mystery / thriller

Check premature clue explanation, detective-summary narration, over-complete villain explanation, and evidence chains made unnaturally tidy. Preserve fair-play clarity.

### Romance / emotional drama

Check generic emotional labels, template melodrama, intimacy without specific habit or choice, and forgiveness without cost. Preserve precise interiority and genre-appropriate tenderness.

### Science fiction / fantasy

Check encyclopedia exposition, unsupported jargon, proper-noun overload, and scale inflation. Preserve rules and operational detail that affect decisions.

### Horror / weird fiction

Check direct fear labels, adjective piles, telegraphed scares, and fully explained threats. Preserve ambiguity, sensory pressure, and delayed understanding.

### Realist / urban / workplace

Check corporate-summary language, unnaturally complete dialogue, generic social labels, and scenes without lived constraints. Preserve plainness and supported speech patterns.

### Web novel / light novel

Check mechanical trope execution, system-message monotony, tag-like reactions, and repeated explanation of every payoff. Preserve momentum, accessibility, and user-approved genre conventions.

## Style Anchor check

Compare the candidate with relevant Project Profile anchors:

- narrative distance and viewpoint;
- sentence/rhythm tendencies;
- dialogue texture;
- emotional explicitness;
- imagery density;
- high-intensity register when applicable.

Do not imitate anchor wording. Preserve observable traits.

If recent promoted chapters consistently diverge from the anchors, report a drift signal for checkpoint audit rather than forcing one chapter to compensate for the entire trend.

## Output

```markdown
## Narrative Humanizer Check

### Project style used
- Project Profile:
- Style Anchors:
- Genre overlay:

### Findings and edits
- [Category] — passage/problem → edit rationale

### Preserved boundaries
- Plot/events unchanged: Yes / No
- Character action/knowledge unchanged: Yes / No
- Clues/rules/reveal timing unchanged: Yes / No
- Required beats/exact phrases preserved: Yes / No
- Work-unit boundary preserved: Yes / No
- Proposed Story Memory Delta unchanged: Yes / No

### Drift signals
- None / [cross-chapter pattern for periodic audit]

Verdict: Pass / Needs targeted revision
```

Any `No` in preserved boundaries blocks handoff and requires correction before Story Fact Check.

## Boundaries

- Keyword counts are diagnostic, not quality targets.
- Do not flatten genre voice into generic literary prose.
- Do not make every sentence unusual.
- Do not increase ornament merely to avoid common phrasing.
- Do not solve continuity or contract problems inside this pass.