# Project Profile Workflow — 项目级风格/元素/基调总控

## Purpose

Every novel project should have a compact project-level control file:

```text
state/project_profile.md
```

This file preserves the book’s selected style, element mix, tone, reader promise, and generation/revision rules. It prevents later chapters and revisions from drifting away from the book’s intended “taste and gameplay.”

## System Bible vs Project Profile

### System Bible

The System Bible is the fact source:
- characters
- relationships
- world/system rules
- factions/institutions
- powers/technology/social rules
- stable canon facts

### Project Profile

The Project Profile is the style/element/tone source:
- writing style
- element mix
- Tone Lock
- reader promise
- forbidden styles/elements
- how elements should be implemented
- revision boundaries

In short:
- System Bible = what is true in the story.
- Project Profile = what this book should feel like and how it plays.

## When to create

Create `state/project_profile.md` after:

1. Topic / Seed confirmation
2. Style selection
3. Element mix selection
4. Compatibility Check + Tone Lock
5. Length / Chapter Scale confirmation

Then use it before:
- initial outline
- System Bible
- detailed plot outline
- chapter preflights
- completed-chapter revisions

## Draft confirmation gate

Before writing `state/project_profile.md`, show the full Project Profile draft to the user and wait for explicit confirmation.

Acceptable confirmations include `确认`, `可以`, `写入`, `按这个执行`, `就这样`, or equivalent.

Do not create or overwrite `state/project_profile.md` from inferred preferences, brainstorming, or partial selections. The file is a project-level rule source, so its first creation and any later project-level update require explicit confirmation.

## Required template

```markdown
# Project Profile

## Basic
- 书名：
- 类型：
- 篇幅：
- 章节数：
- 每章字数范围：

## Style Bible
- 主文风：
- 辅助文风：
- 禁用文风：
- 语言密度：
- 对话风格：
- 情绪表达方式：
- 节奏：
- 允许的修辞：
- 禁用的修辞/表达：

## Element Bible
- 核心元素：
- 辅助元素：
- 禁用元素：
- 元素实现规则：
- 元素冲突处理：

## Tone Lock
- 主情绪：
- 情绪下限：
- 情绪上限：
- 不能出现：
- 读者体验目标：

## Reader Promise
- 这本书承诺给读者的体验：
- 每章尽量提供：
- 不能欺骗读者的地方：

## Generation Rules
- Storyteller 必须遵守：
- Character Agents 必须遵守：
- Lore Auditor 必须检查：
- Prose Stylist 必须保留：
- Narrative Humanizer 必须保留：
- Post-Humanizer Fact Lock 必须确认：

## Revision Rules
- 轻修允许：
- 深修需要确认：
- 禁止自动改动：
```

## Chapter preflight usage

Every chapter preflight should read `state/project_profile.md` when it exists and include a compact section in `state/chapterXX_brief.md`:

```markdown
## Project Profile Constraints
- 主文风：
- 辅助文风：
- 禁用文风：
- 核心元素：
- 本章需要体现的元素：
- 本章不能偏离的 Tone Lock：
- 本章 prose risks：
```

## Revision usage

When revising completed chapters, read `state/project_profile.md` if available. The Humanizer should preserve the project’s style/tone/element logic instead of flattening every book into the same clean literary prose.

## Update rules

### Allowed updates

Update `project_profile.md` only after the user explicitly confirms changes to:
- title
- style
- element mix
- tone
- length/chapter scale
- forbidden styles/elements
- reader promise
- revision boundaries

### Do not update automatically when

- the user is only brainstorming
- the user asks “would this be better?”
- the user complains about one chapter but does not ask to change the whole book style
- the user requests a one-off chapter revision

Temporary discussion is not project-level rule change.

## Existing projects

Do not automatically create or modify `state/project_profile.md` for existing projects unless the user asks. For old books, propose a profile draft first and wait for confirmation.
