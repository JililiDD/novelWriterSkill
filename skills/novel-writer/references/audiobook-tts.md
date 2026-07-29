# Audiobook / TTS workflow notes

Use when converting a generated novel into an audiobook or producing TTS samples for voice selection.

## Fastest free sample path: Edge TTS

`edge-tts` can generate high-quality Chinese speech without an Azure account, Edge login, API key, or registration. It uses Microsoft Edge online neural voices, so it requires internet access and is not the same as a formal Azure commercial API. Good for personal demos, samples, and low-cost audiobook prototyping; review service terms before large-scale commercial distribution.

Recommended first step for Chinese wuxia novels:
1. Extract the first 500-900 Chinese characters from chapter 1 and normalize punctuation lightly.
2. Generate 2-3 sample voices at a slower rate (`rate='-8%'` to `-12%'`).
3. Send MP3 samples to the user before generating the full book.

Known-good voices for Chinese samples:
- `zh-CN-YunyangNeural` — steady male, formal/news-like narration.
- `zh-CN-YunjianNeural` — thicker male voice, often better for wuxia/story narration.
- `zh-CN-XiaoxiaoNeural` — clear female voice, useful for female-character reference or softer narration.

Minimal sample script:
```python
import asyncio
from pathlib import Path
import edge_tts

book = Path('/path/to/book-project')
out = book / 'audiobook' / 'samples'
out.mkdir(parents=True, exist_ok=True)
text = (book / 'chapters/ch01_final.md').read_text(encoding='utf-8')
text = '\n'.join(line.strip().lstrip('#').strip() for line in text.splitlines() if line.strip())[:750]
text = text.replace('“','「').replace('”','」').replace('—','，').replace('……','。')

voices = [
    ('01_yunyang_male_news', 'zh-CN-YunyangNeural'),
    ('02_yunjian_male_story', 'zh-CN-YunjianNeural'),
    ('03_xiaoxiao_female_clear', 'zh-CN-XiaoxiaoNeural'),
]

async def main():
    for name, voice in voices:
        fn = out / f'{name}.mp3'
        await edge_tts.Communicate(text=text, voice=voice, rate='-8%', volume='+0%').save(str(fn))
        print(fn, fn.stat().st_size)

asyncio.run(main())
```

## Open-source options for higher-control audiobook production

- **Microsoft VibeVoice** (`microsoft/VibeVoice`, MIT): likely the Microsoft open-source TTS the user is asking about. More relevant than old SpeechT5 for long-form audiobook work. VibeVoice-TTS supports long-form, multi-speaker generation and English/Chinese, but Chinese can have occasional pronunciation instability; official notes recommend English punctuation even for Chinese text. Needs GPU/cloud for practical use.
- **GPT-SoVITS**: strong Chinese ecosystem, zero-shot/few-shot voice cloning, WebUI, good for a custom narrator voice. Needs reference audio and preferably GPU.
- **F5-TTS**: open-source, good naturalness and voice cloning for Chinese/English. Needs chunking and GPU for smooth long-form production.
- **SpeechT5** (`microsoft/SpeechT5`, MIT): official Microsoft research repo but older; not recommended as the main audiobook path.
- **Piper/Kokoro/Coqui/Chatterbox/Zonos**: useful to evaluate, but for Chinese wuxia long-form the practical first pass should remain Edge TTS, then GPT-SoVITS/F5-TTS/VibeVoice.

## Full audiobook pipeline shape

Target directory:
```text
<project-root>/audiobook/
  samples/      # voice audition MP3s
  chunks/       # per-chapter chunk audio
  chapters/     # merged chapter MP3s
  manifest.json # voice, rate, chunk text, output paths
```

Production steps:
1. Read `chapters/chXX_final.md` files.
2. Strip Markdown headings markers but keep chapter titles.
3. Normalize punctuation and split into manageable chunks (roughly 500-1200 Chinese characters for Edge TTS; shorter if pronunciation/pauses drift).
4. Generate per-chunk audio.
5. Merge with ffmpeg into per-chapter MP3/M4A, then optionally M4B.
6. Add Dashboard audio links/player for each chapter if needed.

## Environment preflight

Before generating audio, verify the actual environment rather than assuming tools are installed:

- import or invoke the selected TTS engine
- check whether `ffmpeg` is available before planning audio merges
- check GPU availability before selecting local neural models
- confirm internet access when using online voices
- record the selected voice, rate, engine, and dependency versions in the audiobook manifest

If local GPU or merge tools are unavailable, generate short voice samples first and use a suitable external compute environment only when the user approves it.
