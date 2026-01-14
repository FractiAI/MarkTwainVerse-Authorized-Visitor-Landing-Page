"""
Tests for protocols module - cycles, entities, events.
"""

import pytest

from samuel_clemens.protocols.cycles import (
    get_day_phase,
    get_season_phase,
    get_breathing_pulse,
    get_expedition_day,
    get_time_of_day,
    get_season,
    get_all_cycles,
    reset_cycles,
)
from samuel_clemens.protocols.entities import (
    get_entity_state,
    get_all_entities,
    interact_with_entity,
    get_hero_hosts,
    get_total_energy,
    EntityType,
    EntityMood,
)
from samuel_clemens.protocols.events import (
    check_events,
    get_active_events,
    trigger_event,
    clear_events,
    EventType,
)


class TestCycles:
    """Tests for cycles module."""

    def test_get_day_phase_range(self) -> None:
        """get_day_phase should return 0-1 range."""
        result = get_day_phase()
        assert 0.0 <= result <= 1.0

    def test_get_season_phase_range(self) -> None:
        """get_season_phase should return 0-1 range."""
        result = get_season_phase()
        assert 0.0 <= result <= 1.0

    def test_get_breathing_pulse_range(self) -> None:
        """get_breathing_pulse should return 0.6-1.0 range."""
        result = get_breathing_pulse()
        assert 0.6 <= result <= 1.0

    def test_get_expedition_day_range(self) -> None:
        """get_expedition_day should return 0-6."""
        result = get_expedition_day()
        assert 0 <= result <= 6

    def test_get_time_of_day_values(self) -> None:
        """get_time_of_day should return valid time."""
        result = get_time_of_day()
        assert result in ["night", "dawn", "morning", "afternoon", "dusk", "evening"]

    def test_get_season_values(self) -> None:
        """get_season should return valid season."""
        result = get_season()
        assert result in ["spring", "summer", "fall", "winter"]

    def test_get_all_cycles(self) -> None:
        """get_all_cycles should return all cycles."""
        result = get_all_cycles()
        assert "breathing" in result
        assert "dayNight" in result
        assert "seasons" in result


class TestEntities:
    """Tests for entities module."""

    def test_get_all_entities(self) -> None:
        """get_all_entities should return entities."""
        result = get_all_entities()
        assert len(result) > 0
        assert "hero-host-mark-twain" in result

    def test_get_entity_state(self) -> None:
        """get_entity_state should return entity by ID."""
        result = get_entity_state("hero-host-mark-twain")
        assert result is not None
        assert result.name == "Mark Twain"
        assert result.entity_type == EntityType.CHARACTER

    def test_get_entity_state_not_found(self) -> None:
        """get_entity_state should return None for unknown ID."""
        result = get_entity_state("nonexistent-entity")
        assert result is None

    def test_interact_with_entity(self) -> None:
        """interact_with_entity should boost energy."""
        entity = get_entity_state("hero-host-mark-twain")
        original_energy = entity.energy if entity else 0
        
        result = interact_with_entity("hero-host-mark-twain")
        assert result is not None
        assert result.energy >= original_energy
        assert result.state.mood == EntityMood.THRIVING

    def test_get_hero_hosts(self) -> None:
        """get_hero_hosts should return Hero Host entities."""
        result = get_hero_hosts()
        assert len(result) >= 1
        assert all("hero-host" in e.id for e in result)

    def test_get_total_energy(self) -> None:
        """get_total_energy should return average energy."""
        result = get_total_energy()
        assert 0.0 <= result <= 1.0


class TestEvents:
    """Tests for events module."""

    def setup_method(self) -> None:
        """Clear events before each test."""
        clear_events()

    def test_check_events_returns_list(self) -> None:
        """check_events should return a list."""
        result = check_events()
        assert isinstance(result, list)

    def test_get_active_events(self) -> None:
        """get_active_events should return active events."""
        result = get_active_events()
        assert isinstance(result, list)

    def test_trigger_event(self) -> None:
        """trigger_event should manually trigger an event."""
        result = trigger_event("morning-greeting")
        assert result is not None
        assert result.event_type == EventType.STORY

    def test_trigger_event_not_found(self) -> None:
        """trigger_event should return None for unknown event."""
        result = trigger_event("nonexistent-event")
        assert result is None

    def test_clear_events(self) -> None:
        """clear_events should remove all events."""
        trigger_event("morning-greeting")
        clear_events()
        result = get_active_events()
        assert len(result) == 0
