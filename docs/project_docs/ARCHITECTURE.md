# Nova Architecture

## Architectural Statement

Nova is a modular AI runtime platform for building persistent, agentic, multimodal companions and autonomous systems.

## High-Level Architecture

Applications
│
├── Nova Rover
├── Creator Intelligence
├── Factory Observer
└── Developer Agent
│
▼
Agentic Layer
│
├── Goal Manager
├── Task Manager
├── Workflow Engine
└── Agent Runtime
│
▼
Nova Core
│
├── Identity Engine
├── Memory Engine
├── Reflection Engine
├── Planner Engine
├── Action Engine
├── Event Bus
├── Plugin Manager
└── Model Provider
│
▼
Plugins
│
├── Speech Plugin
├── Vision Plugin
├── Memory Plugin
├── Movement Plugin
├── Calendar Plugin
└── Enterprise Plugins
│
▼
Models / Hardware
│
├── Azure AI Foundry
├── OpenAI
├── Local Models
├── Raspberry Pi
├── ESP32
└── Sensors

## Design Rules

- Nova Core must never depend on a specific model.
- Nova Core must never depend on a specific hardware platform.
- All capabilities must be implemented as plugins.
- Agents run on top of Nova Core.
- Applications run on top of agents.

## Core Intelligence (mock)

This mock describes the minimal components and data flow for the Core Intelligence stack we will implement first.

- Components:
	- `Identity Engine`: persistent identity, profiles, and persona state.
	- `Memory Engine`: short-term and long-term memory stores, query interfaces, and retention policies.
	- `Planner Engine`: goal decomposition, plan generation, and plan ranking.
	- `Reflection Engine`: runtime telemetry, experience aggregation, and simple update heuristics.
	- `Action Engine`: executes actions via plugins and manages action lifecycle.

- Interaction flow (simplified):
	1. An application or agent issues an intent/goal to the Agentic Layer.
	2. The Planner Engine consults Identity and Memory to generate candidate plans.
	3. The Planner ranks plans and emits a selected plan to the Action Engine.
	4. The Action Engine invokes appropriate plugins (movement, speech, model providers) to execute plan steps.
	5. Execution events are published on the Event Bus and consumed by the Reflection Engine and Memory Engine to update context and learning traces.

- Persistence and models:
	- The Memory Engine persists state to Azure SQL (design to follow) and exposes a lightweight query API.
	- Model calls (Azure AI Foundry) are mediated by the Model Provider abstraction.

This mock is intentionally small and focused: it defines the runtime pieces necessary to deliver goal-driven behavior without coupling to hardware or a specific model API.
