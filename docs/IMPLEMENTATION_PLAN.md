# Nova Implementation Plan

## Overview

Nova is a Python-based AI runtime platform with a core runtime foundation, a plugin architecture, a model provider abstraction, and the Nova Rover application as the first user-facing experience.

### Scope for the next 3 months
- Month 1: Core runtime foundation and runtime scaffolding
- Month 2: Parallel Nova Rover prototype and Agentic Layer foundations
- Month 3: Identity, reflection, persistence, and stabilization

## Project assumptions
- Azure AI Foundry is the initial model provider
- Azure SQL is the persistence target from the start
- Azure AD is the authentication strategy from day one
- Raspberry Pi hardware support is planned after the Rover app is functional

---

## Month 1 (Weeks 1–4)

### Week 1
- Lock architecture and plugin contract
- Centralize project docs under `docs/project_docs/`
- Scaffold runtime service with FastAPI
- Create initial repository structure, requirements, and Dockerfile
- Fix CI to enforce linting and tests

### Week 2
- Implement Plugin Manager and lifecycle interfaces
- Implement Event Bus abstractions and the runtime startup flow
- Implement Model Provider abstraction and Azure AI Foundry stub
- Add basic unit tests for runtime components

### Week 3
- Build core runtime integration and plugin registration
- Add a health/readiness API and runtime status endpoint
- Add first plugin stubs: Memory plugin, Speech plugin, Vision plugin
- Continue documenting design decisions

### Week 4
- Start Nova Rover prototype architecture in parallel
- Define Rover application boundaries and API surface
- Create a minimal Rover runtime entrypoint
- Add simple Azure SQL persistence design notes and schema concept

---

## Month 2 (Weeks 5–8)

### Week 5
- Implement Agentic Layer foundations: Goal Manager, Task Manager, Workflow Engine
- Connect Rover prototype to core runtime via plugin and event abstractions
- Add end-to-end exercise for a simple Rover task

### Week 6
- Add Azure SQL persistence integration for runtime state and agent context
- Add Azure AD authentication scaffolding to the web service
- Refine plugin lifecycle and ensure plugins can be loaded and unloaded cleanly

### Week 7
- Continue Rover prototype development: task execution, action orchestration, sensor event flow
- Expand model provider support and injector patterns for plugins
- Add more test coverage for runtime and Rover flows

### Week 8
- Stabilize core runtime APIs and Rover app skeleton
- Validate the workflow from command intake to action planning
- Prepare a Raspberry Pi readiness design plan for the next phase

---

## Month 3 (Weeks 9–12)

### Week 9
- Implement Identity Engine MVP and persistent identity context
- Implement Reflection Engine for runtime insight and learning traces
- Build planner/action engine stubs for goal-driven behavior

### Week 10
- Refine Nova Rover use cases with plugin-driven actions
- Add integration tests and CI validation for core + Rover paths
- Improve architecture documentation and ADRs

### Week 11
- Add more robust persistence and runtime recovery behavior
- Harden Azure AD and Azure SQL integration designs
- Finalize Docker build and runtime deployment patterns

### Week 12
- Stabilize codebase, polish docs, and prepare next-phase roadmap
- Review core/runtime/plugin APIs
- Create a Raspberry Pi and local model support transition plan

---

## Execution notes
- This is a side project; focus on a high-value incremental delivery cadence.
- We can deliver core runtime capabilities in Month 1 and a working Rover prototype by Month 2.
- I will keep the plan updated in `docs/IMPLEMENTATION_PLAN.md` and `docs/PROJECT_CONTEXT.md`.
