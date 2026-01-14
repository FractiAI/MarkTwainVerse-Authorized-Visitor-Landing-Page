"""
Storyteller - Narrative generation methods for the MarkTwainVerse.

"The difference between the almost right word and the right word is really a large matter.
It's the difference between the lightning bug and the lightning." — Mark Twain
"""

from __future__ import annotations

import random
from dataclasses import dataclass
from enum import Enum
from typing import Optional

from samuel_clemens.narrative.quotes import get_random_quote, get_quote_by_context
from samuel_clemens.utils.logging import story_log


class Emotion(Enum):
    """Emotional tones for storytelling."""
    HUMOR = "humor"
    STORYTELLING = "storytelling"
    CONTEMPLATION = "contemplation"
    WISDOM = "wisdom"
    WARMTH = "warmth"
    ADVENTURE = "adventure"


@dataclass
class Story:
    """A frontier story from Mark Twain."""
    text: str
    emotion: Emotion
    topic: str
    keywords: list[str]

    def __str__(self) -> str:
        return self.text


# Story templates organized by topic
STORY_TEMPLATES: dict[str, list[str]] = {
    "frontier": [
        "Well now, let me tell you about the frontier. It's a place where every sunrise "
        "brings new possibilities and every sunset carries the promise of adventure. "
        "The frontier isn't just a place—it's a state of mind, friend.",
        "The frontier taught me one thing: life's best stories come from the places "
        "where civilization ends and possibility begins. Out here, every person writes "
        "their own chapter.",
        "You want to know about the frontier? It's where dreams go to either die or "
        "become something bigger than their dreamers ever imagined. Most folks find "
        "the latter, if they've got the gumption.",
    ],
    "adventure": [
        "Adventure, my friend, is just trouble you volunteer for. And I've volunteered "
        "for plenty! The best adventures are the ones where you don't know how they'll end "
        "until you're knee-deep in them.",
        "Every adventure starts with a single step into the unknown. The Mississippi taught "
        "me that—each bend in the river hiding something new, something unexpected, "
        "something worth writing home about.",
        "Let me tell you about adventure: it's not the destination that matters, it's the "
        "stories you collect along the way. And friend, I've collected enough to fill "
        "a library.",
    ],
    "wisdom": [
        "Wisdom comes from experience, and experience comes from bad judgment. Don't let "
        "that discourage you—some of my best wisdom came from my worst decisions!",
        "The older I get, the more I realize that wisdom isn't about having all the answers. "
        "It's about knowing which questions are worth asking.",
        "Here's a bit of wisdom from my travels: kindness is a language which the deaf can "
        "hear and the blind can see. Use it liberally.",
    ],
    "river": [
        "The river taught me everything worth knowing. It showed me that life flows in one "
        "direction, but wisdom comes from understanding the currents beneath the surface.",
        "A river pilot learns to read what can't be seen—the hidden snags, the shifting "
        "sandbars, the subtle signs of change. Life's like that too, if you pay attention.",
        "Mississippi. Just saying the word brings back a flood of memories. That river was "
        "my first teacher, my first love, and my longest friend.",
    ],
    "default": [
        "Well now, that's an interesting topic you've brought up. Reminds me of something "
        "I observed in my travels. Life has a way of teaching lessons when you least expect "
        "them, and the best stories come from listening.",
        "You know, in all my years of wandering this world—from Hannibal to Hawaii, from "
        "lecture halls to frontier towns—I've learned that every topic has a story hiding "
        "inside it, waiting to be told.",
    ],
}

# Wisdom snippets for quick insights
WISDOM_SNIPPETS: list[str] = [
    "The secret of getting ahead is getting started.",
    "Continuous improvement is better than delayed perfection.",
    "Courage is resistance to fear, mastery of fear—not absence of fear.",
    "The man who does not read has no advantage over the man who cannot read.",
    "Kindness is a language which the deaf can hear and the blind can see.",
    "Whenever you find yourself on the side of the majority, it is time to pause and reflect.",
    "A person with a new idea is a crank until the idea succeeds.",
    "The lack of money is the root of all evil.",
    "The best way to cheer yourself is to try to cheer someone else up.",
    "Good friends, good books, and a sleepy conscience: this is the ideal life.",
]


def tell_story(
    topic: str = "default",
    emotion: Optional[Emotion] = None,
    include_quote: bool = True,
) -> Story:
    """
    Generate a frontier story on the given topic.
    
    Like a riverboat pilot reading the currents, this method navigates
    through the narrative landscape to find the right story for the moment.
    
    Args:
        topic: The subject matter for the story (frontier, adventure, wisdom, river)
        emotion: Optional emotional tone override
        include_quote: Whether to include an authentic Twain quote
        
    Returns:
        A Story object containing the narrative
    """
    # Get story templates for this topic
    templates = STORY_TEMPLATES.get(topic.lower(), STORY_TEMPLATES["default"])
    text = random.choice(templates)
    
    # Add authentic quote if requested
    if include_quote:
        quote = get_random_quote()
        text = f'{text}\n\nAs I once said: "{quote.text}"'
    
    # Determine emotion
    if emotion is None:
        emotion_map = {
            "frontier": Emotion.ADVENTURE,
            "adventure": Emotion.ADVENTURE,
            "wisdom": Emotion.WISDOM,
            "river": Emotion.CONTEMPLATION,
            "default": Emotion.STORYTELLING,
        }
        emotion = emotion_map.get(topic.lower(), Emotion.STORYTELLING)
    
    story = Story(
        text=text,
        emotion=emotion,
        topic=topic,
        keywords=[topic, emotion.value, "frontier", "twain"],
    )
    
    story_log(f"📖 Story generated: {topic}")
    return story


def spin_yarn(
    topics: list[str],
    length: str = "medium",
) -> Story:
    """
    Spin an extended yarn combining multiple topics.
    
    A yarn is a tall tale, woven from threads of multiple topics
    into something larger than its parts.
    
    Args:
        topics: List of topics to weave together
        length: Desired length (short, medium, long)
        
    Returns:
        A Story object containing the extended narrative
    """
    # Collect stories from each topic
    story_parts: list[str] = []
    
    length_limits = {"short": 1, "medium": 2, "long": 3}
    limit = length_limits.get(length, 2)
    
    for topic in topics[:limit]:
        templates = STORY_TEMPLATES.get(topic.lower(), STORY_TEMPLATES["default"])
        story_parts.append(random.choice(templates))
    
    # Weave together with transitions
    transitions = [
        "And that reminds me of something else...",
        "Which brings me to another tale...",
        "Speaking of which...",
        "Now, here's where it gets interesting...",
    ]
    
    full_text = ""
    for i, part in enumerate(story_parts):
        if i > 0:
            full_text += f"\n\n{random.choice(transitions)}\n\n"
        full_text += part
    
    story = Story(
        text=full_text,
        emotion=Emotion.STORYTELLING,
        topic=", ".join(topics),
        keywords=topics + ["yarn", "frontier", "twain"],
    )
    
    story_log(f"🧶 Yarn spun: {', '.join(topics)}")
    return story


def frontier_wisdom() -> str:
    """
    Dispense a nugget of frontier wisdom.
    
    Quick wisdom for the weary traveler—a single insight
    to light the path forward.
    
    Returns:
        A wisdom snippet from Mark Twain
    """
    wisdom = random.choice(WISDOM_SNIPPETS)
    story_log(f"💡 Wisdom dispensed")
    return wisdom


def get_story_for_context(context: str) -> Story:
    """
    Generate a context-appropriate story.
    
    Analyzes the context string and selects the most appropriate
    story topic and emotional tone.
    
    Args:
        context: Descriptive context for story selection
        
    Returns:
        A Story matched to the context
    """
    # Simple keyword matching for context
    context_lower = context.lower()
    
    topic = "default"
    if any(word in context_lower for word in ["adventure", "journey", "explore"]):
        topic = "adventure"
    elif any(word in context_lower for word in ["river", "mississippi", "water", "boat"]):
        topic = "river"
    elif any(word in context_lower for word in ["frontier", "west", "pioneer"]):
        topic = "frontier"
    elif any(word in context_lower for word in ["wisdom", "advice", "learn"]):
        topic = "wisdom"
    
    return tell_story(topic=topic)
