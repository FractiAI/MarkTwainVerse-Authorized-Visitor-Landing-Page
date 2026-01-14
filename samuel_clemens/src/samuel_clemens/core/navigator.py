"""
Navigator - River and verse navigation utilities for MarkTwainVerse.

"Twenty years from now you will be more disappointed by the things that you 
didn't do than by the ones you did do. So throw off the bowlines. Sail away 
from the safe harbor." — Mark Twain
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Optional

from samuel_clemens.utils.logging import frontier_log


class CourseType(Enum):
    """Types of expedition courses."""
    FISHING = "fishing"
    ECO_ADVENTURE = "eco-adventure"
    STORYTELLING = "storytelling"
    FRONTIER = "frontier"
    WILDERNESS = "wilderness"
    COMMUNITY = "community"


class CurrentStrength(Enum):
    """Strength of verse currents (activity levels)."""
    CALM = "calm"
    STEADY = "steady"
    STRONG = "strong"
    TURBULENT = "turbulent"


@dataclass
class Course:
    """A charted expedition course."""
    destination: str
    course_type: CourseType
    duration_hours: float
    waypoints: list[str]
    description: str

    def __str__(self) -> str:
        return f"Course to {self.destination} ({self.duration_hours}h)"


@dataclass
class Harbor:
    """A safe harbor (stopping point) in the verse."""
    name: str
    community: str
    amenities: list[str]
    description: str

    def __str__(self) -> str:
        return f"{self.name} ({self.community})"


@dataclass
class CurrentReading:
    """A reading of the verse currents."""
    strength: CurrentStrength
    direction: str
    activity_level: float  # 0.0 - 1.0
    dominant_mood: str
    description: str


# Expedition course templates
COURSE_TEMPLATES: dict[CourseType, list[Course]] = {
    CourseType.FISHING: [
        Course(
            destination="Crystal Lake",
            course_type=CourseType.FISHING,
            duration_hours=4.0,
            waypoints=["Town Dock", "River Bend", "Quiet Cove", "Crystal Lake"],
            description="A half-day fishing expedition to the legendary Crystal Lake, "
                        "where the trout run thick and the stories run thicker.",
        ),
        Course(
            destination="Mississippi Tributary",
            course_type=CourseType.FISHING,
            duration_hours=8.0,
            waypoints=["Main Dock", "Sawyer's Bend", "Catfish Hollow", "The Deep Pool"],
            description="A full-day journey into the heart of catfish country. "
                        "Pack your patience and your tall tales.",
        ),
    ],
    CourseType.ECO_ADVENTURE: [
        Course(
            destination="Wilderness Preserve",
            course_type=CourseType.ECO_ADVENTURE,
            duration_hours=6.0,
            waypoints=["Visitor Center", "Old Growth Trail", "Eagle Overlook", "Preserve Core"],
            description="An eco-adventure through pristine wilderness, where nature "
                        "still operates by its own ancient protocols.",
        ),
    ],
    CourseType.STORYTELLING: [
        Course(
            destination="Fireside Circle",
            course_type=CourseType.STORYTELLING,
            duration_hours=2.0,
            waypoints=["Town Square", "Old Oak", "Fireside Circle"],
            description="An evening storytelling session where the frontier's best "
                        "tales are spun under star-filled skies.",
        ),
    ],
    CourseType.FRONTIER: [
        Course(
            destination="Frontier Outpost",
            course_type=CourseType.FRONTIER,
            duration_hours=12.0,
            waypoints=["Town Gate", "Prairie Crossing", "Ridge Trail", "Frontier Outpost"],
            description="A full-day expedition to the edge of settlement, where the "
                        "frontier still feels wild and full of possibility.",
        ),
    ],
    CourseType.WILDERNESS: [
        Course(
            destination="Alpine Heights",
            course_type=CourseType.WILDERNESS,
            duration_hours=24.0,
            waypoints=["Base Camp", "Timber Line", "Snow Field", "Summit Approach", "Alpine Peak"],
            description="A multi-day wilderness expedition to the highest point in "
                        "the verse—for those seeking perspective in the thin air.",
        ),
    ],
    CourseType.COMMUNITY: [
        Course(
            destination="Innovation Hub",
            course_type=CourseType.COMMUNITY,
            duration_hours=3.0,
            waypoints=["Town Center", "Maker's Row", "Innovation Hub"],
            description="A tour of the frontier's innovation district, where dreamers "
                        "and builders are creating tomorrow's reality.",
        ),
    ],
}

# Harbor templates
HARBORS: list[Harbor] = [
    Harbor(
        name="Town Dock",
        community="Frontier Colony",
        amenities=["Supplies", "Lodging", "Storytelling Corner"],
        description="The main harbor where all frontiersmen start their journeys.",
    ),
    Harbor(
        name="Quiet Cove",
        community="Fishing District",
        amenities=["Boat Repair", "Bait Shop", "Fish Smokehouse"],
        description="A peaceful cove where anglers rest between expeditions.",
    ),
    Harbor(
        name="Alpine Lodge",
        community="Alpine Heights",
        amenities=["Warm Fire", "Hot Meals", "Mountain Guides"],
        description="High-altitude sanctuary for wilderness explorers.",
    ),
    Harbor(
        name="Tropical Marina",
        community="Tropical Beach",
        amenities=["Beach Access", "Sunset Views", "Fresh Seafood"],
        description="Where the frontier meets the endless blue horizon.",
    ),
    Harbor(
        name="Hub Terminal",
        community="Innovation Hub",
        amenities=["Co-working Space", "Demo Area", "Networking Lounge"],
        description="The gathering place for frontier innovators and builders.",
    ),
]


def chart_course(
    course_type: CourseType,
    duration_preference: Optional[str] = None,
) -> Course:
    """
    Chart an expedition course through the verse.
    
    Like a river pilot reading the channel markers, this method
    charts the optimal route for your chosen adventure.
    
    Args:
        course_type: Type of expedition to chart
        duration_preference: Optional preference for "short", "medium", or "long"
        
    Returns:
        A Course object with full expedition details
    """
    courses = COURSE_TEMPLATES.get(course_type, COURSE_TEMPLATES[CourseType.FRONTIER])
    
    if duration_preference:
        # Sort by duration and pick accordingly
        sorted_courses = sorted(courses, key=lambda c: c.duration_hours)
        if duration_preference == "short":
            course = sorted_courses[0]
        elif duration_preference == "long":
            course = sorted_courses[-1]
        else:
            course = sorted_courses[len(sorted_courses) // 2]
    else:
        import random
        course = random.choice(courses)
    
    frontier_log(f"🗺️ Course charted: {course.destination}")
    return course


def read_currents(day_phase: float = 0.5, visitor_count: int = 1) -> CurrentReading:
    """
    Read the currents of the verse—sensing activity and mood.
    
    A good navigator knows the feel of the water. This method
    reads the pulse of the MarkTwainVerse.
    
    Args:
        day_phase: Current day/night phase (0.0 = midnight, 0.5 = noon)
        visitor_count: Number of active visitors
        
    Returns:
        A CurrentReading with verse state analysis
    """
    # Calculate activity level based on day phase and visitors
    base_activity = 0.3
    day_bonus = 0.4 if 0.25 <= day_phase <= 0.75 else 0.1
    visitor_bonus = min(0.3, visitor_count * 0.05)
    activity_level = min(1.0, base_activity + day_bonus + visitor_bonus)
    
    # Determine current strength
    if activity_level < 0.3:
        strength = CurrentStrength.CALM
    elif activity_level < 0.5:
        strength = CurrentStrength.STEADY
    elif activity_level < 0.8:
        strength = CurrentStrength.STRONG
    else:
        strength = CurrentStrength.TURBULENT
    
    # Determine direction based on day phase
    if day_phase < 0.25:
        direction = "dawn-rising"
        mood = "awakening"
    elif day_phase < 0.5:
        direction = "morning-flow"
        mood = "active"
    elif day_phase < 0.75:
        direction = "afternoon-drift"
        mood = "thriving"
    else:
        direction = "evening-ebb"
        mood = "resting"
    
    # Generate description
    descriptions = {
        CurrentStrength.CALM: "The verse is quiet, like a river in the early morning mist.",
        CurrentStrength.STEADY: "A steady current flows through the frontier—good traveling weather.",
        CurrentStrength.STRONG: "The currents run strong today—exciting times on the frontier!",
        CurrentStrength.TURBULENT: "Turbulent waters ahead—adventure guaranteed, smooth sailing not.",
    }
    
    reading = CurrentReading(
        strength=strength,
        direction=direction,
        activity_level=activity_level,
        dominant_mood=mood,
        description=descriptions[strength],
    )
    
    frontier_log(f"🌊 Currents read: {strength.value} ({mood})")
    return reading


def find_harbor(
    community: Optional[str] = None,
    amenity_needed: Optional[str] = None,
) -> Harbor:
    """
    Find a safe harbor (stopping point) in the verse.
    
    Every good pilot knows where the safe harbors are.
    This method helps you find rest and resupply.
    
    Args:
        community: Optional community to find harbor in
        amenity_needed: Optional specific amenity required
        
    Returns:
        A Harbor matching the requirements
    """
    candidates = HARBORS
    
    # Filter by community if specified
    if community:
        community_lower = community.lower()
        candidates = [h for h in candidates if community_lower in h.community.lower()]
        if not candidates:
            candidates = HARBORS  # Fall back to all
    
    # Filter by amenity if specified
    if amenity_needed:
        amenity_lower = amenity_needed.lower()
        candidates = [h for h in candidates 
                      if any(amenity_lower in a.lower() for a in h.amenities)]
        if not candidates:
            candidates = HARBORS  # Fall back to all
    
    import random
    harbor = random.choice(candidates)
    
    frontier_log(f"⚓ Harbor found: {harbor.name}")
    return harbor


def get_all_harbors() -> list[Harbor]:
    """
    Get a list of all known harbors in the verse.
    
    Returns:
        Complete list of harbors
    """
    return HARBORS.copy()


def get_expedition_types() -> list[CourseType]:
    """
    Get all available expedition types.
    
    Returns:
        List of all CourseType values
    """
    return list(CourseType)
