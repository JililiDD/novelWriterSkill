# Continuity Bug Audit — 通用状态一致性与因果逻辑检查

This reference strengthens bug hunting for **all long-form fiction genres**. It is not a wuxia-specific checklist and should not force every story into injury/combat auditing. Its purpose is to track any story element whose state can drift across scenes or chapters.

## Core principle

Do not only check whether the current chapter sounds plausible in isolation. Track the **state of relevant entities** across the story:

- characters: body, emotion, knowledge, relationships, promises, secrets, abilities
- objects: ownership, location, damage, usage, scarcity, evidence value
- information: who knows what, when they learned it, whether they can infer it
- locations: access, distance, visibility, weather, damage, social control
- systems: law, magic, technology, money, medicine, organizations, social rules
- language: whether a phrase is literal, metaphorical, uncertain, rumor, dream, or character perception
- scene physics: time, distance, breath, interruption, visibility, pressure, available actions

The audit should ask: **what changed, who knows it, what consequences should follow, and did later prose accidentally forget or reinterpret it?**

## Do not over-specialize

The examples below include wounds, blood, combat, and evidence because those are common places bugs appear. They are examples, not mandatory categories for every novel.

For each project, build ledgers from the story's actual genre and premise:

- Romance: relationship promises, emotional boundaries, prior conversations, family/social constraints.
- Sci-fi: device state, energy/fuel, comms delay, technical limits, chain of command.
- Fantasy/xianxia: magic/cultivation costs, artifacts, contracts, rules, cooldowns, realm limits.
- Mystery/thriller: clue custody, witness knowledge, alibis, access, timestamps, evidence reliability.
- Urban/realist: money, phones, transport, work schedules, legal/social consequences.
- Horror: visibility, exits, injuries/fatigue, what the entity can/cannot do, who has seen what.
- Wuxia/action: wounds, stamina, weapons, recognition, distance, timing, martial limitations.

## General ledger model

Maintain only the ledgers relevant to the current story and chapter. Use broad categories first; add specific sub-ledgers only when needed.

### 1. Character State Ledger

Track character state changes that should affect later behavior.

Possible fields:

```markdown
| Character | Event | State changed | Literal/metaphorical/uncertain? | Immediate effect | Follow-up consequence | Current status |
|---|---|---|---|---|---|---|
```

Examples of state:
- physical: injury, illness, fatigue, pregnancy, hunger, intoxication, sensory loss
- psychological: grief, fear, trust break, obsession, guilt, trauma response
- social: debt, promise, betrayal, public humiliation, rank change
- capability: lost weapon, depleted magic, broken device, exhausted money, burned contact

### 2. Information / Knowledge Ledger

Track who knows what and how they know it.

Questions:
- Has this character seen, heard, read, inferred, or been told this fact?
- Is the name/identity known to them, only to another character, or only to the narrator?
- Is the knowledge certain, suspected, false, rumor, or manipulated?
- Does a later chapter let them act on knowledge they should not have?

### 3. Object / Resource / Evidence Ledger

Track anything that can be held, lost, consumed, copied, damaged, hidden, spent, or used as proof.

Questions:
- Who has it now?
- Where is it?
- Is it intact, damaged, copied, destroyed, fake, or unreliable?
- Has it already been used up or handed off?
- Does later prose use it while it should be elsewhere?

### 4. Scene Feasibility Ledger

Track whether an action or line is possible under the current pressure.

This is not only for combat. It applies to any high-pressure scene: argument, chase, surgery, ritual, meeting, trial, confession, escape, negotiation, disaster, sex/romance scene, stealth, or public confrontation.

Questions:
- Is there enough time to say/do this?
- Is the character able to breathe, see, hear, stand, type, drive, call, cast, aim, remember, or decide?
- Is there an interruption or pause that permits the action?
- Is the description over-complete for the scene pressure?
- Would a simpler fragment, silence, glance, failed attempt, or later recognition be more plausible?

### 5. Literal vs Figurative Language Ledger

Track vivid descriptions that might later be mistaken as facts.

Questions:
- Is this a literal event, metaphor, sensation, rumor, dream, hallucination, character inference, or narrator fact?
- Does later prose accidentally treat a metaphor as literal?
- Does a comparison create a new implied object/injury/event that was never established?

Example pattern:
- `像被钝钉钉入` should be recorded as metaphor for pain/impact unless an actual nail-like object is explicitly introduced.

### 6. Cause → Consequence Ledger

For every major event, check whether consequences appear or are deliberately suppressed/explained.

Questions:
- If someone is injured, humiliated, exposed, betrayed, promoted, poisoned, indebted, or seen, what follows?
- If no consequence appears, is that plausible in this genre/world?
- Did the story forget the cost of an action?

## Audit procedure

Before approving a chapter:

1. **Extract state changes from the draft**
   - character, object, information, relationship, location, system, resource, and language-state changes.

2. **Classify ambiguous descriptions**
   - literal / metaphorical / perception / rumor / dream / uncertain.
   - Do not let later chapters silently convert one category into another.

3. **Compare against prior canon**
   - Read or summarize relevant prior chapter/audit/state. Do not rely on memory.

4. **Check scene feasibility**
   - Actions, dialogue, recognition, physical movement, technical operations, emotional turns, and decisions must fit the time/pressure/knowledge available.

5. **Check consequences**
   - If a change should matter later, either carry it forward or explain why it no longer matters.

6. **Flag severity**
   - Critical: contradiction changes plot, identity, evidence, survival, rules, or a major relationship/decision.
   - Major: state drift, impossible action, or missing consequence that breaks reader trust.
   - Minor: ambiguity or wording that can be fixed with a line-level patch.

7. **Patch with minimal changes**
   - Clarify literal vs metaphorical status.
   - Add or move a pause/opening/consequence when needed.
   - Correct state ownership/source/timing consistently.
   - Do not invent new facts unless necessary and consistent with approved canon.

## Required audit output

```markdown
## Continuity Bug Audit

### Relevant ledgers used
- Character state: used / not relevant
- Information & knowledge: used / not relevant
- Object/resource/evidence: used / not relevant
- Scene feasibility: used / not relevant
- Literal vs figurative language: used / not relevant
- Cause → consequence: used / not relevant
- Other project-specific ledger: [name]

### Findings
- [Category]: Pass / Minor / Major / Critical — details and evidence

### Required fixes
- [Minimal targeted fix]

Verdict: Pass / Needs targeted revision / Regenerate
```

## Common examples to catch

These are examples, not hardcoded categories:

- A metaphor becomes a literal fact later.
- A serious state change has no consequence and no explanation.
- A character says, recognizes, or does something impossible under scene pressure.
- A source/location/ownership state changes without cause.
- A character knows a fact they never learned.
- A relationship or promise is forgotten when it should constrain behavior.
- A genre system's cost or limitation disappears when inconvenient.
