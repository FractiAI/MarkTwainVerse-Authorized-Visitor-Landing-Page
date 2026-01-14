"""
Visualization module - Rich visual output for MarkTwainVerse.

Creates stunning terminal visualizations of stories, cycles, and verse state.
"""

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
from samuel_clemens.visualization.advanced_charts import (
    render_heatmap,
    render_sparkline,
    render_gauge,
    render_entity_matrix,
    render_radar_chart,
    render_histogram,
    render_bar_chart,
    render_stacked_bars,
    render_treemap,
    render_activity_stream,
    render_entity_leaderboard,
    render_correlation_matrix,
)
from samuel_clemens.visualization.layouts import (
    render_split_layout,
    render_triple_layout,
    render_header_body_footer,
    render_main_dashboard,
    render_story_showcase,
    render_entity_cards,
    render_status_bar,
    render_tabbed_view,
    render_notification,
    render_breadcrumb,
    render_progress_steps,
    render_stats_grid,
    render_comparison,
    render_full_report,
)
from samuel_clemens.visualization.exports import (
    export_dashboard_snapshot,
    export_cycle_charts,
    export_entity_charts,
    export_ascii_art_collection,
    export_story_visualization,
    export_expedition_map,
)
from samuel_clemens.visualization.image_export import (
    render_story_card_image,
    render_protocol_card_image,
    render_ascii_to_image,
    ImageConfig,
)

__all__ = [
    # Renderer
    "render_story",
    "render_story_card",
    "render_verse_dashboard",
    "render_expedition_map",
    "render_entity_network",
    "render_story_gallery",
    # Charts
    "render_cycle_chart",
    "render_energy_bars",
    "render_timeline",
    "render_mood_wheel",
    "render_cycle_comparison",
    # ASCII Art
    "render_frontier_banner",
    "render_twain_portrait",
    "render_map_art",
    "render_steamboat",
    "render_campfire",
    "render_welcome_scene",
    "render_goodbye_scene",
    "get_mood_emoji",
    "get_weather_art",
    "FRONTIER_BANNER",
    "TWAIN_PORTRAIT",
    # Advanced Charts
    "render_heatmap",
    "render_sparkline",
    "render_gauge",
    "render_entity_matrix",
    "render_radar_chart",
    "render_histogram",
    "render_bar_chart",
    "render_stacked_bars",
    "render_treemap",
    "render_activity_stream",
    "render_entity_leaderboard",
    "render_correlation_matrix",
    # Layouts
    "render_split_layout",
    "render_triple_layout",
    "render_header_body_footer",
    "render_main_dashboard",
    "render_story_showcase",
    "render_entity_cards",
    "render_status_bar",
    "render_tabbed_view",
    "render_notification",
    "render_breadcrumb",
    "render_progress_steps",
    "render_stats_grid",
    "render_comparison",
    "render_full_report",
    # Exports
    "export_dashboard_snapshot",
    "export_cycle_charts",
    "export_entity_charts",
    "export_ascii_art_collection",
    "export_story_visualization",
    "export_expedition_map",
    # Image Export
    "render_story_card_image",
    "render_protocol_card_image",
    "render_ascii_to_image",
    "ImageConfig",
]

