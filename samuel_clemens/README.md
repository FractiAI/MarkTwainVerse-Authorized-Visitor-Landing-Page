# Samuel Clemens v0.2.0

> *"The secret of getting ahead is getting started."* — Mark Twain

The complete Python methods package for **MarkTwainVerse**. Samuel Clemens (Mark Twain's real name) provides frontier-themed utilities, advanced story generation, rich visualizations, file export, and NSPFRP protocol bridges.

## Installation

```bash
cd samuel_clemens
uv sync
```

## Quick Start

```bash
# Welcome scene
uv run twain welcome

# Generate a story
uv run twain generate --template campfire_yarn

# Export a story to HTML
uv run twain export -o story.html --template river_story --format html

# Interactive mode
uv run twain interactive

# View the dashboard
uv run twain dashboard
```

## CLI Commands (30+ commands)

### Core Commands
```bash
twain greet                    # Frontier greeting from Mark Twain
twain farewell                 # Frontier farewell
twain story --topic adventure  # Generate a simple story
twain wisdom                   # Get a nugget of Twain wisdom
twain status                   # Check verse status
twain expedition --type fishing # Chart an expedition
```

### Story Generation
```bash
twain generate                              # Generate a full story
twain generate --template river_story       # Use specific template
twain generate --dramatic --style card      # Dramatic with card display
twain mashup --count 3 --style chaotic      # Mashup multiple stories
twain gallery --count 6 --layout grid       # Story gallery
twain anthology --chapters 5                # Create interconnected stories
twain templates                             # List all templates
twain elements                              # List characters, settings, themes
twain interactive                           # Interactive storytelling session
```

### Export Commands
```bash
twain export -o story.md                     # Export to Markdown
twain export -o story.html --format html     # Export to HTML
twain export -o story.json --format json     # Export to JSON
twain export-anthology -o stories/ -c 10     # Export anthology directory
```

### Visualization
```bash
twain dashboard     # Full verse dashboard
twain banner        # ASCII banner
twain portrait      # Mark Twain portrait
twain map           # Frontier map
twain campfire      # Campfire scene
twain timeline      # Day-night timeline
twain energy        # Entity energy bars
twain moods         # Mood wheel distribution
twain network       # Entity network tree
twain welcome       # Full welcome scene
twain goodbye       # Goodbye with steamboat
```

### Protocol Commands
```bash
twain cycles        # Natural cycle states
twain entities      # Living entities
twain quotes        # Authentic Twain quotes
twain interact <id> # Interact with entity
```

## Python API

```python
# Story Generation
from samuel_clemens import (
    StoryGenerator, 
    StoryRecombinator,
    generate_campfire_yarn,
)

generator = StoryGenerator()
story = generator.generate(template_name="mystery_tale", dramatic=True)
print(story.text)

# Export to file
from samuel_clemens.stories import export_story, export_anthology
export_story(story, "my_story.html", format="html")

# Interactive session
from samuel_clemens.stories import run_interactive_session
session = run_interactive_session()

# Visualization
from samuel_clemens import render_verse_dashboard, render_campfire
render_verse_dashboard()
```

## Package Structure

```
samuel_clemens/
├── src/samuel_clemens/
│   ├── core/           # Storytelling, navigation, frontier utilities
│   ├── stories/        # Advanced story generation & recombination
│   │   ├── generator.py    # StoryGenerator engine
│   │   ├── recombinator.py # Mashups, crossovers, anthologies
│   │   ├── templates.py    # 6 story templates
│   │   ├── elements.py     # Characters, settings, themes, plots
│   │   ├── export.py       # Markdown/HTML/JSON/text export
│   │   └── interactive.py  # Interactive storytelling session
│   ├── visualization/  # Rich terminal visualizations
│   │   ├── renderer.py     # Story/dashboard rendering
│   │   ├── charts.py       # Cycle/energy/mood charts
│   │   └── ascii_art.py    # Banners, portraits, maps
│   ├── protocols/      # NSPFRP cycle, entity, event bridges
│   ├── cli/            # 30+ CLI commands
│   ├── utils/          # Logging, configuration
│   └── narrative/      # Quotes, context management
└── tests/              # 146 tests
```

## Development

```bash
# Run tests (146 tests)
uv run pytest tests/ -v

# Type checking
uv run mypy src/samuel_clemens/

# Linting
uv run ruff check src/
```

## Philosophy

*"The world operates itself; visitors join its rhythm."*

This package complements the TypeScript NSPFRP engine in `protocols/naturalSystems.ts`, providing Python-powered methods for local development, testing, and verse operations.

---

**MarkTwainVerse** | Syntheverse Frontier | NSPFRP v0.2.0

