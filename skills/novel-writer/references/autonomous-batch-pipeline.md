# Autonomous Batch Pipeline — 自动化连写与整书推进引擎

Use this reference when the user explicitly requests autonomous multi-chapter drafting, continuous volume completion, or whole-book generation without requiring interactive turn-by-turn promotion confirmation for every individual chapter.

---

## 1. Core Operating Principles

1. **Explicit Delegation of Authority**:
   - In standard single-chapter mode, Promotion strictly requires turn-by-turn user confirmation.
   - In Autonomous Batch Mode, the user explicitly grants a **Bounded Batch Promotion Delegation** for a specific scope (e.g. *“连写第 5 到 10 章”*, *“写完第一卷剩余所有章节”*, *“自动推进至完结”*).
   - Within this scope, the system autonomously drafts, reviews, humanizes, scores, promotes, updates `story_memory.md`, and advances to the next chapter.

2. **Hard Circuit Breakers (熔断停机条件)**:
   The autonomous loop **MUST immediately pause and alert the user** if any of the following occur:
   - **Quality Gate Failure**: After 2 automated targeted repair iterations, a chapter still scores $< 9.5 / 10.0$ or any critical dimension is $< 9.0 / 10.0$.
   - **Fact / Knowledge Contradiction**: An unresolvable logical contradiction with `state/story_facts.md` or protected plot boundaries is detected.
   - **Blocking Checkpoint Issue**: A 5-chapter rolling checkpoint audit (`audits/checkpoint_XXX_YYY.md`) identifies a `Blocking Before Next Chapter` issue.
   - **Unresolved User Decision Point**: The volume outline marks a major fork as `[User Decision Required]`.

3. **Incremental Memory & Context Rolling (增量记忆与上下文防膨胀)**:
   - After each chapter is promoted, update `state/story_memory.md` immediately with newly established dynamic states, active goals, and consequences.
   - Next chapter loads only:
     - Durable Master Plan spine + Active Volume Outline;
     - Relevant Project Profile constraints & Style Lock;
     - Compact Character Dialogue Cues (`story_facts.md`);
     - Current dynamic `story_memory.md`;
     - Previous chapter ending paragraphs ($N-1$ interface).
   - This ensures continuous drafting across dozens of chapters never exceeds LLM context windows or degrades into cognitive drift.

---

## 2. The 7-Step Autonomous Chapter Micro-Loop

For each Chapter $K$ in requested range $[M..N]$:

```text
[Loop Start: Chapter K]
  │
  ├─ Step 1: Auto-Brief Generation
  │    - Reads active volume plan for Chapter K contract & objectives.
  │    - Extracts Chapter K-1 ending interface (time, place, items, emotion).
  │    - Generates work/chapter-K/brief.md.
  │
  ├─ Step 2: Auto-Drafting
  │    - Generates candidate prose in work/chapter-K/candidate.md.
  │    - Applies Dialogue Engine (6 drivers), Style Lock, and Character Voice Signatures.
  │    - Respects narrative density: Concludes when dramatic beat finishes cleanly without artificial padding.
  │
  ├─ Step 3: Auto-Review & Chapter Interface Check
  │    - Verifies N-1 -> N transition (time continuity, spatial integrity, object custody).
  │    - Validates against Protected Story Facts.
  │
  ├─ Step 4: Dual-Pass Humanization
  │    - Structural Naturalness Pass (macro): eliminates NPC info kiosks, cognitive acceleration.
  │    - Prose Stylist: refines cadence while preserving hesitation and supported bias.
  │    - Surface Naturalness Pass (micro): removes clipped fragments, summary phrases, clichés.
  │
  ├─ Step 5: Quality Gate & Diagnostic Scan
  │    - Runs 7-dimension scoring table (threshold: >= 9.5 / 10.0, no critical < 9.0).
  │    - Runs scan_chapter.py internally.
  │    - IF Gate FAILS:
  │         Executes up to 2 targeted repair passes.
  │         IF still failing -> TRIP CIRCUIT BREAKER (Pause loop & notify user).
  │
  ├─ Step 6: Autonomous Promotion & State Update
  │    - Copies candidate.md to chapters/chapter-K.md.
  │    - Marks work/chapter-K/audit.md as PROMOTED (Autonomous Mode).
  │    - Updates state/story_memory.md (character location, injuries, plot threads, clues).
  │
  ├─ Step 7: Milestone Audit & Advance
  │    - IF K % 5 == 0: generates audits/checkpoint_...md (checks for blocking flags).
  │    - IF Arc/Volume ends: generates Arc/Volume Completion Record in volume file.
  │    - IF K == N (Target reached): FINISH loop and output batch summary.
  │    - ELSE: K = K + 1 -> immediately loop to Step 1 for next chapter.
```

---

## 3. Supported Batch Delegation Commands

The user can initiate autonomous batch runs via clear natural language commands:

- **Specific Range**:
  - *“使用 novel-writer 自动写完第 3 到第 7 章。”*
  - *“从第 8 章开始自动连写 5 章。”*
- **Volume / Arc Completion**:
  - *“自动连写完成第一卷剩余章节。”*
  - *“把当前电竞赛事弧光（第 12–16 章）自动推进完结。”*
- **Long-Running / Slash Command**:
  - `/goal 依据 master-plan 和 volume-001 大纲，全自动写完前 10 章并完成各章质检自愈。`

---

## 4. Automated Error Recovery (自愈与微调协议)

When a chapter candidate fails the Quality Gate during Step 5:

1. **Diagnosis**: Identify exact sub-9.0 categories (e.g. Dialogue clipped, Summary phrases excess, Rhythm monotonous).
2. **Targeted Surgical Repair (Pass 1)**:
   - Apply targeted rewrite to offending scenes or lines without altering confirmed story events.
   - Re-run Quality Gate.
3. **Secondary Repair (Pass 2)**:
   - If still $< 9.5$, check Structural Naturalness (e.g., scene motivation, information pacing).
   - Re-draft the flawed section and re-score.
4. **Circuit Breaker Halt**:
   - If after 2 repair iterations the score is still $< 9.5$, halt immediately.
   - Output clear diagnostic report showing:
     - Current score and specific defect;
     - What was attempted in repairs;
     - Exact decision or revision needed from the user.

---

## 5. Milestone & Checkpoint Handling in Batch Mode

1. **5-Chapter Checkpoints**:
   - When reaching chapter 5, 10, 15, etc., the pipeline automatically compiles `audits/checkpoint_XXX_YYY.md`.
   - If only `Required During Next Window` or `Watchlist` items are found, the batch continues.
   - If any `Blocking Before Next Chapter` issue is flagged, the pipeline triggers the circuit breaker and stops.

2. **Arc / Volume Completion Records**:
   - When the final chapter of an arc or volume is promoted, the pipeline automatically compiles the compact Arc/Volume Completion Record into `plans/volumes/volume-XXX.md` and updates `master-plan.md` pointer before starting the next arc.
