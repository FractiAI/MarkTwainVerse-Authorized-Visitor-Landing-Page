#!/usr/bin/env python3
"""
run_all.py - Thin Orchestrator for Samuel Clemens Package

"Twenty years from now you will be more disappointed by the things you
didn't do than by the ones you did do." — Mark Twain

This script orchestrates all package demonstrations, generating stories,
visualizations, and exports to the output/ directory.
"""

from __future__ import annotations

import sys
from pathlib import Path
from datetime import datetime

# Self-bootstrap: if imports fail, re-run with uv
try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.progress import Progress, SpinnerColumn, TextColumn
    from rich.table import Table
    import PIL
    import reportlab
except ImportError:
    import subprocess
    print("Dependencies missing. Re-running with uv...")
    subprocess.run(["uv", "run", __file__] + sys.argv[1:], check=True)
    sys.exit(0)

# Package root
PACKAGE_ROOT = Path(__file__).parent
OUTPUT_DIR = PACKAGE_ROOT / "output"

# Add src to path so we can import the package directly
sys.path.insert(0, str(PACKAGE_ROOT / "src"))

console = Console()


def ensure_output_dirs() -> dict[str, Path]:
    """Create output directory structure."""
    dirs = {
        "root": OUTPUT_DIR,
        "stories": OUTPUT_DIR / "stories",
        "anthologies": OUTPUT_DIR / "anthologies",
        "visualizations": OUTPUT_DIR / "visualizations",
        "exports": OUTPUT_DIR / "exports",
        "animations": OUTPUT_DIR / "animations",
        "processing": OUTPUT_DIR / "processing",
        "images": OUTPUT_DIR / "exports" / "images",
        "pdfs": OUTPUT_DIR / "exports" / "pdfs",
        "logs": OUTPUT_DIR / "logs",
    }
    
    for name, path in dirs.items():
        path.mkdir(parents=True, exist_ok=True)
    
    return dirs


def run_story_generation(dirs: dict[str, Path]) -> None:
    """Generate stories and save to output."""
    from samuel_clemens.stories.generator import StoryGenerator
    from samuel_clemens.stories.templates import TEMPLATES
    from samuel_clemens.stories import export_story
    
    console.print("\n[bold cyan]📖 Story Generation[/bold cyan]")
    
    generator = StoryGenerator()
    
    # Generate one story per template
    for template_key in TEMPLATES.keys():
        story = generator.generate(template_name=template_key)
        
        # Export to multiple formats
        md_path = dirs["stories"] / f"{template_key}.md"
        html_path = dirs["stories"] / f"{template_key}.html"
        json_path = dirs["stories"] / f"{template_key}.json"
        
        export_story(story, md_path, format="markdown")
        export_story(story, html_path, format="html")
        export_story(story, json_path, format="json")
        
        # New Image and PDF exports
        from samuel_clemens.visualization import render_story_card_image
        from samuel_clemens.processing import export_story_to_pdf
        
        try:
            img_path = dirs["images"] / f"{template_key}_card.png"
            render_story_card_image(story, img_path)
            
            pdf_path = dirs["pdfs"] / f"{template_key}.pdf"
            export_story_to_pdf(story, pdf_path)
        except Exception as e:
            console.print(f"  [yellow]⚠ Visual export failed: {e}[/yellow]")
        
        console.print(f"  ✓ {template_key}: [dim]{story.title}[/dim]")
    
    console.print(f"  [green]Saved {len(TEMPLATES) * 3} files to {dirs['stories']}[/green]")


def run_anthology_generation(dirs: dict[str, Path]) -> None:
    """Generate anthologies."""
    from samuel_clemens.stories.generator import StoryGenerator
    from samuel_clemens.stories.recombinator import StoryRecombinator
    from samuel_clemens.stories import export_anthology
    
    console.print("\n[bold cyan]📚 Anthology Generation[/bold cyan]")
    
    generator = StoryGenerator()
    recombinator = StoryRecombinator()
    
    # Generate themed anthology
    stories = generator.generate_batch(5)
    anthology_dir = dirs["anthologies"] / "frontier_tales"
    export_anthology(stories, anthology_dir, format="markdown")
    console.print(f"  ✓ frontier_tales: 5 stories")
    
    # Generate mashup anthology
    mashup_stories = []
    for _ in range(3):
        s1, s2 = generator.generate(), generator.generate()
        mashup = recombinator.blend(s1, s2)
        mashup_stories.append(mashup)
    
    mashup_dir = dirs["anthologies"] / "mashup_collection"
    export_anthology(mashup_stories, mashup_dir, format="html")
    console.print(f"  ✓ mashup_collection: 3 mashups")
    
    # PDF Exports
    from samuel_clemens.processing import export_anthology_to_pdf
    
    try:
        export_anthology_to_pdf(
            anthology_dir,
            dirs["pdfs"] / "frontier_tales_anthology.pdf",
            title="Frontier Tales Anthology"
        )
        console.print("  ✓ frontier_tales_anthology.pdf")
        
        # Mashups are HTML only for now? No, we can try to PDF export them
        # But anthology export expects folders of markdown
        pass
    except Exception as e:
        console.print(f"  [yellow]⚠ Anthology PDF export failed: {e}[/yellow]")
    
    console.print(f"  [green]Anthologies saved to {dirs['anthologies']}[/green]")


def run_visualizations(dirs: dict[str, Path]) -> None:
    """Generate visualization outputs."""
    from samuel_clemens.visualization.exports import (
        export_dashboard_snapshot,
        export_cycle_charts,
        export_entity_charts,
        export_ascii_art_collection,
    )
    
    console.print("\n[bold cyan]📊 Visualization Generation[/bold cyan]")
    
    # Export all visualization types
    export_dashboard_snapshot(dirs["visualizations"] / "dashboard.txt")
    console.print("  ✓ Dashboard snapshot")
    
    export_cycle_charts(dirs["visualizations"] / "cycles")
    console.print("  ✓ Cycle charts")
    
    export_entity_charts(dirs["visualizations"] / "entities")
    console.print("  ✓ Entity charts")
    
    export_ascii_art_collection(dirs["visualizations"] / "ascii_art")
    console.print("  ✓ ASCII art collection")
    
    # Export ASCII as PNGs
    from samuel_clemens.visualization.ascii_art import TWAIN_PORTRAIT, FRONTIER_BANNER, render_steamboat
    from samuel_clemens.visualization import render_ascii_to_image
    
    try:
        render_ascii_to_image(TWAIN_PORTRAIT, dirs["images"] / "twain_portrait.png")
        render_ascii_to_image(FRONTIER_BANNER, dirs["images"] / "frontier_banner.png")
        render_ascii_to_image(render_steamboat(), dirs["images"] / "steamboat.png")
        console.print("  ✓ ASCII art rendered to PNG")
    except Exception as e:
        console.print(f"  [yellow]⚠ ASCII image export failed: {e}[/yellow]")
    
    console.print(f"  [green]Visualizations saved to {dirs['visualizations']}[/green]")


def run_animations(dirs: dict[str, Path]) -> None:
    """Generate animation frames and GIFs."""
    from samuel_clemens.animation import (
        generate_cycle_animation,
        generate_entity_animation,
        generate_story_animation,
        export_all_animations_to_gif,
    )
    
    console.print("\n[bold cyan]🎬 Animation Generation[/bold cyan]")
    
    # Generate frame-based animations
    generate_cycle_animation(dirs["animations"] / "cycles")
    console.print("  ✓ Cycle animation frames")
    
    generate_entity_animation(dirs["animations"] / "entities")
    console.print("  ✓ Entity animation frames")
    
    generate_story_animation(dirs["animations"] / "story")
    console.print("  ✓ Story animation frames")
    
    # Generate GIF outputs
    console.print("\n  [bold]Generating GIF files...[/bold]")
    gif_dir = dirs["animations"] / "gifs"
    try:
        gif_paths = export_all_animations_to_gif(gif_dir)
        console.print(f"  ✓ {len(gif_paths)} GIF files created")
    except ImportError as e:
        console.print(f"  [yellow]⚠ GIF export skipped: Pillow not installed[/yellow]")
    except Exception as e:
        console.print(f"  [yellow]⚠ GIF export warning: {e}[/yellow]")
    
    console.print(f"  [green]Animations saved to {dirs['animations']}[/green]")


def run_protocol_exports(dirs: dict[str, Path]) -> None:
    """Export protocol state."""
    import json
    from samuel_clemens.protocols.cycles import get_all_cycles
    from samuel_clemens.protocols.entities import get_all_entities
    from samuel_clemens.protocols.events import get_active_events
    
    console.print("\n[bold cyan]🔄 Protocol State Export[/bold cyan]")
    
    # Export cycles
    cycles = get_all_cycles()
    cycles_data = {
        name: {"name": c.name, "phase": c.phase, "description": c.description}
        for name, c in cycles.items()
    }
    (dirs["exports"] / "cycles.json").write_text(json.dumps(cycles_data, indent=2))
    console.print("  ✓ cycles.json")
    
    # Export entities
    entities = get_all_entities()
    entities_data = {
        eid: {
            "name": e.name,
            "type": e.entity_type.value,
            "energy": e.energy,
            "mood": e.state.mood.value,
        }
        for eid, e in entities.items()
    }
    (dirs["exports"] / "entities.json").write_text(json.dumps(entities_data, indent=2))
    console.print("  ✓ entities.json")
    
    # Export events
    events = get_active_events()
    events_data = [
        {"id": e.id, "name": e.name, "triggered_at": e.triggered_at.isoformat() if e.triggered_at else None}
        for e in events
    ]
    (dirs["exports"] / "events.json").write_text(json.dumps(events_data, indent=2))
    console.print("  ✓ events.json")
    
    console.print(f"  [green]Exports saved to {dirs['exports']}[/green]")


def run_protocol_processing(dirs: dict[str, Path]) -> None:
    """Process and analyze protocol files."""
    from samuel_clemens.processing import (
        parse_protocols_by_prefix,
        export_folder_summary,
        export_emoji_report,
        export_structure_analysis,
        export_protocol_index,
        export_obsidian_vault,
        create_entity_pages,
        export_protocols_to_pdf,
        export_summary_pdf,
    )
    
    console.print("\n[bold cyan]📑 Protocol File Processing[/bold cyan]")
    
    # Find project root (parent of samuel_clemens)
    project_root = PACKAGE_ROOT.parent
    
    # Parse all protocol files
    try:
        protocols = parse_protocols_by_prefix(project_root)
        console.print(f"  ✓ Parsed {len(protocols)} protocol files")
        
        if protocols:
            # Export reports
            export_folder_summary(protocols, dirs["processing"] / "protocol_summary.md")
            console.print("  ✓ protocol_summary.md")
            
            export_emoji_report(protocols, dirs["processing"] / "emoji_report.md")
            console.print("  ✓ emoji_report.md")
            
            export_structure_analysis(protocols, dirs["processing"] / "structure_analysis.md")
            console.print("  ✓ structure_analysis.md")
            
            export_protocol_index(protocols, dirs["processing"] / "protocol_index.md")
            console.print("  ✓ protocol_index.md")
            
            # Obsidian vault export
            console.print("\n  [bold]Exporting Obsidian vault...[/bold]")
            vault_path = dirs["exports"] / "obsidian_vault"
            vault = export_obsidian_vault(protocols, vault_path)
            create_entity_pages(vault, protocols)
            vault.export()
            console.print(f"  ✓ Obsidian vault: {len(vault.pages)} pages")
            
            # Export Protocol Cards (PNG)
            console.print("\n  [bold]Generating Protocol Cards...[/bold]")
            from samuel_clemens.visualization import render_protocol_card_image
            try:
                for p in protocols[:10]:  # Limit to 10 for demo speed
                    card_path = dirs["images"] / f"{p.protocol_id or 'protocol'}_card.png"
                    render_protocol_card_image(p, card_path)
                console.print(f"  ✓ Generated {min(len(protocols), 10)} protocol cards")
            except Exception as e:
                console.print(f"  [yellow]⚠ Protocol card export failed: {e}[/yellow]")
            
            # PDF export
            console.print("\n  [bold]Generating PDF exports...[/bold]")
            try:
                pdf_path = dirs["exports"] / "protocol_documentation.pdf"
                export_protocols_to_pdf(protocols, pdf_path)
                console.print(f"  ✓ protocol_documentation.pdf")
                
                summary_pdf = dirs["exports"] / "protocol_summary.pdf"
                export_summary_pdf(protocols, summary_pdf)
                console.print(f"  ✓ protocol_summary.pdf")
            except ImportError:
                console.print("  [yellow]⚠ PDF export skipped: reportlab not installed[/yellow]")
            except Exception as e:
                console.print(f"  [yellow]⚠ PDF export warning: {e}[/yellow]")
        
        console.print(f"  [green]Processing saved to {dirs['processing']}[/green]")
    except Exception as e:
        console.print(f"  [yellow]⚠ Protocol processing warning: {e}[/yellow]")


def write_log(dirs: dict[str, Path], duration: float) -> None:
    """Write run log."""
    log_path = dirs["logs"] / f"run_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    
    log_content = f"""Samuel Clemens - Run All Log
=============================
Timestamp: {datetime.now().isoformat()}
Duration: {duration:.2f}s

Outputs Generated:
- Stories: {dirs['stories']}
- Anthologies: {dirs['anthologies']}
- Visualizations: {dirs['visualizations']}
- Animations: {dirs['animations']}
- Exports: {dirs['exports']}

Status: SUCCESS
"""
    log_path.write_text(log_content)
    console.print(f"\n[dim]Log saved to {log_path}[/dim]")


def main() -> None:
    """Main orchestrator entry point."""
    import time
    start = time.time()
    
    # Header
    console.print(Panel(
        "[bold yellow]🎩 Samuel Clemens - Run All Orchestrator[/bold yellow]\n\n"
        "Generating stories, visualizations, and exports...",
        border_style="yellow",
    ))
    
    # Setup
    dirs = ensure_output_dirs()
    console.print(f"[dim]Output directory: {OUTPUT_DIR}[/dim]")
    
    # Run all steps
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        task = progress.add_task("Running...", total=None)
        
        try:
            run_story_generation(dirs)
            run_anthology_generation(dirs)
            run_visualizations(dirs)
            run_animations(dirs)
            run_protocol_exports(dirs)
            run_protocol_processing(dirs)
        except Exception as e:
            console.print(f"\n[red]Error: {e}[/red]")
            raise
    
    duration = time.time() - start
    write_log(dirs, duration)
    
    # Summary
    console.print(Panel(
        f"[bold green]✅ Complete![/bold green]\n\n"
        f"Generated outputs in {duration:.2f}s\n"
        f"Location: [cyan]{OUTPUT_DIR}[/cyan]",
        title="Summary",
        border_style="green",
    ))


if __name__ == "__main__":
    main()
