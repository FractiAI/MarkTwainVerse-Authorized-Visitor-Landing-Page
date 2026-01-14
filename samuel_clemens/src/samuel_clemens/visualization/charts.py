"""
Charts - Terminal-based charts for cycle visualization.

Creates visual representations of natural cycles and energy states.
"""

from __future__ import annotations

import math
from typing import Optional

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from samuel_clemens.protocols.cycles import (
    get_all_cycles,
    get_day_phase,
    get_season_phase,
    get_breathing_pulse,
    get_activity_multiplier,
)
from samuel_clemens.protocols.entities import (
    get_all_entities,
    get_total_energy,
    get_dominant_mood,
    EntityMood,
)

console = Console()


def render_cycle_chart(cycle_name: Optional[str] = None) -> None:
    """
    Render a visual chart of natural cycles.
    
    Args:
        cycle_name: Specific cycle to show, or None for all
    """
    if cycle_name:
        _render_single_cycle(cycle_name)
    else:
        _render_all_cycles()


def _render_single_cycle(cycle_name: str) -> None:
    """Render a single cycle with detailed visualization."""
    cycles = get_all_cycles()
    cycle = cycles.get(cycle_name)
    
    if not cycle:
        console.print(f"[red]Unknown cycle: {cycle_name}[/red]")
        return
    
    # Create wave visualization
    wave = _create_wave_visualization(cycle.phase, width=50)
    
    console.print(Panel(
        f"{wave}\n\n"
        f"[bold]Phase:[/bold] {cycle.phase:.4f}\n"
        f"[bold]Duration:[/bold] {cycle.duration_ms / 1000:.1f}s\n"
        f"[bold]Status:[/bold] {cycle.description}",
        title=f"🌀 {cycle.name}",
        border_style="cyan",
    ))


def _render_all_cycles() -> None:
    """Render all cycles in a unified view."""
    cycles = get_all_cycles()
    
    table = Table(title="🌀 Natural Cycles Overview", show_header=True)
    table.add_column("Cycle", style="cyan", width=20)
    table.add_column("Phase Bar", width=30)
    table.add_column("Value", style="green", width=8)
    table.add_column("Status", style="yellow", width=25)
    
    for name, cycle in cycles.items():
        phase_bar = _create_horizontal_bar(cycle.phase, width=25)
        table.add_row(
            cycle.name,
            phase_bar,
            f"{cycle.phase:.3f}",
            cycle.description,
        )
    
    console.print(table)


def _create_wave_visualization(phase: float, width: int = 50) -> str:
    """Create a sine wave visualization with current position marker."""
    lines = []
    height = 5
    
    for y in range(height):
        line = ""
        for x in range(width):
            # Calculate sine wave position
            wave_phase = (x / width) * 2 * math.pi
            wave_y = (math.sin(wave_phase) + 1) / 2 * (height - 1)
            
            # Current position marker
            current_x = int(phase * width)
            
            if x == current_x:
                line += "[bold red]●[/bold red]"
            elif abs(wave_y - (height - 1 - y)) < 0.5:
                line += "[cyan]~[/cyan]"
            else:
                line += " "
        lines.append(line)
    
    return "\n".join(lines)


def _create_horizontal_bar(value: float, width: int = 20) -> str:
    """Create a horizontal progress bar."""
    filled = int(value * width)
    empty = width - filled
    
    # Color based on position in cycle
    if value < 0.25:
        color = "blue"
    elif value < 0.5:
        color = "green"
    elif value < 0.75:
        color = "yellow"
    else:
        color = "magenta"
    
    return f"[{color}]{'█' * filled}[/{color}][dim]{'░' * empty}[/dim]"


def render_energy_bars() -> None:
    """
    Render energy bars for all entities.
    """
    entities = get_all_entities()
    
    table = Table(title="⚡ Entity Energy Levels", show_header=True)
    table.add_column("Entity", style="cyan", width=25)
    table.add_column("Energy Bar", width=30)
    table.add_column("Level", style="green", width=8)
    table.add_column("Mood", style="yellow", width=12)
    
    for entity in entities.values():
        bar = _create_energy_bar_colored(entity.energy)
        table.add_row(
            entity.name,
            bar,
            f"{entity.energy:.2f}",
            entity.state.mood.value,
        )
    
    # Add total
    total = get_total_energy()
    table.add_row(
        "[bold]TOTAL AVERAGE[/bold]",
        _create_energy_bar_colored(total),
        f"[bold]{total:.2f}[/bold]",
        get_dominant_mood().value,
    )
    
    console.print(table)


def _create_energy_bar_colored(energy: float, width: int = 25) -> str:
    """Create a colored energy bar based on level."""
    filled = int(energy * width)
    empty = width - filled
    
    if energy > 0.8:
        color = "green"
        bar = f"[bold green]{'■' * filled}[/bold green][dim]{'□' * empty}[/dim]"
    elif energy > 0.6:
        color = "green"
        bar = f"[green]{'■' * filled}[/green][dim]{'□' * empty}[/dim]"
    elif energy > 0.4:
        color = "yellow"
        bar = f"[yellow]{'■' * filled}[/yellow][dim]{'□' * empty}[/dim]"
    elif energy > 0.2:
        color = "red"
        bar = f"[red]{'■' * filled}[/red][dim]{'□' * empty}[/dim]"
    else:
        color = "red"
        bar = f"[bold red]{'■' * filled}[/bold red][dim]{'□' * empty}[/dim]"
    
    return bar


def render_timeline(hours: int = 24) -> None:
    """
    Render a timeline showing day/night cycle progression.
    
    Args:
        hours: Number of hours to show
    """
    console.print(Panel(
        _create_timeline_visualization(hours),
        title="🌅 Day-Night Timeline",
        border_style="yellow",
    ))


def _create_timeline_visualization(hours: int = 24) -> str:
    """Create a timeline visualization."""
    lines = []
    
    # Time markers
    time_line = ""
    for h in range(0, hours + 1, 6):
        time_line += f"{h:02d}:00".ljust(10)
    lines.append(f"[dim]{time_line}[/dim]")
    
    # Sun/Moon visualization
    current_phase = get_day_phase()
    current_pos = int(current_phase * hours)
    
    symbol_line = ""
    for h in range(hours):
        # Determine if day or night
        phase = h / hours
        if 0.25 <= phase <= 0.75:
            symbol = "☀️" if h == current_pos else "[yellow]·[/yellow]"
        else:
            symbol = "🌙" if h == current_pos else "[blue]·[/blue]"
        symbol_line += symbol
    
    lines.append(symbol_line)
    
    # Activity level line
    activity_line = ""
    for h in range(hours):
        phase = h / hours
        activity = _calculate_activity_for_phase(phase)
        if activity > 0.8:
            activity_line += "[green]█[/green]"
        elif activity > 0.6:
            activity_line += "[green]▓[/green]"
        elif activity > 0.4:
            activity_line += "[yellow]▒[/yellow]"
        else:
            activity_line += "[blue]░[/blue]"
    
    lines.append(f"Activity: {activity_line}")
    
    # Current time marker
    lines.append(f"\n[bold]Current Phase:[/bold] {current_phase:.3f}")
    lines.append(f"[bold]Activity Level:[/bold] {get_activity_multiplier():.2f}")
    
    return "\n".join(lines)


def _calculate_activity_for_phase(phase: float) -> float:
    """Calculate activity level for a given phase."""
    if phase < 0.25:
        return 0.3 + phase * 2.8
    elif phase < 0.75:
        return 1.0
    elif phase < 1.0:
        return 1.0 - ((phase - 0.75) * 2)
    return 0.3


def render_mood_wheel() -> None:
    """
    Render a mood wheel showing entity distribution.
    """
    entities = get_all_entities()
    
    # Count moods
    mood_counts: dict[EntityMood, int] = {}
    for entity in entities.values():
        mood = entity.state.mood
        mood_counts[mood] = mood_counts.get(mood, 0) + 1
    
    # Create wheel visualization
    total = len(entities)
    
    console.print(Panel(
        _create_mood_wheel(mood_counts, total),
        title="🎭 Mood Distribution",
        border_style="magenta",
    ))


def _create_mood_wheel(mood_counts: dict[EntityMood, int], total: int) -> str:
    """Create a text-based mood wheel."""
    lines = []
    
    mood_colors = {
        EntityMood.DORMANT: ("blue", "💤"),
        EntityMood.AWAKENING: ("cyan", "🌅"),
        EntityMood.ACTIVE: ("yellow", "⭐"),
        EntityMood.THRIVING: ("green", "🌟"),
        EntityMood.RESTING: ("magenta", "🌙"),
    }
    
    for mood in EntityMood:
        count = mood_counts.get(mood, 0)
        percentage = (count / total * 100) if total > 0 else 0
        bar_width = int(percentage / 5)  # Scale to reasonable width
        
        color, emoji = mood_colors.get(mood, ("white", "●"))
        bar = f"[{color}]{'█' * bar_width}[/{color}]" if bar_width > 0 else ""
        
        lines.append(f"{emoji} {mood.value.ljust(12)} {bar} {count} ({percentage:.0f}%)")
    
    return "\n".join(lines)


def render_cycle_comparison() -> None:
    """
    Render a comparison of all cycles side by side.
    """
    cycles = get_all_cycles()
    
    # Create side-by-side mini-charts
    panels = []
    for name, cycle in cycles.items():
        mini_wave = _create_mini_wave(cycle.phase)
        panels.append(Panel(
            f"{mini_wave}\n\n[bold]{cycle.phase:.3f}[/bold]",
            title=cycle.name[:15],
            border_style="cyan",
            width=18,
        ))
    
    console.print(Panel(
        Columns(panels, equal=True),
        title="🌀 Cycle Comparison",
        border_style="yellow",
    ))


def _create_mini_wave(phase: float, width: int = 12, height: int = 3) -> str:
    """Create a mini wave visualization."""
    lines = []
    for y in range(height):
        line = ""
        for x in range(width):
            wave_phase = (x / width) * 2 * math.pi
            wave_y = (math.sin(wave_phase) + 1) / 2 * (height - 1)
            current_x = int(phase * width)
            
            if x == current_x:
                line += "[red]●[/red]"
            elif abs(wave_y - (height - 1 - y)) < 0.5:
                line += "[cyan]~[/cyan]"
            else:
                line += " "
        lines.append(line)
    return "\n".join(lines)


# Import Columns for comparison
from rich.columns import Columns
