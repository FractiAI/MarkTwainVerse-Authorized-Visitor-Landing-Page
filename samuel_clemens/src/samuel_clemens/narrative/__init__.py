"""
Narrative module - Story context and quote management.

Contains authentic Mark Twain quotes and verse context utilities.
"""

from samuel_clemens.narrative.quotes import (
    Quote,
    get_random_quote,
    get_quote_by_context,
    get_all_quotes,
    AUTHENTIC_QUOTES,
)
from samuel_clemens.narrative.context import (
    VerseContext,
    get_current_context,
    update_context,
)

__all__ = [
    "Quote",
    "get_random_quote",
    "get_quote_by_context",
    "get_all_quotes",
    "AUTHENTIC_QUOTES",
    "VerseContext",
    "get_current_context",
    "update_context",
]
