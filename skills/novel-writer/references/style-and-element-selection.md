# Style & Element Selection and Compatibility — 文风与元素选型及兼容性分析

Use this reference during startup before creating the Project Profile. It owns the selection procedure, compatibility evaluation framework, and Tone Lock definition. `style-library.md` and `element-library.md` own reusable definitions.

---

## 1. Selection Principles

- Choose exactly **one main style**.
- Choose **zero to two supporting styles**.
- Choose **one to three core elements** and **zero to three secondary elements**.
- Record styles and elements the user explicitly rejects.
- Run the **Compatibility Analysis** before setting final length or outlining.
- Preserve a custom option whenever pre-built libraries do not fit.

Do not maintain a fixed short menu. Scan the premise, then present the 5–8 most relevant options from the Style Library and relevant element groups from the Element Library.

---

## 2. Step 1: Style Candidates

Present candidates with one-line implementation implications:

```markdown
## Suggested Style Directions
1. [Style] — [what it changes in narration, dialogue, pacing, and emotional distance]
2. ...

Choose:
- Main style: one
- Supporting styles: zero to two
- Explicitly avoid:
- Custom direction, if none fit:
```

When the user names a custom style, define its observable traits before using it. Follow `library-expansion-protocol.md` only when saving it as a reusable library entry.

---

## 3. Step 2: Element Mix

Use the Element Library to present premise-relevant choices across identity, mechanism, plot engine, world type, emotional payoff, relationship structure, and organization/growth patterns.

```markdown
## Element Mix
- Core elements: one to three
- Secondary elements: zero to three
- Forbidden elements:
- Required implementation constraints:
```

Core elements must drive plot decisions. Secondary elements add texture or bounded subplots.

---

## 4. Step 3: Four-Dimension Compatibility Analysis

Evaluate the chosen combination across four core dimensions:

### 1. Tone Coherence (基调一致性)
- Verify that chosen styles and emotional promises coexist without cancelling each other out (e.g. grim horror vs slapstick humor).

### 2. Suspense & Information Integrity (悬念与信息完整性)
- Ensure mechanisms (such as systems, preknowledge, or omniscient devices) do not eliminate dramatic uncertainty or investigation tension.

### 3. Complexity Budget (复杂度预算)
- Check whether the target novel length can support the number of factions, magic systems, and relationship tracks. If overloaded, convert core elements to secondary texture or defer them to later volumes.

### 4. Mechanism Dominance (机制主导风险)
- Ensure systems or tropes create constraints and choices rather than replacing character agency and causal storytelling.

### Classification

- **Strong fit**: Components reinforce each other naturally.
- **Conditional fit**: The mix works only with explicit constraints (record in Project Profile).
- **High risk**: The combination threatens logic, pacing, or reader trust unless redesigned or pruned.

```markdown
## Compatibility Check Output
- Strong fits:
- Conditional fits:
- High-risk conflicts:
- Required constraints:
- Complexity-budget assessment:
- Mechanism-dominance risk:
- Recommended core hierarchy:
- Items to weaken, defer, or remove:
```

---

## 5. Step 4: Tone Lock

```markdown
## Tone Lock
- Main emotional texture:
- Lower bound:
- Upper bound:
- Must avoid:
- Reader experience target:
```

Tone Lock defines a bounded emotional range, not a single monotonous tone repeated in every scene.

---

## 6. Step 5: Seed Project Profile Fields

Pass the confirmed selections to `project-profile-workflow.md`:
- main/supporting styles;
- core/secondary/forbidden elements;
- implementation constraints & compatibility rules;
- Tone Lock;
- reader promise & initial drift signals.