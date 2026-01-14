"""
Renderer - Rich visual rendering for stories and verse state.

Creates beautiful terminal output using Rich library.
"""

from __future__ import annotations

from typing import Optional

from rich.console import Console, Group
from rich.panel import Panel
from rich.table import Table
from rich.columns import Columns
from rich.text import Text
from rich.tree import Tree
from rich.layout import Layout
from rich.live import Live
from rich.progress import Progress, SpinnerColumn, TextColumn

from samuel_clemens.core.storyteller import Story
from samuel_clemens.core.navigator import Course, Harbor
from samuel_clemens.protocols.entities import Entity, get_all_entities, get_hero_hosts
from samuel_clemens.protocols.cycles import get_all_cycles, get_time_of_day, get_season

console = Console()


def render_story(story: Story, style: str = "panel") -> None:
    """
    Render a story with beautiful formatting.
    
    Args:
        story: The Story to render
        style: Rendering style (panel, card, minimal, dramatic)
    """
    if style == "panel":
        _render_story_panel(story)
    elif style == "card":
        render_story_card(story)
    elif style == "minimal":
        _render_story_minimal(story)
    elif style == "dramatic":
        _render_story_dramatic(story)
    else:
        _render_story_panel(story)


def _render_story_panel(story: Story) -> None:
    """Render story in a rich panel."""
    console.print(Panel(
        story.text,
        title=f"📖 {story.topic.title()} Tale",
        subtitle=f"[{story.emotion.value}]",
        border_style="magenta",
        padding=(1, 2),
    ))


def _render_story_minimal(story: Story) -> None:
    """Render story with minimal formatting."""
    console.print(f"\n[italic]{story.text}[/italic]\n")


def _render_story_dramatic(story: Story) -> None:
    """Render story with dramatic effect."""
    from time import sleep
    
    console.print("\n[bold yellow]" + "═" * 60 + "[/bold yellow]")
    console.print()
    
    # Print letter by letter for dramatic effect
    words = story.text.split()
    for i, word in enumerate(words):
        if i > 0:
            console.print(" ", end="")
        console.print(f"[cyan]{word}[/cyan]", end="")
        if word.endswith(('.', '!', '?', ':')):
            console.print()
    
    console.print()
    console.print("[bold yellow]" + "═" * 60 + "[/bold yellow]\n")


def render_story_card(story: Story) -> None:
    """
    Render a story as a beautiful card.
    
    Args:
        story: The Story to render
    """
    # Create the card layout
    card_content = Text()
    card_content.append("🎭 ", style="bold")
    card_content.append(story.topic.upper(), style="bold cyan")
    card_content.append("\n\n")
    card_content.append(story.text, style="italic")
    card_content.append("\n\n")
    card_content.append(f"Emotion: {story.emotion.value}", style="dim")
    card_content.append("  |  ", style="dim")
    card_content.append(f"Keywords: {', '.join(story.keywords[:3])}", style="dim")
    
    console.print(Panel(
        card_content,
        title="🎩 Mark Twain Presents",
        border_style="yellow",
    ))


def render_verse_dashboard() -> None:
    """
    Render a comprehensive dashboard of the verse state.
    
    Shows cycles, entities, mood, and current activity.
    """
    layout = Layout()
    layout.split_column(
        Layout(name="header", size=3),
        Layout(name="main"),
        Layout(name="footer", size=3),
    )
    layout["main"].split_row(
        Layout(name="cycles"),
        Layout(name="entities"),
    )
    
    # Header
    header = Panel(
        Text("🏔️ MarkTwainVerse Dashboard", justify="center", style="bold yellow"),
        border_style="yellow",
    )
    
    # Cycles table
    cycles = get_all_cycles()
    cycles_table = Table(title="🌀 Natural Cycles", show_header=True)
    cycles_table.add_column("Cycle", style="cyan")
    cycles_table.add_column("Phase", style="green")
    cycles_table.add_column("State", style="yellow")
    
    for name, cycle in cycles.items():
        phase_bar = _create_phase_bar(cycle.phase)
        cycles_table.add_row(cycle.name, phase_bar, cycle.description)
    
    # Entities table
    entities = get_all_entities()
    entities_table = Table(title="🌟 Living Entities", show_header=True)
    entities_table.add_column("Entity", style="cyan")
    entities_table.add_column("Type", style="green")
    entities_table.add_column("Mood", style="yellow")
    entities_table.add_column("Energy", style="magenta")
    
    for entity in list(entities.values())[:5]:
        energy_bar = _create_energy_bar(entity.energy)
        entities_table.add_row(
            entity.name,
            entity.entity_type.value,
            entity.state.mood.value,
            energy_bar,
        )
    
    # Footer
    time_of_day = get_time_of_day()
    season = get_season()
    footer = Panel(
        Text(f"⏰ {time_of_day.title()} | 🍂 {season.title()} | 📍 Frontier Town Center", 
             justify="center", style="dim"),
        border_style="dim",
    )
    
    # Render
    console.print(header)
    console.print(Columns([cycles_table, entities_table], equal=True, expand=True))
    console.print(footer)


def _create_phase_bar(phase: float, width: int = 10) -> str:
    """Create a visual phase bar."""
    filled = int(phase * width)
    empty = width - filled
    return f"[green]{'█' * filled}[/green][dim]{'░' * empty}[/dim] {phase:.2f}"


def _create_energy_bar(energy: float, width: int = 8) -> str:
    """Create a visual energy bar."""
    filled = int(energy * width)
    empty = width - filled
    color = "green" if energy > 0.7 else "yellow" if energy > 0.4 else "red"
    return f"[{color}]{'■' * filled}[/{color}][dim]{'□' * empty}[/dim]"


def render_expedition_map(course: Course) -> None:
    """
    Render an expedition course as a visual map.
    
    Args:
        course: The Course to visualize
    """
    console.print(Panel(
        _create_expedition_visualization(course),
        title=f"🗺️ Expedition: {course.destination}",
        subtitle=f"Duration: {course.duration_hours}h",
        border_style="blue",
    ))


def _create_expedition_visualization(course: Course) -> str:
    """Create ASCII visualization of expedition route."""
    lines = []
    lines.append(f"[bold cyan]{course.description}[/bold cyan]\n")
    lines.append("[dim]Route:[/dim]\n")
    
    for i, waypoint in enumerate(course.waypoints):
        if i == 0:
            lines.append(f"  🏠 [green]{waypoint}[/green] (Start)")
        elif i == len(course.waypoints) - 1:
            lines.append(f"  │")
            lines.append(f"  ↓")
            lines.append(f"  🎯 [yellow]{waypoint}[/yellow] (Destination)")
        else:
            lines.append(f"  │")
            lines.append(f"  ├─ 📍 {waypoint}")
    
    return "\n".join(lines)


def render_entity_network() -> None:
    """
    Render the network of living entities as a tree.
    """
    tree = Tree("🌍 [bold]MarkTwainVerse Entity Network[/bold]")
    
    # Hero Hosts
    hosts_branch = tree.add("🎭 [cyan]Hero Hosts[/cyan]")
    for host in get_hero_hosts():
        host_node = hosts_branch.add(f"[yellow]{host.name}[/yellow]")
        host_node.add(f"[dim]Energy: {host.energy:.2f}[/dim]")
        host_node.add(f"[dim]Mood: {host.state.mood.value}[/dim]")
        if host.connections:
            conn_node = host_node.add("[dim]Connections:[/dim]")
            for conn in host.connections[:3]:
                conn_node.add(f"[dim]{conn}[/dim]")
    
    # Other entities by type
    entities = get_all_entities()
    buildings = [e for e in entities.values() if e.entity_type.value == "building"]
    landscapes = [e for e in entities.values() if e.entity_type.value == "landscape"]
    systems = [e for e in entities.values() if e.entity_type.value == "system"]
    
    if buildings:
        buildings_branch = tree.add("🏛️ [cyan]Buildings[/cyan]")
        for b in buildings:
            buildings_branch.add(f"{b.name} ({b.state.mood.value})")
    
    if landscapes:
        landscapes_branch = tree.add("🌲 [cyan]Landscapes[/cyan]")
        for l in landscapes:
            landscapes_branch.add(f"{l.name} ({l.state.mood.value})")
    
    if systems:
        systems_branch = tree.add("⚡ [cyan]Systems[/cyan]")
        for s in systems:
            systems_branch.add(f"{s.name}")
    
    console.print(tree)


def render_story_gallery(stories: list[Story], layout: str = "grid") -> None:
    """
    Render multiple stories in a gallery format.
    
    Args:
        stories: List of stories to display
        layout: Layout style (grid, list, carousel)
    """
    if layout == "grid":
        panels = []
        for story in stories[:6]:  # Max 6 for grid
            panels.append(Panel(
                story.text[:100] + "..." if len(story.text) > 100 else story.text,
                title=story.topic.title(),
                border_style="magenta",
                width=40,
            ))
        console.print(Columns(panels, equal=True))
    
    elif layout == "list":
        for i, story in enumerate(stories, 1):
            console.print(f"\n[bold cyan]Story {i}: {story.topic.title()}[/bold cyan]")
            console.print(f"[dim]{story.emotion.value}[/dim]")
            console.print(story.text)
            console.print("[dim]" + "─" * 40 + "[/dim]")
    
    else:  # carousel
        for i, story in enumerate(stories):
            console.print(f"\n[bold]({i+1}/{len(stories)})[/bold]")
            render_story_card(story)


def render_loading_animation(message: str = "Spinning a yarn...") -> Progress:
    """
    Create a loading animation for story generation.
    
    Args:
        message: Loading message to display
        
    Returns:
        Progress object to use with context manager
    """
    return Progress(
        SpinnerColumn(),
        TextColumn(f"[bold cyan]{message}[/bold cyan]"),
        console=console,
    )
