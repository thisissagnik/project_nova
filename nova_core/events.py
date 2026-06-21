from typing import Any, Callable, Dict, List


EventHandler = Callable[[str, Any], None]


class EventBus:
    def __init__(self) -> None:
        self._handlers: Dict[str, List[EventHandler]] = {}

    def subscribe(self, event_name: str, handler: EventHandler) -> None:
        self._handlers.setdefault(event_name, []).append(handler)

    def publish(self, event_name: str, payload: Any) -> None:
        for handler in self._handlers.get(event_name, []):
            handler(event_name, payload)
