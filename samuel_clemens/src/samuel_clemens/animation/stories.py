"""
Story Animations - Animated visualizations for story presentation.

Generate frame sequences for story reveal, typing effects, and campfire scenes.
"""

from __future__ import annotations

import math
import random
from pathlib import Path
from typing import Optional

from samuel_clemens.animation.core import (
    AnimationConfig,
    AnimationSequence,
    AnimationFrame,
    create_animation,
    save_animation_frames,
    create_progress_bar,
    apply_easing,
    EasingFunction,
    create_spinner_frame,
)
from samuel_clemens.stories.generator import StoryGenerator


def _typing_frame_factory(text: str, title: str = "Story"):
    """Create a typing animation frame generator."""
    words = text.split()
    
    def _typing_frame(frame_index: int, progress: float, config: AnimationConfig) -> str:
        # Calculate how many words to show
        num_words = int(progress * len(words))
        visible_text = " ".join(words[:num_words])
        
        # Wrap text
        max_width = 60
        wrapped_lines = []
        current_line = ""
        
        for word in words[:num_words]:
            if len(current_line) + len(word) + 1 <= max_width:
                current_line += (" " if current_line else "") + word
            else:
                wrapped_lines.append(current_line)
                current_line = word
        if current_line:
            wrapped_lines.append(current_line)
        
        # Add cursor
        if progress < 1.0 and wrapped_lines:
            wrapped_lines[-1] += "█"
        
        lines = []
        lines.append("╔" + "═" * 62 + "╗")
        lines.append("║" + f" 📖 {title} ".center(62) + "║")
        lines.append("╠" + "═" * 62 + "╣")
        
        # Add text lines
        for line in wrapped_lines[:20]:  # Limit height
            lines.append("║  " + line.ljust(60) + "║")
        
        # Padding
        while len(lines) < 15:
            lines.append("║" + " " * 62 + "║")
        
        lines.append("╠" + "═" * 62 + "╣")
        lines.append("║" + f"  Progress: {progress*100:.0f}%  |  Words: {num_words}/{len(words)}".ljust(62) + "║")
        lines.append("╚" + "═" * 62 + "╝")
        
        return "\n".join(lines)
    
    return _typing_frame


def _reveal_frame_factory(text: str, title: str = "Story"):
    """Create a reveal animation frame generator."""
    lines_text = text.split("\n")
    
    def _reveal_frame(frame_index: int, progress: float, config: AnimationConfig) -> str:
        # Reveal lines progressively
        num_lines = int(progress * len(lines_text))
        
        lines = []
        lines.append("┌" + "─" * 60 + "┐")
        lines.append("│" + f" ✨ {title} ✨ ".center(60) + "│")
        lines.append("├" + "─" * 60 + "┤")
        
        for i, line in enumerate(lines_text[:15]):
            if i < num_lines:
                # Revealed
                display_line = line[:58]
            else:
                # Hidden with gradient
                reveal_progress = max(0, (num_lines - i + 1) / 2)
                if reveal_progress > 0:
                    display_line = "▒" * min(len(line), int(reveal_progress * 58))
                else:
                    display_line = ""
            
            lines.append("│ " + display_line.ljust(58) + " │")
        
        while len(lines) < 18:
            lines.append("│" + " " * 60 + "│")
        
        lines.append("├" + "─" * 60 + "┤")
        lines.append("│" + f"  Revealing... {progress*100:.0f}%".ljust(60) + "│")
        lines.append("└" + "─" * 60 + "┘")
        
        return "\n".join(lines)
    
    return _reveal_frame


def _campfire_frame(frame_index: int, progress: float, config: AnimationConfig) -> str:
    """Generate campfire storytelling scene."""
    # Flame animation
    flames = [
        ["   (", "  ) ", "   )"],
        ["  ( ", " (  ", "  ) "],
        [" )  ", "  ( ", " (  "],
    ]
    flame_set = flames[frame_index % len(flames)]
    
    # Flicker effect
    flicker = random.choice(["(", ")", " "])
    
    lines = []
    lines.append("")
    lines.append("              " + flame_set[0])
    lines.append("             " + flame_set[1] + flicker)
    lines.append("            " + flame_set[2])
    lines.append("           _______")
    lines.append("          /_______\\")
    lines.append("         /         \\")
    lines.append("        /___________\\")
    lines.append("")
    
    # Story text fading in
    sample_text = "Gather 'round, friends, for I have a tale to tell..."
    visible_chars = int(progress * len(sample_text))
    
    lines.append("  " + "─" * 46)
    lines.append("")
    lines.append(f"   {sample_text[:visible_chars]}")
    lines.append("")
    lines.append("  " + "─" * 46)
    
    # Atmosphere
    if progress > 0.5:
        lines.append("")
        lines.append("   🌙 The fire crackles as the story unfolds...")
    
    if progress > 0.8:
        lines.append("   ⭐ Stars twinkle overhead...")
    
    return "\n".join(lines)


def _title_card_frame(frame_index: int, progress: float, config: AnimationConfig) -> str:
    """Generate animated title card."""
    # Fade in effect
    opacity = min(1.0, progress * 2)
    
    if opacity < 0.5:
        title_char = "░"
    elif opacity < 0.8:
        title_char = "▒"
    else:
        title_char = "█"
    
    lines = []
    
    # Border
    lines.append("")
    lines.append("  " + "═" * 50)
    lines.append("")
    
    # Title with fade effect
    title = "THE TALE UNFOLDS"
    if progress < 0.3:
        display_title = title_char * len(title)
    elif progress < 0.6:
        visible = int((progress - 0.3) / 0.3 * len(title))
        display_title = title[:visible] + title_char * (len(title) - visible)
    else:
        display_title = title
    
    lines.append("  " + display_title.center(50))
    lines.append("")
    
    # Subtitle
    subtitle = "— A Mark Twain Production —"
    if progress > 0.7:
        lines.append("  " + subtitle.center(50))
    else:
        lines.append("  " + " " * 50)
    
    lines.append("")
    lines.append("  " + "═" * 50)
    
    # Decorative elements
    if progress > 0.9:
        lines.append("")
        lines.append("  " + "🎩  📖  ✒️  📜  🎭".center(50))
    
    return "\n".join(lines)


def generate_typing_animation(
    text: Optional[str] = None,
    title: str = "Story",
    output_dir: Optional[Path] = None,
    config: Optional[AnimationConfig] = None,
) -> AnimationSequence:
    """
    Generate typing effect animation.
    
    Args:
        text: Text to type (generates if None)
        title: Story title
        output_dir: Optional directory to save frames
        config: Animation configuration
        
    Returns:
        AnimationSequence
    """
    if text is None:
        generator = StoryGenerator()
        story = generator.generate()
        text = story.text
        title = story.title
    
    config = config or AnimationConfig(fps=15, duration_seconds=8, easing=EasingFunction.LINEAR)
    
    sequence = create_animation(
        name="typing_story",
        generator=_typing_frame_factory(text, title),
        config=config,
    )
    
    if output_dir:
        save_animation_frames(sequence, Path(output_dir), "typing")
    
    return sequence


def generate_reveal_animation(
    text: Optional[str] = None,
    title: str = "Story",
    output_dir: Optional[Path] = None,
    config: Optional[AnimationConfig] = None,
) -> AnimationSequence:
    """
    Generate reveal effect animation.
    
    Args:
        text: Text to reveal (generates if None)
        title: Story title
        output_dir: Optional directory to save frames
        config: Animation configuration
        
    Returns:
        AnimationSequence
    """
    if text is None:
        generator = StoryGenerator()
        story = generator.generate()
        text = story.text
        title = story.title
    
    config = config or AnimationConfig(fps=12, duration_seconds=5, easing=EasingFunction.EASE_IN_OUT)
    
    sequence = create_animation(
        name="reveal_story",
        generator=_reveal_frame_factory(text, title),
        config=config,
    )
    
    if output_dir:
        save_animation_frames(sequence, Path(output_dir), "reveal")
    
    return sequence


def generate_campfire_animation(
    output_dir: Optional[Path] = None,
    config: Optional[AnimationConfig] = None,
) -> AnimationSequence:
    """
    Generate campfire scene animation.
    
    Args:
        output_dir: Optional directory to save frames
        config: Animation configuration
        
    Returns:
        AnimationSequence
    """
    config = config or AnimationConfig(fps=10, duration_seconds=6, loop=True)
    
    sequence = create_animation(
        name="campfire",
        generator=_campfire_frame,
        config=config,
    )
    
    if output_dir:
        save_animation_frames(sequence, Path(output_dir), "campfire")
    
    return sequence


def generate_title_animation(
    output_dir: Optional[Path] = None,
    config: Optional[AnimationConfig] = None,
) -> AnimationSequence:
    """
    Generate title card animation.
    
    Args:
        output_dir: Optional directory to save frames
        config: Animation configuration
        
    Returns:
        AnimationSequence
    """
    config = config or AnimationConfig(fps=15, duration_seconds=3, easing=EasingFunction.EASE_OUT)
    
    sequence = create_animation(
        name="title_card",
        generator=_title_card_frame,
        config=config,
    )
    
    if output_dir:
        save_animation_frames(sequence, Path(output_dir), "title")
    
    return sequence


def generate_story_animation(
    output_dir: Path,
    config: Optional[AnimationConfig] = None,
) -> dict[str, AnimationSequence]:
    """
    Generate all story animations.
    
    Args:
        output_dir: Directory to save frames
        config: Animation configuration
        
    Returns:
        Dictionary of animation sequences
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    return {
        "typing": generate_typing_animation(output_dir=output_dir / "typing", config=config),
        "reveal": generate_reveal_animation(output_dir=output_dir / "reveal", config=config),
        "campfire": generate_campfire_animation(output_dir / "campfire", config),
        "title": generate_title_animation(output_dir / "title", config),
    }
