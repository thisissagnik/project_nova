# Project Docs — Nova

This folder contains the canonical project context files for Nova.

## Purpose

These files are the primary source of truth for the assistant and the project planning process.

## Canonical files

- `AI_CONTEXT.md`
- `ARCHITECTURE.md`
- `DECISIONS.md`
- `PROJECT_STATUS.md`
- `ROADMAP.md`
- `nova_manifest.yaml`

## Notes

- The assistant will read and update these files for project planning and implementation context.
- `docs/PROJECT_CONTEXT.md` is the broader project context document, while `docs/project_docs/` holds the core architecture and status artifacts.
- If this folder is moved or renamed, update `.github/prompts/nova-context.prompt.md` to keep context alignment.
