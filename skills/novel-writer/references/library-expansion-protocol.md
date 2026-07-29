# Library Expansion Protocol — 自定义文风/元素入库机制

Use this when the user proposes a writing style or novel element that is not in the current style/element libraries.

## Core rule

Do not automatically add user phrases to the library. First organize the definition, then ask the user whether to save it.

## Trigger

A possible new library entry appears when the user names a style/element that:
- is not in `style-library.md` or `element-library.md`
- is more than a one-off adjective
- has reusable meaning for future projects
- changes writing, outline, character design, or world mechanics

Examples:
- “废土诗意感” as a style
- “反向系统流” as an element
- “职场克苏鲁” as an element/tone hybrid

## Steps

1. **Classify**
   - Is it a style, element, tone, relationship structure, or hybrid?

2. **Compare**
   - Is there an existing close entry?
   - If yes, offer to use the existing entry with custom notes.
   - If no, draft a new definition.

3. **Draft definition**

Use this template:

```markdown
## [Name]

类型：文风 / 小说元素 / 基调 / 混合项

一句话定义：

适用题材：

核心特征：

适合搭配：

容易冲突：

禁用误用：

示例提示词：

审计检查点：
```

4. **Ask before saving**

```markdown
“[Name]”目前不在库中。
我可以：
1. 只用于当前项目
2. 添加到库，后续项目可复用
3. 先修改定义，你确认后再添加

请选择。
```

5. **Save only after explicit confirmation**

If user chooses option 2 or explicitly says to add it, write it to the appropriate library.

## Where to save

- Styles → `references/style-library.md`
- Elements → `references/element-library.md`
- Hybrids → choose the primary file and cross-reference in the other file if needed.

## Safety

Do not save temporary preferences like “这本稍微轻一点” as a reusable entry unless the user asks.
