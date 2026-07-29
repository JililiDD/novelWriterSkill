# Mobile-Friendly Markdown Dashboard Logic

To make Markdown files readable on mobile devices within the dashboard server, wrap the content in the following HTML template:

```python
html_content = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <style>
        body {{
            background: #0d1117;
            color: #e6edf3;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Noto Sans SC", sans-serif;
            line-height: 1.8;
            padding: 20px;
            max-width: 800px;
            margin: 0 auto;
            font-size: 19px;
        }}
        pre {{
            white-space: pre-wrap;
            word-wrap: break-word;
            background: transparent;
            border: none;
        }}
        @media (max-width: 600px) {{
            body {{ padding: 15px; font-size: 18px; line-height: 1.7; }}
        }}
    </style>
</head>
<body>
    <div class="content"><pre>{content}</pre></div>
</body>
</html>"""
```

### Process Management
Always check for zombie processes on port 8420:
`lsof -ti:8420 | xargs kill -9`

### Multi-book dashboard UX patterns learned
- If the dashboard lists many novels, make the book shelf collapsible and persist the state in `localStorage` so mobile users can keep the chapter panel visible.
- Use soft delete for book removal: move book directories to `ROOT/.deleted_books/<book>_<timestamp>` rather than deleting immediately.
- Add a visible recycle-bin panel backed by `/api/deleted-books`, with `恢复` and `永久删除` actions. Permanent deletion should be limited to paths under `.deleted_books` and should require a second browser confirmation.
- For story outline tabs, expose a finalized full-book outline first, e.g. `state/finalized_plot_outline.md` or `state/approved_plot_outline.md`, before incremental `state/story_outline.md`. The user expects the original confirmed 10-chapter plan to be visible, not only chapter-by-chapter updates appended during generation.
- Render `.md` documents as real Markdown HTML instead of wrapping escaped text in `<pre>`. If Python `markdown` is available, use extensions `extra`, `sane_lists`, `toc`, and `nl2br`, plus mobile-friendly CSS for headings, lists, blockquotes, code fences, and tables. Keep `.yaml/.txt` as escaped `<pre>`.
