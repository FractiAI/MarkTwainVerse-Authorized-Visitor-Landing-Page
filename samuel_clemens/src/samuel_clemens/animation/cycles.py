"""
Cycle Animations - Animated visualizations for natural cycles.

Generate frame sequences showing cycle progression.
"""

from __future__ import annotations

import math
from pathlib import Path
from typing import Optional

from samuel_clemens.animation.core import (
    AnimationConfig,
    AnimationSequence,
    AnimationFrame,
    create_animation,
    save_animation_frames,
    create_progress_bar,
    apply_easing,
    EasingFunction,
)


def _breathing_frame(frame_index: int, progress: float, config: AnimationConfig) -> str:
    """Generate a breathing cycle frame."""
    # Breathing uses sine wave
    breath = (math.sin(progress * 2 * math.pi) + 1) / 2
    
    # Create visual
    width = 40
    center = int(breath * width)
    
    lines = []
    lines.append("╭" + "─" * (width + 2) + "╮")
    lines.append("│ " + " " * width + " │")
    
    # Expanding/contracting visualization
    for row in range(5):
        offset = int(abs(row - 2) * (1 - breath) * 3)
        inner = "█" * (width - offset * 2)
        padding = " " * offset
        lines.append(f"│ {padding}{inner}{padding} │")
    
    lines.append("│ " + " " * width + " │")
    lines.append("╰" + "─" * (width + 2) + "╯")
    lines.append("")
    lines.append(f"  Breathing Phase: {breath:.2f}")
    lines.append(f"  {create_progress_bar(breath, 40, '●', '○', False)}")
    
    if breath > 0.7:
        lines.append("  State: INHALE")
    elif breath < 0.3:
        lines.append("  State: EXHALE")
    else:
        lines.append("  State: TRANSITIONING")
    
    return "\n".join(lines)


def _daynight_frame(frame_index: int, progress: float, config: AnimationConfig) -> str:
    """Generate a day/night cycle frame."""
    # Progress represents time of day (0 = midnight, 0.5 = noon)
    hour = int(progress * 24)
    
    # Sun/moon position
    sun_x = int(progress * 60)
    sun_y = int(5 - 4 * math.sin(progress * math.pi))
    
    # Background based on time
    if 6 <= hour < 18:
        if hour < 8 or hour > 16:
            bg = "░"  # Dawn/dusk
            celestial = "☀"
        else:
            bg = " "  # Day
            celestial = "☀"
    else:
        bg = "▒"  # Night
        celestial = "☽"
    
    # Build frame
    width = 60
    height = 8
    
    lines = []
    lines.append("┌" + "─" * width + "┐")
    
    for y in range(height):
        row = list(bg * width)
        
        # Place celestial body
        if 0 <= sun_x < width and y == sun_y:
            row[sun_x] = celestial
        
        # Ground
        if y == height - 1:
            row = list("▄" * width)
        
        lines.append("│" + "".join(row) + "│")
    
    lines.append("└" + "─" * width + "┘")
    lines.append("")
    lines.append(f"  Time: {hour:02d}:00  |  Phase: {progress:.2f}")
    
    time_desc = ""
    if 6 <= hour < 12:
        time_desc = "Morning"
    elif 12 <= hour < 18:
        time_desc = "Afternoon"
    elif 18 <= hour < 22:
        time_desc = "Evening"
    else:
        time_desc = "Night"
    
    lines.append(f"  Period: {time_desc}")
    
    return "\n".join(lines)


def _expedition_frame(frame_index: int, progress: float, config: AnimationConfig) -> str:
    """Generate an expedition progress frame."""
    # Expedition as journey along a path
    width = 60
    
    waypoints = ["Start", "River", "Mountains", "Valley", "Destination"]
    num_waypoints = len(waypoints)
    
    current_waypoint = int(progress * (num_waypoints - 1))
    waypoint_progress = (progress * (num_waypoints - 1)) % 1
    
    lines = []
    lines.append("═" * width)
    lines.append("  EXPEDITION PROGRESS")
    lines.append("═" * width)
    lines.append("")
    
    # Draw path
    path_line = ""
    traveler_pos = int(progress * (width - 4))
    
    for i in range(width - 4):
        if i == traveler_pos:
            path_line += "🚶"
        elif i % ((width - 4) // (num_waypoints - 1)) == 0:
            path_line += "◆"
        else:
            path_line += "─"
    
    lines.append(f"  {path_line}")
    lines.append("")
    
    # Waypoint labels
    label_line = "  "
    spacing = (width - 4) // (num_waypoints - 1)
    for i, wp in enumerate(waypoints):
        if i == current_waypoint:
            label_line += f"[{wp}]"
        else:
            label_line += wp
        if i < num_waypoints - 1:
            label_line += " " * (spacing - len(wp))
    
    lines.append(label_line[:width])
    lines.append("")
    lines.append(f"  Progress: {create_progress_bar(progress, 40)}")
    lines.append(f"  Current: {waypoints[min(current_waypoint, num_waypoints - 1)]}")
    lines.append(f"  Distance: {progress * 100:.1f}%")
    
    return "\n".join(lines)


def _season_frame(frame_index: int, progress: float, config: AnimationConfig) -> str:
    """Generate a seasonal cycle frame."""
    # Seasons
    seasons = [
        ("Spring", "🌱", "green"),
        ("Summer", "☀️", "yellow"),
        ("Autumn", "🍂", "orange"),
        ("Winter", "❄️", "blue"),
    ]
    
    season_index = int(progress * 4) % 4
    season_progress = (progress * 4) % 1
    
    current = seasons[season_index]
    next_season = seasons[(season_index + 1) % 4]
    
    lines = []
    lines.append("╔" + "═" * 40 + "╗")
    lines.append("║" + " SEASONAL CYCLE ".center(40) + "║")
    lines.append("╠" + "═" * 40 + "╣")
    lines.append("║" + " " * 40 + "║")
    
    # Season display
    season_display = f"  {current[1]} {current[0]} {current[1]}  "
    lines.append("║" + season_display.center(40) + "║")
    lines.append("║" + " " * 40 + "║")
    
    # Progress to next
    lines.append("║" + f"  → {next_season[0]}: {season_progress * 100:.0f}%".ljust(40) + "║")
    lines.append("║" + " " * 40 + "║")
    
    # Seasonal wheel
    wheel = "  "
    for i, (name, emoji, _) in enumerate(seasons):
        if i == season_index:
            wheel += f"[{emoji}]  "
        else:
            wheel += f" {emoji}   "
    
    lines.append("║" + wheel[:40].center(40) + "║")
    lines.append("║" + " " * 40 + "║")
    lines.append("╚" + "═" * 40 + "╝")
    
    return "\n".join(lines)


def generate_breathing_animation(
    output_dir: Optional[Path] = None,
    config: Optional[AnimationConfig] = None,
) -> AnimationSequence:
    """
    Generate breathing cycle animation.
    
    Args:
        output_dir: Optional directory to save frames
        config: Animation configuration
        
    Returns:
        AnimationSequence
    """
    config = config or AnimationConfig(fps=15, duration_seconds=4, loop=True)
    
    sequence = create_animation(
        name="breathing_cycle",
        generator=_breathing_frame,
        config=config,
    )
    
    if output_dir:
        save_animation_frames(sequence, Path(output_dir), "breathing")
    
    return sequence


def generate_daynight_animation(
    output_dir: Optional[Path] = None,
    config: Optional[AnimationConfig] = None,
) -> AnimationSequence:
    """
    Generate day/night cycle animation.
    
    Args:
        output_dir: Optional directory to save frames
        config: Animation configuration
        
    Returns:
        AnimationSequence
    """
    config = config or AnimationConfig(fps=12, duration_seconds=6, loop=True)
    
    sequence = create_animation(
        name="daynight_cycle",
        generator=_daynight_frame,
        config=config,
    )
    
    if output_dir:
        save_animation_frames(sequence, Path(output_dir), "daynight")
    
    return sequence


def generate_expedition_animation(
    output_dir: Optional[Path] = None,
    config: Optional[AnimationConfig] = None,
) -> AnimationSequence:
    """
    Generate expedition progress animation.
    
    Args:
        output_dir: Optional directory to save frames
        config: Animation configuration
        
    Returns:
        AnimationSequence
    """
    config = config or AnimationConfig(fps=10, duration_seconds=5, easing=EasingFunction.EASE_IN_OUT)
    
    sequence = create_animation(
        name="expedition",
        generator=_expedition_frame,
        config=config,
    )
    
    if output_dir:
        save_animation_frames(sequence, Path(output_dir), "expedition")
    
    return sequence


def generate_season_animation(
    output_dir: Optional[Path] = None,
    config: Optional[AnimationConfig] = None,
) -> AnimationSequence:
    """
    Generate seasonal cycle animation.
    
    Args:
        output_dir: Optional directory to save frames
        config: Animation configuration
        
    Returns:
        AnimationSequence
    """
    config = config or AnimationConfig(fps=8, duration_seconds=8, loop=True)
    
    sequence = create_animation(
        name="season_cycle",
        generator=_season_frame,
        config=config,
    )
    
    if output_dir:
        save_animation_frames(sequence, Path(output_dir), "season")
    
    return sequence


def generate_cycle_animation(
    output_dir: Path,
    config: Optional[AnimationConfig] = None,
) -> dict[str, AnimationSequence]:
    """
    Generate all cycle animations.
    
    Args:
        output_dir: Directory to save frames
        config: Animation configuration
        
    Returns:
        Dictionary of animation sequences
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    return {
        "breathing": generate_breathing_animation(output_dir / "breathing", config),
        "daynight": generate_daynight_animation(output_dir / "daynight", config),
        "expedition": generate_expedition_animation(output_dir / "expedition", config),
        "season": generate_season_animation(output_dir / "season", config),
    }
