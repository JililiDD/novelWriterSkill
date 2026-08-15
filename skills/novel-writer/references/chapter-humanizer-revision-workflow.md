# Completed-Prose Revision Policy — 已完成正文修订策略与结构重构

Use this for already-written chapter or scene prose. This file owns revision-specific policy only. Execute applicable stages through `chapter-pipeline.md`; load `run-state-protocol.md` only when its triggers apply.

## Contents

- Revision types and scope
- Protected Story Meaning vs Realization Layer
- Backup, isolation, and Chapter Interface Checks
- Check invalidation and state effects
- Completion report and Promotion Gate

## Revision types

### Light revision
Use for bounded line or paragraph changes that preserve scene order and event meaning:
- clarity and rhythm;
- repetition and imagery;
- dialogue naturalness via Dialogue Engine;
- small continuity wording corrections;
- removal of AI-like phrasing, unearned aphorisms, or workflow leakage.

### Deep revision
Use for substantial pacing, paragraph/scene restructuring, emotional sequencing, or content changes that preserve the approved overall plot contract.
- Requires an approved revision plan, candidate isolation, and fresh confirmation before Promotion.

### Regeneration
Use when the user requests a genuinely different realization of the same approved story unit.
- Create a separate candidate. Preserve protected story meaning while freely redesigning realization staging.

## Protected Story Meaning vs Realization Layer

To prevent revisions from becoming clumsy line-by-line patches over flawed prose, distinguish two layers:

### 1. Protected Story Meaning (受保护故事事实)
Must be strictly preserved unless explicitly approved for revision:
- mandatory plot events and causal sequence;
- character knowledge boundaries (who knows what and when);
- character decisions, motives, and irreversible commitments;
- key clues, evidence items, and custody state;
- core relationship trajectory and established trust/rupture;
- reserved future events and foreshadowing promises;
- chapter starting and ending boundary states.

### 2. Realization Layer (文本实现层)
May be freely re-engineered, rebuilt, or replaced to achieve naturalness:
- dialogue phrasing, tactics, and syntax;
- action staging and choreography;
- micro-sequencing within a scene;
- descriptive focus, sensory anchors, and imagery;
- NPC selection and functional realism;
- paragraph geometry, cadence, and pacing.

> **Deep Rewrite Principle**: Preserve protected story meaning; freely rebuild realization when required by the approved rewrite goal.

## Backup, Isolation, and Chapter Interface Checks

1. **Mandatory Backup**: Back up completed promoted prose to `backups/chapters/chapter-XXX.md` before every approved overwrite.
2. **Candidate Isolation**: All revision and humanization work occurs in `work/chapter-XXX/candidate.md`. Official promoted prose remains untouched until verified and confirmed.
3. **Chapter Interface Check**: When revising an earlier chapter $N$, always check the interface transitions:
   - Chapter $N-1$ ending $\rightarrow$ Chapter $N$ opening;
   - Chapter $N$ ending $\rightarrow$ Chapter $N+1$ opening.
   - Run `scripts/chapter_interface_scan.py` to inspect boundary continuity.

## Check Invalidation Rules

Substantive candidate modifications invalidate downstream review stages (`references/quality-gate.md`):
- Dialogue rewrite $\rightarrow$ stales Character Check, Structural Naturalness, Surface Humanizer, Story Fact Check, Final Verification.
- Staging / blocking rewrite $\rightarrow$ stales Continuity Check, Fact Check, Final Verification.
- Re-run invalidated checks before re-entering `PROMOTION READY`.

## Promotion Confirmation Gate

Revisions follow the mandatory Promotion Confirmation Gate:
1. Complete all required review passes and Quality Gate ($\ge 9.5 / 10$).
2. Assign verdict **`PROMOTION READY`**.
3. Present the diff summary, Quality Gate score, and Interface Check findings to the user.
4. **Obtain fresh, explicit promotion authorization** in the current turn before overwriting official chapter files or applying Story Memory changes.