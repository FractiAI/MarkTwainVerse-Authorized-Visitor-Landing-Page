"""
Advanced Charts - Extended chart visualizations for the MarkTwainVerse.

Additional chart types and visualizations beyond the basics.
"""

from __future__ import annotations

import math
from datetime import datetime
from typing import Optional

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.columns import Columns
from rich.text import Text

from samuel_clemens.protocols.cycles import get_all_cycles
from samuel_clemens.protocols.entities import get_all_entities, EntityMood, EntityType

console = Console()


def render_heatmap(
    data: Optional[dict[str, dict[str, float]]] = None,
    title: str = "Activity Heatmap",
) -> None:
    """
    Render a heatmap visualization.
    
    Args:
        data: 2D data (row -> col -> value), generates demo if None
        title: Chart title
    """
    if data is None:
        # Generate demo data - activity by hour and day
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        hours = ["Morning", "Afternoon", "Evening", "Night"]
        data = {}
        for day in days:
            data[day] = {}
            for hour in hours:
                # Simulate activity patterns
                base = 0.5
                if day in ["Sat", "Sun"]:
                    base += 0.2
                if hour == "Evening":
                    base += 0.15
                elif hour == "Night":
                    base -= 0.3
                data[day][hour] = max(0, min(1, base + (hash(f"{day}{hour}") % 100) / 300))
    
    # Heat chars based on value
    def heat_char(val: float) -> str:
        if val > 0.8:
            return "[bold red]█[/bold red]"
        elif val > 0.6:
            return "[red]▓[/red]"
        elif val > 0.4:
            return "[yellow]▒[/yellow]"
        elif val > 0.2:
            return "[green]░[/green]"
        else:
            return "[dim] [/dim]"
    
    table = Table(title=title, show_header=True)
    table.add_column("", style="cyan")
    
    cols = list(list(data.values())[0].keys())
    for col in cols:
        table.add_column(col, justify="center")
    
    for row_name, row_data in data.items():
        cells = [heat_char(row_data[col]) * 3 for col in cols]
        table.add_row(row_name, *cells)
    
    # Legend
    legend = "  [dim]░[/dim] Low  [green]░[/green] Medium  [yellow]▒[/yellow] High  [red]▓[/red] Very High  [bold red]█[/bold red] Peak"
    
    console.print(table)
    console.print(legend)


def render_sparkline(
    values: list[float],
    title: str = "Trend",
    width: int = 50,
) -> None:
    """
    Render a sparkline (mini line chart).
    
    Args:
        values: List of values to plot
        title: Label for the sparkline
        width: Character width
    """
    if not values:
        return
    
    # Normalize to 0-7 range (8 sparkline chars)
    min_val, max_val = min(values), max(values)
    range_val = max_val - min_val or 1
    
    # Sparkline characters
    chars = "▁▂▃▄▅▆▇█"
    
    # Sample or interpolate to width
    if len(values) > width:
        step = len(values) / width
        sampled = [values[int(i * step)] for i in range(width)]
    else:
        sampled = values
    
    # Convert to sparkline
    sparkline = ""
    for val in sampled:
        normalized = (val - min_val) / range_val
        char_idx = int(normalized * 7)
        sparkline += chars[char_idx]
    
    console.print(f"[cyan]{title}:[/cyan] [green]{sparkline}[/green]")
    console.print(f"  [dim]min: {min_val:.2f}  max: {max_val:.2f}[/dim]")


def render_gauge(
    value: float,
    title: str = "Value",
    min_val: float = 0,
    max_val: float = 100,
    thresholds: Optional[dict[str, float]] = None,
) -> None:
    """
    Render a gauge visualization.
    
    Args:
        value: Current value
        title: Gauge title
        min_val: Minimum value
        max_val: Maximum value
        thresholds: Color thresholds
    """
    if thresholds is None:
        thresholds = {"green": 0.7, "yellow": 0.4, "red": 0}
    
    # Normalize
    normalized = (value - min_val) / (max_val - min_val)
    normalized = max(0, min(1, normalized))
    
    # Determine color
    if normalized >= thresholds["green"]:
        color = "green"
    elif normalized >= thresholds["yellow"]:
        color = "yellow"
    else:
        color = "red"
    
    # Create gauge
    width = 30
    filled = int(normalized * width)
    empty = width - filled
    
    gauge = f"[{color}]{'█' * filled}[/{color}][dim]{'░' * empty}[/dim]"
    
    console.print(Panel(
        f"\n  {gauge}\n\n  [bold]{value:.1f}[/bold] / {max_val}",
        title=f"📊 {title}",
        border_style=color,
    ))


def render_entity_matrix() -> None:
    """Render entity type vs mood matrix."""
    entities = get_all_entities()
    
    # Count entities by type and mood
    matrix: dict[EntityType, dict[EntityMood, int]] = {}
    for e in entities.values():
        if e.entity_type not in matrix:
            matrix[e.entity_type] = {}
        if e.state.mood not in matrix[e.entity_type]:
            matrix[e.entity_type][e.state.mood] = 0
        matrix[e.entity_type][e.state.mood] += 1
    
    table = Table(title="🎭 Entity Type vs Mood Matrix")
    table.add_column("Type", style="cyan")
    
    moods = list(EntityMood)
    for mood in moods:
        table.add_column(mood.value[:3], justify="center")
    
    for entity_type, mood_counts in matrix.items():
        cells = []
        for mood in moods:
            count = mood_counts.get(mood, 0)
            if count > 0:
                cells.append(f"[green]{count}[/green]")
            else:
                cells.append("[dim]·[/dim]")
        table.add_row(entity_type.value, *cells)
    
    console.print(table)


def render_radar_chart(
    values: dict[str, float],
    title: str = "Radar Chart",
    radius: int = 8,
) -> None:
    """
    Render a text-based radar chart.
    
    Args:
        values: Named values (0-1 range)
        title: Chart title
        radius: Chart radius
    """
    labels = list(values.keys())
    vals = list(values.values())
    n = len(labels)
    
    if n < 3:
        console.print("[red]Radar chart requires at least 3 values[/red]")
        return
    
    # Create grid
    size = radius * 2 + 3
    grid = [[" " for _ in range(size)] for _ in range(size)]
    center = radius + 1
    
    # Draw axes
    for i in range(n):
        angle = 2 * math.pi * i / n - math.pi / 2
        for r in range(1, radius + 1):
            x = int(center + r * math.cos(angle))
            y = int(center + r * math.sin(angle))
            if 0 <= x < size and 0 <= y < size:
                grid[y][x] = "·"
    
    # Draw values
    for i, val in enumerate(vals):
        angle = 2 * math.pi * i / n - math.pi / 2
        r = int(val * radius)
        x = int(center + r * math.cos(angle))
        y = int(center + r * math.sin(angle))
        if 0 <= x < size and 0 <= y < size:
            grid[y][x] = "●"
    
    # Center
    grid[center][center] = "+"
    
    # Render
    lines = []
    lines.append(f"  {title}")
    lines.append("  " + "─" * size)
    for row in grid:
        lines.append("  " + "".join(row))
    lines.append("  " + "─" * size)
    
    # Legend
    for i, label in enumerate(labels):
        lines.append(f"  {label}: {vals[i]*100:.0f}%")
    
    console.print("\n".join(lines))


def render_histogram(
    values: list[float],
    bins: int = 10,
    title: str = "Distribution",
) -> None:
    """
    Render a histogram.
    
    Args:
        values: Values to bin
        bins: Number of bins
        title: Chart title
    """
    if not values:
        return
    
    min_val, max_val = min(values), max(values)
    range_val = max_val - min_val or 1
    bin_width = range_val / bins
    
    # Count values in bins
    counts = [0] * bins
    for val in values:
        bin_idx = min(int((val - min_val) / bin_width), bins - 1)
        counts[bin_idx] += 1
    
    max_count = max(counts) or 1
    bar_max = 30
    
    console.print(f"\n[bold]{title}[/bold]")
    console.print()
    
    for i, count in enumerate(counts):
        bin_start = min_val + i * bin_width
        bin_end = bin_start + bin_width
        bar_width = int(count / max_count * bar_max)
        
        label = f"{bin_start:6.2f}-{bin_end:6.2f}"
        bar = "█" * bar_width
        
        console.print(f"  [dim]{label}[/dim] [green]{bar}[/green] {count}")


def render_bar_chart(
    data: dict[str, float],
    title: str = "Bar Chart",
    horizontal: bool = True,
    max_width: int = 40,
) -> None:
    """
    Render a bar chart.
    
    Args:
        data: Label -> value mapping
        title: Chart title
        horizontal: Horizontal or vertical bars
        max_width: Maximum bar width
    """
    if not data:
        return
    
    max_val = max(data.values()) or 1
    
    console.print(f"\n[bold]{title}[/bold]")
    console.print()
    
    if horizontal:
        max_label = max(len(label) for label in data.keys())
        for label, value in data.items():
            bar_width = int(value / max_val * max_width)
            bar = "█" * bar_width
            console.print(f"  [cyan]{label.ljust(max_label)}[/cyan] [green]{bar}[/green] {value:.1f}")
    else:
        # Vertical bars
        height = 10
        labels = list(data.keys())
        values = [data[l] for l in labels]
        
        for row in range(height, 0, -1):
            line = "  "
            threshold = row / height
            for val in values:
                normalized = val / max_val
                if normalized >= threshold:
                    line += " █ "
                else:
                    line += "   "
            console.print(line)
        
        console.print("  " + "─" * (len(labels) * 3 + 1))
        console.print("  " + " ".join(f" {l[:1]} " for l in labels))


def render_stacked_bars(
    data: dict[str, dict[str, float]],
    title: str = "Stacked Bars",
) -> None:
    """
    Render stacked bar chart.
    
    Args:
        data: Category -> {subcategory -> value}
        title: Chart title
    """
    if not data:
        return
    
    colors = ["green", "blue", "yellow", "red", "magenta", "cyan"]
    
    # Get all subcategories
    all_subs = set()
    for subs in data.values():
        all_subs.update(subs.keys())
    all_subs = list(all_subs)
    
    max_total = max(sum(subs.values()) for subs in data.values()) or 1
    bar_max = 40
    
    console.print(f"\n[bold]{title}[/bold]")
    console.print()
    
    for label, subs in data.items():
        bar = ""
        for i, sub in enumerate(all_subs):
            val = subs.get(sub, 0)
            width = int(val / max_total * bar_max)
            color = colors[i % len(colors)]
            bar += f"[{color}]{'█' * width}[/{color}]"
        
        console.print(f"  [cyan]{label:10}[/cyan] {bar}")
    
    # Legend
    console.print()
    legend = "  "
    for i, sub in enumerate(all_subs):
        color = colors[i % len(colors)]
        legend += f"[{color}]█[/{color}] {sub}  "
    console.print(legend)


def render_treemap(
    data: dict[str, float],
    title: str = "Treemap",
    width: int = 60,
    height: int = 12,
) -> None:
    """
    Render a simple treemap visualization.
    
    Args:
        data: Label -> value mapping
        title: Chart title
        width: Output width
        height: Output height
    """
    if not data:
        return
    
    total = sum(data.values()) or 1
    
    # Calculate proportions
    proportions = {k: v / total for k, v in data.items()}
    
    console.print(f"\n[bold]{title}[/bold]")
    console.print("┌" + "─" * width + "┐")
    
    # Simple horizontal layout
    remaining_width = width
    cells = []
    
    for label, prop in sorted(proportions.items(), key=lambda x: -x[1]):
        cell_width = max(1, int(prop * width))
        if remaining_width <= 0:
            break
        cell_width = min(cell_width, remaining_width)
        remaining_width -= cell_width
        cells.append((label, cell_width, prop))
    
    # Render rows
    for _ in range(height // 2):
        line = "│"
        for label, cell_width, _ in cells:
            line += "█" * cell_width
        line = line[:width + 1].ljust(width + 1) + "│"
        console.print(line)
    
    # Labels row
    line = "│"
    for label, cell_width, prop in cells:
        text = f"{label[:cell_width-1]}" if cell_width > len(label) else label[:cell_width]
        line += text.center(cell_width)
    line = line[:width + 1].ljust(width + 1) + "│"
    console.print(line)
    
    # Bottom half
    for _ in range(height // 2 - 1):
        line = "│"
        for label, cell_width, _ in cells:
            line += "░" * cell_width
        line = line[:width + 1].ljust(width + 1) + "│"
        console.print(line)
    
    console.print("└" + "─" * width + "┘")
    
    # Legend
    for label, _, prop in cells:
        console.print(f"  {label}: {prop * 100:.1f}%")


def render_activity_stream() -> None:
    """Render recent activity stream."""
    from samuel_clemens.protocols.events import get_active_events
    
    events = get_active_events()
    
    console.print("\n[bold]🌊 Activity Stream[/bold]")
    console.print("─" * 50)
    
    if not events:
        console.print("  [dim]No recent activity[/dim]")
        return
    
    for event in events[:10]:
        time_str = event.triggered_at.strftime("%H:%M") if event.triggered_at else "??:??"
        console.print(f"  [dim]{time_str}[/dim] │ [cyan]{event.name}[/cyan]")
    
    console.print("─" * 50)


def render_entity_leaderboard() -> None:
    """Render entity energy leaderboard."""
    entities = get_all_entities()
    
    # Sort by energy
    sorted_entities = sorted(
        entities.items(),
        key=lambda x: x[1].energy,
        reverse=True,
    )
    
    table = Table(title="🏆 Entity Energy Leaderboard")
    table.add_column("Rank", style="yellow", justify="center")
    table.add_column("Entity", style="cyan")
    table.add_column("Energy", justify="right")
    table.add_column("Mood")
    
    medals = ["🥇", "🥈", "🥉"]
    
    for i, (eid, entity) in enumerate(sorted_entities[:10]):
        rank = medals[i] if i < 3 else f"#{i + 1}"
        energy_bar = "█" * int(entity.energy * 10)
        mood_emoji = {
            EntityMood.DORMANT: "💤",
            EntityMood.RESTING: "😴",
            EntityMood.ACTIVE: "😊",
            EntityMood.AWAKENING: "😃",
            EntityMood.THRIVING: "🌟",
        }.get(entity.state.mood, "●")
        
        table.add_row(
            rank,
            entity.name,
            f"[green]{energy_bar}[/green] {entity.energy * 100:.0f}%",
            mood_emoji,
        )
    
    console.print(table)


def render_correlation_matrix(
    data: Optional[dict[str, dict[str, float]]] = None,
) -> None:
    """
    Render correlation matrix.
    
    Args:
        data: Correlation data, generates demo if None
    """
    if data is None:
        # Demo: entity metrics correlations
        labels = ["Energy", "Mood", "Activity", "Connection"]
        data = {}
        for l1 in labels:
            data[l1] = {}
            for l2 in labels:
                if l1 == l2:
                    data[l1][l2] = 1.0
                else:
                    # Random correlation
                    data[l1][l2] = (hash(f"{l1}{l2}") % 200 - 100) / 100
    
    def corr_color(val: float) -> str:
        if val > 0.5:
            return "[bold green]█[/bold green]"
        elif val > 0.2:
            return "[green]▓[/green]"
        elif val > -0.2:
            return "[yellow]▒[/yellow]"
        elif val > -0.5:
            return "[red]▓[/red]"
        else:
            return "[bold red]█[/bold red]"
    
    table = Table(title="📈 Correlation Matrix")
    table.add_column("", style="cyan")
    
    labels = list(data.keys())
    for label in labels:
        table.add_column(label[:4], justify="center")
    
    for l1 in labels:
        cells = [corr_color(data[l1].get(l2, 0)) for l2 in labels]
        table.add_row(l1, *cells)
    
    console.print(table)
    console.print("  [bold green]█[/bold green] Strong +  [green]▓[/green] Weak +  [yellow]▒[/yellow] None  [red]▓[/red] Weak -  [bold red]█[/bold red] Strong -")
