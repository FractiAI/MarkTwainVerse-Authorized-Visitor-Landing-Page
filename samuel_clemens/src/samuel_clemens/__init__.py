"""
Samuel Clemens - The Complete Methods Package for MarkTwainVerse

"The secret of getting ahead is getting started." — Mark Twain

Provides frontier-themed utilities, narrative generation, and NSPFRP protocol bridges.
"""

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
    Course,
    Harbor,
)
from samuel_clemens.core.frontier import (
    frontier_greeting,
    frontier_farewell,
    get_frontier_status,
    FrontierStatus,
)
from samuel_clemens.utils.logging import (
    frontier_log,
    story_log,
    event_log,
    get_logger,
)

# Stories module
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
from samuel_clemens.stories.elements import (
    Character,
    Setting,
    Theme,
    PlotPoint,
    get_random_elements,
)
from samuel_clemens.stories.templates import (
    StoryTemplate,
    get_template,
    list_templates,
    create_from_template,
)

# Visualization module
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
)

__version__ = "0.2.0"
__author__ = "MarkTwainVerse Team"

__all__ = [
    # Core - Storyteller
    "tell_story",
    "spin_yarn",
    "frontier_wisdom",
    "Story",
    "Emotion",
    # Core - Navigator
    "chart_course",
    "read_currents",
    "find_harbor",
    "Course",
    "Harbor",
    # Core - Frontier
    "frontier_greeting",
    "frontier_farewell",
    "get_frontier_status",
    "FrontierStatus",
    # Utils - Logging
    "frontier_log",
    "story_log",
    "event_log",
    "get_logger",
    # Stories - Generator
    "StoryGenerator",
    "GeneratedStory",
    "generate_frontier_tale",
    "generate_adventure",
    "generate_wisdom_piece",
    "generate_campfire_yarn",
    "generate_river_story",
    "generate_mystery",
    # Stories - Recombinator
    "StoryRecombinator",
    "RecombinedStory",
    "recombine_stories",
    "blend_themes",
    "create_mashup",
    "create_crossover",
    # Stories - Elements
    "Character",
    "Setting",
    "Theme",
    "PlotPoint",
    "get_random_elements",
    # Stories - Templates
    "StoryTemplate",
    "get_template",
    "list_templates",
    "create_from_template",
    # Visualization - Renderer
    "render_story",
    "render_story_card",
    "render_verse_dashboard",
    "render_expedition_map",
    "render_entity_network",
    "render_story_gallery",
    # Visualization - Charts
    "render_cycle_chart",
    "render_energy_bars",
    "render_timeline",
    "render_mood_wheel",
    "render_cycle_comparison",
    # Visualization - ASCII Art
    "render_frontier_banner",
    "render_twain_portrait",
    "render_map_art",
    "render_steamboat",
    "render_campfire",
    "render_welcome_scene",
    "render_goodbye_scene",
]
