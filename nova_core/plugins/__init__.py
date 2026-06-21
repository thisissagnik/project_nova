from .base import BasePlugin
from .memory import MemoryPlugin


class PluginManager:
    def __init__(self, event_bus):
        self.event_bus = event_bus
        self.plugins: dict[str, BasePlugin] = {}

    def register_plugin(self, name: str, plugin: BasePlugin) -> None:
        self.plugins[name] = plugin
        self.event_bus.publish("plugin.registered", {"name": name})

    async def start_all(self) -> None:
        for name, plugin in self.plugins.items():
            await plugin.start()
            self.event_bus.publish("plugin.started", {"name": name})

    async def stop_all(self) -> None:
        for name, plugin in self.plugins.items():
            await plugin.stop()
            self.event_bus.publish("plugin.stopped", {"name": name})
