# Story Facts Workflow — 稳定故事事实与受保护设定

Use this reference after the Story Kernel, Project Profile, and master-plan direction are approved.

The project authority is:

```text
state/story_facts.md
```

## Contents

- Ownership and decision boundaries
- Story Facts structure and protected facts
- Stable facts versus current state
- Context loading, confirmation, and review

## Ownership

Story Facts is the sole owner of confirmed, durable story facts:

- core character foundations;
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
- Voice Signature:
  - Default tactic:
  - Attention bias:
  - Speech baseline:
  - Pressure or relationship shift:
- Recognition Anchors, 1–3 stable visual or behavioral cues when useful:
- Contrast note, only when another recurring character risks blending:
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

## Minimum viable character voice

Create a Voice Signature only for core or recurring characters whose choices or dialogue affect the project. Four fields are enough:

- **Default tactic** — how the character usually tries to get what they want;
- **Attention bias** — what they notice first, ignore, or misread;
- **Speech baseline** — directness, sentence shape, vocabulary level, and usual degree of explanation;
- **Pressure or relationship shift** — the one material way speech changes under pressure or with a key counterpart.

Use observable, predictive distinctions. `Cold`, `warm`, `funny`, `gentle`, or `sarcastic` alone are not Voice Signatures. Do not assign cast quotas, mandatory catchphrases, accents, verbal tics, or a unique gimmick to every speaker.

A character is distinct enough when a meaningful choice, observation, or line would not transfer unchanged to another major character without losing motive, attention, relationship strategy, or phrasing. Functional short lines may remain shared.

Project Profile's Dialogue Anchor defines the book's shared dialogue floor, not one voice for the whole cast. Temporary deviations caused by injury, secrecy, fear, grief, fatigue, or current relationship state belong in Story Memory or the current brief, not in the stable Voice Signature.

## Selective visual identity

For a core or recurring character, keep at most one to three stable Recognition Anchors when they materially help readers identify the person. Use observable cues such as a lasting physical feature, habitual presentation choice, posture, movement, object-handling pattern, or other repeatable behavior. Do not create a full appearance inventory.

An important character's first formal appearance should normally establish a usable base image when the viewpoint can observe it. Select a small combination of appearance, clothing, posture, action, and effect on the scene; include at least one appearance or clothing cue when natural. Each retained detail should help recognition or reveal identity, status, condition, self-presentation, relationship, or practical constraint.

Temporary clothing, grooming, weather effects, disguise, fatigue, injury presentation, or one-scene visual details belong in the current brief and promoted prose. A lasting physical or presentation change belongs first in Story Memory while active and becomes a Story Facts candidate only when confirmed durable. Later appearances add detail only when a new viewpoint, setting, relationship, state change, or plot use gives it new meaning.

## Stable facts versus current state

Story Facts stores durable background, motivation, baseline voice, capability rules, protected secrets, confirmed relationship foundations, and world rules.

Story Memory stores changing location, injury, inventory, relationship phase, active goal, known information, false belief, active promise movement, and unresolved consequence.

Promoted chapters preserve detailed historical evidence. Completed arc and volume records preserve compact historical outcomes.

When a current condition appears likely to become durable, list it in the chapter audit as a **Stable Setting Candidate**. Do not update Story Facts until the user confirms the durable change.

## Protected facts

Use `Protected Facts` for information requiring special checks, such as:

- true identity;
- survival or death status;
- permanent capability limits;
- irreversible relationship foundations;
- world-rule costs and exceptions;
- protected secrets and reveal conditions;
- facts whose change would invalidate multiple chapters or plans.

A chapter touching a protected fact triggers the relevant Fact Protection check under `creation-paths.md`.

## Fact precision

For every important rule or constraint, state:

- what it permits and forbids;
- its cost or limit;
- who knows it;
- whether exceptions exist;
- what approved evidence established it.

Avoid facts that can be rewritten whenever the plot needs convenience.

## Context loading

Do not automatically load the entire Story Facts file for every chapter.

Load only sections activated by:

- characters present or directly affected;
- relationships moving in the chapter;
- locations, factions, artifacts, or rules used;
- protected facts, secrets, or capability limits touched;
- source conflicts requiring verification.

When the file becomes too large for reliable selective reads, split by domain while retaining one index:

```text
state/story_facts/
├── index.md
├── characters.md
├── relationships.md
├── world-rules.md
├── factions.md
├── locations.md
└── artifacts.md
```

Do not split early. One compact file is preferable for ordinary projects.

## Confirmation

Show the Story Facts draft and obtain explicit confirmation before first use as an authority.

Material changes to identity, world rules, power limits, fixed relationship foundations, protected secrets, durable motivation, or opposition logic require renewed confirmation.

A chapter audit may propose a Stable Setting Candidate but cannot apply it automatically.

Confirmation of Story Facts does not confirm remaining Open Story Kernel or planning items unless those decisions are explicitly shown and approved.

## Review rule

Story Fact and Continuity Review compares candidate prose against:

1. confirmed Story Kernel and master/current-volume plan for story-engine and plan obligations;
2. approved Story Facts for durable facts and protected boundaries;
3. Story Memory for active current state;
4. promoted chapters for original evidence;
5. the approved work-unit brief for current obligations.

Unsupported or contradicted major facts are blocking. When authorities disagree, identify the outdated source and resolve the conflict against approved evidence rather than choosing the convenient version.
