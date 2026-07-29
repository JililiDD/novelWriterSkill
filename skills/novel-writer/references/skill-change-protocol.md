# Skill Change Protocol — 修改 skill 前必须确认

## Core rule

When the user discusses possible improvements to this skill, **do not modify the skill immediately**. First explain the plan and wait for explicit user confirmation.

This applies to:
- `SKILL.md`
- any file under `references/`, `templates/`, `scripts/`, or `assets/`
- reusable style/element libraries
- workflow rules, audit rules, prompts, or hard constraints

## Allowed before confirmation

You may:
1. inspect the current skill
2. identify problems
3. propose a refactor or patch plan
4. list files that would change
5. explain risks and alternatives
6. draft sample wording in the chat

## Requires explicit confirmation

Do **not** call `skill_manage` or edit skill files until the user explicitly says something like:
- 可以改
- 就这么做
- 开始修改
- 确认
- 按这个方案执行
- 可以继续

## Pre-change response template

Before changing the skill, tell the user:

```markdown
我建议这样改：
1. 修改/新增哪些文件
2. 每个文件改什么
3. 是否影响现有流程
4. 是否有风险
5. 是否需要备份

你确认后我再修改 skill。
```

## Exception

If the user directly commands a concrete skill edit (e.g. “把这条规则写进 skill”), that counts as confirmation. Still keep the edit minimal and report exactly what changed.

## After changing

After modifications:
1. report files changed
2. verify required rules exist
3. mention backup path if one was created
4. do not continue adding extra features without a new confirmation
