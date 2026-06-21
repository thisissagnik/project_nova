from fastapi import FastAPI

from .config import settings
from .events import EventBus
from .model_provider.azure_ai_foundry import AzureAIProvider
from .plugins import MemoryPlugin, PluginManager

app = FastAPI(title="Nova Core", version="0.1.0")
event_bus = EventBus()
plugin_manager = PluginManager(event_bus=event_bus)
model_provider = AzureAIProvider(settings=settings)

@app.on_event("startup")
async def startup_event():
    plugin_manager.register_plugin("memory", MemoryPlugin(event_bus=event_bus))
    await plugin_manager.start_all()

@app.on_event("shutdown")
async def shutdown_event():
    await plugin_manager.stop_all()

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/status")
async def status():
    return {
        "status": "ok",
        "plugins": list(plugin_manager.plugins.keys()),
        "model_provider": model_provider.name,
    }
