"""
Story Recombinator - Blend, mashup, and recombine stories.

Creates new narratives by combining elements from multiple sources.
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
    get_random_elements,
    get_compatible_elements,
    CHARACTERS,
    SETTINGS,
    THEMES,
    PLOT_POINTS,
)
from samuel_clemens.stories.generator import GeneratedStory, StoryGenerator
from samuel_clemens.stories.templates import StoryTemplate, get_template, TEMPLATES
from samuel_clemens.core.storyteller import Story, Emotion
from samuel_clemens.utils.logging import story_log


@dataclass
class RecombinedStory:
    """A story created by recombining multiple sources."""
    text: str
    title: str
    source_stories: list[str] = field(default_factory=list)
    blended_elements: dict = field(default_factory=dict)
    mashup_type: str = "blend"
    word_count: int = 0
    
    def __post_init__(self) -> None:
        self.word_count = len(self.text.split())


class StoryRecombinator:
    """
    Recombines, blends, and mashes up stories.
    
    Creates new narratives by intelligently combining
    elements from different sources.
    """
    
    def __init__(self) -> None:
        self.generator = StoryGenerator()
        self._mashup_count = 0
    
    def blend(
        self,
        story1: GeneratedStory,
        story2: GeneratedStory,
        blend_ratio: float = 0.5,
    ) -> RecombinedStory:
        """
        Blend two stories together.
        
        Args:
            story1: First story
            story2: Second story
            blend_ratio: How much of story1 to use (0-1)
            
        Returns:
            RecombinedStory blending both sources
        """
        # Split stories into sentences
        sentences1 = self._split_sentences(story1.text)
        sentences2 = self._split_sentences(story2.text)
        
        # Interleave based on ratio
        blended_sentences = []
        max_len = max(len(sentences1), len(sentences2))
        
        for i in range(max_len):
            if random.random() < blend_ratio and i < len(sentences1):
                blended_sentences.append(sentences1[i])
            elif i < len(sentences2):
                blended_sentences.append(sentences2[i])
        
        # Create coherent transition
        blended_text = self._smooth_transitions(" ".join(blended_sentences))
        
        # Generate title
        title = f"{story1.title} meets {story2.title}"
        
        self._mashup_count += 1
        story_log(f"🔀 Blended stories: {title}")
        
        return RecombinedStory(
            text=blended_text,
            title=title,
            source_stories=[story1.title, story2.title],
            blended_elements={
                "characters": [story1.character, story2.character],
                "settings": [story1.setting, story2.setting],
                "themes": [story1.theme, story2.theme],
            },
            mashup_type="blend",
        )
    
    def mashup(
        self,
        stories: list[GeneratedStory],
        style: str = "sequential",
    ) -> RecombinedStory:
        """
        Mashup multiple stories.
        
        Args:
            stories: List of stories to combine
            style: Mashup style (sequential, interleaved, chaotic)
            
        Returns:
            RecombinedStory combining all sources
        """
        if not stories:
            raise ValueError("Need at least one story to mashup")
        
        if style == "sequential":
            text = self._sequential_mashup(stories)
        elif style == "interleaved":
            text = self._interleaved_mashup(stories)
        elif style == "chaotic":
            text = self._chaotic_mashup(stories)
        else:
            text = self._sequential_mashup(stories)
        
        title = "The Grand Mashup: " + ", ".join(s.title for s in stories[:3])
        if len(stories) > 3:
            title += " and more..."
        
        self._mashup_count += 1
        story_log(f"🎭 Created mashup from {len(stories)} stories")
        
        return RecombinedStory(
            text=text,
            title=title,
            source_stories=[s.title for s in stories],
            mashup_type=style,
        )
    
    def crossover(
        self,
        story1: GeneratedStory,
        story2: GeneratedStory,
    ) -> RecombinedStory:
        """
        Create a crossover where characters from one story
        appear in the setting of another.
        
        Args:
            story1: Source for characters
            story2: Source for setting
            
        Returns:
            Crossover story
        """
        # Generate new story with mixed elements
        new_story = self.generator.generate(
            character=story1.character,
            setting=story2.setting,
            theme=story1.theme,
        )
        
        title = f"{story1.character.name if story1.character else 'A Stranger'} in {story2.setting.name if story2.setting else 'Unknown Land'}"
        
        story_log(f"⚔️ Created crossover: {title}")
        
        return RecombinedStory(
            text=new_story.text,
            title=title,
            source_stories=[story1.title, story2.title],
            blended_elements={
                "character_from": story1.title,
                "setting_from": story2.title,
            },
            mashup_type="crossover",
        )
    
    def remix_with_theme(
        self,
        story: GeneratedStory,
        new_theme: Theme,
    ) -> RecombinedStory:
        """
        Remix a story with a new theme overlay.
        
        Args:
            story: Story to remix
            new_theme: New theme to apply
            
        Returns:
            Remixed story
        """
        # Generate fresh story with original elements but new theme
        remixed = self.generator.generate(
            character=story.character,
            setting=story.setting,
            theme=new_theme,
        )
        
        title = f"{story.title} (Remixed: {new_theme.name})"
        
        story_log(f"🔄 Remixed with theme: {new_theme.name}")
        
        return RecombinedStory(
            text=remixed.text,
            title=title,
            source_stories=[story.title],
            blended_elements={"new_theme": new_theme.name},
            mashup_type="remix",
        )
    
    def create_anthology(
        self,
        count: int = 5,
        theme: Optional[Theme] = None,
    ) -> list[RecombinedStory]:
        """
        Create an anthology of related stories.
        
        Args:
            count: Number of stories in anthology
            theme: Optional unifying theme
            
        Returns:
            List of interconnected stories
        """
        anthology = []
        shared_setting = SETTINGS[random.randint(0, len(SETTINGS) - 1)]
        
        for i in range(count):
            story = self.generator.generate(
                setting=shared_setting,
                theme=theme,
            )
            
            recombined = RecombinedStory(
                text=story.text,
                title=f"Chapter {i+1}: {story.title}",
                source_stories=["anthology"],
                blended_elements={
                    "chapter": i + 1,
                    "shared_setting": shared_setting.name,
                },
                mashup_type="anthology",
            )
            anthology.append(recombined)
        
        story_log(f"📚 Created anthology with {count} chapters")
        return anthology
    
    def random_genesis(self) -> RecombinedStory:
        """
        Create a completely random story from random elements.
        
        Returns:
            Randomly generated story
        """
        # Pick random everything
        character = random.choice(CHARACTERS)
        setting = random.choice(SETTINGS)
        theme = random.choice(THEMES)
        template = random.choice(list(TEMPLATES.values()))
        
        story = self.generator.generate(
            template_name=template.name,
            character=character,
            setting=setting,
            theme=theme,
            dramatic=random.choice([True, False]),
        )
        
        story_log("🎲 Created random genesis story")
        
        return RecombinedStory(
            text=story.text,
            title=f"Random Genesis: {story.title}",
            source_stories=[],
            blended_elements={
                "character": character.name,
                "setting": setting.name,
                "theme": theme.name,
                "template": template.name,
            },
            mashup_type="genesis",
        )
    
    def _split_sentences(self, text: str) -> list[str]:
        """Split text into sentences."""
        import re
        sentences = re.split(r'(?<=[.!?])\s+', text)
        return [s.strip() for s in sentences if s.strip()]
    
    def _smooth_transitions(self, text: str) -> str:
        """Add smooth transitions between combined sections."""
        # Add transitional phrases at paragraph breaks
        paragraphs = text.split('\n\n')
        transitions = [
            "Meanwhile, ",
            "And yet, ",
            "But then, ",
            "As it turned out, ",
            "Little did anyone know, ",
        ]
        
        smoothed = []
        for i, para in enumerate(paragraphs):
            if i > 0 and random.random() < 0.3:
                para = random.choice(transitions) + para[0].lower() + para[1:]
            smoothed.append(para)
        
        return '\n\n'.join(smoothed)
    
    def _sequential_mashup(self, stories: list[GeneratedStory]) -> str:
        """Combine stories sequentially with transitions."""
        parts = []
        for i, story in enumerate(stories):
            if i > 0:
                parts.append("\n\n* * *\n\n")
            parts.append(story.text)
        return "".join(parts)
    
    def _interleaved_mashup(self, stories: list[GeneratedStory]) -> str:
        """Interleave sentences from all stories."""
        all_sentences = [self._split_sentences(s.text) for s in stories]
        result = []
        max_len = max(len(s) for s in all_sentences)
        
        for i in range(max_len):
            for sentences in all_sentences:
                if i < len(sentences):
                    result.append(sentences[i])
        
        return self._smooth_transitions(" ".join(result))
    
    def _chaotic_mashup(self, stories: list[GeneratedStory]) -> str:
        """Randomly sample and shuffle all sentences."""
        all_sentences = []
        for story in stories:
            all_sentences.extend(self._split_sentences(story.text))
        
        random.shuffle(all_sentences)
        
        # Take a reasonable subset
        subset = all_sentences[:min(20, len(all_sentences))]
        return self._smooth_transitions(" ".join(subset))


# Convenience functions
def recombine_stories(
    story1: GeneratedStory,
    story2: GeneratedStory,
) -> RecombinedStory:
    """
    Recombine two stories into one.
    
    Args:
        story1: First story
        story2: Second story
        
    Returns:
        Recombined story
    """
    recombinator = StoryRecombinator()
    return recombinator.blend(story1, story2)


def blend_themes(
    stories: list[GeneratedStory],
) -> RecombinedStory:
    """
    Blend multiple stories focusing on their themes.
    
    Args:
        stories: Stories to blend
        
    Returns:
        Theme-blended story
    """
    recombinator = StoryRecombinator()
    return recombinator.mashup(stories, style="interleaved")


def create_mashup(
    stories: list[GeneratedStory],
    style: str = "sequential",
) -> RecombinedStory:
    """
    Create a mashup from multiple stories.
    
    Args:
        stories: Stories to mashup
        style: Mashup style
        
    Returns:
        Mashup story
    """
    recombinator = StoryRecombinator()
    return recombinator.mashup(stories, style=style)


def create_crossover(
    story1: GeneratedStory,
    story2: GeneratedStory,
) -> RecombinedStory:
    """
    Create a crossover between two stories.
    
    Args:
        story1: Character source
        story2: Setting source
        
    Returns:
        Crossover story
    """
    recombinator = StoryRecombinator()
    return recombinator.crossover(story1, story2)
