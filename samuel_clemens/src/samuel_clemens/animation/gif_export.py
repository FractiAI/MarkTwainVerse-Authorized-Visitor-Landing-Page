"""
GIF Export - Generate animated GIF files from animation sequences.

"The secret of getting started is breaking your complex overwhelming tasks
into small manageable tasks, and then starting on the first one." — Mark Twain

Uses Pillow to create animated GIFs from text-based animation frames.
"""

from __future__ import annotations

import math
from pathlib import Path
from typing import Optional, Callable
from dataclasses import dataclass

try:
    from PIL import Image, ImageDraw, ImageFont
    HAS_PILLOW = True
except ImportError:
    HAS_PILLOW = False

from samuel_clemens.animation.core import (
    AnimationSequence,
    AnimationConfig,
)


@dataclass
class GIFConfig:
    """Configuration for GIF export."""
    width: int = 800
    height: int = 600
    background_color: tuple[int, int, int] = (30, 25, 20)  # Dark brown
    text_color: tuple[int, int, int] = (255, 248, 220)  # Cornsilk
    accent_color: tuple[int, int, int] = (205, 133, 63)  # Peru
    font_size: int = 14
    padding: int = 20
    loop: int = 0  # 0 = infinite loop
    optimize: bool = True


def _get_font(size: int = 14) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    """Get a monospace font for rendering."""
    try:
        # Try common monospace fonts
        for font_name in ["Menlo", "Monaco", "Consolas", "DejaVu Sans Mono", "Courier"]:
            try:
                return ImageFont.truetype(font_name, size)
            except (OSError, IOError):
                continue
        return ImageFont.load_default()
    except Exception:
        return ImageFont.load_default()


def render_frame_to_image(
    frame_content: str,
    config: GIFConfig,
) -> Image.Image:
    """
    Render text frame content to a PIL Image.
    
    Args:
        frame_content: Text content of the frame
        config: GIF configuration
        
    Returns:
        PIL Image
    """
    if not HAS_PILLOW:
        raise ImportError("Pillow is required for GIF export. Install with: pip install Pillow")
    
    # Create image
    img = Image.new("RGB", (config.width, config.height), config.background_color)
    draw = ImageDraw.Draw(img)
    
    # Get font
    font = _get_font(config.font_size)
    
    # Draw border
    draw.rectangle(
        [10, 10, config.width - 10, config.height - 10],
        outline=config.accent_color,
        width=2,
    )
    
    # Draw text
    lines = frame_content.split("\n")
    y = config.padding + 10
    line_height = config.font_size + 4
    
    for line in lines:
        if y + line_height > config.height - config.padding:
            break
        draw.text((config.padding + 10, y), line, fill=config.text_color, font=font)
        y += line_height
    
    # Draw credits
    credits = "MarkTwainVerse | Samuel Clemens"
    draw.text(
        (config.width - 200, config.height - 25),
        credits,
        fill=config.accent_color,
        font=_get_font(10),
    )
    
    return img


def export_to_gif(
    sequence: AnimationSequence,
    filepath: Path,
    config: Optional[GIFConfig] = None,
) -> Path:
    """
    Export an animation sequence to an animated GIF.
    
    Args:
        sequence: Animation sequence to export
        filepath: Path to save GIF
        config: GIF configuration
        
    Returns:
        Path to created GIF
    """
    if not HAS_PILLOW:
        raise ImportError("Pillow is required for GIF export. Install with: pip install Pillow")
    
    config = config or GIFConfig()
    filepath = Path(filepath)
    filepath.parent.mkdir(parents=True, exist_ok=True)
    
    # Convert frames to images
    images = []
    for frame in sequence.frames:
        img = render_frame_to_image(frame.content, config)
        images.append(img)
    
    if not images:
        raise ValueError("No frames to export")
    
    # Calculate frame duration in milliseconds
    duration_ms = int(1000 / sequence.config.fps)
    
    # Save as animated GIF
    images[0].save(
        filepath,
        save_all=True,
        append_images=images[1:],
        duration=duration_ms,
        loop=config.loop,
        optimize=config.optimize,
    )
    
    return filepath


def export_all_animations_to_gif(
    output_dir: Path,
    config: Optional[GIFConfig] = None,
) -> list[Path]:
    """
    Generate and export all animation types to GIF.
    
    Args:
        output_dir: Directory to save GIFs
        config: GIF configuration
        
    Returns:
        List of created file paths
    """
    from samuel_clemens.animation.cycles import (
        generate_breathing_animation,
        generate_daynight_animation,
        generate_expedition_animation,
        generate_season_animation,
    )
    from samuel_clemens.animation.entities import (
        generate_energy_animation,
        generate_mood_animation,
        generate_interaction_animation,
    )
    from samuel_clemens.animation.stories import (
        generate_campfire_animation,
        generate_title_animation,
    )
    
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    created = []
    
    animations = [
        ("breathing_cycle", generate_breathing_animation),
        ("daynight_cycle", generate_daynight_animation),
        ("expedition", generate_expedition_animation),
        ("season_cycle", generate_season_animation),
        ("entity_energy", generate_energy_animation),
        ("mood_wheel", generate_mood_animation),
        ("interactions", generate_interaction_animation),
        ("campfire", generate_campfire_animation),
        ("title_card", generate_title_animation),
    ]
    
    for name, generator in animations:
        try:
            sequence = generator()
            gif_path = output_dir / f"{name}.gif"
            export_to_gif(sequence, gif_path, config)
            created.append(gif_path)
            print(f"✅ Exported {name}.gif")
        except Exception as e:
            print(f"⚠️ Failed to export {name}: {e}")
    
    return created


def create_cycle_gif(
    cycle_type: str,
    output_path: Path,
    duration: float = 5.0,
    fps: int = 12,
) -> Path:
    """
    Create a GIF for a specific natural cycle.
    
    Args:
        cycle_type: Type of cycle (breathing, daynight, expedition, season)
        output_path: Path to save GIF
        duration: Animation duration in seconds
        fps: Frames per second
        
    Returns:
        Path to created GIF
    """
    from samuel_clemens.animation.core import AnimationConfig
    from samuel_clemens.animation.cycles import (
        generate_breathing_animation,
        generate_daynight_animation,
        generate_expedition_animation,
        generate_season_animation,
    )
    
    config = AnimationConfig(fps=fps, duration_seconds=duration, loop=True)
    
    generators = {
        "breathing": generate_breathing_animation,
        "daynight": generate_daynight_animation,
        "expedition": generate_expedition_animation,
        "season": generate_season_animation,
    }
    
    generator = generators.get(cycle_type)
    if not generator:
        raise ValueError(f"Unknown cycle type: {cycle_type}")
    
    sequence = generator(config=config)
    return export_to_gif(sequence, output_path)


def create_story_gif(
    story_text: str,
    title: str,
    output_path: Path,
    animation_type: str = "typing",
    duration: float = 8.0,
) -> Path:
    """
    Create a GIF animating a story.
    
    Args:
        story_text: Story text to animate
        title: Story title
        output_path: Path to save GIF
        animation_type: typing, reveal, or campfire
        duration: Animation duration in seconds
        
    Returns:
        Path to created GIF
    """
    from samuel_clemens.animation.core import AnimationConfig
    from samuel_clemens.animation.stories import (
        generate_typing_animation,
        generate_reveal_animation,
    )
    
    config = AnimationConfig(fps=15, duration_seconds=duration)
    
    if animation_type == "typing":
        sequence = generate_typing_animation(text=story_text, title=title, config=config)
    elif animation_type == "reveal":
        sequence = generate_reveal_animation(text=story_text, title=title, config=config)
    else:
        raise ValueError(f"Unknown animation type: {animation_type}")
    
    return export_to_gif(sequence, output_path)
