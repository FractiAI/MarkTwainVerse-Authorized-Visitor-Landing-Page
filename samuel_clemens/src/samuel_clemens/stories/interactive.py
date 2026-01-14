"""
Interactive - Interactive storytelling mode.

Provides a conversational interface for story creation.
"""

from __future__ import annotations

import random
from dataclasses import dataclass, field
from typing import Optional, Callable

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich.table import Table

from samuel_clemens.stories.generator import StoryGenerator, GeneratedStory
from samuel_clemens.stories.recombinator import StoryRecombinator
from samuel_clemens.stories.elements import (
    CHARACTERS,
    SETTINGS,
    THEMES,
    Character,
    Setting,
    Theme,
)
from samuel_clemens.stories.templates import TEMPLATES, list_templates
from samuel_clemens.visualization.ascii_art import render_campfire
from samuel_clemens.narrative.quotes import get_random_quote
from samuel_clemens.utils.logging import story_log

console = Console()


@dataclass
class InteractiveSession:
    """Tracks an interactive storytelling session."""
    stories_created: list[GeneratedStory] = field(default_factory=list)
    current_character: Optional[Character] = None
    current_setting: Optional[Setting] = None
    current_theme: Optional[Theme] = None
    session_start: str = ""
    
    def __post_init__(self) -> None:
        from datetime import datetime
        self.session_start = datetime.now().isoformat()


def run_interactive_session() -> InteractiveSession:
    """
    Run an interactive storytelling session.
    
    Returns:
        Session with created stories
    """
    session = InteractiveSession()
    generator = StoryGenerator()
    
    # Welcome
    console.print()
    render_campfire()
    console.print()
    console.print(Panel(
        "[bold yellow]Welcome to the Frontier Campfire![/bold yellow]\n\n"
        "Gather 'round, friend. Let's spin some yarns together.\n"
        "I'll help you create stories, one choice at a time.",
        title="🎩 Mark Twain",
        border_style="yellow",
    ))
    console.print()
    
    while True:
        # Main menu
        console.print("\n[bold cyan]What would you like to do?[/bold cyan]")
        console.print("1. Create a new story")
        console.print("2. Choose your character")
        console.print("3. Choose your setting")
        console.print("4. Choose your theme")
        console.print("5. Quick random story")
        console.print("6. View session stories")
        console.print("7. Hear some wisdom")
        console.print("8. Exit")
        console.print()
        
        choice = Prompt.ask("[yellow]Your choice[/yellow]", default="1")
        
        if choice == "1":
            story = _create_story_interactive(generator, session)
            if story:
                session.stories_created.append(story)
        
        elif choice == "2":
            session.current_character = _choose_character()
        
        elif choice == "3":
            session.current_setting = _choose_setting()
        
        elif choice == "4":
            session.current_theme = _choose_theme()
        
        elif choice == "5":
            story = generator.generate(
                character=session.current_character,
                setting=session.current_setting,
                theme=session.current_theme,
            )
            _display_story(story)
            session.stories_created.append(story)
        
        elif choice == "6":
            _show_session_stories(session)
        
        elif choice == "7":
            quote = get_random_quote()
            console.print(Panel(
                f"[italic]{quote.text}[/italic]",
                title="💡 Wisdom",
                border_style="green",
            ))
        
        elif choice == "8":
            if Confirm.ask("Are you sure you want to leave the campfire?"):
                _farewell(session)
                break
        
        else:
            console.print("[red]I don't understand that choice, friend.[/red]")
    
    return session


def _create_story_interactive(
    generator: StoryGenerator,
    session: InteractiveSession,
) -> Optional[GeneratedStory]:
    """Guide user through story creation."""
    console.print("\n[bold]Let's create a story![/bold]\n")
    
    # Choose template
    console.print("[cyan]What kind of story shall we tell?[/cyan]")
    templates = list(TEMPLATES.items())
    for i, (key, template) in enumerate(templates, 1):
        console.print(f"  {i}. {template.name} - {template.description}")
    console.print(f"  {len(templates) + 1}. Surprise me!")
    
    template_choice = Prompt.ask("Choose", default=str(len(templates) + 1))
    
    try:
        idx = int(template_choice) - 1
        if idx < len(templates):
            template_name = templates[idx][0]
        else:
            template_name = None  # Random
    except ValueError:
        template_name = None
    
    # Use session elements or ask for new ones
    character = session.current_character
    if not character and Confirm.ask("Would you like to choose a character?", default=False):
        character = _choose_character()
    
    setting = session.current_setting
    if not setting and Confirm.ask("Would you like to choose a setting?", default=False):
        setting = _choose_setting()
    
    # Dramatic?
    dramatic = Confirm.ask("Should we add some dramatic flourishes?", default=False)
    
    # Generate
    console.print("\n[dim]Spinning the yarn...[/dim]\n")
    
    story = generator.generate(
        template_name=template_name,
        character=character,
        setting=setting,
        theme=session.current_theme,
        dramatic=dramatic,
    )
    
    _display_story(story)
    
    return story


def _choose_character() -> Optional[Character]:
    """Let user choose a character."""
    console.print("\n[bold cyan]Choose your character:[/bold cyan]")
    
    table = Table(show_header=True)
    table.add_column("#", style="dim")
    table.add_column("Name", style="cyan")
    table.add_column("Role", style="green")
    table.add_column("Traits", style="yellow")
    
    for i, char in enumerate(CHARACTERS, 1):
        table.add_row(str(i), char.name, char.role, ", ".join(char.traits[:3]))
    
    console.print(table)
    
    choice = Prompt.ask("Choose a character", default="1")
    
    try:
        idx = int(choice) - 1
        if 0 <= idx < len(CHARACTERS):
            selected = CHARACTERS[idx]
            console.print(f"[green]Selected: {selected.name}[/green]")
            return selected
    except ValueError:
        pass
    
    console.print("[yellow]Using random character.[/yellow]")
    return None


def _choose_setting() -> Optional[Setting]:
    """Let user choose a setting."""
    console.print("\n[bold cyan]Choose your setting:[/bold cyan]")
    
    table = Table(show_header=True)
    table.add_column("#", style="dim")
    table.add_column("Name", style="cyan")
    table.add_column("Atmosphere", style="green")
    
    for i, setting in enumerate(SETTINGS, 1):
        table.add_row(str(i), setting.name, setting.atmosphere)
    
    console.print(table)
    
    choice = Prompt.ask("Choose a setting", default="1")
    
    try:
        idx = int(choice) - 1
        if 0 <= idx < len(SETTINGS):
            selected = SETTINGS[idx]
            console.print(f"[green]Selected: {selected.name}[/green]")
            return selected
    except ValueError:
        pass
    
    console.print("[yellow]Using random setting.[/yellow]")
    return None


def _choose_theme() -> Optional[Theme]:
    """Let user choose a theme."""
    console.print("\n[bold cyan]Choose your theme:[/bold cyan]")
    
    table = Table(show_header=True)
    table.add_column("#", style="dim")
    table.add_column("Name", style="cyan")
    table.add_column("Related", style="yellow")
    
    for i, theme in enumerate(THEMES, 1):
        table.add_row(str(i), theme.name, ", ".join(theme.related_themes[:3]))
    
    console.print(table)
    
    choice = Prompt.ask("Choose a theme", default="1")
    
    try:
        idx = int(choice) - 1
        if 0 <= idx < len(THEMES):
            selected = THEMES[idx]
            console.print(f"[green]Selected: {selected.name}[/green]")
            return selected
    except ValueError:
        pass
    
    console.print("[yellow]Using random theme.[/yellow]")
    return None


def _display_story(story: GeneratedStory) -> None:
    """Display a generated story."""
    console.print(Panel(
        story.text,
        title=f"📖 {story.title}",
        subtitle=f"[{story.template_used}]",
        border_style="magenta",
        padding=(1, 2),
    ))
    console.print(f"[dim]Words: {story.word_count}[/dim]")


def _show_session_stories(session: InteractiveSession) -> None:
    """Show all stories from this session."""
    if not session.stories_created:
        console.print("[yellow]No stories yet! Let's create some.[/yellow]")
        return
    
    console.print(f"\n[bold]Stories from this session ({len(session.stories_created)} total):[/bold]\n")
    
    for i, story in enumerate(session.stories_created, 1):
        console.print(f"[cyan]{i}. {story.title}[/cyan] ({story.word_count} words)")
    
    if Confirm.ask("\nWould you like to read one?", default=False):
        choice = Prompt.ask("Which story?", default="1")
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(session.stories_created):
                _display_story(session.stories_created[idx])
        except ValueError:
            pass


def _farewell(session: InteractiveSession) -> None:
    """Farewell message with session summary."""
    console.print()
    console.print(Panel(
        f"[bold yellow]Thanks for visiting the campfire, friend![/bold yellow]\n\n"
        f"You created {len(session.stories_created)} stories tonight.\n"
        f"May your trails be clear and your stories be true!\n\n"
        f"[italic]— Mark Twain[/italic]",
        title="🎩 Farewell",
        border_style="yellow",
    ))


def quick_story_prompt() -> GeneratedStory:
    """Quick story generation with a single prompt."""
    console.print("[cyan]What kind of story would you like?[/cyan]")
    console.print("(frontier, adventure, mystery, wisdom, river, campfire, or leave blank for random)")
    
    template_map = {
        "frontier": "frontier_tale",
        "adventure": "adventure_quest",
        "mystery": "mystery_tale",
        "wisdom": "wisdom_piece",
        "river": "river_story",
        "campfire": "campfire_yarn",
    }
    
    choice = Prompt.ask("Story type", default="")
    template_name = template_map.get(choice.lower())
    
    generator = StoryGenerator()
    story = generator.generate(template_name=template_name)
    
    _display_story(story)
    return story
