# Execution Modes and Confirmation Gates

Use this reference whenever selecting workflow rigor, deciding whether a confirmation may be combined or skipped, or resolving a request to move faster.

Modes change ceremony, persistence, pass separation, and confirmation frequency. They do not lower prose-quality, continuity, canon, Humanizer, Story Fact Check, leakage-prevention, or Final Verification standards.

## Mode selection

- Use **Standard** when the user does not select a mode.
- Scope a mode to the current workflow or work unit unless the user explicitly records it as a project default.
- Honor an explicit mode when the request is eligible.
- Escalate Fast to Standard before continuing when persistent canon, multi-chapter dependencies, destructive revision, unclear source-of-truth files, or unresolved continuity risk appears. State the reason.
- Recommend Production for publication-oriented, high-continuity, long-running, or high-cost work, but do not silently select it unless project rules already require it.
- A mode change never invalidates approved canon or waives a gate that became mandatory because risk changed.

## Cross-mode invariants

All modes must:

1. Read actual project files before claiming project state, canon, chapter status, or existing prose.
2. Preserve a binding brief whenever canon, supplied constraints, required beats, or forbidden changes matter.
3. Keep final prose free of workflow, audit, planning, and role scaffolding.
4. Run Story Fact Check after Narrative Humanizer whenever prose changes.
5. Run Final Verification before Promotion & State Update and before reporting completion.
6. Keep role inputs and outputs isolated; no role silently overwrites another role's source.
7. Back up completed prose before any in-place revision.
8. Stop immediately when the user asks to stop.
9. Never auto-continue to the next chapter or scene.
10. Modify this reusable Skill only with explicit authorization under `skill-change-protocol.md`.

## Fast

### Purpose and eligibility

Use for low-risk, bounded work where speed matters more than durable process evidence, such as:

- short one-shots;
- exploratory scenes;
- bounded rewrites with supplied source text;
- small prose revisions;
- self-contained work that does not establish broad canon.

Do not use Fast by default for multi-chapter planning, canon-heavy continuation, deep structural revision, or publication/release verification.

### Required behavior

- Use one compact brief or mini-gate before prose unless the user explicitly requests immediate writing and the applicable fast path permits it.
- Preserve requested facts, constraints, required beats, and forbidden changes in a binding statement, even if it is temporary.
- Run every quality check required by the requested operation.
- Keep composite review findings separately labeled and independently checkable.
- Run Story Fact Check after Humanizer and run Final Verification before any official promotion or shared-state update.
- Stop after the requested work unit.

### Permitted shortcuts

- Combine closely related planning confirmations into one compact confirmation.
- Skip Project Profile, full System Bible, or detailed long-form outline when the task is genuinely self-contained.
- Use temporary isolated outputs instead of persisting every intermediate role file.
- Execute Character Review and Lore & Continuity Audit as one Content Review batch when their findings and correction ownership remain distinct.
- Use temporary Prose Stylist and Narrative Humanizer intermediates when their order and separate results remain inspectable.

### Prohibited shortcuts

- Do not skip project-file inspection for existing work.
- Do not skip the binding brief when canon or supplied constraints matter.
- Do not skip Story Fact Check after Humanizer.
- Do not skip Final Verification or move official promotion before it.
- Do not silently remain in Fast after an escalation trigger appears.

### Persistence

Persist final requested artifacts and any project-state change required by the domain workflow. Create prose run state when interruption/recovery is plausible, persistent canon or shared state may change, multiple logical stages are used, or the user requests auditability. Intermediate role outputs may be temporary unless the project already requires durable evidence.

## Standard

### Purpose and eligibility

Use as the default for ordinary novel setup, planning, chapter generation, continuation, and revision.

### Required behavior

- Apply every setup and preflight gate relevant to the request.
- Persist approved project artifacts and chapter briefs required by the domain workflow.
- For supported prose-delivery work, create run state when Preflight starts and execute the complete seven-stage sequence in order, marking only objectively inapplicable stages with reasons.
- Isolate each role's inputs and outputs, whether using subagents or sequential passes.
- Preserve explicit approval requirements for Project Profile, initial outline, System Bible, detailed plot outline, and current chapter preflight when created or materially changed.
- Run Story Fact Check when prose changes, then Final Verification, then Promotion & State Update.

### Permitted shortcuts

- Skip gates and artifacts that are objectively not applicable.
- Reuse an unchanged artifact already approved in project files or confirmed in the current conversation.
- Present related setup decisions together, provided each remains explicit and independently confirmable.
- Skip auxiliary companion workflows that are outside the requested fiction-planning or prose-delivery scope.

### Prohibited shortcuts

- Do not skip current chapter preflight before new chapter prose.
- Do not treat silence as confirmation.
- Do not omit a logical role because the runtime lacks subagents.
- Do not allow roles to overwrite one shared source without an explicit merge step.

### Persistence

Persist the approved brief, required project artifacts, run snapshot, necessary role evidence, final candidate, Final Verification result, promotion result, final prose, audits, and state updates according to the project's established structure.

## Production

### Purpose and eligibility

Use for publication-oriented, high-continuity, long-running, expensive, or maximum-traceability work.

### Required behavior

- Apply every Standard requirement.
- Keep each internal logical role/check as a distinct pass, including both Content Review checks and both Prose Refinement passes.
- Create prose run state when Preflight starts and persist approved inputs and output evidence for every applicable role using the project's established directories or documented equivalents.
- Require explicit review of each applicable foundational artifact and chapter preflight; do not bundle separate artifacts into one implicit approval.
- Back up completed prose before revision.
- Preserve a clear source-to-final merge path and retain audit evidence.
- Treat blocking Character Review, Lore & Continuity Audit, continuity, contract, Humanizer, or Story Fact Check findings as stop conditions until corrected and rechecked.
- Block when freshness cannot be established until a reliable comparison or full required recheck completes.
- Run the complete Final Verification checklist before Promotion & State Update and report remaining known risks.

### Permitted shortcuts

- Skip only objectively inapplicable fiction workflows or external companion work not requested.
- Reuse approved artifacts only after verifying their content and version are unchanged.

### Prohibited shortcuts

- Do not waive a mandatory generation, review, Story Fact Check, Final Verification, or promotion-safety stage while remaining in Production.
- Do not use temporary-only role outputs when durable evidence is expected.
- Do not continue after a blocking finding without correction or an explicit mode downgrade with risk acknowledgement.

### Persistence

Persist all binding inputs, complete obtainable artifact snapshots, role outputs, audits, Story Fact Check and Final Verification evidence, backups required for revision, promotion evidence, final artifacts, and state updates. Report unavailable hash or equivalent integrity evidence as degraded rather than verified.

## Confirmation semantics

- Silence and lack of objection are not confirmation.
- A direct command may count as confirmation only when it clearly authorizes the exact next action and the applicable workflow already permits that form.
- Approval is scoped to the named artifact or work unit. It never authorizes automatic continuation to later chapters.
- Renew confirmation when a change affects binding facts, scope, tone, required beats, or another approved contract.
- When the user asks to skip a gate, apply the mode-specific rule below. Record any accepted waiver in the active brief or execution record.
- A stop request overrides every mode and stage immediately.

## Confirmation-gate matrix

| Gate | Trigger | Fast | Standard | Production | Reuse of prior approval | Skip request and escalation |
|---|---|---|---|---|---|---|
| Premise or seed direction | Starting a new story direction or materially changing the premise | May combine into the compact gate | Explicit confirmation before style/element planning | Separate explicit review and confirmation | Reuse only when unchanged | Fast may skip only for immediate self-contained writing with an explicit premise in the request; otherwise stop. Standard/Production require confirmation. |
| Style, elements, forbidden tendencies, Tone Lock | Creating or materially changing the project's prose and element contract | May combine all fields into one compact confirmation | Explicit confirmation before length and outline | Separate artifact-level review; no implicit bundling with outline | Reuse unchanged approved project rules | A skip is acceptable only for self-contained Fast work with sufficient style direction in the request. Persistent-project work escalates to Standard. |
| Project Profile write or update | First creation or project-level rule change | Usually inapplicable; if persistent rules are needed, escalate to Standard | Show full draft and obtain explicit confirmation before write | Separate full review and explicit confirmation | Reuse unchanged file; any binding change requires renewal | Never infer or silently write. A requested skip means do not create/update the profile. |
| Initial story outline | Creating or materially changing the full-story direction | May use a compact beat outline for self-contained work | Explicit confirmation before System Bible | Separate review and explicit confirmation | Reuse unchanged approved outline | Immediate-writing Fast requests may omit a full outline when no persistent canon is created. Otherwise escalate or stop. |
| System Bible | Creating or materially changing canon rules | May omit for self-contained work with a sufficient binding brief | Explicit confirmation before detailed plot outline | Separate review and explicit confirmation | Reuse only after verifying unchanged canon | If canon complexity requires a Bible, Fast escalates. Standard/Production may not skip required canon definition. |
| Detailed plot outline | Creating or materially changing chapter-level plot obligations | May omit for one-shot/self-contained work | Explicit confirmation before chapter preflight/generation | Separate review and explicit confirmation | Reuse unchanged approved outline | Multi-chapter or obligation-heavy work cannot silently skip; Fast escalates. |
| Current chapter or scene preflight | Before generating new prose that depends on canon, outline, or chapter obligations | Compact brief; explicit confirmation unless immediate-writing fast path applies | Explicit confirmation before new chapter prose | Separate persisted preflight review and explicit confirmation | Reuse only when confirmed in the current conversation and unchanged | Standard/Production cannot skip chapter preflight. Fast may use immediate writing only when the applicable mini-gate permits it and constraints are already explicit. |
| Deep revision or regeneration plan | User requested review-first, deep structural changes, or fresh regeneration | Compact proposed-change confirmation | Explicit approval before editing when the revision workflow requires it | Separate review, backup plan, and explicit approval | Reuse only for the exact unchanged revision scope | Do not edit after a review-first request without approval. Destructive or canon-altering revision escalates from Fast. |
| Continue to next chapter or scene | Current requested unit is complete | Always stop and ask | Always stop and ask | Always stop and ask | Never inferred from approval of the previous unit | This gate cannot be waived prospectively by silence. A direct request naming the next unit authorizes that unit's preflight, not automatic prose unless its preflight is already confirmed. |

## Conflict resolution

When a domain reference appears to conflict with this file:

1. Preserve the stricter canon, quality, Story Fact Check, Final Verification-before-promotion, and no-auto-continue rule.
2. Treat domain-specific artifact fields as owned by the domain reference.
3. Treat mode, confirmation, waiver, persistence, and escalation policy as owned by this file.
4. Surface any remaining behavioral contradiction instead of averaging it.
