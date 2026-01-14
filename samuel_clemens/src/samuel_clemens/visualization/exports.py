"""
Visualization Exports - Export visualizations to files.

Save terminal visualizations as text files for later viewing.
"""

from __future__ import annotations

from pathlib import Path
from datetime import datetime
from io import StringIO

from rich.console import Console


def _capture_output(func, *args, **kwargs) -> str:
    """Capture console output to string."""
    buffer = StringIO()
    console = Console(file=buffer, force_terminal=True, width=100)
    
    # Temporarily replace the console in the module
    import samuel_clemens.visualization.renderer as renderer
    import samuel_clemens.visualization.charts as charts
    import samuel_clemens.visualization.ascii_art as ascii_art
    
    orig_console_r = renderer.console
    orig_console_c = charts.console
    orig_console_a = ascii_art.console
    
    renderer.console = console
    charts.console = console
    ascii_art.console = console
    
    try:
        func(*args, **kwargs)
    finally:
        renderer.console = orig_console_r
        charts.console = orig_console_c
        ascii_art.console = orig_console_a
    
    return buffer.getvalue()


def export_dashboard_snapshot(filepath: Path) -> None:
    """
    Export the verse dashboard to a text file.
    
    Args:
        filepath: Path to save the dashboard
    """
    from samuel_clemens.visualization.renderer import render_verse_dashboard
    
    output = _capture_output(render_verse_dashboard)
    
    filepath = Path(filepath)
    filepath.parent.mkdir(parents=True, exist_ok=True)
    
    header = f"# MarkTwainVerse Dashboard Snapshot\n# Generated: {datetime.now().isoformat()}\n\n"
    filepath.write_text(header + output)


def export_cycle_charts(directory: Path) -> None:
    """
    Export all cycle charts to a directory.
    
    Args:
        directory: Directory to save charts
    """
    from samuel_clemens.visualization.charts import (
        render_cycle_chart,
        render_timeline,
        render_cycle_comparison,
    )
    from samuel_clemens.protocols.cycles import get_all_cycles
    
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    
    # All cycles
    output = _capture_output(render_cycle_chart)
    (directory / "all_cycles.txt").write_text(output)
    
    # Individual cycles
    cycles = get_all_cycles()
    for name in cycles.keys():
        output = _capture_output(render_cycle_chart, cycle_name=name)
        (directory / f"cycle_{name}.txt").write_text(output)
    
    # Timeline
    output = _capture_output(render_timeline)
    (directory / "timeline.txt").write_text(output)
    
    # Comparison
    output = _capture_output(render_cycle_comparison)
    (directory / "comparison.txt").write_text(output)


def export_entity_charts(directory: Path) -> None:
    """
    Export entity charts to a directory.
    
    Args:
        directory: Directory to save charts
    """
    from samuel_clemens.visualization.charts import (
        render_energy_bars,
        render_mood_wheel,
    )
    from samuel_clemens.visualization.renderer import render_entity_network
    
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    
    # Energy bars
    output = _capture_output(render_energy_bars)
    (directory / "energy_bars.txt").write_text(output)
    
    # Mood wheel
    output = _capture_output(render_mood_wheel)
    (directory / "mood_wheel.txt").write_text(output)
    
    # Entity network
    output = _capture_output(render_entity_network)
    (directory / "network.txt").write_text(output)


def export_ascii_art_collection(directory: Path) -> None:
    """
    Export all ASCII art to a directory.
    
    Args:
        directory: Directory to save art
    """
    from samuel_clemens.visualization.ascii_art import (
        render_frontier_banner,
        render_twain_portrait,
        render_map_art,
        render_steamboat,
        render_campfire,
        render_welcome_scene,
        render_goodbye_scene,
    )
    
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    
    # All art pieces
    art_funcs = [
        ("banner_large", lambda: render_frontier_banner(size="large")),
        ("banner_small", lambda: render_frontier_banner(size="small")),
        ("portrait_large", lambda: render_twain_portrait(size="large")),
        ("portrait_small", lambda: render_twain_portrait(size="small")),
        ("map", render_map_art),
        ("steamboat_large", lambda: render_steamboat(size="large")),
        ("steamboat_small", lambda: render_steamboat(size="small")),
        ("campfire", render_campfire),
        ("welcome", render_welcome_scene),
        ("goodbye", render_goodbye_scene),
    ]
    
    for name, func in art_funcs:
        output = _capture_output(func)
        (directory / f"{name}.txt").write_text(output)


def export_story_visualization(
    story,
    filepath: Path,
    style: str = "panel",
) -> None:
    """
    Export a story visualization to file.
    
    Args:
        story: Story to visualize
        filepath: Path to save
        style: Visualization style
    """
    from samuel_clemens.visualization.renderer import render_story
    
    output = _capture_output(render_story, story, style=style)
    
    filepath = Path(filepath)
    filepath.parent.mkdir(parents=True, exist_ok=True)
    filepath.write_text(output)


def export_expedition_map(course, filepath: Path) -> None:
    """
    Export an expedition map to file.
    
    Args:
        course: Course to visualize
        filepath: Path to save
    """
    from samuel_clemens.visualization.renderer import render_expedition_map
    
    output = _capture_output(render_expedition_map, course)
    
    filepath = Path(filepath)
    filepath.parent.mkdir(parents=True, exist_ok=True)
    filepath.write_text(output)
