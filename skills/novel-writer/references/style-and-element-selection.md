# Style & Element Selection — 文风、元素组合与基调锁定

## Purpose

Before outlining a novel, lock the writing style, trope/element mix, and tone. This prevents later drift and helps determine appropriate length.

## Style selection prompt

Ask the user:

```markdown
请选择文风，可组合但要有主次：

1. 轻松诙谐
2. 半文半白
3. 冷峻悬疑
4. 热血爽文
5. 慢热细腻
6. 文学向
7. 轻小说 / 日常感
8. 影视化强剧情
9. 黑色幽默
10. 高燃史诗
11. 自定义

请给出：
- 主文风：1个
- 辅助文风：最多2个
- 明确不要的文风：
```

## Element selection prompt

Ask the user:

```markdown
请选择小说元素，可组合：

身份/开局：穿越、重生、失忆、替身、退婚、废柴、隐藏身份、遗孤、退休高手、反派觉醒、炮灰自救
金手指/机制：系统、面板、签到、模拟器、熟练度、加点、空间、AI辅助、预知梦、时间循环、存档读档、无限流副本
剧情驱动：复仇、查案、生存、升级、争霸、经营、种田、探险、逃亡、寻亲、救亡、家族崛起、门派复兴
世界类型：武侠、仙侠、玄幻、都市异能、历史架空、赛博朋克、星际科幻、末世废土、西幻、克苏鲁、灵异、校园、商战
情绪卖点：爽、虐、甜、燃、悬疑、治愈、沙雕、黑暗、热血、轻松、压抑、群像、反转、宿命感、成长感
关系结构：单主角、双主角、群像、师徒、宿敌、兄弟、伪装夫妻、先婚后爱、强强、破镜重圆、队伍冒险

请给出：
- 核心元素：1–3个
- 辅助元素：0–3个
- 禁用元素：
```

## Compatibility check

After user selection, load and apply `references/style-element-compatibility.md`.

Classify the chosen mix as:
- **Strong fit**: style and elements reinforce each other naturally.
- **Conditional fit**: can work, but requires implementation constraints.
- **High risk**: likely to damage suspense, tone, logic, or length unless redesigned.

Check:
- Are there too many core elements?
- Does style conflict with element mechanics?
- Does the intended tone fit the genre?
- Does the selected length support the complexity?
- Which elements should be core vs secondary/seasoning?
- What constraints are required to make the combination work?

Output format:

```markdown
## Compatibility Check
- Works well:
- Potential conflicts:
- Required constraints:
- Suggested core elements:
- Suggested secondary/seasoning elements:
- Elements to remove or forbid:
```

Do not proceed to length/chapter scale until the user confirms the final style + element + tone mix.

## Tone Lock template

```markdown
## Tone Lock
- 主情绪：
- 情绪下限：
- 情绪上限：
- 不能出现：
- 读者体验目标：
```

## Style Bible template

```markdown
## Style Bible
- 主文风：
- 辅助文风：
- 语言密度：
- 对话风格：
- 情绪表达方式：
- 节奏：
- 禁用文风：
```

## Element Bible template

```markdown
## Element Bible
- 核心元素：
- 辅助元素：
- 禁用元素：
- 元素实现规则：
- 元素冲突处理：
```

## Rule

Style and element choices must be included in the System Bible and passed to Storyteller, Character Agents, Lore Auditor, Prose Stylist, Narrative Humanizer, and Post-Humanizer Fact Lock.
