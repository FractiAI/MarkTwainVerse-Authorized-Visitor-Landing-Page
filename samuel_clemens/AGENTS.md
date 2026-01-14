# Samuel Clemens Package - AGENTS.md

> Guidance for AI agents working with the Samuel Clemens Python package.

## Overview

This is the Python sidecar package for MarkTwainVerse. It provides:
- **Story Generation**: Templates, elements, mashups, anthologies
- **Visualization**: Rich terminal dashboards, charts, ASCII art
- **Protocol Bridges**: NSPFRP cycles, entities, events
- **CLI**: 25+ commands via `twain`

## Key Files

| File | Purpose |
|------|---------|
| `pyproject.toml` | Package config, dependencies |
| `src/samuel_clemens/__init__.py` | Main exports |
| `src/samuel_clemens/stories/` | Story generation engine |
| `src/samuel_clemens/visualization/` | Rich terminal output |
| `src/samuel_clemens/protocols/` | NSPFRP bridges |
| `src/samuel_clemens/cli/main.py` | CLI commands |

## Commands

```bash
# Setup
cd samuel_clemens && uv sync

# Run specific command
uv run twain <command>

# Run tests (116 tests)
uv run pytest tests/ -v
```

## Story Generation

```python
from samuel_clemens.stories.generator import StoryGenerator

generator = StoryGenerator()
story = generator.generate(template_name="campfire_yarn")
```

**Templates**: `frontier_tale`, `river_story`, `campfire_yarn`, `wisdom_piece`, `adventure_quest`, `mystery_tale`

## Narrative Guidelines

1. **Frontier metaphors**: Functions are "trail methods", classes are "establishments"
2. **Twain voice**: Wit, wisdom, warmth
3. **NSPFRP alignment**: Mirror TypeScript protocol patterns

## Architecture

```
samuel_clemens/
├── core/         # Basic storytelling, navigation
├── stories/      # Advanced generation, recombination
├── visualization/# Rich terminal output  
├── protocols/    # NSPFRP bridges
├── cli/          # 25+ commands
├── utils/        # Logging, config
└── narrative/    # Quotes, context
```

## Integration Points

- `protocols/naturalSystems.ts` → `src/samuel_clemens/protocols/`
- `lib/marktwainverse/twainPersonality.ts` → `src/samuel_clemens/narrative/`
