"""
Emoji Processing - Extract and analyze emoji usage in documents.

"The human race has only one really effective weapon and that is laughter."
— Mark Twain
"""

from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass, field
from typing import Optional
from collections import Counter


@dataclass
class EmojiInfo:
    """Information about an emoji character."""
    char: str
    name: str
    category: str
    count: int = 1
    positions: list[int] = field(default_factory=list)
    
    @property
    def code_point(self) -> str:
        """Unicode code point."""
        return f"U+{ord(self.char):04X}"
    
    def __str__(self) -> str:
        return f"{self.char} ({self.name})"


# Emoji category mappings
EMOJI_CATEGORIES = {
    # Status/Action emojis
    "✅": ("checkmark", "status"),
    "❌": ("cross", "status"),
    "⚠️": ("warning", "status"),
    "🚨": ("alert", "status"),
    "💡": ("idea", "status"),
    "🔘": ("button", "status"),
    
    # Objects/Symbols
    "💎": ("gem", "symbol"),
    "⭐": ("star", "symbol"),
    "🌟": ("glowing_star", "symbol"),
    "✨": ("sparkles", "symbol"),
    "🎯": ("target", "symbol"),
    "🔗": ("link", "symbol"),
    "📊": ("chart", "symbol"),
    "📝": ("memo", "symbol"),
    "📖": ("book", "symbol"),
    "📚": ("books", "symbol"),
    "📜": ("scroll", "symbol"),
    "🗺️": ("map", "symbol"),
    "🗂️": ("folder", "symbol"),
    
    # Nature/Weather
    "🌅": ("sunrise", "nature"),
    "🌙": ("moon", "nature"),
    "⛅": ("cloudy", "nature"),
    "🌊": ("wave", "nature"),
    "🔥": ("fire", "nature"),
    "💧": ("drop", "nature"),
    
    # Structures/Buildings
    "🏗️": ("construction", "structure"),
    "🏛️": ("building", "structure"),
    "🏆": ("trophy", "structure"),
    "🔔": ("bell", "structure"),
    
    # Transportation
    "🚀": ("rocket", "transport"),
    "🌐": ("globe", "transport"),
    "🎬": ("camera", "media"),
    
    # People/Characters
    "🎩": ("hat", "character"),
    "🎭": ("masks", "character"),
    "👤": ("person", "character"),
    "💤": ("sleep", "character"),
    "😊": ("smile", "character"),
    "😃": ("happy", "character"),
    "😴": ("sleeping", "character"),
    
    # Cycle/Process
    "🔄": ("cycle", "process"),
    "⚡": ("lightning", "process"),
    "🔒": ("lock", "process"),
    "🔓": ("unlock", "process"),
}


def _is_emoji(char: str) -> bool:
    """Check if character is an emoji."""
    if len(char) == 0:
        return False
    
    # Check for known emojis first
    if char in EMOJI_CATEGORIES:
        return True
    
    # Check unicode category
    try:
        cat = unicodedata.category(char[0])
        # Symbol, Other (So) often contains emojis
        if cat == "So":
            return True
        # Check for emoji presentation
        name = unicodedata.name(char[0], "")
        if any(word in name.upper() for word in ["EMOJI", "FACE", "HAND", "STAR"]):
            return True
    except (ValueError, TypeError):
        pass
    
    # Check code point ranges for common emoji blocks
    code_point = ord(char[0])
    emoji_ranges = [
        (0x1F300, 0x1F9FF),  # Miscellaneous Symbols and Pictographs, Emoticons, etc.
        (0x2600, 0x26FF),    # Miscellaneous Symbols
        (0x2700, 0x27BF),    # Dingbats
        (0x1F600, 0x1F64F),  # Emoticons
        (0x1F680, 0x1F6FF),  # Transport and Map Symbols
    ]
    
    for start, end in emoji_ranges:
        if start <= code_point <= end:
            return True
    
    return False


def extract_emojis(text: str) -> list[EmojiInfo]:
    """
    Extract all emojis from text with their positions.
    
    Args:
        text: Text to analyze
        
    Returns:
        List of EmojiInfo objects
    """
    emoji_dict: dict[str, EmojiInfo] = {}
    
    # Handle multi-character emojis (like flag sequences)
    # and variation selectors
    i = 0
    while i < len(text):
        char = text[i]
        
        # Check for multi-char emoji (up to 4 chars for complex emojis)
        emoji_found = None
        for length in range(4, 0, -1):
            if i + length <= len(text):
                candidate = text[i:i+length]
                if candidate in EMOJI_CATEGORIES or (length == 1 and _is_emoji(candidate)):
                    emoji_found = candidate
                    break
        
        if emoji_found:
            if emoji_found in emoji_dict:
                emoji_dict[emoji_found].count += 1
                emoji_dict[emoji_found].positions.append(i)
            else:
                # Get emoji info
                name_parts = EMOJI_CATEGORIES.get(emoji_found, (None, None))
                if name_parts[0]:
                    name, category = name_parts
                else:
                    try:
                        name = unicodedata.name(emoji_found[0], "unknown").lower()
                    except ValueError:
                        name = "unknown"
                    category = "other"
                
                emoji_dict[emoji_found] = EmojiInfo(
                    char=emoji_found,
                    name=name,
                    category=category,
                    count=1,
                    positions=[i],
                )
            i += len(emoji_found)
        else:
            i += 1
    
    return list(emoji_dict.values())


def count_emojis(text: str) -> int:
    """Count total emojis in text."""
    return sum(e.count for e in extract_emojis(text))


def analyze_emoji_usage(text: str) -> dict[str, any]:
    """
    Analyze emoji usage patterns in text.
    
    Args:
        text: Text to analyze
        
    Returns:
        Dictionary with analysis results
    """
    emojis = extract_emojis(text)
    
    # Count by category
    category_counts: Counter = Counter()
    for emoji in emojis:
        category_counts[emoji.category] += emoji.count
    
    # Find most common
    all_emojis = [(e.char, e.count) for e in emojis]
    all_emojis.sort(key=lambda x: -x[1])
    
    # Calculate emoji density
    total_chars = len(text)
    total_emojis = sum(e.count for e in emojis)
    emoji_density = total_emojis / total_chars if total_chars > 0 else 0
    
    return {
        "total_count": total_emojis,
        "unique_count": len(emojis),
        "emoji_density": emoji_density,
        "by_category": dict(category_counts),
        "most_common": all_emojis[:10],
        "emojis": emojis,
    }


def emoji_to_text(emoji_char: str) -> str:
    """
    Convert emoji to text description.
    
    Args:
        emoji_char: Single emoji character
        
    Returns:
        Text description
    """
    if emoji_char in EMOJI_CATEGORIES:
        return EMOJI_CATEGORIES[emoji_char][0]
    
    try:
        return unicodedata.name(emoji_char[0], "unknown").lower().replace("_", " ")
    except (ValueError, TypeError):
        return "unknown"


def get_emoji_categories() -> dict[str, list[str]]:
    """
    Get emojis organized by category.
    
    Returns:
        Dictionary mapping category to list of emojis
    """
    categories: dict[str, list[str]] = {}
    
    for emoji, (name, category) in EMOJI_CATEGORIES.items():
        if category not in categories:
            categories[category] = []
        categories[category].append(emoji)
    
    return categories


def replace_emojis_with_text(text: str, format: str = "brackets") -> str:
    """
    Replace all emojis with text descriptions.
    
    Args:
        text: Text with emojis
        format: 'brackets' for [emoji_name], 'colon' for :emoji_name:
        
    Returns:
        Text with emojis replaced
    """
    emojis = extract_emojis(text)
    
    # Sort by position descending to maintain positions
    all_positions = []
    for emoji in emojis:
        for pos in emoji.positions:
            all_positions.append((pos, len(emoji.char), emoji.name))
    
    all_positions.sort(key=lambda x: -x[0])
    
    result = text
    for pos, length, name in all_positions:
        if format == "brackets":
            replacement = f"[{name}]"
        else:
            replacement = f":{name}:"
        result = result[:pos] + replacement + result[pos+length:]
    
    return result


def strip_emojis(text: str) -> str:
    """Remove all emojis from text."""
    emojis = extract_emojis(text)
    
    # Sort by position descending
    all_positions = []
    for emoji in emojis:
        for pos in emoji.positions:
            all_positions.append((pos, len(emoji.char)))
    
    all_positions.sort(key=lambda x: -x[0])
    
    result = text
    for pos, length in all_positions:
        result = result[:pos] + result[pos+length:]
    
    return result
