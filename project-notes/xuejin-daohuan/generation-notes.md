# 《雪尽刀还》generation notes

Session-specific lessons worth reusing for wuxia chapter generation.

## Exact contract wording matters

When the approved outline requires a clue phrase or exact line, verify exact wording, not only semantic presence.

Example: Chapter 5 required `井中被下药` / keyword `下药`. Draft used `井里有药`, which was semantically close but failed exact keyword verification. Minimal fix patched both final and draft:

```python
from pathlib import Path
root = Path('/home/ddxy/Desktop/hermes/jobs/novel-generator/xuejin-daohuan')
for rel in ['chapters/ch05_final.md', 'scenes/ch05_s01_draft.md']:
    p = root / rel
    text = p.read_text(encoding='utf-8')
    text = text.replace('井里有药，喝过水的人手软，嗓子哑，连喊都喊不响。',
                        '井中被下药，喝过水的人手软，嗓子哑，连喊都喊不响。')
    p.write_text(text, encoding='utf-8')
```

Then re-run required-keyword and forbidden-token checks.

## Multi-book dashboard verification

The project-level dashboard at `~/Desktop/hermes/jobs/novel-generator` is a multi-book dashboard. It may not expose legacy `/api/status`.

Use:

```python
import urllib.request, json
books = json.load(urllib.request.urlopen('http://127.0.0.1:8420/api/books?ts=1', timeout=5))
book = next(b for b in books if b['id'] == 'xuejin-daohuan')
chapter = next(ch for ch in book['chapters'] if ch['number'] == 5)
url = 'http://127.0.0.1:8420' + chapter['url']
with urllib.request.urlopen(url, timeout=5) as r:
    assert r.status == 200
```

Useful fields: `completed_chapters`, `chars`, `chapters[].title`, `chapters[].chars`, `chapters[].url`, `chapters[].audit_url`.

## Stop/confirm discipline

If the user says `停下`, stop generation immediately and do not continue to prose. If a prior generation completed in the background, summarize and verify its artifacts, but do not move to the next chapter without the required per-chapter preflight confirmation.
