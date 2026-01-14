"""
Layouts - Complex multi-panel layouts and compositions.

Create rich, multi-element visualizations combining various components.
"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from rich.console import Console, Group
from rich.panel import Panel
from rich.table import Table
from rich.columns import Columns
from rich.layout import Layout
from rich.text import Text

from samuel_clemens.protocols.cycles import get_all_cycles
from samuel_clemens.protocols.entities import get_all_entities, EntityMood
from samuel_clemens.narrative.quotes import get_random_quote

console = Console()


def render_split_layout(
    left_content,
    right_content,
    left_title: str = "Left",
    right_title: str = "Right",
    ratio: tuple[int, int] = (1, 1),
) -> None:
    """
    Render a split two-column layout.
    
    Args:
        left_content: Content for left panel
        right_content: Content for right panel
        left_title: Left panel title
        right_title: Right panel title
        ratio: Width ratio
    """
    left_panel = Panel(left_content, title=left_title)
    right_panel = Panel(right_content, title=right_title)
    
    console.print(Columns([left_panel, right_panel], equal=ratio[0] == ratio[1]))


def render_triple_layout(
    left_content,
    center_content,
    right_content,
    titles: tuple[str, str, str] = ("Left", "Center", "Right"),
) -> None:
    """Render a three-column layout."""
    panels = [
        Panel(c, title=t) 
        for c, t in zip([left_content, center_content, right_content], titles)
    ]
    console.print(Columns(panels))


def render_header_body_footer(
    header_content,
    body_content,
    footer_content,
    header_style: str = "bold yellow",
    footer_style: str = "dim",
) -> None:
    """Render header-body-footer layout."""
    console.print(Panel(header_content, border_style=header_style))
    console.print(Panel(body_content, padding=(1, 2)))
    console.print(Panel(footer_content, border_style=footer_style))


def render_main_dashboard() -> None:
    """Render the main MarkTwainVerse dashboard."""
    cycles = get_all_cycles()
    entities = get_all_entities()
    quote = get_random_quote()
    
    # Header
    console.print(Panel(
        "[bold yellow]🎩 MarkTwainVerse Dashboard[/bold yellow]\n"
        f"[dim]{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}[/dim]",
        border_style="yellow",
    ))
    
    # Cycles panel
    cycle_lines = []
    for name, cycle in list(cycles.items())[:4]:
        cycle_lines.append(f"  {name}: {cycle.phase:.0%} ({cycle.name})")
    cycles_panel = Panel("\n".join(cycle_lines), title="🔄 Active Cycles")
    
    # Entities panel
    entity_lines = []
    mood_emoji = {
        EntityMood.DORMANT: "💤",
        EntityMood.RESTING: "😴",
        EntityMood.ACTIVE: "😊",
        EntityMood.AWAKENING: "😃",
        EntityMood.THRIVING: "🌟",
    }
    for eid, e in list(entities.items())[:4]:
        emoji = mood_emoji.get(e.state.mood, "●")
        entity_lines.append(f"  {emoji} {e.name[:15]}: {e.energy*100:.0f}%")
    entities_panel = Panel("\n".join(entity_lines), title="🎭 Entities")
    
    # Side by side
    console.print(Columns([cycles_panel, entities_panel]))
    
    # Quote
    console.print(Panel(
        f"[italic]{quote.text}[/italic]\n\n[dim]— {quote.source}[/dim]",
        title="💡 Wisdom",
        border_style="green",
    ))


def render_story_showcase(stories: list, title: str = "Story Showcase") -> None:
    """
    Render a showcase of stories in card format.
    
    Args:
        stories: List of stories to display
        title: Showcase title
    """
    console.print(f"\n[bold]{title}[/bold]")
    console.print("═" * 60)
    
    cards = []
    for story in stories[:6]:
        card_content = (
            f"[bold]{story.title}[/bold]\n\n"
            f"{story.text[:100]}...\n\n"
            f"[dim]Words: {story.word_count}[/dim]"
        )
        cards.append(Panel(card_content, width=28))
    
    # Display in rows of 3
    for i in range(0, len(cards), 3):
        row = cards[i:i+3]
        console.print(Columns(row))


def render_entity_cards() -> None:
    """Render entities as individual cards."""
    entities = get_all_entities()
    
    console.print("\n[bold]🎭 Entity Cards[/bold]")
    console.print("═" * 60)
    
    cards = []
    for eid, entity in list(entities.items())[:6]:
        mood_emoji = {
            EntityMood.DORMANT: "💤",
            EntityMood.RESTING: "😴",
            EntityMood.ACTIVE: "😊",
            EntityMood.AWAKENING: "😃",
            EntityMood.THRIVING: "🌟",
        }.get(entity.state.mood, "●")
        
        energy_bar = "█" * int(entity.energy * 10) + "░" * (10 - int(entity.energy * 10))
        
        card = Panel(
            f"[bold cyan]{entity.name}[/bold cyan]\n"
            f"{entity.entity_type.value}\n\n"
            f"Energy: [{energy_bar}] {entity.energy*100:.0f}%\n"
            f"Mood: {mood_emoji} {entity.state.mood.value}\n"
            f"Animation: {entity.state.animation}",
            width=28,
        )
        cards.append(card)
    
    for i in range(0, len(cards), 3):
        row = cards[i:i+3]
        console.print(Columns(row))


def render_status_bar(
    items: Optional[dict[str, str]] = None,
) -> None:
    """
    Render a status bar.
    
    Args:
        items: Status items to display
    """
    if items is None:
        cycles = get_all_cycles()
        entities = get_all_entities()
        total_energy = sum(e.energy for e in entities.values())
        avg_energy = total_energy / len(entities) if entities else 0
        
        items = {
            "🕐 Time": datetime.now().strftime("%H:%M"),
            "🎭 Entities": str(len(entities)),
            "⚡ Avg Energy": f"{avg_energy*100:.0f}%",
            "🔄 Cycles": str(len(cycles)),
        }
    
    parts = [f"[cyan]{k}[/cyan]: [green]{v}[/green]" for k, v in items.items()]
    status_line = "  │  ".join(parts)
    
    console.print(Panel(status_line, style="dim"))


def render_tabbed_view(
    tabs: dict[str, str],
    active_tab: Optional[str] = None,
) -> None:
    """
    Render a tabbed interface.
    
    Args:
        tabs: Tab name -> content mapping
        active_tab: Currently active tab
    """
    if not tabs:
        return
    
    if active_tab is None:
        active_tab = list(tabs.keys())[0]
    
    # Tab bar
    tab_bar = ""
    for tab_name in tabs.keys():
        if tab_name == active_tab:
            tab_bar += f" [bold inverse] {tab_name} [/bold inverse] "
        else:
            tab_bar += f" [dim]{tab_name}[/dim] "
    
    console.print(tab_bar)
    console.print("─" * 60)
    
    # Content
    console.print(tabs[active_tab])
    console.print("─" * 60)


def render_notification(
    message: str,
    level: str = "info",
    title: Optional[str] = None,
) -> None:
    """
    Render a notification panel.
    
    Args:
        message: Notification message
        level: info, success, warning, error
        title: Optional title
    """
    styles = {
        "info": ("blue", "ℹ️"),
        "success": ("green", "✅"),
        "warning": ("yellow", "⚠️"),
        "error": ("red", "❌"),
    }
    
    color, emoji = styles.get(level, styles["info"])
    title = title or f"{emoji} {level.title()}"
    
    console.print(Panel(
        message,
        title=title,
        border_style=color,
    ))


def render_breadcrumb(
    path: list[str],
) -> None:
    """
    Render a breadcrumb navigation.
    
    Args:
        path: List of path segments
    """
    breadcrumb = " [dim]→[/dim] ".join(
        f"[cyan]{p}[/cyan]" if i < len(path) - 1 else f"[bold]{p}[/bold]"
        for i, p in enumerate(path)
    )
    console.print(f"  📍 {breadcrumb}")


def render_progress_steps(
    steps: list[str],
    current: int = 0,
) -> None:
    """
    Render progress steps.
    
    Args:
        steps: List of step names
        current: Current step index
    """
    step_display = ""
    for i, step in enumerate(steps):
        if i < current:
            step_display += f" [green]✓ {step}[/green] "
        elif i == current:
            step_display += f" [bold yellow]● {step}[/bold yellow] "
        else:
            step_display += f" [dim]○ {step}[/dim] "
        
        if i < len(steps) - 1:
            if i < current:
                step_display += "[green]──[/green]"
            else:
                step_display += "[dim]──[/dim]"
    
    console.print(step_display)


def render_stats_grid(
    stats: dict[str, tuple[str, str]],
    columns: int = 4,
) -> None:
    """
    Render a grid of statistics.
    
    Args:
        stats: Stat name -> (value, icon) mapping
        columns: Number of columns
    """
    stat_panels = []
    for name, (value, icon) in stats.items():
        content = f"[bold]{icon}[/bold]\n[bold cyan]{value}[/bold cyan]\n[dim]{name}[/dim]"
        stat_panels.append(Panel(content, width=15))
    
    for i in range(0, len(stat_panels), columns):
        row = stat_panels[i:i+columns]
        console.print(Columns(row, equal=True))


def render_comparison(
    left_data: dict,
    right_data: dict,
    left_title: str = "Before",
    right_title: str = "After",
) -> None:
    """
    Render a side-by-side comparison.
    
    Args:
        left_data: Left column data
        right_data: Right column data
        left_title: Left column title
        right_title: Right column title
    """
    table = Table(title="📊 Comparison")
    table.add_column("Metric", style="cyan")
    table.add_column(left_title, justify="right")
    table.add_column("", justify="center")
    table.add_column(right_title, justify="right")
    
    all_keys = set(left_data.keys()) | set(right_data.keys())
    
    for key in all_keys:
        left_val = left_data.get(key, "-")
        right_val = right_data.get(key, "-")
        
        # Determine arrow
        try:
            if float(right_val) > float(left_val):
                arrow = "[green]↑[/green]"
            elif float(right_val) < float(left_val):
                arrow = "[red]↓[/red]"
            else:
                arrow = "[yellow]→[/yellow]"
        except (ValueError, TypeError):
            arrow = "[dim]·[/dim]"
        
        table.add_row(key, str(left_val), arrow, str(right_val))
    
    console.print(table)


def render_full_report() -> None:
    """Render a comprehensive report with all sections."""
    console.print("\n")
    
    # Header
    console.print(Panel(
        "[bold yellow]📊 MARKTWAINVERSE FULL REPORT[/bold yellow]\n"
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        border_style="yellow",
    ))
    
    # Status bar
    render_status_bar()
    
    # Main dashboard
    render_main_dashboard()
    
    # Entity cards
    render_entity_cards()
    
    # Quote
    quote = get_random_quote()
    render_notification(
        f'"{quote.text}"\n\n— {quote.source}',
        level="info",
        title="💡 Closing Wisdom",
    )
