"""
Protocol Bridge - Direct integration with MarkTwainVerse TypeScript protocols.

This module bridges the Python samuel_clemens package with the TypeScript
protocol files in `lib/` and `protocols/` directories, providing Python
equivalents of the NSPFRP (Natural Systems Protocol) data structures.

SOURCE FILES:
- protocols/naturalSystems.ts - Core NSPFRP definitions
- lib/marktwainverse/twainPersonality.ts - Twain personality engine
- lib/marktwainverse/autoTourEngine.ts - Auto-tour functionality
- lib/shared/multimediaEngine.ts - Multimedia generation

"The two most important days in your life are the day you are born and
the day you find out why." — Mark Twain
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime
from typing import Optional, Callable, Any
from pathlib import Path


# =============================================================================
# PROTOCOL PATH CONSTANTS
# =============================================================================

# Relative paths to TypeScript source files from project root
PROTOCOL_PATHS = {
    "natural_systems": "protocols/naturalSystems.ts",
    "twain_personality": "lib/marktwainverse/twainPersonality.ts",
    "auto_tour": "lib/marktwainverse/autoTourEngine.ts",
    "multimedia": "lib/shared/multimediaEngine.ts",
}


# =============================================================================
# NATURAL CYCLES - From naturalSystems.ts lines 60-148
# =============================================================================

class CycleType(Enum):
    """Matches naturalSystems.ts naturalCycles keys."""
    BREATHING = "breathing"
    DAY_NIGHT = "dayNight"
    EXPEDITION = "expeditionCycle"
    SEASONS = "seasons"


@dataclass
class CycleEffect:
    """
    Matches naturalSystems.ts CycleEffect interface (lines 17-21).
    
    interface CycleEffect {
        target: string;
        property: string;
        modulation: (phase: number) => number;
    }
    """
    target: str
    property: str
    modulation: Callable[[float], float]


@dataclass
class NaturalCycle:
    """
    Matches naturalSystems.ts NaturalCycle interface (lines 10-15).
    
    interface NaturalCycle {
        name: string;
        duration: number;
        phase: number;
        effects: CycleEffect[];
    }
    """
    name: str
    duration_ms: int  # milliseconds
    phase: float = 0.0  # 0-1
    effects: list[CycleEffect] = field(default_factory=list)
    
    @property
    def duration_seconds(self) -> float:
        """Duration in seconds."""
        return self.duration_ms / 1000
    
    def update_phase(self, elapsed_ms: int) -> None:
        """Update cycle phase based on elapsed time."""
        self.phase = (self.phase + elapsed_ms / self.duration_ms) % 1.0


# Direct translation of naturalCycles from naturalSystems.ts (lines 60-148)
NATURAL_CYCLES: dict[str, NaturalCycle] = {
    # Fast heartbeat - ambient animation (6 seconds)
    "breathing": NaturalCycle(
        name="Breathing Cycle",
        duration_ms=6000,
        effects=[
            CycleEffect(
                target="living-architecture",
                property="luminosity",
                modulation=lambda phase: 0.8 + math.sin(phase * math.pi * 2) * 0.2,
            ),
            CycleEffect(
                target="landscapes",
                property="scale",
                modulation=lambda phase: 1.0 + math.sin(phase * math.pi * 2) * 0.02,
            ),
        ],
    ),
    
    # Day-night cycle (2 minutes for demo)
    "dayNight": NaturalCycle(
        name="Day-Night Cycle",
        duration_ms=120000,
        effects=[
            CycleEffect(
                target="lighting",
                property="intensity",
                modulation=lambda phase: (
                    phase * 4 if phase < 0.25 else
                    1.0 if phase < 0.75 else
                    1.0 - ((phase - 0.75) * 4) if phase < 1.0 else
                    0.1
                ),
            ),
            CycleEffect(
                target="sky",
                property="hue",
                modulation=lambda phase: phase * 360,
            ),
            CycleEffect(
                target="activity-level",
                property="multiplier",
                modulation=lambda phase: (
                    0.3 + phase * 2.8 if phase < 0.25 else
                    1.0 if phase < 0.75 else
                    1.0 - ((phase - 0.75) * 2) if phase < 1.0 else
                    0.3
                ),
            ),
        ],
    ),
    
    # Weekly expedition cycle (7 minutes)
    "expeditionCycle": NaturalCycle(
        name="Expedition Rhythm",
        duration_ms=420000,
        effects=[
            CycleEffect(
                target="expeditions",
                property="featured",
                modulation=lambda phase: math.floor(phase * 7),
            ),
        ],
    ),
    
    # Seasonal cycle (28 minutes)
    "seasons": NaturalCycle(
        name="Seasonal Progression",
        duration_ms=1680000,
        effects=[
            CycleEffect(
                target="communities",
                property="aesthetic",
                modulation=lambda phase: phase,
            ),
            CycleEffect(
                target="expeditions",
                property="availability",
                modulation=lambda phase: phase,
            ),
        ],
    ),
}


# =============================================================================
# LIVING ENTITIES - From naturalSystems.ts lines 150-450
# =============================================================================

class EntityType(Enum):
    """Matches naturalSystems.ts LivingEntity.type (line 25)."""
    BUILDING = "building"
    LANDSCAPE = "landscape"
    CHARACTER = "character"
    SYSTEM = "system"


class EntityMood(Enum):
    """Matches naturalSystems.ts EntityState.mood (line 36)."""
    DORMANT = "dormant"
    AWAKENING = "awakening"
    ACTIVE = "active"
    THRIVING = "thriving"
    RESTING = "resting"


class BehaviorTrigger(Enum):
    """Matches naturalSystems.ts Behavior.trigger (line 42)."""
    CYCLE = "cycle"
    PROXIMITY = "proximity"
    INTERACTION = "interaction"
    RANDOM = "random"
    ENERGY = "energy"


@dataclass
class EntityState:
    """
    Matches naturalSystems.ts EntityState interface (lines 32-38).
    """
    position: tuple[float, float, float] = (0.0, 0.0, 0.0)
    scale: float = 1.0
    animation: str = "idle"
    mood: EntityMood = EntityMood.ACTIVE
    age_ms: int = 0


@dataclass
class Behavior:
    """
    Matches naturalSystems.ts Behavior interface (lines 40-45).
    """
    name: str
    trigger: BehaviorTrigger
    probability: float = 1.0
    action: Optional[Callable] = None


@dataclass
class WorldContext:
    """
    Matches naturalSystems.ts WorldContext interface (lines 47-54).
    """
    time: float = 0.0
    day_phase: float = 0.5  # 0 = midnight, 0.5 = noon
    season_phase: float = 0.0
    visitor_count: int = 0
    total_energy: float = 0.0
    dominant_mood: str = "active"


@dataclass
class LivingEntity:
    """
    Matches naturalSystems.ts LivingEntity interface (lines 23-30).
    """
    id: str
    entity_type: EntityType
    state: EntityState = field(default_factory=EntityState)
    behaviors: list[Behavior] = field(default_factory=list)
    connections: list[str] = field(default_factory=list)
    energy: float = 0.5
    name: str = ""
    description: str = ""
    
    def __post_init__(self):
        if not self.name:
            self.name = self.id.replace("-", " ").title()


# Direct translation of livingEntities from naturalSystems.ts (lines 154-450)
LIVING_ENTITIES: dict[str, LivingEntity] = {
    # Mark Twain - Hero Host (lines 156-205)
    "hero-host-mark-twain": LivingEntity(
        id="hero-host-mark-twain",
        name="Mark Twain",
        entity_type=EntityType.CHARACTER,
        state=EntityState(
            position=(0, 0, 0),
            animation="idle-storytelling",
            mood=EntityMood.THRIVING,
        ),
        behaviors=[
            Behavior(name="spontaneous-story", trigger=BehaviorTrigger.RANDOM, probability=0.05),
            Behavior(name="greet-newcomers", trigger=BehaviorTrigger.PROXIMITY, probability=1.0),
            Behavior(name="rest-at-night", trigger=BehaviorTrigger.CYCLE, probability=1.0),
        ],
        connections=["daily-bulletin", "all-communities", "all-expeditions"],
        energy=0.9,
        description="The Hero Host - 24/7 storyteller and guide",
    ),
    
    # Town Center (lines 207-241)
    "frontier-town-center": LivingEntity(
        id="frontier-town-center",
        name="Frontier Town Center",
        entity_type=EntityType.BUILDING,
        state=EntityState(
            animation="breathing",
            mood=EntityMood.ACTIVE,
        ),
        behaviors=[
            Behavior(name="pulse-with-activity", trigger=BehaviorTrigger.ENERGY, probability=1.0),
            Behavior(name="emit-light", trigger=BehaviorTrigger.CYCLE, probability=1.0),
        ],
        connections=["all-communities"],
        energy=0.8,
        description="The beating heart of the frontier",
    ),
    
    # Frontier Colony (lines 243-280)
    "frontier-colony-district": LivingEntity(
        id="frontier-colony-district",
        name="Frontier Colony",
        entity_type=EntityType.BUILDING,
        state=EntityState(
            position=(-100, 0, 50),
            animation="breathing",
            mood=EntityMood.ACTIVE,
        ),
        connections=["town-center", "expeditions"],
        energy=0.75,
        description="The main residential district",
    ),
    
    # Wilderness Preserve
    "wilderness-preserve-zone": LivingEntity(
        id="wilderness-preserve-zone",
        name="Wilderness Preserve",
        entity_type=EntityType.LANDSCAPE,
        state=EntityState(
            position=(200, 0, -150),
            animation="wind-sway",
            mood=EntityMood.THRIVING,
        ),
        connections=["eco-expeditions"],
        energy=1.0,
        description="Pristine wilderness - highest natural energy",
    ),
    
    # Nikola Tesla - Hero Host
    "hero-host-nikola-tesla": LivingEntity(
        id="hero-host-nikola-tesla",
        name="Nikola Tesla",
        entity_type=EntityType.CHARACTER,
        state=EntityState(
            position=(150, 0, 100),
            animation="idle-teaching",
            mood=EntityMood.THRIVING,
        ),
        connections=["hhf-mri-system", "syntheverse-os", "all-verses"],
        energy=0.95,
        description="Hero Host for Science Discovery Museum",
    ),
    
    # HHF-AI MRI System
    "hhf-ai-mri-system": LivingEntity(
        id="hhf-ai-mri-system",
        name="HHF-AI MRI System",
        entity_type=EntityType.SYSTEM,
        state=EntityState(
            position=(150, 0, 100),
            animation="operating",
            mood=EntityMood.ACTIVE,
        ),
        connections=["tesla-entity", "syntheverse-cloud", "awareness-nodes"],
        energy=1.0,
        description="Operating at 1.420 GHz - perpetual awareness emitter",
    ),
}


# =============================================================================
# TWAIN PERSONALITY - From twainPersonality.ts
# =============================================================================

class TwainEmotion(Enum):
    """Matches twainPersonality.ts TwainResponse.emotion."""
    HUMOR = "humor"
    STORYTELLING = "storytelling"
    CONTEMPLATION = "contemplation"
    WISDOM = "wisdom"
    WARMTH = "warmth"


class TwainGesture(Enum):
    """Matches twainPersonality.ts TwainResponse.gestureHint."""
    POINTING = "pointing"
    STORYTELLING = "storytelling"
    EXPLAINING = "explaining"
    OBSERVING = "observing"
    WELCOMING = "welcoming"


@dataclass
class TwainResponse:
    """
    Matches twainPersonality.ts TwainResponse interface (lines 7-12).
    """
    text: str
    emotion: TwainEmotion = TwainEmotion.WARMTH
    gesture_hint: TwainGesture = TwainGesture.WELCOMING
    keywords: list[str] = field(default_factory=list)


# Twain speaking patterns from twainPersonality.ts TWAIN_TRAITS
TWAIN_PATTERNS = [
    "Well now, let me tell you...",
    "I remember when...",
    "There's a story about...",
    "You know, in my travels...",
    "Here's the thing about...",
]

TWAIN_FILLER_WORDS = [
    "indeed",
    "if you please",
    "truth be told",
    "I do declare",
    "well now",
]


# =============================================================================
# AUTO-TOUR ENGINE - From autoTourEngine.ts
# =============================================================================

@dataclass
class TourStage:
    """
    Matches autoTourEngine.ts TourStage interface (lines 7-17).
    """
    id: int
    name: str
    title: str
    duration_ms: int
    narration: list[str] = field(default_factory=list)
    keywords: list[str] = field(default_factory=list)
    protocols_highlighted: list[int] = field(default_factory=list)
    interactive_elements: list[str] = field(default_factory=list)
    section: Optional[str] = None


@dataclass
class TourState:
    """
    Matches autoTourEngine.ts TourState interface (lines 148-156).
    """
    is_active: bool = False
    is_paused: bool = False
    current_stage: int = 0
    stage_progress: float = 0.0
    narration_index: int = 0
    total_elapsed: int = 0
    interaction_count: int = 0


# =============================================================================
# UTILITY FUNCTIONS
# =============================================================================

def get_project_root() -> Path:
    """Get the MarkTwainVerse project root directory."""
    # Walk up from samuel_clemens to find project root
    current = Path(__file__).parent
    while current.name != "MarkTwainVerse-Authorized-Visitor-Landing-Page":
        parent = current.parent
        if parent == current:
            raise FileNotFoundError("Could not find project root")
        current = parent
    return current


def get_protocol_path(protocol: str) -> Path:
    """Get the full path to a TypeScript protocol file."""
    root = get_project_root()
    if protocol not in PROTOCOL_PATHS:
        raise KeyError(f"Unknown protocol: {protocol}")
    return root / PROTOCOL_PATHS[protocol]


def load_protocol_source(protocol: str) -> str:
    """Load the source code of a TypeScript protocol file."""
    path = get_protocol_path(protocol)
    return path.read_text()


def get_cycle(cycle_name: str) -> Optional[NaturalCycle]:
    """Get a natural cycle by name."""
    return NATURAL_CYCLES.get(cycle_name)


def get_entity(entity_id: str) -> Optional[LivingEntity]:
    """Get a living entity by ID."""
    return LIVING_ENTITIES.get(entity_id)


def get_all_cycles() -> dict[str, NaturalCycle]:
    """Get all natural cycles."""
    return NATURAL_CYCLES.copy()


def get_all_entities() -> dict[str, LivingEntity]:
    """Get all living entities."""
    return LIVING_ENTITIES.copy()


def compute_world_context() -> WorldContext:
    """Compute current world context based on cycles and entities."""
    total_energy = sum(e.energy for e in LIVING_ENTITIES.values())
    avg_energy = total_energy / len(LIVING_ENTITIES) if LIVING_ENTITIES else 0
    
    # Get current time-based phases
    now = datetime.now()
    hour = now.hour + now.minute / 60
    day_phase = hour / 24  # 0 at midnight, 0.5 at noon
    
    # Season phase based on day of year
    day_of_year = now.timetuple().tm_yday
    season_phase = day_of_year / 365
    
    # Determine dominant mood
    mood_counts: dict[EntityMood, int] = {}
    for entity in LIVING_ENTITIES.values():
        mood = entity.state.mood
        mood_counts[mood] = mood_counts.get(mood, 0) + 1
    
    dominant_mood = max(mood_counts, key=lambda m: mood_counts[m]).value if mood_counts else "active"
    
    return WorldContext(
        time=now.timestamp(),
        day_phase=day_phase,
        season_phase=season_phase,
        total_energy=avg_energy,
        dominant_mood=dominant_mood,
    )
