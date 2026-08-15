# Startup Workflow & Autonomous Project Genesis — 新故事立项、多版本推演与全案初始化

Use this reference when starting a new novel, executing one-click autonomous project genesis, or materially re-establishing an existing project.

Load `creation-paths.md` first for path selection and confirmation boundaries. `layered-novel-planning.md` owns persisted master/volume/arc planning. `style-calibration.md` owns style calibration. `style-and-element-selection.md` owns element compatibility.

---

## 1. Two Startup Modes

| Startup Mode | Description | Typical Use Case |
|---|---|---|
| **Interactive Discovery Mode** (交互共创模式) | Step-by-step interview exploring core appeal, protagonist drive, and style choices in 1–2 questions per turn. | Author wants deep hands-on control over every plot seed and relationship bond. |
| **Autonomous Project Genesis Mode** (一键全案立项模式) | Single-prompt autonomous generation of complete novel architecture: multi-variant comparison, master plan, volume 1 chapter outlines, style lock, and character dialogue profiles. | User provides a high-level theme or seed and wants AI to autonomously design the whole book. |

---

## 2. Autonomous Project Genesis Mode (一键全案智能立项)

When the user provides a high-level theme or requests autonomous project setup (e.g. *“我想写一本五代十国权谋小说，帮我自动完成全书立项与第一卷大纲”*), execute the following 5-phase protocol:

```text
User Theme / Seed Prompt
      ↓
[Phase 1] Multi-Variant Concept Generation & Tradeoff Analysis (2–3 distinct architectural variants)
      ↓
[Phase 2] Deep Project Architecture Drafting (Master Plan, Vol 1 Chapter Beats, Style Lock, Story Facts)
      ↓
[Phase 3] Genesis Architecture Self-Audit (Core Drive, Opposition, Arc Feasibility, Mechanism Agency)
      ↓
[Phase 4] Presentation & Confirmation Gate
      ├─ Branch A (Default / Review): Present Executive Brief for User Review & Approval
      └─ Branch B (Direct Auto-Start): If user commanded full delegation ("无需确认直接开写"), bypass turn
      ↓
[Phase 5] Seamless Handoff to Autonomous Batch Pipeline or Interactive Chapter Drafting
```

---

### Phase 1: Multi-Variant Concept Generation & Tradeoff Analysis (多方案对比推演)

For a given genre seed, construct **2–3 distinct architectural variants (方案 A / B / C)** combining different elements from `element-library.md` and styles from `style-library.md`:

```markdown
### 方案 A：[方案名称，例如：沉浸式历史权谋正剧]
- **核心元素组合**：[例如：真假身份 + 幕后推演 + 阶层博弈]
- **主线钩子与主角设定**：[一句话核心动力与内在矛盾]
- **核心看点与读者爽点**：[阅读吸引力所在]
- **潜在风险与写作难度**：[复杂度预算与节奏要求]

### 方案 B：[方案名称，例如：经营面板与暗线博弈流]
- **核心元素组合**：[例如：经营面板 + 宗门/商帮基建 + 隐藏身份]
...
```

*Note: If the user directly commands an immediate, single-track setup without wanting variants, pick the single highest-compatibility architecture and proceed directly to Phase 2.*

---

### Phase 2: Full Project Artifact Generation

Generate the canonical set of project files:

1. **`plans/master-plan.md`**:
   - **Story Kernel**: Core appeal, protagonist external goal, current pressure, internal contradiction, opposition logic, 1–3 core relationships, first irreversible choice, climactic value conflict.
   - **Whole-Book Roadmap**: Target scale (e.g. 3–4 volumes), volume titles, core conflicts, and climax turning points.
2. **`plans/volumes/volume-001.md`**:
   - Volume 1 Theme, flexible word count range, and Arc breakdown.
   - **Chapter-by-Chapter Beat Contracts** for Arc 1 (Ch 1–10/15):
     - *Opening Situation & POV*;
     - *Immediate Goal & Opposition Friction*;
     - *Turning Point & Consequence/Cost*;
     - *Clue / Connection to next chapter*.
3. **`state/project_profile.md`**:
   - Selected Main/Supporting Styles, Element Mix, Tone Lock, Flexible Chapter Scale Benchmark (e.g. 2,500–4,000 words, tension-first, zero artificial padding), and **800-character Narrative Anchor Sample** (pre-calibrated benchmark text).
4. **`state/story_facts.md`**:
   - Core Character **Dialogue Profiles** (Goal, Knowledge baseline, Status impact, Default tactic, Pressure shift) and 1–3 Recognition Anchors.
   - Established world/historical rules and protected plot secrets.
5. **`state/story_memory.md`**:
   - Initialized dynamic state ready for Chapter 1.

---

### Phase 3: Genesis Alignment Self-Audit (题材与读者承诺对齐自检)

Before presenting or finalizing the project, run a **Genre-Adaptive Health Check** to ensure the design fulfills the specific core appeal of the user's chosen genre (rather than imposing a one-size-fits-all serious literary standard):

| Dimension | Verification Question | Genre-Adaptive Standard |
|---|---|---|
| **1. Reader Promise & Core Appeal** | Does the outline deliver the specific emotional payoff of the chosen genre? | • **爽文 / 打脸 / 无敌流**：爽点节奏明确，升级或惩处反馈爽快直接；<br>• **正剧 / 权谋 / 历史**：博弈有来有回，动机扎实；<br>• **日常 / 甜宠 / 种田**：氛围舒适轻快，互动有化学反应；<br>• **悬疑 / 规则怪谈**：悬念充足，谜面有吸引力。 |
| **2. Core Mechanism / Golden Finger** | Does the core mechanism (gold finger, system, identity, or skill) fit the genre's power level? | • **无敌 / 爽文流**：金手指反馈直接，发挥应有的爽感威力；<br>• **硬核 / 成长流**：机制有清晰规则与代价约束。 |
| **3. Pacing & Hook Delivery** | Is the core hook established promptly in Chapter 1–3? | The reader gets the promised hook and engine without unnecessary delay. |
| **4. Internal Setting Coherence** | Does the story stay coherent within its own established premise? | Powers, identities, and world rules operate consistently according to the chosen genre's internal logic. |

Adjust the outlines and characters to maximize the chosen genre's core appeal before delivery.

---

### Phase 4: Confirmation & Bypass Gate (确认与直达开关)

#### Branch A: Executive Review (Default / Recommended)
Present the executive summary to the user:
- 📖 **Story Kernel & Hook** (一句话主线与终极冲突)
- 🎭 **Character Voice & Recognition Anchors** (核心人物卡)
- 🗺️ **Volume 1 Chapter-by-Chapter Outlines** (第一卷逐章细纲)
- 🎨 **Style Lock & Text Anchor Preview** (文风试写段落)

Ask the user:
> *“全案立项与第一卷细纲已设计完成并通过架构自检。您是否需要微调大纲或人物设定？如无异议，可直接回复‘确认’，或发送‘自动连写第 1–5 章’开始创作。”*

#### Branch B: Direct Auto-Start (全权托管直达)
If the user's initial prompt explicitly said *"无需向我确认，自动立项并直接连写第 1–5 章"* or *"全权托管完成立项与正文创作"*:
1. Initialize all project files directly;
2. Verify Phase 3 Self-Audit passes;
3. Output a 1-paragraph confirmation notice;
4. **Immediately transition into `references/autonomous-batch-pipeline.md`** to draft chapters without pausing.

---

## 3. Interactive Discovery Mode (传统交互共创模式)

When the user prefers step-by-step collaborative discussion:

1. Scan user's seed information into Known, Suggested, Open, and Rejected categories.
2. Ask at most **two primary high-leverage questions per turn** regarding Core appeal, Protagonist contradiction, or Opposition logic.
3. Confirm Story Kernel before generating formal files.
4. Offer Optional Style Calibration (`references/style-calibration.md`).
5. Initialize canonical project files progressively.