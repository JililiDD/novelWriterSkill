# Story Facts Workflow — 稳定故事事实、人物对白配置与受保护设定

Use this reference after the Story Kernel, Project Profile, and master-plan direction are approved.

The project authority is:

```text
state/story_facts.md
```

## Contents

- Ownership and decision boundaries
- Story Facts structure and Dialogue Profiles
- Stable facts versus current state
- Functional Character Realism for secondary characters
- Context loading, confirmation, and review

## Ownership

Story Facts is the sole owner of confirmed, durable story facts:

- core character foundations and Dialogue Profiles (`references/dialogue-engine.md`);
- stable relationship foundations and hidden relationships;
- opposition foundations;
- world, magic, technology, institutional, legal, social, or genre-system rules;
- stable factions, locations, artifacts, identities, and constraints;
- protected facts and reveal conditions;
- facts that later prose must not contradict without explicit confirmation.

It answers:

> What remains durably true in this story world?

Story Kernel owns the story engine. Master and volume plans own future intended direction. Story Memory owns active/open current state. Promoted prose owns original evidence of happened events.

Do not store current injuries, locations, possessions, knowledge state, relationship phase, active promises, foreshadowing progress, or open consequences here.

Do not duplicate Project Profile style, elements, Tone Lock, reader promise, or Style Anchors.

## Decision-status boundary

Before creating or updating Story Facts, inspect the Story Kernel and approved planning decisions:

- **Confirmed** material may become stable story facts;
- **Suggested** material remains a proposal;
- **Open** material stays unresolved except for the minimum boundary needed by current planning;
- **Rejected** material must not return under another label.

When a proposed fact would decide an Open Story Kernel or plan question, return that decision to the user instead of resolving it silently.

## Default structure

```markdown
# Story Facts

## Authority
- Project Profile path/revision:
- Master plan path/revision:
- Confirmed Story Kernel revision:
- Effective revision:

## Core Characters
### [Character]
- Role in the confirmed story engine:
- Stable identity/background:
- Durable external motivation:
- Internal contradiction or durable pressure:
- Cost-producing method/belief when confirmed:
- Dialogue Profile:
  - Wants / Habitual drive:
  - Notices first / Attention bias:
  - Knowledge baseline (deep vs blind):
  - Default conversational tactic:
  - Status speech impact:
  - Under pressure behavior:
  - With trusted counterparts:
  - Typical refusal style:
  - Typical request style:
- Recognition Anchors (1–3 stable visual/behavioral cues):
- Contrast note (only when another recurring character risks blending):
- Capabilities and fixed limits:
- Protected secrets:
- Long-term change direction:
- Approved source/evidence:

## Stable Relationships
- Relationship:
- Mutual durable needs:
- Directionality:
- Important asymmetry:
- Durable conflict/bond:
- Hidden facts:
- Change or rupture pressure:
- Conditions required for major change:
- Approved source/evidence:

## Opposition Foundations
- Opposing force:
- Independent objective or operating logic:
- Valid reasoning from its perspective:
- Stable resources and constraints:
- Structural incompatibility with protagonist:

## World and System Rules
- Rule:
- What it permits:
- What it forbids:
- Cost or limit:
- Who knows it:
- Known exceptions:
- Approved source/evidence:

## Factions, Institutions, and Locations
- Stable role:
- Authority/resources:
- Fixed constraints:
- Approved source/evidence:

## Stable Artifacts and Identities
- Stable identity/function:
- Fixed limitations:
- Protected reveal conditions:
- Approved source/evidence:

## Protected Facts
- Fact:
- Protection reason:
- Reveal/change condition:
- May change automatically: No
- Approved source/evidence:

## Deliberately Open
- Confirmed planning questions intentionally left undecided:
```

Use only relevant sections. Do not manufacture an encyclopedia before the story needs it.

## Character Dialogue Engine & Voice Profiles

Create a Dialogue Profile in Story Facts for core and recurring characters (`references/dialogue-engine.md`):

- **Wants / Habitual drive** — default social objective in dialogue;
- **Notices first / Attention bias** — what they register immediately;
- **Knowledge baseline** — what they understand deeply vs what they are blind to;
- **Default tactic** — habitual conversational strategy (e.g. transactional, evasive, aggressive probing);
- **Status speech impact** — how station, profession, and vulnerability shape word choices;
- **Under pressure behavior** — syntax and composure changes under stress;
- **With trusted counterparts** — register shift with allies;
- **Typical refusal & request styles** — how they decline or ask for help.

Do not assign cast quotas, mandatory catchphrases, accents, or verbal gimmicks. Meaningful dialogue must pass the **Speaker-Substitution Check** (`references/dialogue-engine.md`).

## Functional Character Realism for Secondary Characters

Secondary characters and NPCs operate under **Functional Character Realism ("Ordinary People Mode")**:
1. **Partial knowledge**: they understand their immediate workspace and duty, not the grand conspiracy.
2. **Self-preservation**: wages, physical safety, blame avoidance, and family come before the protagonist's quest.
3. **Concrete particulars**: express concrete tangible experiences (*"别又算在我头上"*) rather than abstract authorial analysis.
4. **Natural imperfection**: hesitation, non-linear recall, and answering only what they comprehend.

## Selective visual identity

For core and recurring characters, keep at most 1–3 stable Recognition Anchors (lasting physical trait, habitual posture, object-handling pattern). Do not create a full appearance dossier.

Temporary clothing, grooming, disguise, fatigue, or injury presentation belong in the brief and Story Memory, not in stable Story Facts.

## Stable facts versus current state

Story Facts stores durable background, motivation, baseline voice, capability rules, protected secrets, confirmed relationship foundations, and world rules.

Story Memory stores changing location, injury, inventory, relationship phase, active goal, known information, false belief, active promise movement, and unresolved consequence.

When a current condition appears likely to become durable, list it in the chapter audit as a **Stable Setting Candidate**. Do not update Story Facts until the user confirms the durable change.

## Context loading

Do not automatically load the entire Story Facts file for every chapter. Load only sections activated by present characters, moving relationships, used locations/rules, or touched protected facts.

## Review rule

Story Fact and Continuity Review compares candidate prose against confirmed Story Kernel, approved planning, Story Facts, Story Memory, and original promoted prose. Unsupported or contradicted facts are blocking.
