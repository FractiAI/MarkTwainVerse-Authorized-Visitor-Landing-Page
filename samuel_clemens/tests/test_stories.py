"""
Tests for stories module - generator, recombinator, templates, elements.
"""

import pytest

from samuel_clemens.stories.elements import (
    Character,
    Setting,
    Theme,
    PlotPoint,
    get_random_character,
    get_random_setting,
    get_random_theme,
    get_random_elements,
    get_elements_by_tag,
    CHARACTERS,
    SETTINGS,
    THEMES,
)
from samuel_clemens.stories.templates import (
    StoryTemplate,
    get_template,
    list_templates,
    create_from_template,
    get_random_template,
    TEMPLATES,
)
from samuel_clemens.stories.generator import (
    StoryGenerator,
    GeneratedStory,
    generate_frontier_tale,
    generate_adventure,
    generate_wisdom_piece,
    generate_campfire_yarn,
    generate_river_story,
    generate_mystery,
)
from samuel_clemens.stories.recombinator import (
    StoryRecombinator,
    RecombinedStory,
    recombine_stories,
    blend_themes,
    create_mashup,
    create_crossover,
)


class TestElements:
    """Tests for story elements."""

    def test_characters_exist(self) -> None:
        """CHARACTERS should contain predefined characters."""
        assert len(CHARACTERS) >= 5
        assert all(isinstance(c, Character) for c in CHARACTERS)

    def test_settings_exist(self) -> None:
        """SETTINGS should contain predefined settings."""
        assert len(SETTINGS) >= 5
        assert all(isinstance(s, Setting) for s in SETTINGS)

    def test_themes_exist(self) -> None:
        """THEMES should contain predefined themes."""
        assert len(THEMES) >= 5
        assert all(isinstance(t, Theme) for t in THEMES)

    def test_get_random_character(self) -> None:
        """get_random_character should return a Character."""
        char = get_random_character()
        assert isinstance(char, Character)
        assert char.name

    def test_get_random_setting(self) -> None:
        """get_random_setting should return a Setting."""
        setting = get_random_setting()
        assert isinstance(setting, Setting)
        assert setting.name

    def test_get_random_theme(self) -> None:
        """get_random_theme should return a Theme."""
        theme = get_random_theme()
        assert isinstance(theme, Theme)
        assert theme.name

    def test_get_random_elements(self) -> None:
        """get_random_elements should return dict of elements."""
        elements = get_random_elements()
        assert "character" in elements
        assert "setting" in elements
        assert "theme" in elements

    def test_get_elements_by_tag(self) -> None:
        """get_elements_by_tag should filter by tag."""
        frontier_elements = get_elements_by_tag("frontier")
        assert len(frontier_elements) > 0


class TestTemplates:
    """Tests for story templates."""

    def test_templates_exist(self) -> None:
        """TEMPLATES should contain predefined templates."""
        assert len(TEMPLATES) >= 5

    def test_list_templates(self) -> None:
        """list_templates should return template names."""
        names = list_templates()
        assert "frontier_tale" in names
        assert "river_story" in names
        assert "campfire_yarn" in names

    def test_get_template(self) -> None:
        """get_template should return template by name."""
        template = get_template("frontier_tale")
        assert template is not None
        assert template.name == "Frontier Tale"

    def test_get_template_not_found(self) -> None:
        """get_template should return None for unknown template."""
        template = get_template("nonexistent")
        assert template is None

    def test_get_random_template(self) -> None:
        """get_random_template should return a template."""
        template = get_random_template()
        assert isinstance(template, StoryTemplate)

    def test_create_from_template(self) -> None:
        """create_from_template should generate story text."""
        story = create_from_template("frontier_tale")
        assert story is not None
        assert len(story) > 0

    def test_template_has_patterns(self) -> None:
        """Templates should have opening, middle, and closing patterns."""
        template = get_template("frontier_tale")
        assert template.opening_patterns
        assert template.middle_patterns
        assert template.closing_patterns


class TestGenerator:
    """Tests for story generator."""

    def test_generator_init(self) -> None:
        """StoryGenerator should initialize."""
        generator = StoryGenerator()
        assert generator.templates
        assert generator.characters

    def test_generate_returns_story(self) -> None:
        """generate should return GeneratedStory."""
        generator = StoryGenerator()
        story = generator.generate()
        assert isinstance(story, GeneratedStory)
        assert story.text
        assert story.title

    def test_generate_with_template(self) -> None:
        """generate should accept template name."""
        generator = StoryGenerator()
        story = generator.generate(template_name="campfire_yarn")
        assert story.template_used == "Campfire Yarn"

    def test_generate_with_dramatic(self) -> None:
        """generate with dramatic should add flourishes."""
        generator = StoryGenerator()
        story = generator.generate(dramatic=True)
        assert story.word_count > 0

    def test_generate_batch(self) -> None:
        """generate_batch should return multiple stories."""
        generator = StoryGenerator()
        stories = generator.generate_batch(count=3)
        assert len(stories) == 3
        assert all(isinstance(s, GeneratedStory) for s in stories)

    def test_generate_sequel(self) -> None:
        """generate_sequel should continue a story."""
        generator = StoryGenerator()
        original = generator.generate()
        sequel = generator.generate_sequel(original)
        assert "Part II" in sequel.title

    def test_to_story_conversion(self) -> None:
        """GeneratedStory should convert to base Story."""
        generator = StoryGenerator()
        generated = generator.generate()
        story = generated.to_story()
        assert story.text == generated.text

    def test_generate_frontier_tale(self) -> None:
        """generate_frontier_tale convenience function."""
        story = generate_frontier_tale()
        assert story.template_used == "Frontier Tale"

    def test_generate_adventure(self) -> None:
        """generate_adventure convenience function."""
        story = generate_adventure()
        assert story.text

    def test_generate_wisdom_piece(self) -> None:
        """generate_wisdom_piece convenience function."""
        story = generate_wisdom_piece()
        assert story.template_used == "Wisdom Piece"

    def test_generate_campfire_yarn(self) -> None:
        """generate_campfire_yarn convenience function."""
        story = generate_campfire_yarn()
        assert story.template_used == "Campfire Yarn"

    def test_generate_river_story(self) -> None:
        """generate_river_story convenience function."""
        story = generate_river_story()
        assert story.template_used == "River Story"

    def test_generate_mystery(self) -> None:
        """generate_mystery convenience function."""
        story = generate_mystery()
        assert story.template_used == "Mystery Tale"


class TestRecombinator:
    """Tests for story recombinator."""

    def test_recombinator_init(self) -> None:
        """StoryRecombinator should initialize."""
        recombinator = StoryRecombinator()
        assert recombinator.generator

    def test_blend_stories(self) -> None:
        """blend should combine two stories."""
        generator = StoryGenerator()
        recombinator = StoryRecombinator()
        
        s1 = generator.generate()
        s2 = generator.generate()
        
        blended = recombinator.blend(s1, s2)
        assert isinstance(blended, RecombinedStory)
        assert blended.mashup_type == "blend"
        assert len(blended.source_stories) == 2

    def test_mashup_sequential(self) -> None:
        """mashup with sequential style."""
        generator = StoryGenerator()
        recombinator = StoryRecombinator()
        
        stories = generator.generate_batch(2)
        mashup_result = recombinator.mashup(stories, style="sequential")
        
        assert mashup_result.mashup_type == "sequential"

    def test_mashup_interleaved(self) -> None:
        """mashup with interleaved style."""
        generator = StoryGenerator()
        recombinator = StoryRecombinator()
        
        stories = generator.generate_batch(2)
        mashup_result = recombinator.mashup(stories, style="interleaved")
        
        assert mashup_result.mashup_type == "interleaved"

    def test_mashup_chaotic(self) -> None:
        """mashup with chaotic style."""
        generator = StoryGenerator()
        recombinator = StoryRecombinator()
        
        stories = generator.generate_batch(2)
        mashup_result = recombinator.mashup(stories, style="chaotic")
        
        assert mashup_result.mashup_type == "chaotic"

    def test_crossover(self) -> None:
        """crossover should combine character and setting."""
        generator = StoryGenerator()
        recombinator = StoryRecombinator()
        
        s1 = generator.generate()
        s2 = generator.generate()
        
        crossover_result = recombinator.crossover(s1, s2)
        assert crossover_result.mashup_type == "crossover"

    def test_create_anthology(self) -> None:
        """create_anthology should generate interconnected stories."""
        recombinator = StoryRecombinator()
        anthology = recombinator.create_anthology(count=3)
        
        assert len(anthology) == 3
        assert all(isinstance(s, RecombinedStory) for s in anthology)

    def test_random_genesis(self) -> None:
        """random_genesis should create completely random story."""
        recombinator = StoryRecombinator()
        story = recombinator.random_genesis()
        
        assert story.mashup_type == "genesis"

    def test_recombine_stories_convenience(self) -> None:
        """recombine_stories convenience function."""
        generator = StoryGenerator()
        s1 = generator.generate()
        s2 = generator.generate()
        
        result = recombine_stories(s1, s2)
        assert isinstance(result, RecombinedStory)

    def test_create_mashup_convenience(self) -> None:
        """create_mashup convenience function."""
        generator = StoryGenerator()
        stories = generator.generate_batch(2)
        
        result = create_mashup(stories)
        assert isinstance(result, RecombinedStory)
