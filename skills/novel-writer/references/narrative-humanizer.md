# Narrative Humanizer — 小说语言自然度、结构去模板化与双层诊断

Use this as the canonical naturalness reference for both draft-time prevention and post-draft humanization passes. It preserves the approved story, Project Profile, Style Lock, Style Anchors, viewpoint, and work-unit contract.

Narrative Humanizer is not a continuity auditor, plot editor, or story-fact authority. Factual or structural defects return to the owning stage. Every changed candidate still passes Story Fact Check.

---

## Contents

- Dual-pass operational model
- Draft-time naturalness guardrails & Explanation Budget
- Pass 1: Structural Naturalness Pass (Macro)
- Pass 2: Surface Naturalness Pass (Micro)
- Skeptical Reader Test & Genre overlays
- Script-assisted diagnostics

---

## Dual-Pass Operational Model

Naturalness cannot be achieved merely by swapping adjectives or polishing sentences if the underlying scene architecture is artificial. Humanization operates across two distinct passes:

```text
Draft Writing (applies positive generation principles & Explanation Budget)
  ↓
Pass 1: Structural Naturalness Pass (Macro logic, NPC utility, cognitive pacing)
  ↓
Prose Stylist (clarity, imagery, and rhythm refinement)
  ↓
Pass 2: Surface Naturalness Pass (Micro cadence, clichés, unearned aphorisms)
  ↓
Story Fact Check (semantic & factual verification)
```

The governing principle is:

> Do not pursue roughness. Preserve irregularity that has a source in viewpoint, character, pressure, relationship, setting, or genre.

---

## Draft-Time Guardrails & Explanation Budget

### Five Positive Generation Principles
1. **POV owns the prose**: narration, attention, and sensory radius belong strictly to the viewpoint character.
2. **Characters speak from motive, knowledge, status, relationship, and pressure**: apply the generative Dialogue Engine (`references/dialogue-engine.md`).
3. **Evidence precedes interpretation**: show concrete evidence, behavior, and physical consequences before narration.
4. **Competence is behavioral**: protagonist competence is shown through selective attention, questions asked, verification actions, and cost management.
5. **Causal closure**: scenes end after meaningful causal state change, not after thematic summary.

### The Explanation Budget
```text
Evidence shown in scene
  ↓
Can a reasonable reader understand enough to follow the next decision?
  ├─ YES → STOP EXPLAINING IMMEDIATELY.
  └─ NO  → Add minimum necessary interpretation for the next action.
```
- Each critical piece of evidence permits at most **one** necessary interpretation.
- If dialogue, action, or physical consequence has already conveyed meaning, delete narrator summaries.
- Never add a final paragraph summarizing the philosophical or dramatic theme of the chapter.

---

## Pass 1: Structural Naturalness Pass (Macro Diagnostic)

Execute this pass **before** Prose Stylist. If macro structures are artificial, surface polishing cannot rescue the prose.

### 1. Smartness Inflation & Instant Dedication (FP-003)
- Check whether the protagonist makes gigantic deductive leaps without trial, error, or physical verification costs.
- Ensure the protagonist's conclusions are earned through specific sensory clues.

### 2. NPC Friction & Functional Realism (FP-002)
- Check whether secondary characters act as frictionless information kiosks.
- Verify **Functional Character Realism**: NPCs care about their wages, safety, blame avoidance, and have fragmented, imperfect knowledge.

### 3. Universal Service to Protagonist (FP-007)
- Check whether surrounding characters exist solely to react, praise, or be tested by the protagonist.
- Ensure named characters have independent tasks, schedules, and ongoing concerns.

### 4. Monotonous Scene Architecture (FP-005)
- Check whether every paragraph or exchange follows a neat, uniform cycle (Setup $\rightarrow$ Explanation $\rightarrow$ Reaction $\rightarrow$ Summary).
- Restore asymmetrical attention, pauses, interruptions, and unresolved friction.

*Action*: If a scene fails Structural Naturalness, choose **Return Upstream** to restructure scene motivation rather than attempting surface phrasing patches.

---

## Pass 2: Surface Naturalness Pass (Micro Diagnostic)

Execute this pass **after** Prose Stylist.

### 1. Clipped Dialogue & Fragment Chains (FP-001)
- Scan for high-frequency 2–5 character fragments (*“为何？”*, *“不然？”*, *“走。”*).
- Verify that dialogue expresses complete grammatical units shaped by the speaker's status and strategy.
- Run `scripts/dialogue_scan.py` to highlight suspect lines.

### 2. Explanatory Echoes & Insight Phrases (FP-004)
- Flag repeated narrator insight summaries (*“他知道”*, *“这意味着”*, *“他意识到”*, *“换句话说”*).
- Run `scripts/repetition_scan.py` to identify excessive summary counts.

### 3. Stock Body Reaction Clichés
- Eliminate repetitive physical shortcuts: tightening knuckles (*指关节发白*), caught breath (*倒吸一口凉气*), darkened eyes (*瞳孔微缩*), cold spines (*后背发凉*).
- Replace with scene-specific actions, object interactions, posture changes, or silence.

### 4. Unearned Aphorisms & Manufactured Depth (FP-006)
- Flag pseudo-philosophical generalizations inserted into ordinary logistical scenes.
- Delete unearned summary sentences at paragraph and chapter ends.

### 5. Paragraph Shape Monotony
- Run `scripts/paragraph_shape_scan.py` to detect long runs of ultra-short paragraphs or unnaturally uniform paragraph lengths.

### 6. Tautological Collocations & Quantifier Clashes (FP-009)
- Scan for hybrid collision of borrowed quantifiers and metaphors (e.g., *“一豆如豆”*, *“一抹如墨”*, *“一丝如丝”*). Enforce single-choice clarity (*“一豆黄光”* OR *“如豆的黄光”*).
- Eliminate redundant psychological adverbs and verbs (e.g., *“心中暗自心想”* $\rightarrow$ *“心想”* / *“暗忖”*).
- Eliminate adverbial duplication (*“忍不住不禁”* $\rightarrow$ *“不禁”*) and organ/perception redundancies (*“双目目光”* $\rightarrow$ *“目光”*).

---

## The Skeptical Reader Test

Before granting a Pass verdict, evaluate the 9 diagnostic questions in `references/quality-gate.md`:
1. *Does the author feel present arranging characters to supply information?*
2. *Does the protagonist deduce truths faster and more correctly than everyone else without cause?*
3. *Do supporting characters vanish the moment the protagonist no longer needs them?*
4. *Is there an unearned aphorism designed solely for superficial depth?*
5. *Would any paragraph be stronger if its final summary sentence were deleted?*
6. *If character names are masked, can key dialogue lines still be distinguished?*
7. *Is every emotional beat explained too completely?*
8. *Does anyone say something exceeding their knowledge, status, or self-interest?*
9. *Was redundant filler prose, padded dialogue, or artificial expansion added merely to hit an arbitrary word count?*

---

## Genre Overlays

Apply only overlays required by the approved Project Profile:

- **Wuxia / Xianxia**: Check decorative pseudo-classical diction, technique-list combat, and realm exposition that halts the scene. Preserve tactical breath, physical injury, and semi-classical cadence.
- **Mystery / Thriller**: Check premature clue explanation, detective-summary narration, and tidy evidence chains.
- **Romance / Emotional Drama**: Check generic emotional labels and intimacy without specific personal habits or choices.
- **Sci-Fi / Fantasy**: Check encyclopedia exposition and unsupported jargon overload. Preserve operational rules.
- **Historical / Court Politics**: Check modern corporate jargon (*“信息粒度”*, *“底层逻辑”*) and ensure dialogue reflects strict feudal status vulnerability.

---

## Output Template

```markdown
## Narrative Humanizer Check

### Passes Evaluated
- Structural Naturalness Pass: Pass | Needs Restructuring
- Surface Naturalness Pass: Pass | Targeted Edits Applied

### Diagnostic Script Findings
- Dialogue Scan: [Clipped count / Question chains]
- Repetition Scan: [Summary phrases count / Clichés count]
- Paragraph Shape Scan: [Rhythm health / Short chains]

### Skeptical Reader Test (8 Questions)
- 1. Information Kiosk: No / [Finding]
- 2. Instant Insight: No / [Finding]
- 3. NPC Utility: No / [Finding]
- 4. Unearned Aphorism: No / [Finding]
- 5. Paragraph Summary: No / [Finding]
- 6. Masked Voice: No / [Finding]
- 7. Over-Explanation: No / [Finding]
- 8. Status Leakage: No / [Finding]

### Findings and Edits
- [Category] — passage/problem → keep / targeted correction / return upstream — rationale

### Preserved Boundaries
- Plot events unchanged: Yes / No
- Character knowledge unchanged: Yes / No
- Protected secrets & rules unchanged: Yes / No
- Proposed Story Memory Changes unchanged: Yes / No

Verdict: Pass / Needs Targeted Revision / Return Upstream
```