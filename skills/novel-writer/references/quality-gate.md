# Chapter Quality Gate & Invalidation Rules — 章节质量门槛与检查失效规则

Use this reference during Content Review, Prose Refinement, Story Fact Check, and Final Verification to evaluate whether a candidate meets the objective threshold for `PROMOTION READY`.

---

## 1. Quality Scoring Framework

A simple binary Pass/Fail is insufficient for long-form quality assurance. The Quality Gate evaluates candidate prose across seven weighted dimensions totaling **10.0 points**.

### The Seven Dimensions

| Dimension | Standard Weight | Focus & Verification |
|---|---:|---|
| **Contract / Continuity** | 20% (2.0 pts) | Brief contract fulfillment, factual alignment, knowledge boundaries, timeline feasibility, object custody, no promise leakage. |
| **Character / Voice** | 20% (2.0 pts) | Dialogue Engine alignment, speaker-substitution differentiation, Functional Character Realism for NPCs, emotional continuity. |
| **Naturalness / Anti-Template** | 20% (2.0 pts) | Absence of AI construction habits (structural naturalness), absence of unearned aphorisms, diverse sentence shapes. |
| **Scene / Pacing** | 15% (1.5 pts) | Tension control, spatial anchoring, sensory grounding, clear causal state change before scene closure. |
| **POV / Cognitive Ownership** | 10% (1.0 pts) | Narration stays within viewpoint sensory & cognitive radius; behavioral competence without narrator cheerleading. |
| **Prose Precision / Rhythm** | 10% (1.0 pts) | Evocative phrasing, absence of cliché body shorthand, mixed sentence cadence, clean rhythm. |
| **Chapter Interface** | 5% (0.5 pts) | Seamless transition with Chapter $N-1$ ending and Chapter $N+1$ opening (time, location, physical/emotional aftermath). |

---

## 2. Gate Threshold for `PROMOTION READY`

A candidate qualifies for `PROMOTION READY` **only if both conditions are met**:

$$\text{Total Score} \ge 9.5 / 10.0 \quad \text{AND} \quad \text{No critical dimension} < 9.0 / 10.0$$

### Dynamic Weight Adjustments
Specialized chapter types may adjust dimensional weights by up to $\pm 5\%$:
- **Dialogue-heavy chapter**: Voice & Character increases to 25%; Scene/Pacing decreases to 10%.
- **Action / Battle chapter**: Continuity & Spatial Pacing increases to 25%; Voice decreases to 15%.
- **Emotional Turning Point**: POV & Character increases to 25%; Scene decreases to 10%.

*Constraint*: Adjustments must never be used to artificially boost an underperforming candidate past the 9.5 threshold.

---

## 3. Substantive Check Invalidation Matrix

When a candidate is edited following a review finding, previously passed checks may become **stale and invalid**.

```text
Any substantive prose change invalidates dependent downstream checks.
```

### Invalidation Rules

| Type of Edit | Scope of Invalidation | Required Re-Execution |
|---|---|---|
| **Dialogue Rewrite** | Stales Character Check, Structural Naturalness, Surface Humanizer, Story Fact Check, Final Verification | Re-run Dialogue Engine check, Humanizer, Fact Check, and Final Verification |
| **Action / Staging Change** | Stales Continuity Check, POV Check, Scene/Pacing, Fact Check, Final Verification | Re-run Continuity Check, Story Fact Check, and Final Verification |
| **Emotional / Interiority Edit** | Stales Structural Naturalness, Surface Humanizer, POV Check, Final Verification | Re-run Humanizer and Final Verification |
| **Interface / Transition Edit** | Stales Chapter Interface Check, Continuity Check, Final Verification | Re-run Interface Check and Final Verification |
| **Safe Edit (Minor typo / punctuation)** | **Safe Scope**: Does not stale upstream checks | Re-verify affected lines only; proceed to Final Verification |

---

## 4. The Skeptical Reader Test (反向读者测试)

Before approving Final Verification, run this 8-point diagnostic scan:

1. **Information Kiosk Check**: Can the reader feel the author orchestrating characters solely to feed facts to the protagonist?
2. **Instant Insight Check**: Does the protagonist deduce complex truths faster and more correctly than everyone else without paying verification costs?
3. **NPC Existence Check**: Do secondary characters vanish into thin air the moment the protagonist no longer needs their services?
4. **Unearned Aphorism Check**: Is there a grandiose philosophical generalization inserted merely to make the prose sound profound?
5. **Paragraph Summary Check**: Would any paragraph become stronger or punchier if its final explanatory sentence were deleted?
6. **Masked Voice Check**: If character names are removed, can the speaker of every consequential dialogue line still be identified?
7. **Over-Explanation Check**: Is every emotional beat, reaction, or clue explained to the reader multiple times?
8. **Knowledge / Status Leakage**: Does any character speak outside their social station, professional reality, or self-interest?

*Action*: Any `YES` answer must be resolved through targeted revision or upstream structural adjustment before granting `PROMOTION READY`.
