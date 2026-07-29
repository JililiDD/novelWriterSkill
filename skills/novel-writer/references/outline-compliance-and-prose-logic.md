# Outline Compliance & Prose Logic Pitfalls

Session-derived lessons from generating 《雪尽刀还》.

## Pitfall 1: Treating approved plot outline as loose inspiration

Failure mode: User-approved Chapter 2 was `青川旧帖` with required beats:
- 沈照带铁牌入青川镇查旧案
- 青川镇百姓对沈家讳莫如深
- 柳照水提醒别直接去武盟分舵
- 十年前青川武盟发布“江湖公帖”，称沈家勾结外敌，死不足惜
- 夜探武盟分舵，旧帖副本被焚，只剩半页
- 陆青崖登场，奉命追捕沈照但对旧案有所怀疑
- 半页旧帖上有顾沉舟印押，且印押墨迹与正文不一致

The generated chapter drifted into an unrelated `孤灯镇客栈问路局` premise. User corrected that the chapter must follow the discussed outline exactly.

### Required fix
Before generation, Orchestrator must create an `Approved Outline Contract` in `state/chapterXX_brief.md` by copying the exact user-confirmed chapter outline. Subagents may enrich transitions and scene mechanics only; they may not replace title, location, premise, required events, turning point, or foreshadowing.

Lore Auditor must include `Outline Compliance Audit` and mark every approved bullet as:
- Satisfied
- Partially Satisfied
- Missing
- Contradicted

Any Missing/Contradicted main plot, turning point, required character, or foreshadowing item is a Critical Bug requiring regeneration before delivery.

## Pitfall 2: Prose Stylist only beautifies but misses semantic awkwardness

User flagged this sentence as logically odd:

> 十年可以把热闹磨成灰，也可以把活人的嘴磨成石。

Problem: sounds poetic but literal logic is strained (`把活人的嘴磨成石`), metaphor is forced, and it reads like artificial “金句腔”.

### Required fix
Prose Stylist must run a `Prose Logic & Naturalness Sanity Pass`:
1. Scan metaphors/similes for common-sense logic.
2. Replace forced aphorisms with concrete action/setting details.
3. Flag sentences that sound clever but fail literal reading.
4. If more than 3 awkward/illogical sentences appear, return to Storyteller for rewrite.

Better alternatives:
- `十年过去，旧街冷了，镇上的人也学会了闭口。`
- `十年足够让一条街失了烟火，也足够让活人不敢多说一句话。`
- Prefer concrete reactions: tea seller lowers voice, door closes quickly, bystanders stop talking.

## Pitfall 3: Meta-narrative leakage in prose

User flagged this delivered prose as wrong:

> 第一章里那句“定案”，至此有了纸面。

Problem: this is not merely repetition. It breaks immersion because `第一章` is a reader/author-level concept. Characters do not know they are in chapters, and the narrator should not refer to chapter structure inside the novel正文.

### Required fix
Storyteller, Lore Auditor, and Prose Stylist must prevent meta-narrative leakage.

Forbidden in novel prose:
- `第一章里...`
- `上一章...`
- `本章...`
- `前文提到...`
- `这个伏笔...`
- `读者会发现...`
- `此处埋下...`
- any agent/audit/outline/scene-planning language

Correct approach: reference earlier events from inside the story world:
- `雪夜里那黑衣人临死前吐出的两个字，至此有了纸面。`
- `那夜将死之人留下的话，终于在这半页残纸上露出痕迹。`
- `沈照记起旧铸房外，那人临死前的低语。`

Lore Auditor must include `Meta-Narrative Leakage Check`; any occurrence in prose is at least a Major Bug and must be rewritten before delivery.

## Pitfall 4: Dashboard should support all books and setting sections

The earlier generic dashboard script was hardcoded to one project path/title. User requested a dashboard that can switch between all generated novels and show not only chapter prose but also story settings.

Current multi-book dashboard:

`~/Desktop/hermes/jobs/novel-generator/dashboard.py`

Key features:
- bind to `0.0.0.0:8420` for phone access
- scan `~/Desktop/hermes/jobs/novel-generator/` for active and archived novel projects
- switch books freely in the UI
- list chapter files such as `chapters/chXX_final.md`, `chapters/chXX_draft.md`, `chapter_XX.md`
- link audit files such as `audits/chXX_lore_audit.md`
- show setting sections:
  - 故事大纲 (`state/story_outline.md`, `plot_outline.md`, `novel_state.yaml`)
  - 人物设定 / 关系图 (`state/character_bible.md`, `system_bible.md`, `system_bible.yaml`)
  - 伏笔计划 / Tracking (`state/foreshadowing_tracker.md`, `foreshadowing_tracker.yaml`)
  - 章节规划 / Preflight (`state/*.md`)
- count Chinese characters via CJK count, not `split()`
- mobile reading CSS: 19px font, 1.8 line-height, pre-wrap

For `xuejin-daohuan`, these project setting files were created:
- `state/story_outline.md`
- `state/character_bible.md`
- `state/foreshadowing_tracker.md`

Verification / restart commands:
```bash
cd ~/Desktop/hermes/jobs/novel-generator
python3 -m py_compile dashboard.py
# kill old 8420 if needed, then:
python3 dashboard.py
curl http://127.0.0.1:8420/api/books
```

Phone URL example:
`http://192.168.18.11:8420`

## Pitfall 5: Hardcoding humanizer rules to one genre

Failure mode: A de-AI / humanizer prompt says `You are the Narrative Humanizer for a Chinese wuxia novel`, then gets reused for sci-fi, romance, mystery, urban realism, horror, or other genres. This leaks wuxia assumptions into unrelated projects and may incorrectly treat valid genre conventions as flaws.

### Required fix
Use a genre-neutral `Narrative Humanizer`:
- Universal checks apply to every novel: forced aphorisms, explanatory narration, repetitive rhythm, over-neat structures, abstract emotion labels, interchangeable dialogue, ill-fitting metaphors, meta-narrative leakage, frictionless AI polish.
- Genre-specific checks are overlays selected from the project bible/genre profile, not defaults.
- The Humanizer must preserve the user-approved genre and style instead of flattening everything into generic literary prose.
- Humanizer edits may only change sentence/paragraph delivery, dialogue naturalness, or over-abstract narration. It may not change plot facts, clues, world rules, character knowledge boundaries, or approved outline beats.
- After Humanizer, run `Post-Humanizer Fact Lock`.

See `references/narrative-humanizer.md`.

## Pitfall 6: Reusing the same metaphor family or stock gesture too often

Failure mode: The prose avoids literally broken metaphors but keeps returning to similar “pretty” images or body cues. Examples include repeated snow-as-stone/bone/ash imagery, repeated wound/crack/shadow/mouth images, or repeated shorthand gestures such as `指节发白`, `喉头发紧`, `眼神一暗`, `呼吸一滞`.

Problem: Repetition is allowed as a deliberate motif, but frequent reuse without new meaning feels machine-generated and makes characters' emotional reactions interchangeable.

### Required fix
Narrative Humanizer and Prose Stylist must check both metaphor correctness and metaphor frequency:
1. Scan the current chapter for repeated image families, not only exact repeated words.
2. Cross-check recent chapters when a motif is likely overused.
3. Allow repetition only when it is intentional, spaced, and develops meaning.
4. If a shorthand phrase already expresses the moment clearly and has not been overused, keep it. Do not replace simplicity with decorative object choreography.
5. Do not mechanically ban phrases like `指节发白`; the rule is “not frequent repetition,” not “never use.”
6. When a similar effect is needed, first look for a different expression path: action, object interaction, posture, silence, interrupted dialogue, scene-specific sensory detail, or changed sentence rhythm. Writing should stay flexible, not rotate through a fixed synonym list.
7. Only use object/action details when they truly reveal environment, character state, relationship pressure, or plot tension. If the reader cannot infer why the cup, door, sleeve, phone, weapon, or other object detail matters, it is confusing filler and should be removed.

See `references/narrative-humanizer.md`.

## Pitfall 7: Weak bug checks miss state continuity and cross-chapter causality

Failure mode: The audit checks outline and general canon, but misses concrete state drift. The examples below are from one action-heavy project, but the rule is genre-neutral:
- A character performs an action or says a full line under pressure without enough time, ability, or interruption.
- A metaphor or perception is later misread as a literal fact.
- A serious state change has no later consequence or explanation.
- A source, location, ownership, relationship, resource, or knowledge state changes without cause.

### Required fix
Lore Auditor must run a strengthened, **genre-neutral** `Continuity Bug Audit`:
1. Use only the ledgers relevant to the current story/chapter. Do not force wound/combat ledgers into romance, sci-fi, urban, literary, or other projects when irrelevant.
2. Track Character State: body, emotion, relationships, promises, secrets, abilities, resources, and constraints.
3. Track Information / Knowledge: who knows what, how they learned it, and whether certainty/rumor/inference is being confused.
4. Track Object / Resource / Evidence: ownership, location, damage, consumption, scarcity, proof value.
5. Track Scene Feasibility: whether the action, line, recognition, emotional turn, technical operation, escape, confession, or decision fits time, pressure, visibility, ability, and available pauses.
6. Track Literal vs Figurative Language: do not convert metaphor, sensation, rumor, dream, hallucination, or character perception into narrator fact without an explicit event.
7. Track Cause → Consequence: important changes must either affect later behavior or be deliberately explained as resolved/irrelevant.
8. Treat cross-chapter state drift as a Major or Critical Bug, not a stylistic issue.

See `references/continuity-bug-audit.md`.
