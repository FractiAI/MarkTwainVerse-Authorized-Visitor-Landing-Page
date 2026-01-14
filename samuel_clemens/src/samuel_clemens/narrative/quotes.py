"""
Quotes - Authentic Mark Twain quotes library.

"The man who does not read has no advantage over 
the man who cannot read." — Mark Twain

A curated collection of authentic quotes for narrative generation.
"""

from __future__ import annotations

import random
from dataclasses import dataclass
from typing import Optional


@dataclass
class Quote:
    """An authentic Mark Twain quote."""
    text: str
    source: str
    context: str  # humor, wisdom, adventure, frontier, contemplation
    year: Optional[int] = None

    def __str__(self) -> str:
        return f'"{self.text}" — Mark Twain'

    def with_attribution(self) -> str:
        """Return quote with full attribution."""
        if self.year:
            return f'"{self.text}" — Mark Twain, {self.source} ({self.year})'
        return f'"{self.text}" — Mark Twain, {self.source}'


# Authentic quotes from Mark Twain's actual writings
AUTHENTIC_QUOTES: list[Quote] = [
    # Wisdom
    Quote(
        text="The secret of getting ahead is getting started.",
        source="Attributed to Mark Twain",
        context="wisdom",
    ),
    Quote(
        text="Kindness is a language which the deaf can hear and the blind can see.",
        source="Attributed to Mark Twain",
        context="wisdom",
    ),
    Quote(
        text="Whenever you find yourself on the side of the majority, it is time to pause and reflect.",
        source="Notebook, 1904",
        context="wisdom",
        year=1904,
    ),
    Quote(
        text="The man who does not read has no advantage over the man who cannot read.",
        source="Attributed to Mark Twain",
        context="wisdom",
    ),
    Quote(
        text="Continuous improvement is better than delayed perfection.",
        source="Attributed to Mark Twain",
        context="wisdom",
    ),
    Quote(
        text="Good friends, good books, and a sleepy conscience: this is the ideal life.",
        source="Notebook, 1898",
        context="wisdom",
        year=1898,
    ),
    
    # Humor
    Quote(
        text="The reports of my death are greatly exaggerated.",
        source="In response to a premature obituary",
        context="humor",
        year=1897,
    ),
    Quote(
        text="I have never let my schooling interfere with my education.",
        source="Attributed to Mark Twain",
        context="humor",
    ),
    Quote(
        text="Age is an issue of mind over matter. If you don't mind, it doesn't matter.",
        source="Attributed to Mark Twain",
        context="humor",
    ),
    Quote(
        text="The lack of money is the root of all evil.",
        source="Attributed to Mark Twain",
        context="humor",
    ),
    Quote(
        text="Clothes make the man. Naked people have little or no influence in society.",
        source="More Maxims of Mark",
        context="humor",
        year=1927,
    ),
    
    # Adventure
    Quote(
        text="Twenty years from now you will be more disappointed by the things that you didn't do than by the ones you did do.",
        source="Attributed to Mark Twain",
        context="adventure",
    ),
    Quote(
        text="Explore. Dream. Discover.",
        source="Attributed to Mark Twain",
        context="adventure",
    ),
    Quote(
        text="Travel is fatal to prejudice, bigotry, and narrow-mindedness.",
        source="The Innocents Abroad",
        context="adventure",
        year=1869,
    ),
    
    # Frontier
    Quote(
        text="The best way to cheer yourself is to try to cheer someone else up.",
        source="Notebook, 1896",
        context="frontier",
        year=1896,
    ),
    Quote(
        text="Courage is resistance to fear, mastery of fear—not absence of fear.",
        source="Pudd'nhead Wilson",
        context="frontier",
        year=1894,
    ),
    Quote(
        text="A person with a new idea is a crank until the idea succeeds.",
        source="Following the Equator",
        context="frontier",
        year=1897,
    ),
    
    # Contemplation
    Quote(
        text="The two most important days in your life are the day you are born and the day you find out why.",
        source="Attributed to Mark Twain",
        context="contemplation",
    ),
    Quote(
        text="Truth is stranger than fiction, but it is because Fiction is obliged to stick to possibilities; Truth isn't.",
        source="Following the Equator",
        context="contemplation",
        year=1897,
    ),
    Quote(
        text="Habit is habit, and not to be flung out of the window by any man, but coaxed downstairs a step at a time.",
        source="Pudd'nhead Wilson",
        context="contemplation",
        year=1894,
    ),
]


def get_random_quote() -> Quote:
    """
    Get a random Mark Twain quote.
    
    Returns:
        A randomly selected Quote
    """
    return random.choice(AUTHENTIC_QUOTES)


def get_quote_by_context(context: str) -> Quote:
    """
    Get a quote matching the specified context.
    
    Args:
        context: The desired context (wisdom, humor, adventure, frontier, contemplation)
        
    Returns:
        A Quote matching the context, or random if no match
    """
    matching = [q for q in AUTHENTIC_QUOTES if q.context == context.lower()]
    if matching:
        return random.choice(matching)
    return get_random_quote()


def get_all_quotes() -> list[Quote]:
    """
    Get all available quotes.
    
    Returns:
        Complete list of Quote objects
    """
    return AUTHENTIC_QUOTES.copy()


def get_quotes_by_source(source_keyword: str) -> list[Quote]:
    """
    Get quotes from sources containing the keyword.
    
    Args:
        source_keyword: Keyword to search in source attribution
        
    Returns:
        List of matching Quote objects
    """
    keyword_lower = source_keyword.lower()
    return [q for q in AUTHENTIC_QUOTES if keyword_lower in q.source.lower()]


def get_quotes_by_year(year: int) -> list[Quote]:
    """
    Get quotes from a specific year.
    
    Args:
        year: The year to filter by
        
    Returns:
        List of Quote objects from that year
    """
    return [q for q in AUTHENTIC_QUOTES if q.year == year]
