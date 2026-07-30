# Ongoing Serial Handoff — Compatibility Reference

This former standalone continuation module is retained only for backward compatibility.

For an existing serial:

1. use `long-form-continuity.md` to bootstrap or read Story Memory and assemble current context;
2. use `chapter-pipeline.md` for the next chapter's Preflight, seven-stage delivery, Proposed Story Memory Delta, verification, and promotion;
3. use `execution-modes.md` for the next-unit confirmation gate;
4. use `run-state-protocol.md` for recovery, freshness, stale propagation, and candidate selection.

A request such as `继续下一章` authorizes entry into the next chapter's Preflight. It does not bypass an unresolved confirmation or conflict. Stop after the requested chapter; never auto-continue.