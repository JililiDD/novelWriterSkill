# Feedback Promotion Protocol & Project Craft Lessons — 用户反馈升级与项目写作经验沉淀

Use this reference to capture, upgrade, and persist recurring writing feedback into project-level craft lessons in `state/writing_lessons.md`, and to look up established failure patterns (`FP-001` through `FP-008`).

---

## 1. Problem & Purpose

In long serialized projects, AI models frequently repeat systemic writing habits (e.g. clipped dialogue, all characters sounding like cold strategists, narrator repeatedly summarizing themes at paragraph ends).

Treating these issues solely as local single-chapter bugs leads to repetitive patching. **Feedback Promotion systematically converts repeated user corrections into persistent project-level craft rules.**

---

## 2. Feedback Promotion Protocol

```text
Level 1: Local Feedback
  │  (User corrects a single phrase, line, or paragraph)
  ▼
Fix applied locally in candidate.md
  │
  ├─ If issue is isolated → Done.
  │
  └─ If similar feedback occurs 2+ times across chapters/scenes
        │
        ▼
Level 2: Repeated Pattern Recognition
  │  (Assistant identifies the underlying generative defect)
  │  (Assistant drafts a proposed Project Craft Rule)
  ▼
Propose Craft Rule to User
  │
  ├─ User declines → Kept as local preference.
  │
  └─ User explicitly confirms ("对，以后都按这个规矩写", "确认加入项目经验")
        │
        ▼
Level 3: Project Craft Lesson Persistence
  │  (Write to state/writing_lessons.md and reference in Project Profile)
  ▼
Active Enforcement in all subsequent Briefs, Drafting, and Humanizer passes
```

---

## 3. Project Craft Lessons File (`state/writing_lessons.md`)

When confirmed by the user, store project lessons in `state/writing_lessons.md` using the standard format:

```markdown
# Project Craft Lessons

## FP-001 — [Title of Failure Pattern]

### Symptom
- [Observable manifestations in text, e.g., consecutive 2–5 character interrogative fragments]
- [Multiple distinct characters sharing the same abrupt rhythm]

### Why it fails
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

---

## 5. Authority & Maintenance Rules

1. **Explicit User Approval Required**: The assistant must never silently write or alter `state/writing_lessons.md` without explicit user confirmation.
2. **Selective Context Loading**: Subsequent chapter briefs load only the active lesson summaries relevant to that chapter’s specific risks.
3. **Audit Enforcement**: `audit.md` verifies compliance against confirmed project craft lessons during Content Review and Narrative Humanizer stages.
