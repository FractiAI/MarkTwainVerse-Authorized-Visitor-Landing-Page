"""
Story Elements - Building blocks for story generation.

Characters, settings, plot points, and themes for the frontier narrative.
"""

from __future__ import annotations

import random
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class ElementType(Enum):
    """Types of story elements."""
    CHARACTER = "character"
    SETTING = "setting"
    PLOT_POINT = "plot_point"
    THEME = "theme"
    CONFLICT = "conflict"
    RESOLUTION = "resolution"


@dataclass
class StoryElement:
    """Base class for story elements."""
    name: str
    element_type: ElementType
    description: str
    tags: list[str] = field(default_factory=list)
    
    def __str__(self) -> str:
        return self.name


@dataclass
class Character(StoryElement):
    """A character in the story."""
    role: str = "supporting"  # protagonist, antagonist, supporting, mentor
    traits: list[str] = field(default_factory=list)
    motivation: str = ""
    backstory: str = ""
    
    def __post_init__(self) -> None:
        self.element_type = ElementType.CHARACTER


@dataclass
class Setting(StoryElement):
    """A setting/location in the story."""
    atmosphere: str = "neutral"  # peaceful, tense, mysterious, lively
    time_period: str = "present"
    features: list[str] = field(default_factory=list)
    
    def __post_init__(self) -> None:
        self.element_type = ElementType.SETTING


@dataclass
class PlotPoint(StoryElement):
    """A plot point or event in the story."""
    sequence: int = 0  # Order in the story
    tension_level: float = 0.5  # 0-1
    requires_resolution: bool = False
    
    def __post_init__(self) -> None:
        self.element_type = ElementType.PLOT_POINT


@dataclass
class Theme(StoryElement):
    """A thematic element of the story."""
    universal: bool = True
    related_themes: list[str] = field(default_factory=list)
    
    def __post_init__(self) -> None:
        self.element_type = ElementType.THEME


# Pre-built character library
CHARACTERS: list[Character] = [
    Character(
        name="The Riverboat Captain",
        element_type=ElementType.CHARACTER,
        description="A weathered pilot who knows every bend in the Mississippi",
        role="mentor",
        traits=["wise", "patient", "observant", "storyteller"],
        motivation="To pass on river wisdom to the next generation",
        backstory="Forty years on the river, knows more secrets than the fish",
        tags=["river", "mentor", "wisdom"],
    ),
    Character(
        name="The Young Adventurer",
        element_type=ElementType.CHARACTER,
        description="An eager youth seeking fortune and stories on the frontier",
        role="protagonist",
        traits=["curious", "brave", "naive", "hopeful"],
        motivation="To make a name and find adventure",
        backstory="Left home with nothing but dreams and determination",
        tags=["adventure", "youth", "frontier"],
    ),
    Character(
        name="The Frontier Widow",
        element_type=ElementType.CHARACTER,
        description="A resilient woman running the town's only boarding house",
        role="supporting",
        traits=["resourceful", "kind", "tough", "wise"],
        motivation="To protect and provide for her community",
        backstory="Survived everything the frontier could throw at her",
        tags=["frontier", "resilience", "community"],
    ),
    Character(
        name="The Wandering Philosopher",
        element_type=ElementType.CHARACTER,
        description="A curious soul who speaks in riddles and insights",
        role="mentor",
        traits=["eccentric", "wise", "humorous", "cryptic"],
        motivation="To understand the deeper truths of existence",
        backstory="Nobody knows where he came from or where he's going",
        tags=["wisdom", "mystery", "humor"],
    ),
    Character(
        name="The Town Sheriff",
        element_type=ElementType.CHARACTER,
        description="The lone law in a lawless land, tired but determined",
        role="supporting",
        traits=["just", "weary", "determined", "principled"],
        motivation="To bring order without losing his soul",
        backstory="Once an outlaw himself, now walks a straighter path",
        tags=["frontier", "justice", "redemption"],
    ),
    Character(
        name="The Treasure Hunter",
        element_type=ElementType.CHARACTER,
        description="Always chasing the next big find, never satisfied",
        role="antagonist",
        traits=["greedy", "clever", "persistent", "desperate"],
        motivation="To find the one treasure that will finally be enough",
        backstory="Has found fortunes and lost them all",
        tags=["adventure", "conflict", "greed"],
    ),
]

# Pre-built settings library
SETTINGS: list[Setting] = [
    Setting(
        name="The Mississippi River",
        element_type=ElementType.SETTING,
        description="The great river, wide and brown, carrying stories and secrets",
        atmosphere="mysterious",
        time_period="frontier era",
        features=["steamboats", "sandbars", "fog", "endless flow"],
        tags=["river", "adventure", "journey"],
    ),
    Setting(
        name="Frontier Town Main Street",
        element_type=ElementType.SETTING,
        description="Dusty road lined with wooden buildings, full of life and danger",
        atmosphere="lively",
        time_period="frontier era",
        features=["saloon", "general store", "hotel", "stables"],
        tags=["town", "frontier", "community"],
    ),
    Setting(
        name="The Wilderness Campfire",
        element_type=ElementType.SETTING,
        description="A circle of warmth in the vast, dark wilderness",
        atmosphere="peaceful",
        time_period="any",
        features=["crackling fire", "starlit sky", "forest sounds"],
        tags=["wilderness", "stories", "night"],
    ),
    Setting(
        name="The Abandoned Mine",
        element_type=ElementType.SETTING,
        description="Dark tunnels promising riches or doom",
        atmosphere="tense",
        time_period="frontier era",
        features=["darkness", "echoes", "old equipment", "mystery"],
        tags=["adventure", "danger", "treasure"],
    ),
    Setting(
        name="The Alpine Summit",
        element_type=ElementType.SETTING,
        description="High above the world, where the air is thin and views are endless",
        atmosphere="peaceful",
        time_period="any",
        features=["snow", "eagles", "silence", "perspective"],
        tags=["wilderness", "achievement", "reflection"],
    ),
    Setting(
        name="The Innovation Hub",
        element_type=ElementType.SETTING,
        description="A frontier workshop where dreamers build tomorrow",
        atmosphere="lively",
        time_period="present",
        features=["machines", "plans", "inventors", "possibilities"],
        tags=["innovation", "future", "creation"],
    ),
]

# Pre-built plot points library
PLOT_POINTS: list[PlotPoint] = [
    PlotPoint(
        name="The Stranger Arrives",
        element_type=ElementType.PLOT_POINT,
        description="A mysterious figure enters town, bringing change",
        sequence=1,
        tension_level=0.3,
        requires_resolution=False,
        tags=["opening", "mystery", "change"],
    ),
    PlotPoint(
        name="The Hidden Truth",
        element_type=ElementType.PLOT_POINT,
        description="A long-buried secret comes to light",
        sequence=2,
        tension_level=0.6,
        requires_resolution=True,
        tags=["revelation", "conflict", "secret"],
    ),
    PlotPoint(
        name="The River Rising",
        element_type=ElementType.PLOT_POINT,
        description="Natural forces threaten everything",
        sequence=3,
        tension_level=0.8,
        requires_resolution=True,
        tags=["danger", "nature", "crisis"],
    ),
    PlotPoint(
        name="The Unlikely Alliance",
        element_type=ElementType.PLOT_POINT,
        description="Enemies must work together to survive",
        sequence=4,
        tension_level=0.5,
        requires_resolution=False,
        tags=["teamwork", "redemption", "change"],
    ),
    PlotPoint(
        name="The Final Showdown",
        element_type=ElementType.PLOT_POINT,
        description="Everything comes to a head in one decisive moment",
        sequence=5,
        tension_level=1.0,
        requires_resolution=True,
        tags=["climax", "resolution", "stakes"],
    ),
    PlotPoint(
        name="The Journey Home",
        element_type=ElementType.PLOT_POINT,
        description="After everything, the path back to where it began",
        sequence=6,
        tension_level=0.2,
        requires_resolution=False,
        tags=["resolution", "reflection", "home"],
    ),
]

# Pre-built themes library
THEMES: list[Theme] = [
    Theme(
        name="The Search for Meaning",
        element_type=ElementType.THEME,
        description="What gives life purpose in a vast, indifferent world?",
        universal=True,
        related_themes=["identity", "purpose", "existence"],
        tags=["philosophy", "deep", "universal"],
    ),
    Theme(
        name="Civilization vs. Wilderness",
        element_type=ElementType.THEME,
        description="The eternal tension between tamed and wild",
        universal=True,
        related_themes=["freedom", "order", "nature"],
        tags=["frontier", "conflict", "nature"],
    ),
    Theme(
        name="The Power of Stories",
        element_type=ElementType.THEME,
        description="How narratives shape reality and identity",
        universal=True,
        related_themes=["truth", "memory", "identity"],
        tags=["meta", "storytelling", "truth"],
    ),
    Theme(
        name="Redemption's Long Road",
        element_type=ElementType.THEME,
        description="Can past wrongs ever truly be made right?",
        universal=True,
        related_themes=["guilt", "forgiveness", "change"],
        tags=["moral", "character", "growth"],
    ),
    Theme(
        name="Human Connection",
        element_type=ElementType.THEME,
        description="The bonds that make life worth living",
        universal=True,
        related_themes=["love", "friendship", "community"],
        tags=["relationships", "warmth", "universal"],
    ),
    Theme(
        name="Adventure's Call",
        element_type=ElementType.THEME,
        description="The irresistible pull of the unknown",
        universal=True,
        related_themes=["curiosity", "courage", "discovery"],
        tags=["adventure", "excitement", "journey"],
    ),
]


def get_random_character() -> Character:
    """Get a random character."""
    return random.choice(CHARACTERS)


def get_random_setting() -> Setting:
    """Get a random setting."""
    return random.choice(SETTINGS)


def get_random_plot_point() -> PlotPoint:
    """Get a random plot point."""
    return random.choice(PLOT_POINTS)


def get_random_theme() -> Theme:
    """Get a random theme."""
    return random.choice(THEMES)


def get_random_elements(count: int = 4) -> dict[str, StoryElement]:
    """
    Get a random set of story elements.
    
    Args:
        count: Number of each element type to include
        
    Returns:
        Dictionary with element types as keys
    """
    return {
        "character": get_random_character(),
        "setting": get_random_setting(),
        "plot_point": get_random_plot_point(),
        "theme": get_random_theme(),
    }


def get_elements_by_tag(tag: str) -> list[StoryElement]:
    """
    Get all elements matching a tag.
    
    Args:
        tag: Tag to search for
        
    Returns:
        List of matching elements
    """
    all_elements: list[StoryElement] = CHARACTERS + SETTINGS + PLOT_POINTS + THEMES
    return [e for e in all_elements if tag.lower() in [t.lower() for t in e.tags]]


def get_compatible_elements(element: StoryElement) -> list[StoryElement]:
    """
    Get elements that are compatible with the given element.
    
    Args:
        element: Element to find matches for
        
    Returns:
        List of compatible elements
    """
    compatible: list[StoryElement] = []
    
    for tag in element.tags:
        matches = get_elements_by_tag(tag)
        for match in matches:
            if match != element and match not in compatible:
                compatible.append(match)
    
    return compatible
