# Audiobook / TTS Companion Boundary

Audiobook production is not part of the core Novel Writer writing workflow.

Use a separate audiobook companion project or Skill when the user asks to select current TTS engines, clone voices, generate audio, merge chapters, create manifests, or publish audiobook formats. That workflow must verify current products, licensing, network access, GPU availability, dependencies, voice quality, and distribution requirements at execution time.

Novel Writer provides only stable handoff requirements:

- use promoted final prose, not drafts or unverified candidates;
- preserve chapter titles and reading order;
- remove Markdown control syntax without changing wording;
- record the source chapter revision used for each audio output;
- keep voice, pronunciation, normalization, chunking, and output settings in an external audiobook manifest;
- do not alter canon or prose merely to accommodate one TTS engine without an approved revision run.

Do not hardcode current model recommendations, voices, APIs, credentials, local paths, GPU assumptions, or merge commands in this core reference.