# Project Status — Nova

Last updated: 2026-06-21

## High-level decisions (locked)
- Language: Python
- Model provider (initial): Azure AI Foundry
- Persistence: Azure SQL DB (managed)
- Auth: Azure AD + Managed Identity
- Deployment: Dockerized web service; CI/CD via GitHub Actions; target Raspberry Pi later via multi-arch images

## Current focus
- Build: Nova Core (platform) first; Nova Rover later as an application on top of the core

## Short-term todo (tracked in the agent todo list)
- Confirm scope & requirements — completed
- Define plugin contract and lifecycle — in-progress (drafted)
- Design core APIs and data flows — in-progress
- Implement Plugin Manager — in-progress (basic implementation added)
- Implement Event Bus — completed
- Implement Model Provider abstraction — in-progress (Azure stub added)
- Add unit tests and CI — completed

## Where project context and decisions live
- Primary docs: `docs/project_docs/ARCHITECTURE.md`, `docs/project_docs/ROADMAP.md`, `docs/project_docs/AI_CONTEXT.md`, `docs/project_docs/DECISIONS.md`
- I will maintain an evolving project context file at `docs/PROJECT_CONTEXT.md` and keep this `docs/project_docs/PROJECT_STATUS.md` up to date.
- Architecture decisions / ADRs continue in `docs/project_docs/DECISIONS.md`.

## Next immediate actions
1. Formalize plugin contract into `docs/project_docs/ARCHITECTURE.md` and `docs/PROJECT_CONTEXT.md`
2. Harden the `PluginManager` and `BasePlugin` interface and add tests
3. Begin Nova Rover prototype skeleton (parallel to core hardening)
4. Design Azure SQL persistence schema and integration plan
5. Add Azure AD auth scaffolding and environment configuration

If any of the above content should be stored elsewhere, tell me where and I will move it.
