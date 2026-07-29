# Chapter Humanizer Revision Workflow — 已完成章节轻修流程

Use this when the user asks to revise an already-written chapter for AI-like prose, weak metaphors, repeated phrasing, or continuity/state bugs. This workflow is for **targeted light revision**, not rewriting.

## Trigger

User asks for changes such as:
- “按刚才讨论的方式修改第 X 章”
- “看看 bug、不合适比喻、重复说法，然后轻修”
- “目的不是重写，只修不自然/bug/重复”

## Principles

1. **Review before rewriting if the user asks for review first.**
   - Report planned fixes before editing when requested.
   - Do not immediately rewrite an entire chapter.

2. **Light revision, not plot rewrite.**
   - Preserve chapter title, scene order, plot events, clues, evidence, reveals, and character boundaries.
   - Prefer minimal line/paragraph patches.
   - Do not invent new facts unless necessary to clarify an existing state and canon supports it.

3. **Fix continuity by clarifying state, not adding drama.**
   - Align wounds/body states/resources/objects with prior chapters.
   - Distinguish literal fact from metaphor, perception, rumor, dream, or character inference.
   - If a prior metaphor may become a bug, rewrite it to reduce entity-like/literal interpretation.

4. **Humanize with restraint.**
   - Remove or reduce ornamental comparisons that do not add meaning.
   - Reduce repeated image families and stock gestures.
   - If a direct cue (`指节发白`, `脸色发白`, `喉间泛甜`) is clear and not overused, keep it.
   - Object/action detail is only better when the reader can infer its purpose; otherwise it is confusing filler.

5. **Prefer concrete but not over-elaborate replacements.**
   - Bad replacement: swapping one stock cue for another.
   - Better: use the simplest expression that fits scene pressure, viewpoint, and reader comprehension.

## Procedure

1. **Load relevant references**
   - `references/narrative-humanizer.md`
   - `references/continuity-bug-audit.md`
   - Optional: `references/outline-compliance-and-prose-logic.md`
   - If available, read the project’s `state/project_profile.md` so revisions preserve the selected style, element mix, Tone Lock, reader promise, and revision boundaries.

2. **Read the chapter, prior chapter, brief, and any relevant audit/state**
   - At minimum: `chapters/chXX_final.md`, `state/chapterXX_brief.md`.
   - For continuity fixes: read recent chapter(s) and state files relevant to the bug.

3. **Run targeted scans**
   - Count/inspect `像`, `仿佛`, `如同` and repeated image families.
   - Scan stock body cues (`没有回头`, `喉间`, `眼神`, `指节`, `脸色`, etc.) but do not ban mechanically.
   - Scan state terms that can drift: body part, wound, blood, object location, evidence ownership, knowledge source.
   - Scan forbidden meta/technical leakage.

4. **If user requested a plan first, stop and summarize**
   - List must-fix, recommended-fix, and keep-as-is items.
   - Explain why each fix preserves canon.

5. **Patch deterministically**
   - Back up final chapter: `chapters/chXX_final.md.bak_humanizer_fix` or timestamped equivalent.
   - Apply the same accepted minimal patches to `scenes/chXX_sYY_draft.md` when it mirrors final text, to keep draft/final aligned.
   - Use Python file I/O when shell helpers are unreliable.

6. **Verify after patch**
   - File exists and non-zero size.
   - Forbidden/meta terms absent.
   - Required outline contract terms/events still present.
   - Known problem phrases removed or reduced.
   - Continuity bug fixed without creating new facts.
   - Dashboard read endpoint returns HTTP 200 if dashboard is running.

## Batch revision workflow

Use this when the user asks to apply the same light-revision method to many completed chapters.

1. Split the range into manageable chunks and, when available, use subagents in parallel; otherwise process the chunks sequentially with isolated inputs and outputs.
2. Give every subagent the same invariants:
   - light revision only; do not rewrite plot/structure
   - preserve canon, evidence chains, reveal timing, character knowledge boundaries, and required wording
   - back up every edited final + matching draft file before patching
   - sync `chapters/chXX_final.md` and matching `scenes/chXX_sYY_draft.md`
   - verify forbidden/meta terms and required chapter terms after editing
3. Include known cross-chapter state facts in the task context so subagents do not reintroduce old bugs.
   - Example: after a chapter-1 fix, “沈照 first wound is chest-front shallow cut; later right-rib wound only exists if a later chapter explicitly creates it.”
4. After all revision passes finish, the orchestrating process must independently sample and verify the results rather than trusting summaries only:
   - sizes/non-empty for every edited file
   - forbidden/meta-term scan across the full range
   - required keyword/event scan per chapter
   - known risky phrase counts (`钝钉`, wrong wound location, blood-source drift, etc.)
   - dashboard read endpoint HTTP 200 for each chapter if running
5. Do not over-normalize style across the range. Reducing `像/仿佛` counts is a warning metric, not a target. Keep metaphors that are clear, viewpoint-appropriate, and not overused.

## Generic revision examples

- A metaphor such as “a nail driving into the chest” may later be misread as a literal injury. Clarify that it is a sensation unless the story establishes a physical wound.
- If an attack initially damages only clothing but later scenes show bleeding and treatment, either establish a shallow wound at the original strike or remove the unsupported consequences.
- If a gesture or sentence is repeated several times, keep the most meaningful occurrence and replace the others with concrete current action.
- If a wound, object, location, or possession changes between chapters without an intervening event, align the later reference with the established state.
- Replace ornamental comparisons with observable behavior only when doing so improves clarity; do not drive metaphor counts toward zero as a mechanical target.
- For batch passes, divide chapters into isolated chunks but re-run full-range verification for cross-chapter state drift after all chunks are complete.

## Report format

After editing, report:
- files changed
- backup path
- categories fixed
- verification results
- key required terms/events preserved

Keep the report concise; the user wants the result, not a full rewrite transcript.
