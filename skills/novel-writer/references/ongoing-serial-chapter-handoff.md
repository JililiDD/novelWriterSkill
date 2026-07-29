# Ongoing Serial Chapter Handoff

Use this when continuing an already-running novel project across turns or after context compaction, especially when the user says variants of `继续下一章`, `继续写下一章`, or `进入第X章`.

## Routing

1. If the next chapter's preflight has not been confirmed in the current conversation, create/update `state/chapterXX_brief.md` and stop for user confirmation.
2. If the user explicitly confirms the current preflight (`可以`, `确认`, `继续写第X章`, `生成正文`), run the chapter-generation pipeline using available subagents or isolated sequential role passes.
3. Do not treat a compacted-session summary as sufficient factual grounding. Use it to locate files, then read the actual project files.

## Minimum file refresh before next-chapter preflight

Read the live files for:
- latest completed `chapters/chapterNN_final.md`
- latest completed `audits/chapterNN_audit.md`
- `outline/...` around the next chapter
- `state/volume*_bible.md` or project system bible
- long foreshadowing / state ledger when present
- latest `state/chapterNN_brief.md` if it clarifies the immediate handoff

## Preflight contents to preserve continuity

The next `chapterXX_brief.md` should include:
- Story so far / locked canon facts from the latest final chapter and audit
- Approved chapter contract: title, POV, main event chain, ending hook, forbidden content
- Character state and knowledge boundaries
- New character/location provenance gate if any named team, person, location, artifact, or faction becomes prominent
- Foreshadowing plan with boundaries on what must not be paid off yet
- Proposed scene flow
- Continuity hazards
- Required beat checklist
- Forbidden/meta leakage terms

## Final verification after prose generation

After all generation and review passes complete, independently verify before reporting success:
- final, draft, and audit files exist and are non-empty
- title is exact
- required ending or exact clue phrase is present
- forbidden/meta terms are absent
- prohibited future-content terms are absent
- audit contains pipeline completion, outline compliance, meta leakage, continuity/fact audit, humanizer check, fact lock, verdict

If verification reveals a missing exact phrase or forbidden content, patch or request targeted revision before sending the file.