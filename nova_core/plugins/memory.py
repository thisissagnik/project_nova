from .base import BasePlugin


class MemoryPlugin(BasePlugin):
    @property
    def name(self) -> str:
        return "memory"

    async def start(self) -> None:
        self.emit_event("memory.started", {"plugin": self.name})

    async def stop(self) -> None:
        self.emit_event("memory.stopped", {"plugin": self.name})
