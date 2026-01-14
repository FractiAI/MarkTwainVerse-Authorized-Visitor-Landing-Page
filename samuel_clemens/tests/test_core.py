"""
Tests for core module - storyteller, navigator, frontier.
"""

import pytest

from samuel_clemens.core.storyteller import (
    tell_story,
    spin_yarn,
    frontier_wisdom,
    Story,
    Emotion,
)
from samuel_clemens.core.navigator import (
    chart_course,
    read_currents,
    find_harbor,
    CourseType,
    CurrentStrength,
)
from samuel_clemens.core.frontier import (
    frontier_greeting,
    frontier_farewell,
    get_frontier_status,
)


class TestStoryteller:
    """Tests for storyteller module."""

    def test_tell_story_returns_story(self) -> None:
        """tell_story should return a Story object."""
        result = tell_story()
        assert isinstance(result, Story)
        assert result.text
        assert result.topic

    def test_tell_story_with_topic(self) -> None:
        """tell_story should accept topic parameter."""
        result = tell_story(topic="adventure")
        assert result.topic == "adventure"
        assert result.emotion == Emotion.ADVENTURE

    def test_tell_story_includes_quote(self) -> None:
        """tell_story should include quote by default."""
        result = tell_story(include_quote=True)
        assert "As I once said:" in result.text

    def test_tell_story_no_quote(self) -> None:
        """tell_story should skip quote when requested."""
        result = tell_story(include_quote=False)
        assert "As I once said:" not in result.text

    def test_spin_yarn_combines_topics(self) -> None:
        """spin_yarn should combine multiple topics."""
        result = spin_yarn(topics=["frontier", "adventure"])
        assert isinstance(result, Story)
        assert "frontier" in result.topic.lower() or "adventure" in result.topic.lower()

    def test_frontier_wisdom_returns_string(self) -> None:
        """frontier_wisdom should return a wisdom snippet."""
        result = frontier_wisdom()
        assert isinstance(result, str)
        assert len(result) > 0


class TestNavigator:
    """Tests for navigator module."""

    def test_chart_course_returns_course(self) -> None:
        """chart_course should return a Course object."""
        result = chart_course(CourseType.FISHING)
        assert result.destination
        assert result.course_type == CourseType.FISHING
        assert result.duration_hours > 0

    def test_chart_course_with_duration(self) -> None:
        """chart_course should respect duration preference."""
        short = chart_course(CourseType.FISHING, duration_preference="short")
        long = chart_course(CourseType.FISHING, duration_preference="long")
        # Short should be <= long
        assert short.duration_hours <= long.duration_hours

    def test_read_currents_returns_reading(self) -> None:
        """read_currents should return a CurrentReading."""
        result = read_currents()
        assert result.strength in CurrentStrength
        assert 0.0 <= result.activity_level <= 1.0

    def test_read_currents_day_phase(self) -> None:
        """read_currents should respond to day phase."""
        day = read_currents(day_phase=0.5)
        night = read_currents(day_phase=0.1)
        assert day.activity_level >= night.activity_level

    def test_find_harbor_returns_harbor(self) -> None:
        """find_harbor should return a Harbor."""
        result = find_harbor()
        assert result.name
        assert result.community


class TestFrontier:
    """Tests for frontier module."""

    def test_frontier_greeting_returns_string(self) -> None:
        """frontier_greeting should return a greeting."""
        result = frontier_greeting()
        assert isinstance(result, str)
        assert len(result) > 0

    def test_frontier_greeting_with_name(self) -> None:
        """frontier_greeting should personalize with name."""
        result = frontier_greeting(visitor_name="Partner")
        # Name should replace "friend" or "traveler"
        assert "Partner" in result or "friend" not in result

    def test_frontier_farewell_returns_string(self) -> None:
        """frontier_farewell should return a farewell."""
        result = frontier_farewell()
        assert isinstance(result, str)
        assert len(result) > 0

    def test_get_frontier_status(self) -> None:
        """get_frontier_status should return status."""
        result = get_frontier_status()
        assert result.is_operational
        assert result.season in ["Spring", "Summer", "Fall", "Winter"]
        assert result.message
