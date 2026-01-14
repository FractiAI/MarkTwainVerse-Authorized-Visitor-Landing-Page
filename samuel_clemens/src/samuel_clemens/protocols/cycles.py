"""
Cycles - NSPFRP natural cycle integration.

Bridges to the TypeScript naturalSystems.ts cycle management.

Cycle Reference (from naturalSystems.ts):
- Breathing: 6 second ambient animation cycle
- Day-Night: 2 min demo / 24h production
- Expedition: 7 min weekly cycle
- Seasons: 28 min demo / 1 year production
"""

from __future__ import annotations

import math
import time
from dataclasses import dataclass
from typing import Optional


@dataclass
class CycleState:
    """Current state of a natural cycle."""
    name: str
    phase: float  # 0.0 - 1.0
    duration_ms: int
    description: str


# Cycle durations (demo mode - from naturalSystems.ts)
CYCLE_DURATIONS = {
    "breathing": 6000,        # 6 seconds
    "dayNight": 120000,       # 2 minutes
    "expedition": 420000,     # 7 minutes
    "seasons": 1680000,       # 28 minutes
}

# Start time for cycle calculations
_start_time: Optional[float] = None


def _get_phase(cycle_name: str) -> float:
    """Calculate current phase for a cycle."""
    global _start_time
    if _start_time is None:
        _start_time = time.time() * 1000  # Convert to milliseconds
    
    duration = CYCLE_DURATIONS.get(cycle_name, 6000)
    elapsed = (time.time() * 1000) - _start_time
    return (elapsed % duration) / duration


def get_day_phase() -> float:
    """
    Get the current day/night cycle phase.
    
    Phase values:
    - 0.0 = Midnight
    - 0.25 = Dawn
    - 0.5 = Noon  
    - 0.75 = Dusk
    - 1.0 = Midnight (wraps)
    
    Returns:
        Phase value between 0.0 and 1.0
    """
    return _get_phase("dayNight")


def get_season_phase() -> float:
    """
    Get the current seasonal cycle phase.
    
    Phase values:
    - 0.0-0.25 = Spring
    - 0.25-0.5 = Summer
    - 0.5-0.75 = Fall
    - 0.75-1.0 = Winter
    
    Returns:
        Phase value between 0.0 and 1.0
    """
    return _get_phase("seasons")


def get_breathing_pulse() -> float:
    """
    Get the current breathing cycle pulse.
    
    Used for ambient animations - a gentle 6-second
    oscillation that gives the world its "breath".
    
    Returns:
        Pulse value for luminosity/scale modulation
    """
    phase = _get_phase("breathing")
    # Returns 0.8-1.0 sinusoidal value (from naturalSystems.ts)
    return 0.8 + math.sin(phase * math.pi * 2) * 0.2


def get_expedition_day() -> int:
    """
    Get the current featured expedition day (0-6).
    
    The expedition cycle rotates through 7 featured
    expeditions over the week (7/day in production).
    
    Returns:
        Day index 0-6
    """
    phase = _get_phase("expedition")
    return int(phase * 7) % 7


def get_time_of_day() -> str:
    """
    Get descriptive time of day from cycle phase.
    
    Returns:
        One of: 'night', 'dawn', 'morning', 'afternoon', 'dusk', 'evening'
    """
    phase = get_day_phase()
    if phase < 0.20:
        return "night"
    elif phase < 0.30:
        return "dawn"
    elif phase < 0.50:
        return "morning"
    elif phase < 0.70:
        return "afternoon"
    elif phase < 0.80:
        return "dusk"
    else:
        return "evening"


def get_season() -> str:
    """
    Get current season name.
    
    Returns:
        One of: 'spring', 'summer', 'fall', 'winter'
    """
    phase = get_season_phase()
    if phase < 0.25:
        return "spring"
    elif phase < 0.5:
        return "summer"
    elif phase < 0.75:
        return "fall"
    else:
        return "winter"


def get_activity_multiplier() -> float:
    """
    Get activity level multiplier based on day phase.
    
    From naturalSystems.ts day-night cycle effects:
    - Night: 0.3
    - Morning awakening: 0.3 to 1.0
    - Day: 1.0
    - Evening: 1.0 to 0.5
    
    Returns:
        Activity multiplier 0.3-1.0
    """
    phase = get_day_phase()
    if phase < 0.25:
        return 0.3 + phase * 2.8  # Morning awakening
    elif phase < 0.75:
        return 1.0  # Full day activity
    elif phase < 1.0:
        return 1.0 - ((phase - 0.75) * 2)  # Evening slowing
    return 0.3  # Night


def get_all_cycles() -> dict[str, CycleState]:
    """
    Get the current state of all natural cycles.
    
    Returns:
        Dictionary of cycle states
    """
    return {
        "breathing": CycleState(
            name="Breathing Cycle",
            phase=_get_phase("breathing"),
            duration_ms=CYCLE_DURATIONS["breathing"],
            description="Ambient animation - the world's breath",
        ),
        "dayNight": CycleState(
            name="Day-Night Cycle",
            phase=get_day_phase(),
            duration_ms=CYCLE_DURATIONS["dayNight"],
            description=f"Current: {get_time_of_day()}",
        ),
        "expedition": CycleState(
            name="Expedition Rhythm",
            phase=_get_phase("expedition"),
            duration_ms=CYCLE_DURATIONS["expedition"],
            description=f"Featured expedition day: {get_expedition_day()}",
        ),
        "seasons": CycleState(
            name="Seasonal Progression",
            phase=get_season_phase(),
            duration_ms=CYCLE_DURATIONS["seasons"],
            description=f"Current season: {get_season()}",
        ),
    }


def reset_cycles() -> None:
    """Reset cycle start time (useful for testing)."""
    global _start_time
    _start_time = time.time() * 1000
