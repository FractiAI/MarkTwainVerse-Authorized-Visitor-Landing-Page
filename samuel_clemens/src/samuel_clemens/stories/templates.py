"""
Story Templates - Narrative structure templates for story generation.

Pre-built story frameworks that can be filled with elements.
"""

from __future__ import annotations

import random
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, Callable

from samuel_clemens.stories.elements import (
    Character,
    Setting,
    PlotPoint,
    Theme,
    get_random_character,
    get_random_setting,
    get_random_theme,
)


class TemplateType(Enum):
    """Types of story templates."""
    ADVENTURE = "adventure"
    WISDOM = "wisdom"
    HUMOR = "humor"
    MYSTERY = "mystery"
    FRONTIER = "frontier"
    RIVER = "river"
    CAMPFIRE = "campfire"


@dataclass
class StoryTemplate:
    """
    A template for generating stories.
    
    Contains structure, required elements, and generation logic.
    """
    name: str
    template_type: TemplateType
    description: str
    structure: list[str]  # List of section markers
    required_elements: list[str]  # character, setting, theme, etc.
    opening_patterns: list[str]
    middle_patterns: list[str]
    closing_patterns: list[str]
    mood: str = "neutral"
    min_length: int = 100
    max_length: int = 500
    
    def generate(
        self,
        character: Optional[Character] = None,
        setting: Optional[Setting] = None,
        theme: Optional[Theme] = None,
    ) -> str:
        """
        Generate a story using this template.
        
        Args:
            character: Optional character to use
            setting: Optional setting to use
            theme: Optional theme to use
            
        Returns:
            Generated story text
        """
        # Get random elements if not provided
        char = character or get_random_character()
        loc = setting or get_random_setting()
        th = theme or get_random_theme()
        
        # Select patterns
        opening = random.choice(self.opening_patterns)
        middle = random.choice(self.middle_patterns)
        closing = random.choice(self.closing_patterns)
        
        # Fill in templates
        story_parts = []
        
        # Opening
        story_parts.append(
            opening.format(
                character=char.name,
                setting=loc.name,
                theme=th.name,
                character_desc=char.description,
                setting_desc=loc.description,
            )
        )
        
        # Middle
        story_parts.append(
            middle.format(
                character=char.name,
                setting=loc.name,
                theme=th.name,
            )
        )
        
        # Closing
        story_parts.append(
            closing.format(
                character=char.name,
                setting=loc.name,
                theme=th.name,
            )
        )
        
        return " ".join(story_parts)


# Pre-built templates
TEMPLATES: dict[str, StoryTemplate] = {
    "frontier_tale": StoryTemplate(
        name="Frontier Tale",
        template_type=TemplateType.FRONTIER,
        description="A classic frontier adventure story",
        structure=["opening", "journey", "challenge", "resolution"],
        required_elements=["character", "setting"],
        opening_patterns=[
            "It was on {setting} that {character} first learned what frontier life truly meant.",
            "They say {character} came to {setting} looking for one thing but found something else entirely.",
            "The day {character} arrived at {setting}, nobody knew the world was about to change.",
        ],
        middle_patterns=[
            "What happened next would become legend in those parts. {character} faced trials that would break lesser souls.",
            "The frontier has a way of testing people, and {character} was tested mightily.",
            "Day after day, the challenges mounted. But {character} had something the frontier couldn't take away.",
        ],
        closing_patterns=[
            "In the end, {character} understood what the old-timers meant about {theme}. Some lessons only the frontier can teach.",
            "Years later, folks still tell the tale. And if you listen close, you can hear the wisdom in it.",
            "That's how {character} came to understand the truth about life on the frontier.",
        ],
        mood="adventurous",
    ),
    
    "river_story": StoryTemplate(
        name="River Story",
        template_type=TemplateType.RIVER,
        description="A tale of life on the Mississippi",
        structure=["departure", "journey", "revelation", "return"],
        required_elements=["character", "theme"],
        opening_patterns=[
            "The river was running high when {character} set out, like life itself pushing toward something new.",
            "Nobody knows the river like {character} knew it—every bend, every sandbar, every secret.",
            "There's a saying on the Mississippi: the river takes more than it gives. {character} learned that truth.",
        ],
        middle_patterns=[
            "Mile after mile, the current carried them forward. And with each mile, {character} understood a little more.",
            "The river doesn't care about your plans. It flows where it will, and {character} had to flow with it.",
            "Between the shores, {character} found space to think about {theme} in ways never possible on land.",
        ],
        closing_patterns=[
            "When the journey ended, {character} stepped ashore a different person. The river had worked its changes.",
            "They say {character} was never quite the same after that voyage. But then, who would be?",
            "The river gave {character} exactly what was needed—not what was wanted, but what was needed.",
        ],
        mood="contemplative",
    ),
    
    "campfire_yarn": StoryTemplate(
        name="Campfire Yarn",
        template_type=TemplateType.CAMPFIRE,
        description="A tall tale for fireside telling",
        structure=["setup", "exaggeration", "punchline"],
        required_elements=["character"],
        opening_patterns=[
            "Now, I'm going to tell you about {character}, and every word of this is true—mostly.",
            "Gather 'round, because this tale about {character} is one you won't believe—until you do.",
            "Did I ever tell you about {character}? No? Well, pull up closer to the fire.",
        ],
        middle_patterns=[
            "Now, {character} wasn't ordinary by any measure. Ask anyone who knew them. I say that's underselling it.",
            "The thing about {character} was this: nothing was ever simple, and everything was twice as big.",
            "What {character} did next would make a lesser storyteller refuse to tell it. But I'm not a lesser storyteller.",
        ],
        closing_patterns=[
            "And that, friends, is the honest truth about {character}. Well, mostly honest. The fire's burning low, so that'll have to do.",
            "Believe it or don't—but I was there, and I saw it with my own two eyes. Goodnight, now.",
            "Now, you might think I'm exaggerating. But the frontier was a place where exaggeration was just good reporting.",
        ],
        mood="humorous",
    ),
    
    "wisdom_piece": StoryTemplate(
        name="Wisdom Piece",
        template_type=TemplateType.WISDOM,
        description="A contemplative piece on life lessons",
        structure=["observation", "reflection", "insight"],
        required_elements=["theme"],
        opening_patterns=[
            "I've been thinking about {theme} lately. Not because I have answers, but because the questions won't leave me alone.",
            "There's something about {theme} that the young can't understand. You have to live a while to see it clearly.",
            "Let me tell you what I've learned about {theme}—and more importantly, what I've unlearned.",
        ],
        middle_patterns=[
            "See, {theme} isn't what most people think. It's slipperier than that, and more honest.",
            "I used to believe one thing about {theme}. Now I believe something closer to its opposite.",
            "The truth about {theme} is that it changes depending on where you're standing.",
        ],
        closing_patterns=[
            "Maybe I'm wrong. I've been wrong before, and I expect I'll be wrong again. But this feels true.",
            "Take it or leave it—that's what the years have taught me about {theme}.",
            "In the end, {theme} is simpler than we make it. And harder than we admit.",
        ],
        mood="contemplative",
    ),
    
    "adventure_quest": StoryTemplate(
        name="Adventure Quest",
        template_type=TemplateType.ADVENTURE,
        description="An action-packed adventure story",
        structure=["call", "journey", "trials", "triumph"],
        required_elements=["character", "setting"],
        opening_patterns=[
            "When {character} heard about what lay hidden at {setting}, there was no question—the adventure had to begin.",
            "Some folks are content to stay home. {character} was not that kind of folk.",
            "The map showed {setting}, but what it didn't show was the danger—and the glory.",
        ],
        middle_patterns=[
            "Adventure isn't for the faint of heart, and {character} learned that quickly. But quitting wasn't an option.",
            "Every obstacle at {setting} seemed designed to turn {character} back. Every obstacle failed.",
            "The journey tested every skill, every belief, every breath. And {character} kept moving forward.",
        ],
        closing_patterns=[
            "When {character} finally reached the goal, it was different than expected—better in some ways, stranger in others.",
            "Victory has a taste, and {character} had earned it. The adventure was over, but the stories had just begun.",
            "Some adventures change the world. This one changed {character}—and that was enough.",
        ],
        mood="exciting",
    ),
    
    "mystery_tale": StoryTemplate(
        name="Mystery Tale",
        template_type=TemplateType.MYSTERY,
        description="A mysterious frontier tale",
        structure=["question", "investigation", "revelation"],
        required_elements=["character", "setting"],
        opening_patterns=[
            "Something wasn't right at {setting}. {character} could feel it before there was proof.",
            "The mystery of {setting} had puzzled folks for years. Then {character} started asking questions.",
            "When {character} arrived at {setting}, the silence was the first clue that something was wrong.",
        ],
        middle_patterns=[
            "Every answer led to more questions. {character} dug deeper, despite the warnings.",
            "The truth about {setting} was buried deep, but {character} was used to digging.",
            "Piece by piece, the puzzle came together. And the picture it made was unsettling.",
        ],
        closing_patterns=[
            "When {character} finally understood, everything made sense—terrible, perfect sense.",
            "Some mysteries are better left unsolved. This wasn't one of them.",
            "The truth about {setting} changed everything. And {character} had to decide what to do with it.",
        ],
        mood="mysterious",
    ),
}


def get_template(name: str) -> Optional[StoryTemplate]:
    """
    Get a template by name.
    
    Args:
        name: Template name
        
    Returns:
        Template if found, None otherwise
    """
    return TEMPLATES.get(name)


def list_templates() -> list[str]:
    """
    Get list of available template names.
    
    Returns:
        List of template names
    """
    return list(TEMPLATES.keys())


def get_templates_by_type(template_type: TemplateType) -> list[StoryTemplate]:
    """
    Get all templates of a specific type.
    
    Args:
        template_type: Type to filter by
        
    Returns:
        List of matching templates
    """
    return [t for t in TEMPLATES.values() if t.template_type == template_type]


def create_from_template(
    template_name: str,
    character: Optional[Character] = None,
    setting: Optional[Setting] = None,
    theme: Optional[Theme] = None,
) -> Optional[str]:
    """
    Create a story from a named template.
    
    Args:
        template_name: Name of the template to use
        character: Optional character
        setting: Optional setting
        theme: Optional theme
        
    Returns:
        Generated story or None if template not found
    """
    template = get_template(template_name)
    if template:
        return template.generate(character, setting, theme)
    return None


def get_random_template() -> StoryTemplate:
    """
    Get a random story template.
    
    Returns:
        Random template
    """
    return random.choice(list(TEMPLATES.values()))
