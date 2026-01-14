"""
Frontier - General frontier utilities for MarkTwainVerse.

"I have never let my schooling interfere with my education." — Mark Twain

Contains greetings, farewells, and general verse status utilities.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from samuel_clemens.utils.logging import frontier_log


@dataclass
class FrontierStatus:
    """Current status of the MarkTwainVerse frontier."""
    is_operational: bool
    day_phase: float
    season: str
    visitor_count: int
    dominant_mood: str
    hero_host_status: str
    message: str

    def __str__(self) -> str:
        return f"Frontier: {self.message}"


# Greeting templates based on time of day
GREETINGS: dict[str, list[str]] = {
    "morning": [
        "Well now, good morning friend! The sun's coming up over the frontier, "
        "and it looks like it's going to be a fine day for adventure.",
        "Rise and shine, traveler! The frontier waits for no one, but it always "
        "welcomes those with the courage to explore.",
        "Morning! There's fresh coffee at the town center and stories waiting to be told. "
        "What brings you to the Syntheverse today?",
    ],
    "afternoon": [
        "Good afternoon, friend! The frontier's in full swing—expeditions departing, "
        "stories being told, adventures unfolding. What can I show you?",
        "Afternoon, traveler! You've arrived at the busiest time in the verse. "
        "The communities are thriving and the possibilities are endless.",
        "Well, look who's here! Perfect timing—the afternoon's when the frontier "
        "really comes alive. Ready to join the rhythm?",
    ],
    "evening": [
        "Good evening, friend! The sun's setting on another frontier day, "
        "but the stories are just getting started. Care to join us by the fire?",
        "Evening, traveler! This is my favorite time—when the day's adventures "
        "turn into tonight's tales. Pull up a chair.",
        "Ah, you've come at the golden hour! The frontier settles into its evening "
        "rhythm, and there's nothing quite like it.",
    ],
    "night": [
        "Well now, a night owl! The frontier rests, but it never truly sleeps. "
        "Some of the best stories happen under these stars.",
        "Good evening, friend—or should I say good night? The verse is quiet now, "
        "but there's peace in the silence.",
        "Midnight visitor! The frontier's wrapped in starlight, and the nocturnal "
        "stories are the most mysterious of all.",
    ],
}

# Farewell templates
FAREWELLS: list[str] = [
    "Safe travels, friend! The frontier will be here when you return—and so will I.",
    "Farewell, traveler! May your path be clear and your stories be worth telling.",
    "Until next time! Remember: the frontier isn't just a place, it's a state of mind. "
    "Carry it with you.",
    "Go well, friend! And remember what I always say: the secret of getting ahead "
    "is getting started.",
    "So long! The verse will keep turning, and we'll be ready when you return.",
    "Safe journeys! And don't be a stranger—good stories need good listeners.",
]


def frontier_greeting(
    visitor_name: Optional[str] = None,
    time_of_day: Optional[str] = None,
) -> str:
    """
    Generate a Mark Twain-style frontier greeting.
    
    A proper frontiersman always greets visitors with warmth
    and an invitation to adventure.
    
    Args:
        visitor_name: Optional name to personalize greeting
        time_of_day: Optional time (morning, afternoon, evening, night)
        
    Returns:
        A warm frontier greeting
    """
    import random
    
    # Determine time of day if not specified
    if not time_of_day:
        hour = datetime.now().hour
        if 5 <= hour < 12:
            time_of_day = "morning"
        elif 12 <= hour < 17:
            time_of_day = "afternoon"
        elif 17 <= hour < 21:
            time_of_day = "evening"
        else:
            time_of_day = "night"
    
    greetings = GREETINGS.get(time_of_day, GREETINGS["afternoon"])
    greeting = random.choice(greetings)
    
    if visitor_name:
        # Insert name into greeting
        greeting = greeting.replace("friend", visitor_name, 1)
        greeting = greeting.replace("traveler", visitor_name, 1)
    
    frontier_log(f"👋 Greeting delivered ({time_of_day})")
    return greeting


def frontier_farewell(visitor_name: Optional[str] = None) -> str:
    """
    Generate a Mark Twain-style frontier farewell.
    
    Never let a visitor leave without words of wisdom
    and a promise of return.
    
    Args:
        visitor_name: Optional name to personalize farewell
        
    Returns:
        A warm frontier farewell
    """
    import random
    
    farewell = random.choice(FAREWELLS)
    
    if visitor_name:
        farewell = farewell.replace("friend", visitor_name, 1)
        farewell = farewell.replace("traveler", visitor_name, 1)
    
    frontier_log(f"👋 Farewell delivered")
    return farewell


def get_frontier_status(
    day_phase: float = 0.5,
    visitor_count: int = 1,
) -> FrontierStatus:
    """
    Get the current status of the MarkTwainVerse frontier.
    
    Every good host knows the pulse of their establishment.
    This method reads the heartbeat of the verse.
    
    Args:
        day_phase: Current day/night phase (0.0 = midnight, 0.5 = noon)
        visitor_count: Number of active visitors
        
    Returns:
        FrontierStatus with complete verse state
    """
    # Determine season (could integrate with NSPFRP seasonPhase)
    import random
    seasons = ["Spring", "Summer", "Fall", "Winter"]
    season = seasons[int(datetime.now().month / 3.5) % 4]
    
    # Determine mood based on activity
    if visitor_count == 0:
        mood = "dormant"
    elif visitor_count < 3:
        mood = "awakening"
    elif visitor_count < 10:
        mood = "active"
    else:
        mood = "thriving"
    
    # Hero Host status
    if 0.25 <= day_phase <= 0.75:
        host_status = "active-storytelling"
    elif day_phase < 0.25:
        host_status = "dawn-greeting"
    else:
        host_status = "evening-tales"
    
    # Generate message
    messages = {
        "dormant": "The frontier rests peacefully under starlight.",
        "awakening": "The frontier stirs with the first light of possibility.",
        "active": "The frontier hums with the energy of adventure.",
        "thriving": "The frontier is alive with stories, expeditions, and dreams!",
    }
    
    status = FrontierStatus(
        is_operational=True,
        day_phase=day_phase,
        season=season,
        visitor_count=visitor_count,
        dominant_mood=mood,
        hero_host_status=host_status,
        message=messages[mood],
    )
    
    frontier_log(f"📊 Status check: {mood}")
    return status


def get_time_of_day_from_phase(day_phase: float) -> str:
    """
    Convert a day phase (0-1) to time of day string.
    
    Args:
        day_phase: 0.0 = midnight, 0.5 = noon, 1.0 = midnight
        
    Returns:
        Time of day: morning, afternoon, evening, or night
    """
    if day_phase < 0.25:
        return "night"
    elif day_phase < 0.5:
        return "morning"
    elif day_phase < 0.75:
        return "afternoon"
    else:
        return "evening"
