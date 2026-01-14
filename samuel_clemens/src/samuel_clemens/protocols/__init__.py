"""
Protocols module - NSPFRP bridges for MarkTwainVerse.

Interfaces with the TypeScript Natural Systems Protocol engine.

SOURCE FILES:
- protocols/naturalSystems.ts - Core NSPFRP definitions
- lib/marktwainverse/twainPersonality.ts - Twain personality engine
- lib/marktwainverse/autoTourEngine.ts - Auto-tour functionality
- lib/shared/multimediaEngine.ts - Multimedia generation
"""

from samuel_clemens.protocols.cycles import (
    get_day_phase,
    get_season_phase,
    get_breathing_pulse,
    get_expedition_day,
    get_all_cycles,
)
from samuel_clemens.protocols.entities import (
    Entity,
    EntityType,
    EntityMood,
    EntityState,
    get_entity_state,
    get_all_entities,
    interact_with_entity,
)
from samuel_clemens.protocols.events import (
    Event,
    check_events,
    subscribe_to_events,
    get_active_events,
)
from samuel_clemens.protocols.bridge import (
    # Protocol paths
    PROTOCOL_PATHS,
    # Natural cycles from naturalSystems.ts
    NaturalCycle,
    CycleEffect,
    CycleType,
    NATURAL_CYCLES,
    # Living entities from naturalSystems.ts  
    LivingEntity,
    Behavior,
    BehaviorTrigger,
    WorldContext,
    LIVING_ENTITIES,
    # Twain personality from twainPersonality.ts
    TwainResponse,
    TwainEmotion,
    TwainGesture,
    TWAIN_PATTERNS,
    # Auto-tour from autoTourEngine.ts
    TourStage,
    TourState,
    # Utilities
    get_project_root,
    get_protocol_path,
    load_protocol_source,
    compute_world_context,
)

__all__ = [
    # Cycles
    "get_day_phase",
    "get_season_phase",
    "get_breathing_pulse",
    "get_expedition_day",
    "get_all_cycles",
    # Entities
    "Entity",
    "EntityType",
    "EntityMood",
    "EntityState",
    "get_entity_state",
    "get_all_entities",
    "interact_with_entity",
    # Events
    "Event",
    "check_events",
    "subscribe_to_events",
    "get_active_events",
    # Bridge - Protocol Paths
    "PROTOCOL_PATHS",
    # Bridge - Natural Cycles (from naturalSystems.ts)
    "NaturalCycle",
    "CycleEffect",
    "CycleType",
    "NATURAL_CYCLES",
    # Bridge - Living Entities (from naturalSystems.ts)
    "LivingEntity",
    "Behavior",
    "BehaviorTrigger",
    "WorldContext",
    "LIVING_ENTITIES",
    # Bridge - Twain Personality (from twainPersonality.ts)
    "TwainResponse",
    "TwainEmotion",
    "TwainGesture",
    "TWAIN_PATTERNS",
    # Bridge - Auto-Tour (from autoTourEngine.ts)
    "TourStage",
    "TourState",
    # Bridge - Utilities
    "get_project_root",
    "get_protocol_path",
    "load_protocol_source",
    "compute_world_context",
]

