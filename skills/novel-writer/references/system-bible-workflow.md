# System Bible Workflow — 系统圣经工作流

Use after topic/style/element/tone and initial outline are confirmed.

## Purpose

The System Bible is the stable fact source for generation and audit. Subagents should receive the final approved System Bible, not brainstorming history.

## Required sections

### 1. Project Profile Summary

Read `state/project_profile.md` if it exists. The System Bible should reference or summarize the project profile, but should not duplicate the whole file unless the project needs a single-file canon package.

```markdown
## Project Profile Summary
- Title:
- Genre:
- Main style:
- Supporting styles:
- Tone Lock:
- Core elements:
- Forbidden styles/elements:
- Target length/chapter scale:
- Reader promise:
```

### 2. Character Bible

For every major character:
- role
- age/basic identity where needed
- appearance only where useful
- background
- personality
- motivation
- fear/flaw
- speaking style
- skills/capabilities
- knowledge boundaries
- character arc

Do not force every character to have a unique scar/birthmark/tattoo. Distinguishing features should serve plot or identification.

### 3. Relationship Map

Use text or ASCII map.

Track:
- relationship type
- directionality
- conflict
- secret/unknown relationship facts
- how relationship changes over time

### 4. World/System Rules

Generate according to genre:
- Wuxia: martial tiers, factions, law/officialdom, jianghu rules
- Xianxia: cultivation realms, sects, artifacts, costs, restrictions
- Sci-fi: technology levels, politics, ships/devices, communication limits
- Urban/realist: institutions, class, jobs, legal/social rules
- Fantasy: magic rules, factions, geography, costs
- Horror: entity rules, limits, visibility, taboo, escalation

### 5. Style Bible

Use the locked style choices:
- main style
- supporting styles
- language density
- dialogue style
- emotional expression
- pacing
- forbidden style drift

### 6. Element Bible

Use the locked element mix:
- core elements
- secondary elements
- forbidden elements
- implementation rules
- element conflict handling

## Confirmation

Show the System Bible to the user and wait for explicit confirmation before detailed plot outline.

## Audit rule

Lore Auditor must compare draft facts 1:1 against System Bible. Unsupported or contradicted major facts are Critical Bugs.
