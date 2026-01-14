"""
CLI Main - The `twain` command-line interface.

"I have made it a rule never to smoke more than one cigar at a time." — Mark Twain

Provides frontier-themed commands for verse operations.
"""

from __future__ import annotations

import click
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


@click.group()
@click.version_option(version="0.2.0", prog_name="twain")
def cli() -> None:
    """
    🎩 Samuel Clemens - The MarkTwainVerse Command Line
    
    Welcome to the frontier, friend! This here command line gives you
    access to all the tools and tales of the Syntheverse.
    
    \b
    COMMANDS:
      Core:     greet, farewell, story, wisdom, status, expedition
      Stories:  generate, mashup, gallery, templates, elements
      Visual:   dashboard, banner, portrait, map, timeline, energy
      Protocol: cycles, entities, quotes, interact
    """
    pass


# ================== CORE COMMANDS ==================

@cli.command()
@click.option("--name", "-n", default=None, help="Your name, traveler")
def greet(name: str | None) -> None:
    """
    Get a frontier greeting from Mark Twain.
    
    Example: twain greet --name "Partner"
    """
    from samuel_clemens.core.frontier import frontier_greeting
    
    greeting = frontier_greeting(visitor_name=name)
    console.print(Panel(greeting, title="🎩 Mark Twain", border_style="yellow"))


@cli.command()
@click.option("--name", "-n", default=None, help="Your name, traveler")
def farewell(name: str | None) -> None:
    """
    Get a frontier farewell from Mark Twain.
    
    Example: twain farewell --name "Partner"
    """
    from samuel_clemens.core.frontier import frontier_farewell
    
    farewell_msg = frontier_farewell(visitor_name=name)
    console.print(Panel(farewell_msg, title="🎩 Mark Twain", border_style="yellow"))


@cli.command()
@click.option(
    "--topic", "-t",
    type=click.Choice(["frontier", "adventure", "wisdom", "river", "default"]),
    default="default",
    help="Story topic",
)
@click.option("--no-quote", is_flag=True, help="Skip the authentic quote")
def story(topic: str, no_quote: bool) -> None:
    """
    Hear a story from Mark Twain.
    
    Example: twain story --topic adventure
    """
    from samuel_clemens.core.storyteller import tell_story
    
    result = tell_story(topic=topic, include_quote=not no_quote)
    console.print(Panel(
        result.text,
        title=f"📖 {result.topic.title()} Story",
        subtitle=f"[{result.emotion.value}]",
        border_style="magenta",
    ))


@cli.command()
def wisdom() -> None:
    """
    Get a nugget of frontier wisdom.
    
    Example: twain wisdom
    """
    from samuel_clemens.core.storyteller import frontier_wisdom
    
    nugget = frontier_wisdom()
    console.print(Panel(
        f"💡 {nugget}",
        title="Frontier Wisdom",
        border_style="green",
    ))


@cli.command()
def status() -> None:
    """
    Check the status of the MarkTwainVerse.
    
    Example: twain status
    """
    from samuel_clemens.core.frontier import get_frontier_status
    from samuel_clemens.protocols.cycles import get_day_phase, get_season
    from samuel_clemens.protocols.entities import get_total_energy, get_dominant_mood
    
    day_phase = get_day_phase()
    status_info = get_frontier_status(day_phase=day_phase)
    
    table = Table(title="🏔️ MarkTwainVerse Status")
    table.add_column("Property", style="cyan")
    table.add_column("Value", style="green")
    
    table.add_row("Operational", "✅ Yes" if status_info.is_operational else "❌ No")
    table.add_row("Season", status_info.season)
    table.add_row("Day Phase", f"{day_phase:.2f} ({get_season()})")
    table.add_row("Mood", status_info.dominant_mood)
    table.add_row("Hero Host", status_info.hero_host_status)
    table.add_row("Energy", f"{get_total_energy():.2f}")
    table.add_row("Dominant Mood", get_dominant_mood().value)
    
    console.print(table)
    console.print(f"\n[italic]{status_info.message}[/italic]")


@cli.command()
@click.option(
    "--type", "-t", "exp_type",
    type=click.Choice(["fishing", "eco-adventure", "storytelling", "frontier", "wilderness", "community"]),
    default="frontier",
    help="Expedition type",
)
def expedition(exp_type: str) -> None:
    """
    Chart an expedition course.
    
    Example: twain expedition --type fishing
    """
    from samuel_clemens.core.navigator import chart_course, CourseType
    
    type_map = {
        "fishing": CourseType.FISHING,
        "eco-adventure": CourseType.ECO_ADVENTURE,
        "storytelling": CourseType.STORYTELLING,
        "frontier": CourseType.FRONTIER,
        "wilderness": CourseType.WILDERNESS,
        "community": CourseType.COMMUNITY,
    }
    
    course = chart_course(type_map[exp_type])
    
    console.print(Panel(
        f"[bold]{course.destination}[/bold]\n\n"
        f"{course.description}\n\n"
        f"[dim]Duration: {course.duration_hours} hours[/dim]\n"
        f"[dim]Waypoints: {' → '.join(course.waypoints)}[/dim]",
        title=f"🗺️ {exp_type.title()} Expedition",
        border_style="blue",
    ))


# ================== STORY COMMANDS ==================

@cli.command()
@click.option(
    "--template", "-t",
    type=click.Choice(["frontier_tale", "river_story", "campfire_yarn", "wisdom_piece", "adventure_quest", "mystery_tale"]),
    default=None,
    help="Story template to use",
)
@click.option("--dramatic", "-d", is_flag=True, help="Add dramatic flourishes")
@click.option("--no-quote", is_flag=True, help="Skip the ending quote")
@click.option("--style", "-s", 
    type=click.Choice(["panel", "card", "minimal", "dramatic"]),
    default="panel",
    help="Display style",
)
def generate(template: str | None, dramatic: bool, no_quote: bool, style: str) -> None:
    """
    Generate a complete story using the story engine.
    
    \b
    Examples:
      twain generate
      twain generate --template campfire_yarn --dramatic
      twain generate --style card --no-quote
    """
    from samuel_clemens.stories.generator import StoryGenerator
    from samuel_clemens.visualization.renderer import render_story
    
    generator = StoryGenerator()
    generated = generator.generate(
        template_name=template,
        include_quote=not no_quote,
        dramatic=dramatic,
    )
    
    # Convert to base Story and render
    story_obj = generated.to_story()
    render_story(story_obj, style=style)
    
    # Show metadata
    console.print(f"\n[dim]Template: {generated.template_used} | Words: {generated.word_count}[/dim]")


@cli.command()
@click.option("--count", "-c", default=2, help="Number of stories to mashup")
@click.option(
    "--style", "-s",
    type=click.Choice(["sequential", "interleaved", "chaotic"]),
    default="sequential",
    help="Mashup style",
)
def mashup(count: int, style: str) -> None:
    """
    Create a mashup from multiple generated stories.
    
    \b
    Examples:
      twain mashup
      twain mashup --count 3 --style chaotic
    """
    from samuel_clemens.stories.generator import StoryGenerator
    from samuel_clemens.stories.recombinator import StoryRecombinator
    
    generator = StoryGenerator()
    recombinator = StoryRecombinator()
    
    # Generate stories
    console.print(f"[dim]Generating {count} stories...[/dim]")
    stories = generator.generate_batch(count)
    
    # Mashup
    console.print(f"[dim]Creating {style} mashup...[/dim]\n")
    mashup_result = recombinator.mashup(stories, style=style)
    
    console.print(Panel(
        mashup_result.text,
        title=f"🎭 {mashup_result.title}",
        subtitle=f"[{mashup_result.mashup_type}]",
        border_style="magenta",
    ))
    
    console.print(f"\n[dim]Sources: {', '.join(mashup_result.source_stories)} | Words: {mashup_result.word_count}[/dim]")


@cli.command()
@click.option("--count", "-c", default=4, help="Number of stories in gallery")
@click.option(
    "--layout", "-l",
    type=click.Choice(["grid", "list", "carousel"]),
    default="grid",
    help="Gallery layout",
)
def gallery(count: int, layout: str) -> None:
    """
    Generate and display a gallery of stories.
    
    \b
    Examples:
      twain gallery
      twain gallery --count 6 --layout list
    """
    from samuel_clemens.stories.generator import StoryGenerator
    from samuel_clemens.visualization.renderer import render_story_gallery
    
    generator = StoryGenerator()
    
    console.print(f"[dim]Generating {count} stories for gallery...[/dim]\n")
    stories = [generator.generate().to_story() for _ in range(count)]
    
    render_story_gallery(stories, layout=layout)


@cli.command()
def templates() -> None:
    """
    List all available story templates.
    
    Example: twain templates
    """
    from samuel_clemens.stories.templates import TEMPLATES
    
    table = Table(title="📚 Story Templates")
    table.add_column("Name", style="cyan")
    table.add_column("Type", style="green")
    table.add_column("Mood", style="yellow")
    table.add_column("Description", style="dim", max_width=40)
    
    for name, template in TEMPLATES.items():
        table.add_row(
            name,
            template.template_type.value,
            template.mood,
            template.description,
        )
    
    console.print(table)


@cli.command()
def elements() -> None:
    """
    List all available story elements (characters, settings, themes).
    
    Example: twain elements
    """
    from samuel_clemens.stories.elements import CHARACTERS, SETTINGS, THEMES
    
    # Characters
    char_table = Table(title="🎭 Characters")
    char_table.add_column("Name", style="cyan")
    char_table.add_column("Role", style="green")
    char_table.add_column("Traits", style="yellow", max_width=30)
    
    for char in CHARACTERS:
        char_table.add_row(
            char.name,
            char.role,
            ", ".join(char.traits[:3]),
        )
    
    console.print(char_table)
    console.print()
    
    # Settings
    set_table = Table(title="🌍 Settings")
    set_table.add_column("Name", style="cyan")
    set_table.add_column("Atmosphere", style="green")
    set_table.add_column("Features", style="yellow", max_width=30)
    
    for setting in SETTINGS:
        set_table.add_row(
            setting.name,
            setting.atmosphere,
            ", ".join(setting.features[:3]),
        )
    
    console.print(set_table)
    console.print()
    
    # Themes
    theme_table = Table(title="💡 Themes")
    theme_table.add_column("Name", style="cyan")
    theme_table.add_column("Related", style="yellow", max_width=40)
    
    for theme in THEMES:
        theme_table.add_row(
            theme.name,
            ", ".join(theme.related_themes[:3]),
        )
    
    console.print(theme_table)


@cli.command()
@click.option("--chapters", "-c", default=3, help="Number of chapters")
def anthology(chapters: int) -> None:
    """
    Create an anthology of interconnected stories.
    
    \b
    Examples:
      twain anthology
      twain anthology --chapters 5
    """
    from samuel_clemens.stories.recombinator import StoryRecombinator
    
    recombinator = StoryRecombinator()
    
    console.print(f"[dim]Creating anthology with {chapters} chapters...[/dim]\n")
    stories = recombinator.create_anthology(count=chapters)
    
    for story in stories:
        console.print(Panel(
            story.text[:300] + "..." if len(story.text) > 300 else story.text,
            title=story.title,
            border_style="magenta",
        ))
        console.print()


@cli.command("export")
@click.option(
    "--template", "-t",
    type=click.Choice(["frontier_tale", "river_story", "campfire_yarn", "wisdom_piece", "adventure_quest", "mystery_tale"]),
    default=None,
    help="Story template to use",
)
@click.option(
    "--format", "-f",
    type=click.Choice(["markdown", "html", "json", "text"]),
    default="markdown",
    help="Export format",
)
@click.option("--output", "-o", type=click.Path(), required=True, help="Output file path")
def export_story_cmd(template: str | None, format: str, output: str) -> None:
    """
    Generate and export a story to file.
    
    \b
    Examples:
      twain export -o story.md
      twain export --template river_story --format html -o story.html
      twain export --format json -o stories/tale.json
    """
    from pathlib import Path
    from samuel_clemens.stories.generator import StoryGenerator
    from samuel_clemens.stories import export_story
    
    generator = StoryGenerator()
    
    console.print(f"[dim]Generating story...[/dim]")
    story = generator.generate(template_name=template)
    
    console.print(f"[dim]Exporting to {output}...[/dim]")
    export_story(story, Path(output), format=format)
    
    console.print(f"[green]✅ Exported '{story.title}' to {output}[/green]")
    console.print(f"[dim]Words: {story.word_count} | Format: {format}[/dim]")


@cli.command("export-anthology")
@click.option("--count", "-c", default=5, help="Number of stories")
@click.option(
    "--format", "-f",
    type=click.Choice(["markdown", "html", "json", "text"]),
    default="markdown",
    help="Export format",
)
@click.option("--output", "-o", type=click.Path(), required=True, help="Output directory")
def export_anthology_cmd(count: int, format: str, output: str) -> None:
    """
    Generate and export an anthology to a directory.
    
    \b
    Examples:
      twain export-anthology -o stories/
      twain export-anthology --count 10 --format html -o anthology/
    """
    from pathlib import Path
    from samuel_clemens.stories.generator import StoryGenerator
    from samuel_clemens.stories import export_anthology
    
    generator = StoryGenerator()
    
    console.print(f"[dim]Generating {count} stories...[/dim]")
    stories = generator.generate_batch(count)
    
    console.print(f"[dim]Exporting anthology to {output}...[/dim]")
    created = export_anthology(stories, Path(output), format=format)
    
    console.print(f"[green]✅ Exported {len(created)} files to {output}[/green]")


@cli.command("interactive")
def interactive_mode() -> None:
    """
    Start an interactive storytelling session.
    
    Create stories with guided prompts around the virtual campfire.
    
    Example: twain interactive
    """
    from samuel_clemens.stories.interactive import run_interactive_session
    
    session = run_interactive_session()
    
    if session.stories_created:
        console.print(f"\n[dim]Session ended with {len(session.stories_created)} stories.[/dim]")


# ================== VISUALIZATION COMMANDS ==================

@cli.command()
def dashboard() -> None:
    """
    Display the comprehensive verse dashboard.
    
    Example: twain dashboard
    """
    from samuel_clemens.visualization.renderer import render_verse_dashboard
    
    render_verse_dashboard()


@cli.command()
@click.option("--size", "-s", type=click.Choice(["large", "small"]), default="small", help="Banner size")
def banner(size: str) -> None:
    """
    Display the MarkTwainVerse banner.
    
    Example: twain banner --size large
    """
    from samuel_clemens.visualization.ascii_art import render_frontier_banner
    
    render_frontier_banner(size=size)


@cli.command()
@click.option("--size", "-s", type=click.Choice(["large", "small"]), default="large", help="Portrait size")
def portrait(size: str) -> None:
    """
    Display Mark Twain's ASCII portrait.
    
    Example: twain portrait
    """
    from samuel_clemens.visualization.ascii_art import render_twain_portrait
    
    render_twain_portrait(size=size)


@cli.command("map")
def show_map() -> None:
    """
    Display the frontier map.
    
    Example: twain map
    """
    from samuel_clemens.visualization.ascii_art import render_map_art
    
    render_map_art()


@cli.command()
def timeline() -> None:
    """
    Display the day-night timeline.
    
    Example: twain timeline
    """
    from samuel_clemens.visualization.charts import render_timeline
    
    render_timeline()


@cli.command()
def energy() -> None:
    """
    Display entity energy levels.
    
    Example: twain energy
    """
    from samuel_clemens.visualization.charts import render_energy_bars
    
    render_energy_bars()


@cli.command()
def moods() -> None:
    """
    Display the mood wheel distribution.
    
    Example: twain moods
    """
    from samuel_clemens.visualization.charts import render_mood_wheel
    
    render_mood_wheel()


@cli.command()
def campfire() -> None:
    """
    Display the campfire scene for storytelling.
    
    Example: twain campfire
    """
    from samuel_clemens.visualization.ascii_art import render_campfire
    
    render_campfire()


@cli.command()
def welcome() -> None:
    """
    Display a full welcome scene.
    
    Example: twain welcome
    """
    from samuel_clemens.visualization.ascii_art import render_welcome_scene
    
    render_welcome_scene()


@cli.command()
def goodbye() -> None:
    """
    Display a goodbye scene with steamboat.
    
    Example: twain goodbye
    """
    from samuel_clemens.visualization.ascii_art import render_goodbye_scene
    
    render_goodbye_scene()


# ================== PROTOCOL COMMANDS ==================

@cli.command()
def cycles() -> None:
    """
    Show current natural cycle states.
    
    Example: twain cycles
    """
    from samuel_clemens.protocols.cycles import get_all_cycles
    
    cycles_data = get_all_cycles()
    
    table = Table(title="🌀 Natural Cycles")
    table.add_column("Cycle", style="cyan")
    table.add_column("Phase", style="green")
    table.add_column("Description", style="yellow")
    
    for name, cycle in cycles_data.items():
        table.add_row(cycle.name, f"{cycle.phase:.3f}", cycle.description)
    
    console.print(table)


@cli.command()
def entities() -> None:
    """
    List all living entities in the verse.
    
    Example: twain entities
    """
    from samuel_clemens.protocols.entities import get_all_entities
    
    entities_data = get_all_entities()
    
    table = Table(title="🌟 Living Entities")
    table.add_column("Name", style="cyan")
    table.add_column("Type", style="green")
    table.add_column("Mood", style="yellow")
    table.add_column("Energy", style="magenta")
    
    for entity in entities_data.values():
        table.add_row(
            entity.name,
            entity.entity_type.value,
            entity.state.mood.value,
            f"{entity.energy:.2f}",
        )
    
    console.print(table)


@cli.command()
def quotes() -> None:
    """
    Display all authentic Mark Twain quotes.
    
    Example: twain quotes
    """
    from samuel_clemens.narrative.quotes import get_all_quotes
    
    quotes_list = get_all_quotes()
    
    table = Table(title="📜 Authentic Twain Quotes")
    table.add_column("#", style="dim")
    table.add_column("Quote", style="cyan", max_width=60)
    table.add_column("Context", style="green")
    
    for i, quote in enumerate(quotes_list, 1):
        table.add_row(str(i), quote.text, quote.context)
    
    console.print(table)


@cli.command()
@click.argument("entity_id")
def interact(entity_id: str) -> None:
    """
    Interact with a living entity.
    
    Example: twain interact hero-host-mark-twain
    """
    from samuel_clemens.protocols.entities import interact_with_entity
    
    entity = interact_with_entity(entity_id)
    if entity:
        console.print(Panel(
            f"[bold]{entity.name}[/bold] responds with {entity.state.mood.value} energy!\n\n"
            f"[dim]Energy: {entity.energy:.2f}[/dim]\n"
            f"[dim]Animation: {entity.state.animation}[/dim]",
            title="⚡ Interaction",
            border_style="yellow",
        ))
    else:
        console.print(f"[red]Entity '{entity_id}' not found.[/red]")
        console.print("[dim]Use 'twain entities' to see available entities.[/dim]")


@cli.command()
def network() -> None:
    """
    Display the entity network as a tree.
    
    Example: twain network
    """
    from samuel_clemens.visualization.renderer import render_entity_network
    
    render_entity_network()


if __name__ == "__main__":
    cli()

