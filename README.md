# Novel Writer

Novel Writer is a GitHub-installable plugin and reusable Skill for adaptive story development, standalone fiction, persistent novel planning, autonomous batch continuous drafting, style calibration, generative dialogue engineering, dual-pass narrative humanization, chapter quality gates, seven-stage prose delivery, selective context loading, continuity control, revision, and multi-volume maintenance.

Version 2.6.0 introduces the **Autonomous Batch Pipeline & Whole-Book Generation**, **Single-Command Unified Diagnostic Scanner (`scan_chapter.py`)**, **Batch Chapter Inspector (`batch_runner.py`)**, alongside **Mandatory Promotion Confirmation Gate**, **Style Calibration & Style Lock**, the **Dialogue Engine**, and the **7-Dimension Chapter Quality Gate**.

## Install from GitHub

The repository is both the marketplace and plugin source.

### Claude Code

```bash
claude plugin marketplace add JililiDD/novelWriterSkill
claude plugin install novel-writer@novel-writer
```

Restart Claude Code or open a new session after installation.

### Codex

```bash
codex plugin marketplace add JililiDD/novelWriterSkill
codex plugin add novel-writer@novel-writer
```

Restart Codex or open a new session after installation.

## Install from a local checkout

Replace `/absolute/path/to/novelWriterSkill` with this repository's absolute path.

### Claude Code

```bash
claude plugin marketplace add /absolute/path/to/novelWriterSkill
claude plugin install novel-writer@novel-writer
```

### Codex

```bash
codex plugin marketplace add /absolute/path/to/novelWriterSkill
codex plugin add novel-writer@novel-writer
```

## Use the plugin

Skills activate when the request matches their purpose. Example requests:

```text
Use novel-writer to develop the Story Kernel and calibrate narrative style for a new historical novel.
Use novel-writer to autonomously draft and verify chapters 1 to 5 with rolling checkpoints.
Use novel-writer to write this as a standalone one-shot with no project state.
Use novel-writer to prepare chapter 8 brief, candidate, audit, and quality gate scoring.
Use novel-writer to compact the completed arc and prepare the next arc.
Use novel-writer to revise chapter 3 without changing protected story facts.
```

## Two creation paths & Autonomous Batch Mode

### Standalone Creation
Use for a self-contained one-shot, scene, experiment, or bounded rewrite that does not need continuing project state. Default deliverables: `brief.md`, `candidate.md`, `audit.md`, `final.md`.

### Project Creation
Use for multi-chapter, serialized, shared-setting, or existing-project work that must preserve planning, stable facts, and current state. Length alone does not select a path.

### Autonomous Batch Mode
When explicitly authorized (e.g. *“自动连写第 5 到 10 章”*, *“按大纲写完第一卷”*, or slash command `/goal`), Novel Writer enters autonomous batch execution:
- Autonomously iterates: `Auto-Brief` $\rightarrow$ `Auto-Draft` $\rightarrow$ `Auto-Review & Interface` $\rightarrow$ `Dual-Pass Humanizer` $\rightarrow$ `Quality Gate` $\rightarrow$ `Auto-Promote` $\rightarrow$ `Incremental Memory Update` $\rightarrow$ Advance to next chapter.
- **Circuit Breakers**: Immediately halts and alerts the user if quality score $< 9.5$ after 2 auto-repair iterations, an unresolvable story fact conflict occurs, or a 5-chapter rolling checkpoint flags a blocking issue.

## Adaptive story discovery & Autonomous Project Genesis

Novel Writer supports two project startup workflows:
1. **Autonomous Project Genesis (一键全案智能立项)**:
   - For a single theme seed (e.g. *"五代十国权谋账房"*), autonomously constructs **2–3 distinct architectural variants (方案 A/B/C)** with pros/cons tradeoff analysis.
   - Autonomously drafts full project files: `master-plan.md` (Story Kernel & Volume Map), `volume-001.md` (Arc 1 Chapter-by-Chapter Beat Contracts), `project_profile.md` (Style Lock & Narrative Anchor Sample), and `story_facts.md` (Character Dialogue Profiles).
   - Executes the **Genesis Architecture Self-Audit** (evaluating protagonist agency, opposition logic, and arc escalation).
   - **Confirmation Gate**: Presents an Executive Brief for user confirmation by default, or directly initiates continuous drafting if the user explicitly commanded full delegation.
2. **Interactive Discovery Mode (深度交互共创)**:
   - Explores core appeal, internal contradiction, and choice architecture in 1–2 high-leverage questions per turn.
   - Offers optional **Style Calibration** (`references/style-calibration.md`): generates 2–4 controlled variants (600–1,500 Chinese characters) to lock Style Lock and Narrative Anchor.

## Project information model

- **Master plan** (`plans/master-plan.md`) — Story Kernel, whole-book direction, volume map, active pointer, full-book boundaries.
- **Volume files** (`plans/volumes/volume-XXX.md`) — each volume, its arcs, and compact Completion Records.
- **Project Profile** (`state/project_profile.md`) — style, elements, Tone Lock, reader promise, Style Lock, Style Anchors, Rejected Drift Notes.
- **Story Facts** (`state/story_facts.md`) — stable confirmed facts, protected facts, Dialogue Profiles, Recognition Anchors.
- **Story Memory** (`state/story_memory.md`) — active/open dynamic current state only.
- **Project Craft Lessons** (`state/writing_lessons.md`) — confirmed project-level writing rules and failure pattern mitigations.
- **Promoted chapters** (`chapters/chapter-XXX.md`) — original evidence of happened events.
- **Work brief & audit** (`work/chapter-XXX/`) — current contract, isolated candidate, Quality Gate scores, verification, and promotion record.

Candidate prose is isolated and has **zero authority** until officially promoted.

## Recommended project structure

```text
novel-project/
├── plans/
│   ├── master-plan.md
│   └── volumes/
│       ├── volume-001.md
│       └── volume-002.md
├── state/
│   ├── project_profile.md
│   ├── story_facts.md
│   ├── story_memory.md
│   └── writing_lessons.md          # project craft lessons & failure pattern rules
├── chapters/
│   ├── chapter-XXX.md
│   └── index.md                    # optional when historical lookup becomes costly
├── work/
│   └── chapter-XXX/
│       ├── brief.md
│       ├── candidate.md
│       └── audit.md
├── audits/                         # rolling checkpoints and active cross-range issues
├── runs/                           # optional recovery/selection records
├── backups/                        # backups created before official overwrite
└── archive/                        # completed arc/work retention
```

## Dialogue Engine & Character Realism

Novel Writer generates dialogue from six active forces:
$$\text{Dialogue} = \text{Current Goal} + \text{Knowledge Boundary} + \text{Status/Occupation} + \text{Relationship} + \text{Immediate Emotion} + \text{Speaker Strategy}$$

- **Core & recurring characters** maintain a Dialogue Profile in Story Facts.
- Key decisions and conflict lines undergo the **Speaker-Substitution Check** to ensure voice differentiation.
- **Secondary characters & NPCs** follow **Functional Character Realism ("Ordinary People Mode")**: partial knowledge, immediate self-preservation stakes (wages, safety, liability), concrete particulars over abstract summaries, and natural imperfections.

## Dual-Pass Humanizer & Evidence Before Explanation

Naturalness is enforced across two passes:
1. **Pass 1: Structural Naturalness Pass** (Macro) — eliminates smartness inflation, NPC info kiosks, cognitive acceleration, all-service-to-protagonist scenes, and symmetrical paragraph shapes before stylistic polishing.
2. **Pass 2: Surface Naturalness Pass** (Micro) — eliminates clipped dialogue chains, insight summary phrases (*“他知道”*, *“这意味着”*), body reaction clichés, and unearned aphorisms.

The **Explanation Budget** dictates: *Evidence first; explanation only when necessary for the next action. If the reader can already follow, stop explaining.*

## Chapter Quality Gate & Invalidation Rules

Before a candidate is eligible for promotion, it must pass the 7-Dimension Quality Gate (`references/quality-gate.md`):
- Contract / Continuity (20%, 2.0 pts)
- Character / Voice (20%, 2.0 pts)
- Naturalness / Anti-Template (20%, 2.0 pts)
- Scene / Pacing (15%, 1.5 pts)
- POV / Cognitive Ownership (10%, 1.0 pts)
- Prose Precision / Rhythm (10%, 1.0 pts)
- Chapter Interface (5%, 0.5 pts)

**Gate Threshold**: Total Score $\ge 9.5 / 10.0$ and no critical category $< 9.0 / 10.0$.
Substantive candidate modifications invalidate dependent downstream checks and require re-execution.

## Dynamic Chapter Scale & Anti-Padding Principle

- Chapter word counts (e.g. 2,500–4,000 words) are flexible guidance targets, not rigid boundaries.
- **Narrative tension and dramatic completeness strictly override word count quotas**: if a chapter naturally and completely delivers its core dramatic beat, turning point, and closing hook in 2,500 words, artificial expansion/padding to reach 5,000 words is forbidden.

## Mandatory Promotion Confirmation Gate

1. Final Verification passing verdict yields **`PROMOTION READY`**, never silent Promotion in standard interactive mode.
2. Candidate prose and proposed Story Memory changes are **never** written to official project files without a fresh, explicit user confirmation in the current turn (unless explicitly operating under Autonomous Batch Mode delegation).
3. Official chapters are protected with pre-overwrite backups and post-write rereads.

## Seven-stage prose delivery

1. **Preflight** — context assembly & dependency verification.
2. **Draft Writing** — candidate drafting applying positive generation principles & Dialogue Engine.
3. **Content Review** — Character Check, Story Fact & Continuity Check, Chapter Interface Check.
4. **Prose Refinement** — Structural Naturalness $\rightarrow$ Prose Stylist $\rightarrow$ Surface Humanizer.
5. **Story Fact Check** — semantic comparison against protected facts & brief.
6. **Final Verification & Quality Gate** — Quality Gate scoring ($\ge 9.5$) & Skeptical Reader Test $\rightarrow$ `PROMOTION READY`.
7. **Promotion & State Update** — official chapter overwrite, backup, post-write reread, Story Memory update $\rightarrow$ `PROMOTED`.

## Rolling checkpoint audits

Project Creation defaults to one Checkpoint per five promoted chapters (`audits/checkpoint_001_005.md`). It reviews only the new 5 chapters, inherits Carry-Forward Constraints, and classifies findings into **Blocking Before Next Chapter**, **Required During Next Window**, and **Watchlist**.

## Diagnostic scan scripts

Included in `skills/novel-writer/scripts/`:
- `scan_chapter.py` — unified single-command diagnostic scanner (dialogue, repetition, paragraph cadence, interface).
- `batch_runner.py` — batch multi-chapter sequence checker, word count aggregator, and diagnostic verifier.
- `dialogue_scan.py` — scans clipped dialogue fragments and interrogative chains.
- `repetition_scan.py` — scans explanatory summary phrases and reaction clichés.
- `paragraph_shape_scan.py` — detects ultra-short paragraph runs and geometric monotony.
- `chapter_interface_scan.py` — extracts boundary paragraphs across Chapter $N-1 \rightarrow N \rightarrow N+1$.

## Plugin structure

- `.claude-plugin/plugin.json` — Claude plugin manifest (v2.6.0)
- `.codex-plugin/plugin.json` — Codex plugin manifest (v2.6.0)
- `.agents/plugins/marketplace.json` — Codex marketplace metadata (v2.6.0)
- `.claude-plugin/marketplace.json` — Claude marketplace metadata (v2.6.0)
- `skills/novel-writer/SKILL.md` — compact control plane and intent router
- `skills/novel-writer/agents/openai.yaml` — ChatGPT Skill interface metadata
- `skills/novel-writer/references/` — 23 selectively loaded planning, batch automation, style calibration, dialogue engine, delivery, state, continuity, and quality protocols
- `skills/novel-writer/scripts/` — Python diagnostic and batch automation utilities
- `skills/novel-writer/assets/` — Story Memory, optional run-record, and cross-range audit templates

## License

MIT
