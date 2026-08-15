# Feedback Promotion Protocol — 用户反馈升级与双层写作经验沉淀

Use this reference to capture, upgrade, and persist recurring writing feedback into:
1. **Global Writing Rules** (`~/.novel-writer/global_writing_rules.md`) — universal linguistic and craft rules across **all novel projects**;
2. **Project Craft Lessons** (`state/writing_lessons.md`) — novel-specific craft lessons and style boundaries;
and to look up established failure patterns (`FP-001` through `FP-009`).

---

## 1. Problem & Purpose

In long serialized projects, AI models frequently repeat systemic writing habits (e.g. clipped dialogue, tautological modifier collisions, all characters sounding like cold strategists, narrator repeatedly summarizing themes at paragraph ends).

Treating these issues solely as local single-chapter bugs leads to repetitive patching. **Feedback Promotion systematically converts repeated user corrections into persistent global or project-level rules.**

---

## 2. Feedback Promotion Protocol & Dual-Tier Architecture

```text
Level 1: Local Feedback
  │  (User corrects a single phrase, line, or paragraph)
  ▼
Fix applied locally in candidate.md
  │
  ├─ If issue is isolated → Done.
  │
  └─ If similar feedback occurs 2+ times OR is a fundamental linguistic/craft rule
        │
        ▼
Level 2: Scope Classification & Rule Drafting
  │
  ├─ [Universal Craft / Linguistic Bug] (e.g. 语义叠床架屋 "一豆如豆", NPC问答机, 解释预算超标)
  │    └─ Target: Global Writing Rules (~/.novel-writer/global_writing_rules.md)
  │
  └─ [Project-Specific Style / Tone Drift] (e.g. 当前小说的特定阵营语气、术语规范、门派口吻)
       └─ Target: Project Craft Lessons (state/writing_lessons.md)
        │
        ▼
Propose Rule & Target Scope to User
  │
  ├─ User declines → Kept as local preference.
  │
  └─ User explicitly confirms ("加入全局规则" / "加入本书经验")
        │
        ▼
Level 3: Rule Persistence & Cascade Loading
  │  (Writes to ~/.novel-writer/global_writing_rules.md OR state/writing_lessons.md)
  ▼
Cascade Enforcement across all subsequent Briefs, Drafting, Humanizer, and Quality Gate passes
```

---

## 3. Storage Formats

### (A) Global Writing Rules (`~/.novel-writer/global_writing_rules.md`)
Stored globally in user's home directory. Automatically loaded across **all novel projects**:
- Core linguistic invariants (e.g., anti-tautology, explanation budget, cognitive pacing);
- Universal AI anti-template and anti-cliché rules;
- Cross-project narrative humanization standards.

### (B) Project Craft Lessons (`state/writing_lessons.md`)
Stored inside the specific novel's repository under `state/`. Owns book-specific constraints:

```markdown
# Project Craft Lessons

## FP-XXX — [Title of Project Lesson]

### Symptom
- [Observable manifestations in text]

### Why it fails
- [Root cause / specific tone conflict with this novel's style lock]

### Correction
- [Actionable positive generation rule for this book]

### Scope
- Project-level confirmed lesson. Effective from Chapter [XXX] onward.
```
- [Root cause, e.g., mistaking clipped sentence fragments for intelligence or historical gravity]
- [Homogenizes dialogue cadence across the cast]

### Correction
- [Actionable positive generation rule, e.g., dialogue must express complete grammatical units by default, shaped by the speaker's specific social status and immediate objective]

### Check
- [Diagnostic method: Dialogue Scan / Speaker-Substitution Check / Humanizer inspection]

### Scope
- Project-level confirmed lesson. Effective from Chapter [XXX] onward.
```

---

## 4. Catalog of Common Failure Patterns

Use these standard templates when diagnosing issues or proposing project-level rules:

### FP-001: Clipped Dialogue & Shared Cynical Fragments (碎片化假精明对白)
- **Symptom**: Dialogue dominated by 2–5 character fragments (*“为何？”*, *“不然？”*, *“走。”*). Multiple characters share an abrupt, cynical cadence.
- **Why it fails**: Confuses omission with strategic intelligence. Destroys voice differentiation.
- **Generative Correction**: Default to complete grammatical units. Generate dialogue from the speaker’s goal, status vulnerability, and relationship strategy (`references/dialogue-engine.md`).

### FP-002: Frictionless NPC Information Kiosks (NPC 信息问答机)
- **Symptom**: Secondary characters immediately, accurately, and dispassionately provide exactly the data the protagonist requires.
- **Why it fails**: Eliminates social friction; makes the world feel like a convenient video game menu.
- **Generative Correction**: Apply **Functional Character Realism** (`references/dialogue-engine.md`): NPCs care about wages, blame avoidance, physical safety, and possess fragmented knowledge.

### FP-003: Cognitive Acceleration & Instant Insight (主角认知超速)
- **Symptom**: Protagonist sees a tiny ambiguous clue and immediately deduces the full conspiracy without false leads or verification costs.
- **Why it fails**: Eliminates dramatic tension and makes competence feel authorially declared.
- **Generative Correction**: **Competence is behavioral**: show the protagonist noticing clues, testing hypotheses, paying verification costs, and managing uncertainty.

### FP-004: Explanatory Echo & Theme Summaries (多重解释与段尾主题总结)
- **Symptom**: Evidence presented $\rightarrow$ Character explains $\rightarrow$ Narrator explains again $\rightarrow$ Paragraph concludes with an abstract moral.
- **Why it fails**: Violates **Evidence Before Explanation**; insults reader intelligence.
- **Generative Correction**: Enforce the **Explanation Budget**: once concrete action or dialogue conveys meaning, stop explaining immediately.

### FP-005: Symmetrical & Homogeneous Paragraph Shapes (模板化段落节律)
- **Symptom**: Every paragraph follows identical geometry: 2 lines setup $\rightarrow$ 2 lines reaction $\rightarrow$ 1 line summary.
- **Why it fails**: Creates a hypnotic, monotonous cadence that flattens narrative momentum.
- **Generative Correction**: Let syntax follow **cognition and scene pressure**. Asymmetrical movements replace mechanical paragraphs.

### FP-006: Manufactured Depth & Unearned Aphorisms (强行金句与虚假深刻)
- **Symptom**: Unprovoked philosophical generalizations (*“这世间的人心，大抵如此”*) inserted into ordinary logistical scenes.
- **Why it fails**: Sounds like self-conscious authorial posturing.
- **Generative Correction**: Anchor resonance in concrete material choices and physical losses rather than generic slogans.

### FP-007: Universal Service to Protagonist (全员服务型世界)
- **Symptom**: All surrounding characters exist solely to react, praise, or be tested by the protagonist.
- **Why it fails**: The world feels sterile and artificial.
- **Generative Correction**: Every named character must have independent daily duties, schedules, and reasons to act even when the protagonist is absent.

### FP-008: Premature Emotional Resolution (情绪超速消化)
- **Symptom**: Extreme shock, betrayal, or injury is acknowledged in one sentence and completely resolved in the next.
- **Why it fails**: Strips dramatic events of lasting consequence.
- **Generative Correction**: Track emotional aftermath across scenes as active friction: fatigue, altered attention, hesitation, and physical exhaustion.

### FP-009: Tautological Collocation & Semantic Collision (语义叠床架屋与量词修饰撞车)
- **Symptom**:
  1. *Quantifier / Metaphor collision*: e.g., “一豆如豆的黄光”, “一抹如墨的夜色”, “一丝如丝的凉风”.
  2. *Psychological tautology*: e.g., “心中暗自心想”, “暗暗心下忖度”, “心底暗想”.
  3. *Adverbial duplication*: e.g., “忍不住不禁”, “由不得禁不住”, “仿佛好像”.
  4. *Organ / perception redundancy*: e.g., “双目目光望去”, “耳边耳畔听闻”.
- **Why it fails**: Autoregressive attention blends mutually exclusive collocations, resulting in ungrammatical stuttering and semantic bloating.
- **Generative Correction**: Enforce single-choice clarity:
  - Pick either quantifier or metaphor: *“一豆黄光”* OR *“如豆的黄光”* (NEVER both).
  - Pick either verb or adverb: *“心想”* OR *“暗忖”* (NEVER *“暗自心想”*).
  - Pick single adverb: *“不禁”* OR *“忍不住”*.
  - Surface Naturalness Pass scans and eliminates all modifier collisions.

---

## 5. Authority & Maintenance Rules

1. **Dual Cascade Loading**: All novel writing workflows automatically load:
   - `~/.novel-writer/global_writing_rules.md` (Global cross-novel invariants);
   - `state/writing_lessons.md` (Project-specific lessons, if present).
2. **Explicit User Approval Required**: The assistant must never silently write or alter `global_writing_rules.md` or `state/writing_lessons.md` without explicit user confirmation.
3. **Selective Brief Loading**: Subsequent chapter briefs load the active lesson IDs relevant to that chapter's specific risks.
4. **Audit Enforcement**: `audit.md` verifies compliance against both global and project craft lessons during Content Review and Narrative Humanizer stages.
