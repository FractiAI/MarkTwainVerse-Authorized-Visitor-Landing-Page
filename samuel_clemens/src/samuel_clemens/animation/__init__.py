"""
Animation module - Generate animated visualizations for the MarkTwainVerse.

"Life is short, break the rules." — Mark Twain

Provides frame-based animation generation for cycles, entities, and stories.
"""

from samuel_clemens.animation.cycles import (
    generate_cycle_animation,
    generate_breathing_animation,
    generate_daynight_animation,
    generate_expedition_animation,
    generate_season_animation,
)
from samuel_clemens.animation.entities import (
    generate_entity_animation,
    generate_energy_animation,
    generate_mood_animation,
    generate_interaction_animation,
)
from samuel_clemens.animation.stories import (
    generate_story_animation,
    generate_typing_animation,
    generate_reveal_animation,
    generate_campfire_animation,
)
from samuel_clemens.animation.core import (
    AnimationFrame,
    AnimationSequence,
    AnimationConfig,
    create_animation,
    save_animation_frames,
    render_animation_preview,
)
from samuel_clemens.animation.gif_export import (
    GIFConfig,
    export_to_gif,
    export_all_animations_to_gif,
    create_cycle_gif,
    create_story_gif,
    render_frame_to_image,
)

__all__ = [
    # Cycles
    "generate_cycle_animation",
    "generate_breathing_animation",
    "generate_daynight_animation",
    "generate_expedition_animation",
    "generate_season_animation",
    # Entities
    "generate_entity_animation",
    "generate_energy_animation",
    "generate_mood_animation",
    "generate_interaction_animation",
    # Stories
    "generate_story_animation",
    "generate_typing_animation",
    "generate_reveal_animation",
    "generate_campfire_animation",
    # Core
    "AnimationFrame",
    "AnimationSequence",
    "AnimationConfig",
    "create_animation",
    "save_animation_frames",
    "render_animation_preview",
    # GIF Export
    "GIFConfig",
    "export_to_gif",
    "export_all_animations_to_gif",
    "create_cycle_gif",
    "create_story_gif",
    "render_frame_to_image",
]

