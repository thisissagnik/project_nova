from abc import ABC, abstractmethod
from typing import Any


class BasePlugin(ABC):
    def __init__(self, event_bus: Any) -> None:
        self.event_bus = event_bus

    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    async def start(self) -> None:
        raise NotImplementedError

    @abstractmethod
    async def stop(self) -> None:
        raise NotImplementedError

    def emit_event(self, event_name: str, payload: Any) -> None:
        self.event_bus.publish(event_name, payload)
