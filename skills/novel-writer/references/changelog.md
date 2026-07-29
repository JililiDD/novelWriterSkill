# Changelog

## Unreleased

- Chapter preflight now explicitly reads the prior final chapter and prior audit/Fact Lock when available, preventing next-chapter briefs from relying only on memory or the outline.
- Added chapter boundary control for multi-chapter events: preflight must state what must not be resolved yet and the exact hand-off hook.
- Parent verification now checks target length and whether reserved next-chapter events were accidentally resolved early.

## v2.6.2 — Project Profile workflow

- Added `project-profile-workflow.md` for per-book `state/project_profile.md`.
- Startup flow now creates Project Profile after style/element/tone/length confirmation and before outline/System Bible.
- Added an explicit Project Profile draft confirmation gate before writing `state/project_profile.md`.
- Chapter preflight now reads `state/project_profile.md` when available and includes project profile constraints in chapter briefs.
- Completed-chapter revision now preserves project profile style/tone/element logic.
- System Bible workflow now references/summarizes Project Profile without duplicating the whole file.
- Synchronized `SKILL.md` frontmatter version to `2.6.2`.
- Main `SKILL.md` routing/index now includes Project Profile creation/update.

## v2.6.1 — Step 2A style/element library expansion

- Expanded `style-library.md` with richer Chinese novel/web-novel styles: 废土诗意感, 新怪谈感, 克苏鲁低语感, 市井烟火气, 港风江湖, 赛博冷感, 荒诞寓言, 现实主义冷叙事, 短剧强钩子风, 晋江细腻情绪流, 起点升级爽文风, 日式轻小说吐槽流, 民俗志怪感, 权谋厚重感, 治愈温暖感.
- Expanded `element-library.md` with web-novel mechanisms, emotional/relationship elements, suspense/horror elements, and organization/growth elements.
- Added `style-element-compatibility.md` for strong/conditional/high-risk style-element combinations.
- Updated `style-and-element-selection.md` to require compatibility analysis before length/chapter scale.

## v2.6.0 — Modular refactor

- Slimmed main `SKILL.md` into a hard-rule + module index structure.
- Added skill modification safety protocol: discuss first, modify only after explicit user confirmation.
- Added project notes policy: do not embed full novel manuscripts or large project context into universal references.
- Added startup workflow: topic → style → element mix → tone lock → length → outline → system bible → plot outline → chapters.
- Added style and element selection workflow.
- Added built-in style library and element library.
- Added library expansion protocol for user-defined styles/elements.
- Added chapter pipeline reference.
- Added system bible workflow reference.

## v2.5.x — Previous session-learned improvements

- Narrative Humanizer added as a genre-neutral prose integrity pass.
- Continuity Bug Audit generalized into state/knowledge/object/scene/language/cause ledgers.
- Chapter revision workflow added for already-written chapters.
- Dashboard/mobile/audiobook references split out as supporting modules.
