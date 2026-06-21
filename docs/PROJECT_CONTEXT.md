# Project Context — Nova

This document captures the project's current technical context and immediate implementation plan.

## Mission
Build an open-source AI runtime platform (Nova) that is model- and hardware-agnostic. Nova Rover is the first application running on top of the platform.

## Locked technology choices (as of 2026-06-11)
- Language: Python (server runtime)
- Web framework: FastAPI (scaffold planned)
- Containerization: Docker with multi-arch builds (buildx) for future Raspberry Pi deployment
- CI/CD: GitHub Actions (basic workflow scaffolded in `.github/workflows/ci.yml`)
- Model provider: Azure AI Foundry initially, with a Model Provider abstraction for future OpenAI/local adapters
- Persistence: Azure SQL DB (managed) for long-term storage; prototypes may use SQLite
- Auth: Azure AD + Managed Identity for service authentication

## Architectural intent
- Keep Nova Core model- and hardware-agnostic.
- Implement all capabilities as plugins with a clean plugin contract.
- Agentic capabilities live in the Agentic Layer (Goal Manager, Task Manager, Workflow Engine, Agent Runtime).
- Core runtime (Identity, Memory, Planner, Action, Reflection, Event Bus, Plugin Manager, Model Provider) is the primary deliverable.

## Immediate implementation plan (next 2 weeks)
1. Define a minimal Plugin Contract and lifecycle (registration, start/stop, capabilities metadata, events)
2. Design core API surfaces for Event Bus, Plugin Manager, and Model Provider
3. Scaffold a minimal FastAPI app with a single health endpoint and a stub Model Provider adapter for Azure AI Foundry
4. Add Dockerfile and GitHub Actions to build and lint the service

## What I need from you
- Azure subscription details when ready (resource naming, or I can propose a namespaced naming scheme)
- Permission to add basic CI workflow and scaffold; secrets for publish will be placeholders until you add them to GitHub repository settings
- Any existing ADRs or constraints not yet in `docs/project_docs/DECISIONS.md` to capture

## Notes on storage of project context
- I will keep evolving this file and `docs/project_docs/PROJECT_STATUS.md` as authoritative snapshots. Major ADRs remain in `docs/project_docs/DECISIONS.md`.
