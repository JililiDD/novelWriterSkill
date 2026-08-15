# Style Calibration & Recalibration — 文风受控校准与重校准

Use this reference when establishing the narrative style for a new story or recalibrating style during an ongoing project. It translates abstract style preferences into observable, enforceable realization rules before scale.

---

## 1. Problem & Purpose

Abstract style descriptions (e.g. “有质感”, “偏权谋”, “现代白话”, “网文感强一点”, “不要太文艺”) are too vague to reliably determine:

- narrative distance (close vs medium vs panoramic);
- sentence cadence and paragraph rhythm;
- description density;
- psychological explicitness (unspoken subtext vs internal monologue);
- dialogue texture and speech cadence;
- information release speed;
- emotional temperature and hook placement.

Waiting for style to stabilize across multiple chapters causes extensive downstream rewrites. **Style Calibration locks language and realization parameters before drafting Chapter 1.**

---

## 2. When to Suggest Style Calibration

### Recommend when:
- starting a new persistent project (`Project Creation`);
- the user provides abstract style keywords;
- no mature official prose or pre-existing Narrative Anchor is available;
- the user expresses high sensitivity to voice, prose rhythm, or dialogue texture.

### Skip when:
- the user supplies an approved sample text as the explicit Narrative Anchor;
- an established novel project already has promoted chapters and active anchors;
- the user explicitly declines multi-version comparison and requests immediate drafting.

Style Calibration is an **optional mechanism, not a blocking gate**.

---

## 3. Controlled Comparison Protocol

All comparison versions must lock story meaning and vary only the realization layer:

```text
LOCKED STORY MEANING:
- Same POV and viewpoint character
- Same cast present in the scene
- Same physical setting and spatial anchors
- Same core actions and event sequence
- Same information gained / revealed
- Same ending boundary state
```

```text
VARIED REALIZATION LAYER:
- Narrative distance
- Sentence rhythm and paragraph shape
- Psychological explicitness vs behavioral restraint
- Description density vs action velocity
- Dialogue texture and subtext density
- Explanation level and information pacing
- Emotional temperature
```

### Sample Length
- **600–1,500 Chinese characters** per version.
- Do not draft multiple full chapters for calibration; short scenes isolate prose texture from plotting variables.

---

## 4. Standard Calibration Profiles

When generating 2–4 candidate realizations, offer meaningfully distinct profiles such as:

### Profile A — 冷静克制型 (Restrained / Observational)
- **Narrative distance**: Tight third-person limited, medium-close.
- **Rhythm**: Compact sentences, decisive stops under pressure.
- **Interiority**: Restrained; decisions proven through actions and observational attention.
- **Information**: Strict evidence-first; narrator rarely summarizes.

### Profile B — 强推进连载型 (Propulsive / Serialized Momentum)
- **Narrative distance**: Direct, high clarity, rapid scene transition.
- **Rhythm**: Brisk cadence, quick exchanges, clear situational tension.
- **Interiority**: Immediate goal-focused cognition; minimal decorative reflection.
- **Information**: Faster reveal of practical stakes, prominent scene hooks.

### Profile C — 细腻沉浸型 (Immersive / Sensory & Psychological)
- **Narrative distance**: Intimate, bodily and environmental texture foregrounded.
- **Rhythm**: Layered sentences with sensory pacing and longer transitions.
- **Interiority**: Deeper psychological tracking, unspoken social hesitation.
- **Information**: Layered observation; sensory immersion precedes action.

---

## 5. Style Lock & Project Profile Integration

After user selection (single profile, hybridized choice, or adjusted sample), decompose the choice into actionable dimensions in `state/project_profile.md`:

```markdown
## Narrative Style Lock

### Narrative distance
- [e.g. Third-person limited, close-medium; camera stays strictly within viewpoint's sensory radius]

### Cognitive movement
- [e.g. Observe sensory evidence → infer immediate risk → act/decide; avoid pre-emptive narrator summary]

### Sentence rhythm
- [e.g. Mixed sentence lengths; avoid uniform short-sentence cadence; short landing lines only under high pressure]

### Description density
- [e.g. Functional and scene-grounded; 1–2 sharp tactile/spatial cues; avoid decorative tours]

### Psychological explicitness
- [e.g. Restrained by default; show emotion through avoidance, task focus, or physical friction; expand only at turning points]

### Dialogue floor
- [e.g. Natural modern vernacular; goal-driven; no pseudo-classical filler; no shared clipped aphorisms]

### Information release
- [e.g. Evidence before explanation; zero summary of what dialogue already revealed]

### Competence display
- [e.g. Shown through questions asked, verification actions, and cost management; not narrator praise]

### Forbidden drift
- [e.g. Over-explaining obvious clues, characters sharing identical clipped syntax, speechifying NPCs]

### Narrative Anchor
- [Selected sample passage or reference excerpt]

### Rejected Drift Notes
- [e.g. Option B was too fast/generic; Option C had excessive descriptive pauses]
```

### Recording Rejected Drift Notes
Keep brief reasons for declined options to prevent the assistant from drifting back toward rejected tendencies during long serial runs.

---

## 6. Style Recalibration (Mid-Project)

### Triggers:
- User repeatedly remarks: “风格还是不对”, “人物说话太像了”, “改了几遍还是不够味”, or “对白太文绉绉”.
- Rolling Checkpoint or cross-range audit detects persistent drift away from the Narrative Anchor.
- Narrative tone needs an intentional shift across volume boundaries (e.g. transition from peacetime intrigue to active war).

### Recalibration Workflow:
1. **Pause new chapter drafting.**
2. Select a representative 800–1,200 character scene from a recent chapter or the current candidate.
3. Lock story facts and generate 2–3 calibration versions varying the realization layer according to user feedback.
4. Obtain user selection or adjustment.
5. Update `state/project_profile.md` (Style Lock, Narrative Anchor, Rejected Drift Notes).
6. Resume chapter drafting or revise affected candidate prose using the refreshed anchor.
