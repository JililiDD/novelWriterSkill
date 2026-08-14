# Dialogue Engine & Functional Character Realism — 对白生成引擎与人物真实感

Use this reference to generate, audit, and refine dialogue across core, recurring, and secondary characters. It replaces negative bans with a positive generative framework and enforces functional character realism.

---

## 1. The Generative Dialogue Engine

Dialogue is not an authorial explanation vehicle. Every consequential line is generated from six active forces:

$$\text{Dialogue} = \text{Current Goal} + \text{Knowledge Boundary} + \text{Status/Occupation} + \text{Relationship} + \text{Immediate Emotion} + \text{Speaker Strategy}$$

### The Six Drivers

1. **Current Goal (当下动机)**
   - What does the speaker want *from the other person right now*?
   - Examples: deflect suspicion, obtain a specific number, buy time, provoke an emotional reaction, secure payment, establish dominance, avoid taking responsibility.

2. **Knowledge Boundary (认知边界)**
   - What does the speaker actually know, suspect, misunderstand, or not know?
   - A speaker never speaks from the narrator’s, author’s, or protagonist’s omniscient perspective.

3. **Status & Occupation (身份与职业习惯)**
   - Lived constraints, social power, professional vocabulary, and vulnerability to consequences.
   - A warehouse clerk, a military commander, and a corrupt magistrate perceive and discuss the same cargo through entirely different risks and vocabularies.

4. **Relationship (人物关系与权力差)**
   - Hierarchy, mutual debt, shared history, trust or suspicion, past grievances, etiquette taboos.
   - Words change drastically depending on whether the counterpart is a superior, subordinate, rival, trusted ally, or stranger.

5. **Immediate Emotion & Pressure (即时情绪与压力)**
   - Fatigue, panic, impatience, grief, fear, or cold calculation.
   - High pressure typically degrades rhetorical complexity or forces defensive brevity; intimacy or safety allows elaboration or hesitation.

6. **Speaker Strategy (交际策略与话术习惯)**
   - The speaker’s habitual method: direct interrogation, transactional bargaining, passive defiance, feigned ignorance, flattery, diversion, counter-questioning, or loaded silence.

---

## 2. Character Dialogue Profile in Story Facts

For core and recurring characters, define the following fields in `state/story_facts.md`:

```markdown
### Dialogue Profile
- Wants / Habitual drive: [Core social/practical objective in interactions]
- Notices first: [What details/tones/weaknesses they register immediately]
- Knowledge baseline: [What they understand deeply vs what they are blind to]
- Default tactic: [E.g., transactional negotiation, deceptive compliance, aggressive probing]
- Status speech impact: [How their social/professional station shapes their words]
- Under pressure: [E.g., sentences shorten, speaks with colder precision, rambles defensively]
- With trusted counterparts: [E.g., drops formal honorifics, exhibits dry sarcasm, admits uncertainty]
- Typical refusal style: [How they say "no" — blunt, delayed, bureaucratic, evasive]
- Typical request style: [How they ask for help or demand compliance]
```

Do **not** use catchphrases, dialect gimmicks, or verbal tics as substitutes for character motivation and relationship dynamics.

---

## 3. Functional Character Realism (“普通人模式”)

### The AI NPC Trap
AI-generated secondary characters frequently act as frictionless information kiosks:
- perfectly accurate and immediate recall;
- zero hesitation or misunderstanding;
- no personal stakes, fear, or fatigue;
- speaking in crisp, abstract analytical summaries;
- anticipating exactly what the protagonist needs.

### Realism Principles for Ordinary People

1. **Partial Knowledge (碎片化认知)**
   - Ordinary characters know their immediate workspace, daily duties, and local gossip. They do not understand the overarching conspiracy or grand strategy.

2. **Self-Preservation & Immediate Stakes (切身利益优先)**
   - Real people care about their wages, safety, blame avoidance, family, mealtime, and going home on time.
   - When questioned, their first instinct is often: *“Will this get me into trouble? Who has to pay for this?”*

3. **Concrete Particulars over Abstract Concepts (具象代替抽象)**
   - **Abstract Authorial Concept**: “基层账目记录的信息粒度正在丢失。”
   - **Real Worker Dialogue**: “以后东西少了，别又回来算在我头上。我就管过秤，里头装的是生铁还是石头，封条又不是我贴的。”

4. **Imperfect Delivery (不完美的日常表达)**
   - Ordinary speech allows self-correction, recounting the conclusion before the premise, citing tangible examples rather than theories, and expressing reasonable uncertainty (*“记不清了”, “大约是初五或者初六吧”*).

---

## 4. Speaker-Substitution Check (换人测试)

### Priority Inspection Targets
Perform the Speaker-Substitution Check on high-consequence dialogue:
- key deductions and strategic choices;
- refusals and demands;
- major confessions and promises;
- conflict confrontations and relationship turning points.

### Inspection Procedure
1. Mask the character name.
2. Place the line into the mouth of another major character in the same scene.
3. Evaluate: *Does the line still make complete sense with identical phrasing, attitude, and rhetorical strategy?*
   - **If YES**: Voice convergence detected. Rebuild the line using the original speaker’s specific goal, status vulnerability, and cognitive bias.
   - **If NO**: Voice differentiation verified.

### Scope Boundary
Functional short responses (e.g. *“拿去。”*, *“走这边。”*, *“几点了？”*) do not require artificial uniqueness. Do not force bizarre phrasing onto ordinary actions.
