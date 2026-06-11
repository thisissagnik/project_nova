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
