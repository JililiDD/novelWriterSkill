# Novel Dashboard Companion Boundary

Dashboard and mobile-reader implementation is not part of the core Novel Writer writing workflow.

Use a separate dashboard companion project or Skill when the user asks to build, run, deploy, or modify a reading interface. That workflow should inspect the actual application, framework, project paths, APIs, ports, authentication, and deployment environment before making changes.

The core Novel Writer Skill may provide only stable content contracts:

- discover project-specific final chapters and approved state files;
- render Markdown accessibly on desktop and mobile;
- avoid hardcoded book names, absolute machine paths, or one fixed chapter convention;
- use safe path validation for file reads and project selection;
- keep destructive file operations outside reading endpoints;
- verify the real application after implementation.

Do not use fixed ports, kill processes, delete directories, or assume a specific framework from this reference.