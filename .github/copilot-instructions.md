<!--
Short, focused Copilot instructions for contributors and AI agents.
Generated/updated: 2025-11-02 (merged & condensed)
-->

# Quick project snapshot
- Purpose: a content-first repo of AI-generated teaching materials (Markdown + LiaScript). Primary folders: `lessons/`, `prompts/`, and `exercises/`.
- No build pipeline—lessons are edited and previewed as Markdown/LiaScript.

# What matters for an AI agent (concise)
- Start files: `prompts/teaching-guide.md` (style rules) and `lessons/lesson-template.md` (structure). Follow both when authoring lessons.
- Lessons: place in `lessons/*.md`. Preserve top HTML metadata (author, date, version, language). Example: see `lessons/03_Data_Science_Basics.md`.
- Exercises: put runnable code in `exercises/*.py` and reference them from lessons instead of embedding long scripts.

# Project-specific patterns & examples
- LiaScript: interactive markers like `--{{0}}--` are used to split blocks—keep them for interactive lessons.
- Template placeholders: remove/replace `{{LESSON_TITLE}}` when instantiating templates (`lessons/lesson-template.md`).
- Avoid stray generator artifacts: remove chat-mode fences (lines containing ````chatmode````) and doubled code-fence blocks.

# Developer workflows & common commands
- Preview Markdown in-editor for formatting. For LiaScript interactive testing use a LiaScript-compatible viewer (external).
- Run python exercises locally (PowerShell):
  powershell: python .\exercises\<example>.py
- Add `requirements.txt` only when adding third-party libraries; document install steps in the lesson (do not assume package managers).

# Integration points & constraints
- Consumers: LiaScript viewer or any Markdown renderer. No web server or CI detected—treat outputs as static content.
- If you add library code (scikit-learn, pandas), include `requirements.txt` and a short `run.ps1` under `tools/` or docs in the lesson.

# Authoring rules (actionable)
- Objectives: 3–5 short items starting with an action verb (explain, identify, apply).
- Code examples: small, self-contained, with inline comments and a one-line "what this teaches" note.
- Metadata: keep or add `author: Masub Makhdoom` when appropriate; do not remove existing metadata.

# If unclear, ask the maintainer
- Ask which viewer/LMS will consume the lessons (LiaScript host, SCORM export, static site) — this changes required metadata.

---
If you'd like, I can (A) commit this condensed file into `.github/` now, or (B) run a repo scan and auto-fix obvious issues (remove chat-mode fences, ensure metadata). Which do you prefer?
<!--
Short, focused Copilot instructions for contributors and AI coding agents.
Generated/updated: 2025-11-02
-->

# Project snapshot (big picture)
- Purpose: this repo is a collection of AI-generated teaching materials (Markdown + LiaScript). Lessons live under `lessons/`, prompts under `prompts/`, and small runnable examples under `exercises/`.
- The repo is *content-first* (no build system). Treat each lesson file as the primary source used for delivery (LiaScript/Markdown viewers, or static site generators).

# Key files and patterns (quick reference)
- `prompts/teaching-guide.md` — authoritative style + output rules (3–5 learning objectives, simple language, code comment rule: include "what this teaches"). Use this when generating lessons.
- `lessons/lesson-template.md` — canonical lesson structure. New lessons should match this layout: Title, Objectives, Introduction, Main Content (numbered), Guided Activity, Quiz, Summary.
- `lessons/*.md` — content lessons. LiaScript lessons include metadata headers (HTML comment block) and LiaScript markers like `--{{0}}--` for interactive breaks.
- `exercises/*.py` — runnable examples referenced by lessons (e.g., `exercises/knn_simple.py`). Keep examples small, dependency-free where possible.
- `README.md` — high-level project purpose and links to lessons.

# Conventions for generated lessons
- Objectives: 3–5 items, start with action verbs (explain, identify, apply, reflect).
- Language: simple, beginner-friendly sentences. Define new technical terms the first time they appear (dataset, feature, label, inference).
- Code blocks: include inline comments and a short "what this teaches" note. Prefer small, self-contained examples in `exercises/` instead of long scripts inside lessons.
- LiaScript metadata: when producing interactive lessons, include a top HTML comment with `author`, `date`, `version`, `language`, and an optional `comment` field (see `lessons/03_Data_Science_Basics.md`).

# How to be productive (for AI agents)
- When editing or generating a lesson, open `prompts/teaching-guide.md` and `lessons/lesson-template.md` first — follow both strictly.
- Preserve existing author metadata when updating a lesson; add `author: Masub Makhdoom` where appropriate.
- Prefer creating or updating `exercises/*.py` for runnable code examples rather than embedding long scripts into lesson Markdown.
- Remove stray chat-mode fences (e.g., lines like ````chatmode````) — lessons must be valid Markdown/LiaScript.

# Developer workflows & debugging
- There is no central build or CI in this repo. To preview lessons:
  - Use your editor's Markdown preview to check formatting.
  - For LiaScript interactive testing, open lessons in a LiaScript-compatible viewer (external to this repo).
- To run exercises locally (Windows PowerShell):
  ```powershell
  python exercises\knn_simple.py
  ```
  Keep examples dependency-free or add `requirements.txt` only when adding a library example; document install steps in the lesson.

# Integration points & external dependencies
- External viewers: LiaScript or any Markdown renderer are the primary consumers. No web server or package manifests found.
- If adding scikit-learn or other libs, include `requirements.txt` at repo root and reference installation steps in the lesson (do not assume a system package manager).

# Patterns and gotchas observed in this repo
- Some generated files previously contained stray chat-mode fences and doubled code fences; remove these when finalizing content.
- Template placeholders: `{{LESSON_TITLE}}` appears in `lessons/lesson-template.md` — replace or remove when instantiating a lesson.
- LiaScript break markers like `--{{0}}--` are used to split interactive blocks; keep them if generating interactive content.

# Merge guidance (if `.github/copilot-instructions.md` already exists)
- Preserve any project-specific instructions already present. Append or replace only sections that are stale. Keep this file concise (20–50 lines).

# Example edits an AI agent might do
- Create `lessons/topic-name.md` by copying `lessons/lesson-template.md`, replacing `{{LESSON_TITLE}}`, filling Objectives (3–5), Introduction, Main Content, Guided Activity and Quiz per `prompts/teaching-guide.md`.
- Add a small runnable example to `exercises/` and reference it from the lesson using a relative path.
- Ensure metadata header is present for LiaScript lessons; remove any leftover chat-mode markers.

# If something is unclear — ask the maintainer
- Ask which viewers or LMS this will be used with (LiaScript web host, exported SCORM, or static site) — that affects required metadata.
- Ask whether adding a `requirements.txt` and small `Makefile` or `run.ps1` is acceptable for exercises needing packages.

---
If you want I can now:
- (A) Add/merge this file into `.github/` (I will do that). 
- (B) Run a quick scan for other pattern deviations and propose automated fixes (remove chat-mode fences, ensure metadata present).
Tell me which next step you prefer.
