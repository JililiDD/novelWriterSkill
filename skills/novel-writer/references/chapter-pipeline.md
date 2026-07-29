# Chapter Pipeline — 逐章生成流程

Use this after the user has confirmed the detailed plot outline and asks to generate a chapter.

## Non-negotiable rules

1. Keep drafting, review, humanization, and verification as distinct role passes.
2. Use available subagents when supported; otherwise run the same passes sequentially with separate intermediate files.
3. Every chapter requires a preflight plan and explicit user confirmation before prose drafting.
4. The approved chapter contract is binding.
5. After Humanizer, run Fact Lock.
6. After all role passes complete, independently verify the generated files.

## Per-chapter flow

### 1. Orchestrator preflight

Create `state/chapterXX_brief.md` containing:
- story so far / canon facts
- approved chapter contract
- project profile constraints from `state/project_profile.md` when available: main style, supporting styles, forbidden styles, core elements, relevant chapter elements, Tone Lock, and prose risks
- previous-chapter locked facts when available: read the prior final chapter and prior audit/Fact Lock directly; do not rely on memory or outline alone
- new-character/new-location provenance gate
- character state and knowledge boundaries
- foreshadowing plan
- style/tone reminders
- continuity hazards
- proposed scene flow
- chapter boundary control: if an event spans multiple chapters, explicitly state what must **not** be resolved in this chapter and the exact ending hook/hand-off point for the next chapter
- length target and verification expectation: include the target word/character range and whether slight overflow is acceptable for match/action density or should trigger compression

Stop and ask user for confirmation.

### 2. Storyteller draft

After confirmation only:
- write scene prose using approved brief
- no scene headers inside prose
- save to `scenes/chXX_sYY_draft.md` or current project convention

### 3. Character Agents

Major characters check:
- voice authenticity
- action consistency
- knowledge boundary
- relationship state

### 4. Lore Auditor

Audit against:
- System Bible
- `state/project_profile.md` when available / Style Bible / Element Bible
- chapter brief
- prior relevant canon
- foreshadowing tracker

Must include:
- Outline Compliance Audit
- Meta-Narrative Leakage Check
- Continuity Bug Audit from `continuity-bug-audit.md`
- severity: Critical / Major / Minor

### 5. Prose Stylist

Polish according to Style Bible, not a hardcoded genre.

Checklist:
- remove technical markers
- remove meta/chapter self-reference
- scan metaphor/simile logic
- scan over-repeated image families and stock body cues
- reduce forced aphorism and generic polish

### 6. Narrative Humanizer

Use `narrative-humanizer.md`.

Goal: reduce AI-like prose while preserving genre, facts, character voice, and plot.

### 7. Post-Humanizer Fact Lock

Confirm no changes to:
- plot events
- clues/evidence
- world rules
- character knowledge boundaries
- required outline beats
- foreshadowing obligations

### 8. Orchestrator state update

Update:
- chapter status
- foreshadowing tracker
- any state files used by the project

### 9. Final verification

The orchestrating process must independently verify:
- expected files exist and non-empty
- final chapter can be read
- forbidden/meta terms absent
- required chapter contract items preserved
- chapter boundary respected: events reserved for the next chapter were not accidentally resolved early
- length target checked against the approved brief/project profile; if outside range, either request/perform compression or explicitly report why the overflow is acceptable
- audit contains required sections
- dashboard endpoint returns HTTP 200 if running

## Delivering completed chapter files

When the user asks to see or receive a completed chapter `.md` file on a messaging platform, send the existing file directly with a native media/file response (e.g. `MEDIA:/absolute/path/to/chapters/chapterXX_final.md`) instead of pasting the full chapter text into chat. If the user combines file delivery with a next-step request (e.g. “send the md, then enter next preflight”), deliver the file and continue with the requested preflight in the same turn.

## Never auto-continue

After reporting completion, stop and ask whether to continue to the next chapter.
