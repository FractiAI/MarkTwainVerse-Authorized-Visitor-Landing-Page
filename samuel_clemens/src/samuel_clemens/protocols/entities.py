"""
Entities - NSPFRP living entity management.

Bridges to the TypeScript naturalSystems.ts entity system.

Entity types (from naturalSystems.ts):
- character: Mark Twain, Tesla, Humboldt
- building: Town Center, Frontier Colony
- landscape: Wilderness Preserve
- system: HHF-AI MRI
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Optional

from samuel_clemens.utils.logging import event_log


class EntityType(Enum):
    """Types of living entities in the verse."""
    CHARACTER = "character"
    BUILDING = "building"
    LANDSCAPE = "landscape"
    SYSTEM = "system"


class EntityMood(Enum):
    """Mood states for entities."""
    DORMANT = "dormant"
    AWAKENING = "awakening"
    ACTIVE = "active"
    THRIVING = "thriving"
    RESTING = "resting"


@dataclass
class EntityState:
    """Current state of a living entity."""
    position: tuple[float, float, float]
    scale: float
    animation: str
    mood: EntityMood
    age_ms: int


@dataclass
class Entity:
    """A living entity in the MarkTwainVerse."""
    id: str
    name: str
    entity_type: EntityType
    state: EntityState
    energy: float
    connections: list[str]
    description: str

    def __str__(self) -> str:
        return f"{self.name} ({self.entity_type.value})"


# Default entities (mirror of naturalSystems.ts livingEntities)
_ENTITIES: dict[str, Entity] = {
    "hero-host-mark-twain": Entity(
        id="hero-host-mark-twain",
        name="Mark Twain",
        entity_type=EntityType.CHARACTER,
        state=EntityState(
            position=(0, 0, 0),
            scale=1.0,
            animation="idle-storytelling",
            mood=EntityMood.THRIVING,
            age_ms=0,
        ),
        energy=0.9,
        connections=["daily-bulletin", "all-communities", "all-expeditions"],
        description="The Hero Host - 24/7 storyteller and guide",
    ),
    "frontier-town-center": Entity(
        id="frontier-town-center",
        name="Frontier Town Center",
        entity_type=EntityType.BUILDING,
        state=EntityState(
            position=(0, 0, 0),
            scale=1.0,
            animation="breathing",
            mood=EntityMood.ACTIVE,
            age_ms=0,
        ),
        energy=0.8,
        connections=["all-communities"],
        description="The beating heart of the frontier",
    ),
    "frontier-colony-district": Entity(
        id="frontier-colony-district",
        name="Frontier Colony",
        entity_type=EntityType.BUILDING,
        state=EntityState(
            position=(-100, 0, 50),
            scale=1.0,
            animation="breathing",
            mood=EntityMood.ACTIVE,
            age_ms=0,
        ),
        energy=0.75,
        connections=["town-center", "expeditions"],
        description="The main residential district",
    ),
    "wilderness-preserve-zone": Entity(
        id="wilderness-preserve-zone",
        name="Wilderness Preserve",
        entity_type=EntityType.LANDSCAPE,
        state=EntityState(
            position=(200, 0, -150),
            scale=1.0,
            animation="wind-sway",
            mood=EntityMood.THRIVING,
            age_ms=0,
        ),
        energy=1.0,
        connections=["eco-expeditions"],
        description="Pristine wilderness - highest natural energy",
    ),
    "hero-host-nikola-tesla": Entity(
        id="hero-host-nikola-tesla",
        name="Nikola Tesla",
        entity_type=EntityType.CHARACTER,
        state=EntityState(
            position=(150, 0, 100),
            scale=1.0,
            animation="idle-teaching",
            mood=EntityMood.THRIVING,
            age_ms=0,
        ),
        energy=0.95,
        connections=["hhf-mri-system", "syntheverse-os", "all-verses"],
        description="Hero Host for Science Discovery Museum",
    ),
    "hhf-ai-mri-system": Entity(
        id="hhf-ai-mri-system",
        name="HHF-AI MRI System",
        entity_type=EntityType.SYSTEM,
        state=EntityState(
            position=(150, 0, 100),
            scale=1.0,
            animation="operating",
            mood=EntityMood.ACTIVE,
            age_ms=0,
        ),
        energy=1.0,
        connections=["tesla-entity", "syntheverse-cloud", "awareness-nodes"],
        description="Operating at 1.420 GHz - perpetual awareness emitter",
    ),
}


def get_entity_state(entity_id: str) -> Optional[Entity]:
    """
    Get the current state of a living entity.
    
    Args:
        entity_id: The entity's unique identifier
        
    Returns:
        Entity if found, None otherwise
    """
    return _ENTITIES.get(entity_id)


def get_all_entities() -> dict[str, Entity]:
    """
    Get all living entities in the verse.
    
    Returns:
        Dictionary of all entities by ID
    """
    return _ENTITIES.copy()


def get_entities_by_type(entity_type: EntityType) -> list[Entity]:
    """
    Get all entities of a specific type.
    
    Args:
        entity_type: The type to filter by
        
    Returns:
        List of matching entities
    """
    return [e for e in _ENTITIES.values() if e.entity_type == entity_type]


def interact_with_entity(entity_id: str) -> Optional[Entity]:
    """
    Interact with an entity (boosts its energy).
    
    Args:
        entity_id: The entity to interact with
        
    Returns:
        Updated entity if found, None otherwise
    """
    entity = _ENTITIES.get(entity_id)
    if entity:
        # Boost energy (capped at 1.0)
        entity.energy = min(1.0, entity.energy + 0.1)
        entity.state.mood = EntityMood.THRIVING
        event_log(f"⚡ Interaction: {entity.name} energy boosted to {entity.energy:.2f}")
        return entity
    return None


def get_hero_hosts() -> list[Entity]:
    """
    Get all Hero Host character entities.
    
    Returns:
        List of Hero Host entities
    """
    return [
        e for e in _ENTITIES.values()
        if e.entity_type == EntityType.CHARACTER and "hero-host" in e.id
    ]


def get_total_energy() -> float:
    """
    Calculate total energy across all entities.
    
    Returns:
        Average energy level (0.0-1.0)
    """
    if not _ENTITIES:
        return 0.0
    return sum(e.energy for e in _ENTITIES.values()) / len(_ENTITIES)


def get_dominant_mood() -> EntityMood:
    """
    Determine the dominant mood across all entities.
    
    Returns:
        The most common mood
    """
    mood_counts: dict[EntityMood, int] = {}
    for entity in _ENTITIES.values():
        mood = entity.state.mood
        mood_counts[mood] = mood_counts.get(mood, 0) + 1
    
    if mood_counts:
        return max(mood_counts, key=lambda m: mood_counts[m])
    return EntityMood.ACTIVE
