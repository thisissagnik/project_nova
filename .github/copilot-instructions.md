# Nova Project Instructions

Nova is an open-source AI runtime platform for building persistent, multimodal, agentic companions and autonomous systems.

## Vision

Nova is NOT a robot.

Nova Rover is the first application built on top of Nova.

The platform should support:

- AI Companions
- Enterprise Agents
- Factory Intelligence
- Creator Intelligence
- Developer Agents

## Architecture

Applications
↓
Agentic Layer
↓
Nova Core
↓
Plugins
↓
Models and Hardware

## Nova Core

- Identity Engine
- Memory Engine
- Reflection Engine
- Planner Engine
- Action Engine
- Event Bus
- Plugin Manager
- Model Provider

## Rules

- Everything is a plugin.
- Models must be abstracted.
- Hardware must be abstracted.
- Agents run on top of Nova Core.
- Applications run on top of agents.
- Human approval required for code modifications.

## Current Phase

Phase 1

Building:

- Plugin Interface
- Plugin Manager
- Event Bus
- Base Agent
- Model Provider

Not Started:

- Speech
- Vision
- Memory