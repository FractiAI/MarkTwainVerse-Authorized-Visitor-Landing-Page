"""
Events - NSPFRP autonomous event handling.

Bridges to the TypeScript naturalSystems.ts event system.
"""

from __future__ import annotations

import time
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Callable, Optional

from samuel_clemens.protocols.cycles import get_day_phase
from samuel_clemens.utils.logging import event_log


class EventType(Enum):
    """Types of autonomous events."""
    STORY = "story"
    ANNOUNCEMENT = "announcement"
    SPECIAL_OFFER = "special-offer"
    COMMUNITY_EVENT = "community-event"
    EXPEDITION_DEPARTURE = "expedition-departure"


@dataclass
class EventContent:
    """Content payload for an event."""
    title: str
    message: str
    from_host: Optional[str] = None
    data: Optional[dict[str, Any]] = None


@dataclass
class Event:
    """An autonomous event in the verse."""
    id: str
    name: str
    event_type: EventType
    content: EventContent
    duration_ms: int
    triggered_at: float = field(default_factory=time.time)

    def is_active(self) -> bool:
        """Check if event is still active."""
        elapsed = (time.time() - self.triggered_at) * 1000
        return elapsed < self.duration_ms


# Event definitions (mirror of naturalSystems.ts autonomousEvents)
_EVENT_DEFINITIONS: list[dict[str, Any]] = [
    {
        "id": "morning-greeting",
        "name": "Mark Twain's Morning Greeting",
        "trigger_phase": (0.24, 0.26),  # Dawn
        "cooldown_ms": 120000,
        "event_type": EventType.STORY,
        "content": {
            "title": "Good morning, frontier friends!",
            "message": "Well now, looks like the sun's come up on another fine day in the Syntheverse. Let me tell you what's happening today...",
            "from_host": "Mark Twain",
        },
        "duration_ms": 5000,
    },
    {
        "id": "expedition-departure",
        "name": "Expedition Group Departing",
        "trigger_phase": (0.30, 0.32),  # Morning
        "cooldown_ms": 120000,
        "event_type": EventType.EXPEDITION_DEPARTURE,
        "content": {
            "title": "Expedition Departing",
            "message": "A group is heading out to Crystal Lake for the Morning Catch Adventure!",
            "from_host": None,
        },
        "duration_ms": 3000,
    },
    {
        "id": "evening-fireside",
        "name": "Fireside Tales with Mark Twain",
        "trigger_phase": (0.78, 0.82),  # Evening
        "cooldown_ms": 120000,
        "event_type": EventType.STORY,
        "content": {
            "title": "Fireside Tales - Evening Gathering",
            "message": "The fire's crackling, the stars are coming out, and I've got stories to tell. Gather 'round, friends!",
            "from_host": "Mark Twain",
        },
        "duration_ms": 8000,
    },
    {
        "id": "weather-change",
        "name": "Weather Pattern Shift",
        "trigger_phase": None,  # Random trigger
        "random_chance": 0.05,
        "cooldown_ms": 180000,
        "event_type": EventType.ANNOUNCEMENT,
        "content": {
            "title": "Weather Shifting",
            "message": "A frontier storm's rolling in from the west. Beautiful sight from the Alpine Heights!",
            "from_host": None,
        },
        "duration_ms": 30000,
    },
]

# Event state tracking
_last_triggered: dict[str, float] = {}
_active_events: list[Event] = []
_subscribers: dict[EventType, list[Callable[[Event], None]]] = {}


def check_events(visitor_count: int = 1) -> list[Event]:
    """
    Check for and trigger autonomous events.
    
    Args:
        visitor_count: Current number of visitors (affects some triggers)
        
    Returns:
        List of newly triggered events
    """
    now = time.time()
    day_phase = get_day_phase()
    new_events: list[Event] = []
    
    for event_def in _EVENT_DEFINITIONS:
        event_id = event_def["id"]
        
        # Check cooldown
        last = _last_triggered.get(event_id, 0)
        cooldown = event_def["cooldown_ms"] / 1000  # Convert to seconds
        if now - last < cooldown:
            continue
        
        # Check trigger conditions
        should_trigger = False
        
        # Phase-based trigger
        trigger_phase = event_def.get("trigger_phase")
        if trigger_phase:
            phase_min, phase_max = trigger_phase
            if phase_min <= day_phase <= phase_max:
                should_trigger = True
        
        # Random trigger
        random_chance = event_def.get("random_chance")
        if random_chance:
            import random
            if random.random() < random_chance:
                should_trigger = True
        
        if should_trigger:
            content = EventContent(
                title=event_def["content"]["title"],
                message=event_def["content"]["message"],
                from_host=event_def["content"].get("from_host"),
            )
            
            event = Event(
                id=event_id,
                name=event_def["name"],
                event_type=event_def["event_type"],
                content=content,
                duration_ms=event_def["duration_ms"],
                triggered_at=now,
            )
            
            _last_triggered[event_id] = now
            _active_events.append(event)
            new_events.append(event)
            
            event_log(f"🎭 {event.name}")
            
            # Notify subscribers
            _notify_subscribers(event)
    
    # Clean up expired events
    _active_events[:] = [e for e in _active_events if e.is_active()]
    
    return new_events


def subscribe_to_events(
    event_type: EventType,
    callback: Callable[[Event], None],
) -> None:
    """
    Subscribe to events of a specific type.
    
    Args:
        event_type: Type of events to subscribe to
        callback: Function to call when event triggers
    """
    if event_type not in _subscribers:
        _subscribers[event_type] = []
    _subscribers[event_type].append(callback)


def unsubscribe_from_events(
    event_type: EventType,
    callback: Callable[[Event], None],
) -> None:
    """
    Unsubscribe from events.
    
    Args:
        event_type: Type of events to unsubscribe from
        callback: The callback to remove
    """
    if event_type in _subscribers:
        _subscribers[event_type] = [
            cb for cb in _subscribers[event_type] if cb != callback
        ]


def _notify_subscribers(event: Event) -> None:
    """Notify all subscribers of an event."""
    callbacks = _subscribers.get(event.event_type, [])
    for callback in callbacks:
        try:
            callback(event)
        except Exception as e:
            event_log(f"⚠️ Subscriber error: {e}")


def get_active_events() -> list[Event]:
    """
    Get all currently active events.
    
    Returns:
        List of active events
    """
    return [e for e in _active_events if e.is_active()]


def trigger_event(event_id: str) -> Optional[Event]:
    """
    Manually trigger a specific event.
    
    Args:
        event_id: ID of the event to trigger
        
    Returns:
        The triggered Event, or None if not found
    """
    for event_def in _EVENT_DEFINITIONS:
        if event_def["id"] == event_id:
            content = EventContent(
                title=event_def["content"]["title"],
                message=event_def["content"]["message"],
                from_host=event_def["content"].get("from_host"),
            )
            
            event = Event(
                id=event_id,
                name=event_def["name"],
                event_type=event_def["event_type"],
                content=content,
                duration_ms=event_def["duration_ms"],
            )
            
            _active_events.append(event)
            event_log(f"🎭 Manual trigger: {event.name}")
            _notify_subscribers(event)
            return event
    
    return None


def clear_events() -> None:
    """Clear all active events and cooldowns."""
    global _active_events, _last_triggered
    _active_events = []
    _last_triggered = {}
