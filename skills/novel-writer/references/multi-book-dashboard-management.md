# Multi-Book Dashboard Companion Boundary

Multi-book dashboard behavior belongs to a separate dashboard companion project or Skill, not to the core Novel Writer workflow.

A companion implementation may consume Novel Writer project artifacts, but it must define and verify its own:

- project discovery and safe IDs;
- chapter/state/audit file adapters;
- mobile navigation and accessibility;
- authentication and authorization;
- archive, deletion, and recovery behavior;
- API, framework, process, port, and deployment configuration.

Do not copy environment-specific server commands or destructive file-management behavior into Novel Writer. Treat this file as a compatibility pointer only.