# Novel Writer

Novel Writer is a GitHub-installable plugin and reusable Skill for adaptive story development, standalone fiction, persistent novel planning, seven-stage prose delivery, selective context loading, continuity control, revision, recovery, and multi-volume maintenance.

Version 2.0 is a clean break. Projects created under older layouts must migrate active information into the canonical Project Profile, Story Facts, Story Memory, master-plan, volume, chapter, and work owners before continuing.

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
Use novel-writer to develop the Story Kernel with me and create a persistent novel project.
Use novel-writer to write this as a standalone one-shot with no project state.
Use novel-writer to prepare chapter 8 brief, candidate, and audit.
Use novel-writer to compact the completed arc and prepare the next arc.
Use novel-writer to revise chapter 3 without changing stable story facts.
```

## Two creation paths

### Standalone Creation

Use for a self-contained one-shot, scene, experiment, or bounded rewrite that does not need continuing project state.

Default files:

```text
brief.md
candidate.md
audit.md
final.md
```

### Project Creation

Use for multi-chapter, serialized, shared-setting, or existing-project work that must preserve planning, stable facts, and current state.

Length alone does not select a path. A short chapter inside a novel is Project Creation; a long independent one-shot may remain Standalone Creation.

Novel Writer has no rigor modes. One quality workflow applies throughout. Extra checks are added only when the task touches protected facts, plan boundaries, or file-safety risks.

## Adaptive story discovery

For a new persistent project, Novel Writer first scans what the user supplied and asks only high-leverage questions about:

- core appeal and reader promise;
- protagonist goal, current pressure, and internal contradiction;
- opposition objective or stable pressure logic;
- one to three plot-relevant relationships;
- the first irreversible choice and climactic value conflict.

Each turn asks at most two primary questions. Confirmed, Suggested, Open, and Rejected directions remain distinct. The result becomes the Story Kernel inside `plans/master-plan.md`.

## Project information model

Novel Writer separates information by authority:

- **Master plan** — Story Kernel, whole-book direction, volume map, current pointer, and full-book boundaries
- **Volume files** — each volume, its arcs, and compact Completion Records
- **Project Profile** — style, elements, Tone Lock, reader promise, and Style Anchors
- **Story Facts** — stable confirmed facts, protected facts, and recurring-character Voice Signatures
- **Story Memory** — active/open current state only
- **Promoted chapters** — original evidence of happened events
- **Brief** — current work-unit contract, selected context, and triggered checks
- **Audit** — findings, proposed Story Memory changes, Stable Setting Candidates, verification, and Promotion Result

Future plans are not happened events. Stable Setting Candidates do not become Story Facts without explicit confirmation.

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
│   └── story_memory.md
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
│   ├── active/
│   └── archive/
├── backups/                        # only before official overwrite
└── archive/                        # only when completed work needs retention
```

Existing projects must migrate active information into the canonical owners before continuing. Superseded active files should be archived or deleted so each information class has one authority.

## Volume and arc lifecycle

`plans/master-plan.md` remains compact and indexes all volumes.

Each `plans/volumes/volume-XXX.md` permanently stores that volume. The active arc keeps detailed planning. When an arc completes, its detail is compacted into an Arc Completion Record containing actual outcome, character/relationship/knowledge/object changes, promises, consequences, deviations, next-arc conditions, and key source chapters.

At volume completion, a Volume Completion Record preserves the compact end state and next-volume conditions. A separate Arc or Volume Audit file is not created unless a cross-range issue requires it.

## Hot, warm, and cold context

### Hot

Loaded by default:

- compact master direction and current pointer;
- current volume and active arc;
- relevant Project Profile and Story Facts sections;
- active Story Memory;
- current brief;
- the minimum promoted prose needed to establish the current starting state;
- explicitly activated evidence.

### Warm

Loaded only when triggered:

- completed arc or previous-volume summaries;
- returning characters, objects, secrets, promises, or consequences;
- original chapters needed for evidence;
- unresolved cross-chapter issues.

### Cold

Excluded by default:

- historical candidates;
- completed runs;
- closed audits;
- backups;
- superseded plans;
- old revisions;
- completed arcs' original detailed plans;
- brainstorming and abandoned directions.

## Ordinary chapter artifacts

A normal Project Creation chapter uses at most three core artifact roles:

```text
work/chapter-XXX/
├── brief.md
├── candidate.md
└── audit.md
```

They are created progressively and loaded by the active stage rather than treated as a fixed three-file context set. The combined audit keeps Contract, Character, Story Fact and Continuity, Language, conditional checks, Proposed Story Memory Changes, Stable Setting Candidates, Story Fact Check, Final Verification, and Promotion Result separately identifiable.

A run record, backup, split evidence, or impact analysis is created only when recovery, multiple candidates, batch revision, source conflict, official overwrite, artifact size, or requested auditability requires it.

## Character voice differentiation

The Project Profile Dialogue Anchor defines the book's shared dialogue floor, not a single cast-wide voice. Core and recurring characters use a compact Story Facts Voice Signature with four fields: default tactic, attention bias, speech baseline, and one pressure or relationship shift. Chapter briefs load only one compact cue line for each important speaker.

The system does not require personality quotas, catchphrases, accents, or a verbal gimmick for every character. Meaningful dialogue is checked against motive, attention, relationship strategy, and phrasing; ordinary functional lines may remain shared.

## Natural voice and anti-template control

Naturalness is applied twice. Draft Writing prevents obvious construction patterns by grounding narration and attention in the current viewpoint, avoiding automatic explanation and polished over-completion, and letting rhythm follow cognition and pressure. Prose Stylist may improve expression but must not regularize supported hesitation, bias, evasion, interruption, or unfinished thought.

Narrative Humanizer then checks constructedness, voice and thought ownership, cognition-shaped rhythm, emotional explanation without choice or cost, manufactured depth, dialogue credibility, and artificial roughness. It keeps supported polish, makes targeted corrections, or returns motivational and structural falseness upstream. It does not make prose casually fragmented, slang-heavy, or imprecise merely to look human.

Story Fact Check follows every Humanizer change so naturalness work cannot silently alter events, knowledge, relationships, clues, rules, reveal timing, or state changes.

## Selective visual emphasis

Core and recurring characters may keep one to three stable Recognition Anchors in Story Facts. An important first formal appearance or meaningful re-entry receives a small viewpoint-selected combination of appearance or clothing, action/posture, and effect on the scene; later detail is added only when a new viewpoint, relationship, state, setting, or plot use gives it new meaning.

Key scenes establish enough spatial relation, dominant sensory information, and action-relevant objects or constraints for the reader to follow movement and pressure. The brief activates these Emphasis Targets only when needed. Reviews flag both under-description and appearance inventories, static location tours, repeated entrance formulas, or detail the viewpoint would not naturally notice.

## Rolling checkpoint audits

Project Creation defaults to one Checkpoint per five promoted chapters:

```text
audits/checkpoint_001_005.md
audits/checkpoint_006_010.md
audits/checkpoint_011_015.md
```

Before starting the first chapter of a new window, Novel Writer verifies the previous window's Checkpoint. Each Checkpoint fully reviews only the new five chapters, then uses the previous report's unresolved findings and Carry-Forward Constraints, current Story Memory and planning, and targeted historical evidence. It does not repeatedly audit the whole manuscript.

Findings are classified as **Blocking Before Next Chapter**, **Required During Next Window**, or **Watchlist**. The audit is read-only: proposed prose, Story Memory, or planning repairs require a separate approved revision workflow. When a window ends with an Arc or Volume, the Checkpoint is merged into that Completion Record instead of creating a duplicate report.

## Conditional checks

- **Fact Protection** — stable facts, protected secrets, knowledge boundaries, critical objects, or permanent changes
- **Plan Boundary** — reveal windows, reserved events, volume obligations, reader promises, or climax constraints
- **File Safety** — official overwrite, multiple candidates, batch work, recovery, source conflict, or uncertain freshness

These are explicit checks, not hidden modes.

## Seven-stage prose delivery

1. Preflight
2. Draft Writing
3. Content Review
4. Prose Refinement
5. Story Fact Check
6. Final Verification
7. Promotion & State Update

Final Verification happens before official Promotion or Story Memory update. Stable-setting changes require separate explicit confirmation.

## Plugin structure

- `.claude-plugin/marketplace.json` — Claude-compatible GitHub marketplace
- `.claude-plugin/plugin.json` — Claude plugin manifest
- `.codex-plugin/plugin.json` — Codex plugin manifest
- `.agents/plugins/marketplace.json` — Codex marketplace registration metadata
- `skills/novel-writer/SKILL.md` — compact control plane and intent router
- `skills/novel-writer/agents/openai.yaml` — ChatGPT Skill interface metadata
- `skills/novel-writer/references/` — selectively loaded planning, delivery, state, continuity, and quality protocols
- `skills/novel-writer/assets/` — Story Memory, optional run-record, and rolling-checkpoint/cross-range-audit templates
- `project-notes/` — project-specific material excluded from the reusable Skill package
- `dist/` — generated release archives; ignored by Git

## Development

Validate the complete Skill before distribution. Generated packages belong in `dist/` and should not be committed. Publish `dist/skill.zip` with `novel-writer/` as the archive root. The v2 release contains 26 canonical Skill files; removed references and assets are not packaged.

## License

MIT
