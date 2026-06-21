# Architecture Decision Records

## ADR-001

Nova is a platform, not a robot.

Reason:
The robot is the first application.

## ADR-002

Everything is a plugin.

Reason:
Extensibility and community contributions.

## ADR-003

Movement is a plugin.

Reason:
Movement is an action, not intelligence.

## ADR-004

Identity and Memory belong to the core runtime.

Reason:
Persistent behavior requires continuity.

## ADR-005

Agentic capabilities belong to the Agentic Layer.

Reason:
Separates cognition from platform services.

## ADR-006

Nova may propose code changes but cannot directly modify production code.

Reason:
Safety and maintainability.

## ADR-007

Azure AI Foundry is the first model provider implementation.

Reason:
Rapid development and existing Azure credits.

## ADR-008

Local model support is a strategic future goal.

Reason:
Offline operation and hardware independence.
