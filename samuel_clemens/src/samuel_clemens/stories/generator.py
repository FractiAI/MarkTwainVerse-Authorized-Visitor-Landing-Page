"""
Story Generator - Advanced story generation engine.

Creates complete stories using templates, elements, and Twain's style.
"""

from __future__ import annotations

import random
from dataclasses import dataclass, field
from typing import Optional

from samuel_clemens.stories.elements import (
    Character,
    Setting,
    Theme,
    PlotPoint,
    get_random_character,
    get_random_setting,
    get_random_theme,
    get_random_plot_point,
    get_random_elements,
    CHARACTERS,
    SETTINGS,
    THEMES,
)
from samuel_clemens.stories.templates import (
    StoryTemplate,
    get_template,
    get_random_template,
    create_from_template,
    TEMPLATES,
)
from samuel_clemens.narrative.quotes import get_random_quote, get_quote_by_context
from samuel_clemens.core.storyteller import Story, Emotion
from samuel_clemens.utils.logging import story_log


@dataclass
class GeneratedStory:
    """A story produced by the generator."""
    text: str
    title: str
    template_used: Optional[str] = None
    character: Optional[Character] = None
    setting: Optional[Setting] = None
    theme: Optional[Theme] = None
    word_count: int = 0
    emotion: Emotion = Emotion.STORYTELLING
    quote: Optional[Any] = None  # Quote object
    
    def __post_init__(self) -> None:
        self.word_count = len(self.text.split())
    
    def to_story(self) -> Story:
        """Convert to base Story object."""
        return Story(
            text=self.text,
            emotion=self.emotion,
            topic=self.title,
            keywords=[
                self.template_used or "custom",
                self.character.name if self.character else "unknown",
                self.theme.name if self.theme else "general",
            ],
        )


class StoryGenerator:
    """
    Advanced story generation engine.
    
    Combines templates, elements, and Twain's storytelling style
    to create unique frontier tales.
    """
    
    def __init__(self) -> None:
        self.templates = TEMPLATES
        self.characters = CHARACTERS
        self.settings = SETTINGS
        self.themes = THEMES
        self._story_count = 0
    
    def generate(
        self,
        template_name: Optional[str] = None,
        character: Optional[Character] = None,
        setting: Optional[Setting] = None,
        theme: Optional[Theme] = None,
        include_quote: bool = True,
        dramatic: bool = False,
    ) -> GeneratedStory:
        """
        Generate a complete story.
        
        Args:
            template_name: Specific template to use (random if None)
            character: Specific character (random if None)
            setting: Specific setting (random if None)
            theme: Specific theme (random if None)
            include_quote: Include a Twain quote at the end
            dramatic: Add dramatic flourishes
            
        Returns:
            GeneratedStory with full text
        """
        # Select template
        if template_name:
            template = get_template(template_name)
            if template is None:
                template = get_random_template()
        else:
            template = get_random_template()
        
        # Generate base story
        story_text = template.generate(character, setting, theme)
        
        # Generate title
        title = self._generate_title(template, character, setting)
        
        # Add dramatic elements if requested
        if dramatic:
            story_text = self._add_dramatic_elements(story_text)
        
        # Add quote if requested
        quote = None
        if include_quote:
            quote = get_random_quote()
            story_text += f'\n\nAs I always say: "{quote.text}"'
        
        # Determine emotion
        emotion = self._determine_emotion(template)
        
        self._story_count += 1
        story_log(f"📖 Generated story #{self._story_count}: {title}")
        
        return GeneratedStory(
            text=story_text,
            title=title,
            template_used=template.name,
            character=character or get_random_character(),
            setting=setting or get_random_setting(),
            theme=theme or get_random_theme(),
            emotion=emotion,
            quote=quote,
        )
    
    def generate_batch(self, count: int = 3) -> list[GeneratedStory]:
        """
        Generate multiple stories.
        
        Args:
            count: Number of stories to generate
            
        Returns:
            List of generated stories
        """
        return [self.generate() for _ in range(count)]
    
    def generate_themed(self, theme_name: str) -> GeneratedStory:
        """
        Generate a story around a specific theme.
        
        Args:
            theme_name: Theme to center the story around
            
        Returns:
            GeneratedStory focused on the theme
        """
        # Find matching theme
        theme = next(
            (t for t in self.themes if theme_name.lower() in t.name.lower()),
            get_random_theme(),
        )
        
        return self.generate(theme=theme)
    
    def generate_character_story(self, character_name: str) -> GeneratedStory:
        """
        Generate a story featuring a specific character.
        
        Args:
            character_name: Character to feature
            
        Returns:
            GeneratedStory featuring the character
        """
        # Find matching character
        character = next(
            (c for c in self.characters if character_name.lower() in c.name.lower()),
            get_random_character(),
        )
        
        return self.generate(character=character)
    
    def generate_sequel(self, previous: GeneratedStory) -> GeneratedStory:
        """
        Generate a sequel to an existing story.
        
        Args:
            previous: Story to continue
            
        Returns:
            Sequel story
        """
        # Use same character and setting but different template
        # Find template key by matching display name
        template_keys = list(TEMPLATES.keys())
        new_template_key = random.choice(template_keys)
        
        # Try to pick a different template
        attempts = 0
        while TEMPLATES[new_template_key].name == previous.template_used and attempts < 10:
            new_template_key = random.choice(template_keys)
            attempts += 1
        
        sequel = self.generate(
            template_name=new_template_key,
            character=previous.character,
            setting=previous.setting,
        )
        
        sequel.title = f"{previous.title} - Part II"
        return sequel
    
    def _generate_title(
        self,
        template: StoryTemplate,
        character: Optional[Character],
        setting: Optional[Setting],
    ) -> str:
        """Generate a title for the story."""
        title_patterns = [
            "The Tale of {character}",
            "{character} at {setting}",
            "A {mood} Story",
            "{character}'s Journey",
            "The {setting} Adventure",
            "{character} and the {theme}",
        ]
        
        pattern = random.choice(title_patterns)
        
        # Fill in what we have
        char_name = character.name if character else "A Stranger"
        set_name = setting.name if setting else "the Frontier"
        
        title = pattern.format(
            character=char_name,
            setting=set_name,
            mood=template.mood.title(),
            theme="Mystery",
        )
        
        return title
    
    def _add_dramatic_elements(self, text: str) -> str:
        """Add dramatic flourishes to the story."""
        # Add dramatic opening
        openings = [
            "Listen close, for this tale is not for the faint of heart.\n\n",
            "What I'm about to tell you will change how you see the world.\n\n",
            "This is a story they tried to keep quiet. But truth will out.\n\n",
        ]
        
        # Add dramatic closing
        closings = [
            "\n\nAnd so it was. And so it remains. And so it shall always be.",
            "\n\nDraw your own conclusions. I've told you what I saw.",
            "\n\nThe fire's burning low now. Time to carry this story home.",
        ]
        
        return random.choice(openings) + text + random.choice(closings)
    
    def _determine_emotion(self, template: StoryTemplate) -> Emotion:
        """Determine the emotional tone from the template."""
        mood_to_emotion = {
            "adventurous": Emotion.ADVENTURE,
            "contemplative": Emotion.CONTEMPLATION,
            "humorous": Emotion.HUMOR,
            "exciting": Emotion.ADVENTURE,
            "mysterious": Emotion.STORYTELLING,
            "neutral": Emotion.STORYTELLING,
        }
        return mood_to_emotion.get(template.mood, Emotion.STORYTELLING)


# Convenience functions
def generate_frontier_tale(
    character: Optional[Character] = None,
    setting: Optional[Setting] = None,
) -> GeneratedStory:
    """
    Generate a frontier tale.
    
    Args:
        character: Optional character
        setting: Optional setting
        
    Returns:
        Generated frontier story
    """
    generator = StoryGenerator()
    return generator.generate(
        template_name="frontier_tale",
        character=character,
        setting=setting,
    )


def generate_adventure(
    character: Optional[Character] = None,
    dramatic: bool = True,
) -> GeneratedStory:
    """
    Generate an adventure story.
    
    Args:
        character: Optional character
        dramatic: Include dramatic elements
        
    Returns:
        Generated adventure story
    """
    generator = StoryGenerator()
    return generator.generate(
        template_name="adventure_quest",
        character=character,
        dramatic=dramatic,
    )


def generate_wisdom_piece(theme: Optional[Theme] = None) -> GeneratedStory:
    """
    Generate a wisdom/reflection piece.
    
    Args:
        theme: Optional theme to reflect on
        
    Returns:
        Generated wisdom piece
    """
    generator = StoryGenerator()
    return generator.generate(
        template_name="wisdom_piece",
        theme=theme,
    )


def generate_campfire_yarn(character: Optional[Character] = None) -> GeneratedStory:
    """
    Generate a campfire tall tale.
    
    Args:
        character: Optional character to feature
        
    Returns:
        Generated yarn
    """
    generator = StoryGenerator()
    return generator.generate(
        template_name="campfire_yarn",
        character=character,
    )


def generate_river_story() -> GeneratedStory:
    """
    Generate a Mississippi river story.
    
    Returns:
        Generated river story
    """
    generator = StoryGenerator()
    return generator.generate(template_name="river_story")


def generate_mystery() -> GeneratedStory:
    """
    Generate a mystery tale.
    
    Returns:
        Generated mystery
    """
    generator = StoryGenerator()
    return generator.generate(template_name="mystery_tale")
