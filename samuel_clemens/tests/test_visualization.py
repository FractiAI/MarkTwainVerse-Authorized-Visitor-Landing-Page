"""
Tests for visualization module - renderer, charts, ascii_art.
"""

import pytest
from io import StringIO

from samuel_clemens.visualization.renderer import (
    render_story,
    render_story_card,
    render_verse_dashboard,
    render_expedition_map,
    render_entity_network,
    render_story_gallery,
)
from samuel_clemens.visualization.charts import (
    render_cycle_chart,
    render_energy_bars,
    render_timeline,
    render_mood_wheel,
    render_cycle_comparison,
)
from samuel_clemens.visualization.ascii_art import (
    render_frontier_banner,
    render_twain_portrait,
    render_map_art,
    render_steamboat,
    render_campfire,
    render_welcome_scene,
    render_goodbye_scene,
    get_mood_emoji,
    get_weather_art,
    FRONTIER_BANNER,
    TWAIN_PORTRAIT,
)
from samuel_clemens.core.storyteller import Story, Emotion
from samuel_clemens.core.navigator import chart_course, CourseType


class TestRenderer:
    """Tests for renderer module."""

    def test_render_story_panel(self) -> None:
        """render_story should run without error (panel style)."""
        story = Story(
            text="Test story text",
            emotion=Emotion.ADVENTURE,
            topic="test",
            keywords=["test"],
        )
        # Should not raise
        render_story(story, style="panel")

    def test_render_story_card(self) -> None:
        """render_story_card should run without error."""
        story = Story(
            text="Test story text",
            emotion=Emotion.ADVENTURE,
            topic="test",
            keywords=["test"],
        )
        # Should not raise
        render_story_card(story)

    def test_render_story_minimal(self) -> None:
        """render_story should work with minimal style."""
        story = Story(
            text="Test story text",
            emotion=Emotion.ADVENTURE,
            topic="test",
            keywords=["test"],
        )
        # Should not raise
        render_story(story, style="minimal")

    def test_render_verse_dashboard(self) -> None:
        """render_verse_dashboard should run without error."""
        # Should not raise
        render_verse_dashboard()

    def test_render_expedition_map(self) -> None:
        """render_expedition_map should run without error."""
        course = chart_course(CourseType.FRONTIER)
        # Should not raise
        render_expedition_map(course)

    def test_render_entity_network(self) -> None:
        """render_entity_network should run without error."""
        # Should not raise
        render_entity_network()

    def test_render_story_gallery_grid(self) -> None:
        """render_story_gallery should work with grid layout."""
        stories = [
            Story(text=f"Story {i}", emotion=Emotion.STORYTELLING, topic="test", keywords=[])
            for i in range(4)
        ]
        # Should not raise
        render_story_gallery(stories, layout="grid")

    def test_render_story_gallery_list(self) -> None:
        """render_story_gallery should work with list layout."""
        stories = [
            Story(text=f"Story {i}", emotion=Emotion.STORYTELLING, topic="test", keywords=[])
            for i in range(3)
        ]
        # Should not raise
        render_story_gallery(stories, layout="list")


class TestCharts:
    """Tests for charts module."""

    def test_render_cycle_chart_all(self) -> None:
        """render_cycle_chart should show all cycles."""
        # Should not raise
        render_cycle_chart()

    def test_render_cycle_chart_single(self) -> None:
        """render_cycle_chart should show single cycle."""
        # Should not raise
        render_cycle_chart(cycle_name="breathing")

    def test_render_energy_bars(self) -> None:
        """render_energy_bars should run without error."""
        # Should not raise
        render_energy_bars()

    def test_render_timeline(self) -> None:
        """render_timeline should run without error."""
        # Should not raise
        render_timeline()

    def test_render_timeline_custom_hours(self) -> None:
        """render_timeline should accept custom hours."""
        # Should not raise
        render_timeline(hours=12)

    def test_render_mood_wheel(self) -> None:
        """render_mood_wheel should run without error."""
        # Should not raise
        render_mood_wheel()

    def test_render_cycle_comparison(self) -> None:
        """render_cycle_comparison should run without error."""
        # Should not raise
        render_cycle_comparison()


class TestASCIIArt:
    """Tests for ASCII art module."""

    def test_frontier_banner_exists(self) -> None:
        """FRONTIER_BANNER should be defined."""
        assert len(FRONTIER_BANNER) > 0

    def test_twain_portrait_exists(self) -> None:
        """TWAIN_PORTRAIT should be defined."""
        assert len(TWAIN_PORTRAIT) > 0

    def test_render_frontier_banner_large(self) -> None:
        """render_frontier_banner should work with large size."""
        # Should not raise
        render_frontier_banner(size="large")

    def test_render_frontier_banner_small(self) -> None:
        """render_frontier_banner should work with small size."""
        # Should not raise
        render_frontier_banner(size="small")

    def test_render_twain_portrait_large(self) -> None:
        """render_twain_portrait should work with large size."""
        # Should not raise
        render_twain_portrait(size="large")

    def test_render_twain_portrait_small(self) -> None:
        """render_twain_portrait should work with small size."""
        # Should not raise
        render_twain_portrait(size="small")

    def test_render_map_art(self) -> None:
        """render_map_art should run without error."""
        # Should not raise
        render_map_art()

    def test_render_steamboat_large(self) -> None:
        """render_steamboat should work with large size."""
        # Should not raise
        render_steamboat(size="large")

    def test_render_steamboat_small(self) -> None:
        """render_steamboat should work with small size."""
        # Should not raise
        render_steamboat(size="small")

    def test_render_campfire(self) -> None:
        """render_campfire should run without error."""
        # Should not raise
        render_campfire()

    def test_render_welcome_scene(self) -> None:
        """render_welcome_scene should run without error."""
        # Should not raise
        render_welcome_scene()

    def test_render_goodbye_scene(self) -> None:
        """render_goodbye_scene should run without error."""
        # Should not raise
        render_goodbye_scene()

    def test_get_mood_emoji(self) -> None:
        """get_mood_emoji should return emoji for mood."""
        assert get_mood_emoji("dormant") == "💤"
        assert get_mood_emoji("thriving") == "🌟"
        assert get_mood_emoji("unknown") == "●"

    def test_get_weather_art(self) -> None:
        """get_weather_art should return art for weather."""
        sunny = get_weather_art("sunny")
        assert len(sunny) > 0
        
        unknown = get_weather_art("unknown_weather")
        assert unknown == ""
