"""
Context - Verse context management for MarkTwainVerse.

Tracks and manages the current state of the verse for narrative continuity.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Optional


@dataclass
class VerseContext:
    """
    The current context of the MarkTwainVerse.
    
    Tracks world state, visitor information, and narrative history
    to maintain continuity across interactions.
    """
    # Time and cycles
    time: datetime = field(default_factory=datetime.now)
    day_phase: float = 0.5  # 0=midnight, 0.5=noon
    season_phase: float = 0.25  # 0=spring start
    
    # Visitor state
    visitor_count: int = 0
    visitor_name: Optional[str] = None
    visitor_type: str = "tourist"  # tourist, resident, citizen
    
    # World state
    total_energy: float = 0.8
    dominant_mood: str = "active"
    
    # Hero Host state
    hero_host_animation: str = "idle-storytelling"
    hero_host_mood: str = "thriving"
    
    # Narrative history
    stories_told: int = 0
    topics_explored: list[str] = field(default_factory=list)
    last_interaction: Optional[datetime] = None
    
    # Session tracking
    session_start: datetime = field(default_factory=datetime.now)
    session_id: Optional[str] = None

    def update_time(self) -> None:
        """Update time to current."""
        self.time = datetime.now()
        self.last_interaction = datetime.now()
    
    def record_story(self, topic: str) -> None:
        """Record a story being told."""
        self.stories_told += 1
        if topic not in self.topics_explored:
            self.topics_explored.append(topic)
        self.last_interaction = datetime.now()
    
    def get_time_of_day(self) -> str:
        """Get current time of day string."""
        if self.day_phase < 0.25:
            return "night"
        elif self.day_phase < 0.5:
            return "morning"
        elif self.day_phase < 0.75:
            return "afternoon"
        else:
            return "evening"
    
    def get_season(self) -> str:
        """Get current season string."""
        if self.season_phase < 0.25:
            return "spring"
        elif self.season_phase < 0.5:
            return "summer"
        elif self.season_phase < 0.75:
            return "fall"
        else:
            return "winter"
    
    def to_dict(self) -> dict[str, Any]:
        """Convert context to dictionary."""
        return {
            "time": self.time.isoformat(),
            "day_phase": self.day_phase,
            "season_phase": self.season_phase,
            "visitor_count": self.visitor_count,
            "visitor_name": self.visitor_name,
            "visitor_type": self.visitor_type,
            "total_energy": self.total_energy,
            "dominant_mood": self.dominant_mood,
            "hero_host_animation": self.hero_host_animation,
            "hero_host_mood": self.hero_host_mood,
            "stories_told": self.stories_told,
            "topics_explored": self.topics_explored,
            "last_interaction": self.last_interaction.isoformat() if self.last_interaction else None,
            "session_start": self.session_start.isoformat(),
            "session_id": self.session_id,
        }


# Global context instance
_context: Optional[VerseContext] = None


def get_current_context() -> VerseContext:
    """
    Get the current verse context.
    
    Returns:
        The singleton VerseContext
    """
    global _context
    if _context is None:
        _context = VerseContext()
    return _context


def update_context(**kwargs: Any) -> VerseContext:
    """
    Update the current verse context.
    
    Args:
        **kwargs: Fields to update on the context
        
    Returns:
        Updated VerseContext
    """
    context = get_current_context()
    for key, value in kwargs.items():
        if hasattr(context, key):
            setattr(context, key, value)
    context.update_time()
    return context


def reset_context() -> VerseContext:
    """
    Reset context to defaults.
    
    Returns:
        Fresh VerseContext
    """
    global _context
    _context = VerseContext()
    return _context


def add_visitor(name: Optional[str] = None, visitor_type: str = "tourist") -> VerseContext:
    """
    Add a visitor to the verse.
    
    Args:
        name: Optional visitor name
        visitor_type: Type of visitor
        
    Returns:
        Updated context
    """
    context = get_current_context()
    context.visitor_count += 1
    if name:
        context.visitor_name = name
    context.visitor_type = visitor_type
    context.update_time()
    return context


def remove_visitor() -> VerseContext:
    """
    Remove a visitor from the verse.
    
    Returns:
        Updated context
    """
    context = get_current_context()
    context.visitor_count = max(0, context.visitor_count - 1)
    context.update_time()
    return context
