# Skill Change Protocol & Data Isolation — Skill 修改确认与项目数据隔离规范

Use this reference when proposing modifications to this reusable Skill or enforcing data isolation between reusable methods and novel-specific project files.

---

## 1. Skill Change Core Rule

When discussing possible improvements to this skill, **do not modify the skill immediately**. First explain the plan and wait for explicit user confirmation.

This applies to:
- `SKILL.md`
- any file under `references/`, `scripts/`, or `assets/`
- reusable style and element libraries
- workflow rules, audit gates, prompts, or hard constraints

### Allowed Before Confirmation
1. Inspect current skill files
2. Identify problems and architectural bottlenecks
3. Propose refactoring or patch plans
4. List files that would change
5. Draft sample wording in chat

### Requires Explicit Confirmation
Do **not** edit skill files until the user explicitly confirms (e.g. *“可以改”*, *“就这么做”*, *“开始修改”*, *“确认”*, *“可以继续”*).

---

## 2. Pre-Change Response Template

Before modifying the skill, report:

```markdown
我建议这样改：
1. 修改/新增/删除哪些文件
2. 每个文件改什么
3. 是否影响现有流程
4. 是否有风险
5. 是否需要备份

你确认后我再修改 skill。
```

---

## 3. Data Isolation Policy (项目数据与通用 Skill 物理隔离)

The reusable `novel-writer` skill stores **universal methods, protocols, and tools**, never specific novel manuscripts or book-specific lore.

### What Belongs in Reusable Skill References
- reusable workflow protocols and decision gates
- abstracted failure patterns (`FP-XXX`)
- compact checklists and diagnostic criteria
- universal quality gates and review metrics
- diagnostic scanning utilities (`scripts/`)

### What Stays Exclusively in the Novel Project Directory
- novel manuscripts (`chapters/`)
- project planning (`plans/`)
- dynamic state (`state/story_memory.md`, `state/story_facts.md`)
- book-specific lessons (`state/writing_lessons.md`)
- chapter candidate and audit drafts (`work/chapter-XXX/`)
- project backups and historical archives (`backups/`, `archive/`)

Never copy a specific novel's full text, character dossiers, or plot notes into this reusable plugin repository.
