"""
Stories module - Advanced story creation, recombination, and generation.

"The humorous story is American, the comic story is English, 
the witty story is French." — Mark Twain
"""

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
from samuel_clemens.stories.templates import (
    StoryTemplate,
    TemplateType,
    get_template,
    list_templates,
    create_from_template,
    get_random_template,
    TEMPLATES,
)
from samuel_clemens.stories.elements import (
    StoryElement,
    Character,
    Setting,
    PlotPoint,
    Theme,
    get_random_elements,
    get_random_character,
    get_random_setting,
    get_random_theme,
    CHARACTERS,
    SETTINGS,
    THEMES,
)
from samuel_clemens.stories.export import (
    export_story,
    export_to_markdown,
    export_to_html,
    export_to_json,
    export_to_text,
    export_anthology,
)
from samuel_clemens.stories.interactive import (
    InteractiveSession,
    run_interactive_session,
    quick_story_prompt,
)

__all__ = [
    # Generator
    "StoryGenerator",
    "GeneratedStory",
    "generate_frontier_tale",
    "generate_adventure",
    "generate_wisdom_piece",
    "generate_campfire_yarn",
    "generate_river_story",
    "generate_mystery",
    # Recombinator
    "StoryRecombinator",
    "RecombinedStory",
    "recombine_stories",
    "blend_themes",
    "create_mashup",
    "create_crossover",
    # Templates
    "StoryTemplate",
    "TemplateType",
    "get_template",
    "list_templates",
    "create_from_template",
    "get_random_template",
    "TEMPLATES",
    # Elements
    "StoryElement",
    "Character",
    "Setting",
    "PlotPoint",
    "Theme",
    "get_random_elements",
    "get_random_character",
    "get_random_setting",
    "get_random_theme",
    "CHARACTERS",
    "SETTINGS",
    "THEMES",
    # Export
    "export_story",
    "export_to_markdown",
    "export_to_html",
    "export_to_json",
    "export_to_text",
    "export_anthology",
    # Interactive
    "InteractiveSession",
    "run_interactive_session",
    "quick_story_prompt",
]

