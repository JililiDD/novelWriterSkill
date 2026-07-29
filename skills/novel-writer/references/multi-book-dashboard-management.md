# Multi-book Dashboard Management Notes

Use these patterns when maintaining a project-level dashboard that discovers and serves multiple novel directories.

## Problem
When many novel projects exist, the top "选择书籍" list consumes too much vertical space on mobile. The user also wants a way to remove old novels from the dashboard list.

## Implemented pattern
- Make the book-selector panel collapsible with a `收起 / 展开` button.
- Persist collapse state in browser `localStorage` (e.g. `novelBooksCollapsed`) so mobile users do not need to collapse it every visit.
- Add a per-book `删除` button in the book list.
- Deletion must be safe by default: move the book directory to `ROOT/.deleted_books/<book_name>_<timestamp>` instead of permanently deleting.
- Exclude `.deleted_books` from dashboard discovery so removed books disappear from `/api/books`.
- Use `POST /api/delete-book` with JSON `{ "id": "<book-id>" }`, and resolve ids through the same `safe_id(book_dir)` map used by `/read/...`.
- Validate deletion scope: only allow directories under dashboard `ROOT`, never `ROOT` itself.

## Verification checklist
1. Syntax check the actual dashboard entrypoint, for example: `python3 -m py_compile <dashboard-path>.py`.
2. Restart the dashboard bound to `0.0.0.0:8420`.
3. Check home HTML includes `toggleBookPanel`, `deleteBook`, and `book-panel`.
4. Check `/api/books` returns active books and no `.deleted_books` paths.
5. Browser-test: click `收起`, confirm the book list hides and button becomes `展开`.
6. Create a temporary test book directory, confirm it appears in `/api/books`, call `POST /api/delete-book`, then confirm it moved under `.deleted_books` and disappeared from `/api/books`.

## Notes
This is a dashboard UX feature, not a novel-generation step. Use deterministic file operations and verify the actual application after each change.