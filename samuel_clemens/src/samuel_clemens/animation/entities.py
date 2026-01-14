"""
Entity Animations - Animated visualizations for verse entities.

Generate frame sequences showing entity states and interactions.
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
from samuel_clemens.protocols.entities import get_all_entities, EntityMood


def _energy_bar_frame(frame_index: int, progress: float, config: AnimationConfig) -> str:
    """Generate entity energy bar frame."""
    entities = get_all_entities()
    
    lines = []
    lines.append("╔" + "═" * 60 + "╗")
    lines.append("║" + " ENTITY ENERGY LEVELS ".center(60) + "║")
    lines.append("╠" + "═" * 60 + "╣")
    
    for entity_id, entity in list(entities.items())[:6]:
        # Animate energy fluctuation
        base_energy = entity.energy
        fluctuation = math.sin(progress * 2 * math.pi + hash(entity_id) % 10) * 0.1
        animated_energy = max(0, min(1, base_energy + fluctuation))
        
        # Energy bar
        bar_width = 30
        filled = int(animated_energy * bar_width)
        
        if animated_energy > 0.7:
            bar = f"[{'█' * filled}{'░' * (bar_width - filled)}]"
        elif animated_energy > 0.4:
            bar = f"[{'▓' * filled}{'░' * (bar_width - filled)}]"
        else:
            bar = f"[{'▒' * filled}{'░' * (bar_width - filled)}]"
        
        name = entity.name[:18].ljust(18)
        energy_pct = f"{animated_energy * 100:5.1f}%"
        
        lines.append(f"║  {name} {bar} {energy_pct}  ║")
    
    lines.append("╠" + "═" * 60 + "╣")
    lines.append(f"║  Frame: {frame_index:4d}  |  Progress: {progress * 100:5.1f}%".ljust(60) + "  ║")
    lines.append("╚" + "═" * 60 + "╝")
    
    return "\n".join(lines)


def _mood_wheel_frame(frame_index: int, progress: float, config: AnimationConfig) -> str:
    """Generate mood distribution frame with rotation."""
    moods = [
        (EntityMood.DORMANT, "💤", "Dormant"),
        (EntityMood.RESTING, "😴", "Resting"),
        (EntityMood.ACTIVE, "😊", "Active"),
        (EntityMood.AWAKENING, "😃", "Awakening"),
        (EntityMood.THRIVING, "🌟", "Thriving"),
    ]
    
    # Rotate through moods
    rotation = int(progress * len(moods)) % len(moods)
    
    lines = []
    lines.append("┌" + "─" * 40 + "┐")
    lines.append("│" + " MOOD WHEEL ".center(40) + "│")
    lines.append("├" + "─" * 40 + "┤")
    lines.append("│" + " " * 40 + "│")
    
    # Wheel visualization
    wheel_line = "  "
    for i, (mood, emoji, name) in enumerate(moods):
        adjusted_i = (i - rotation) % len(moods)
        if adjusted_i == 0:
            wheel_line += f"→{emoji}← "
        else:
            wheel_line += f" {emoji}  "
    
    lines.append("│" + wheel_line.center(40) + "│")
    lines.append("│" + " " * 40 + "│")
    
    # Current mood details
    current = moods[rotation]
    lines.append("│" + f"  Current: {current[1]} {current[2]}".ljust(40) + "│")
    lines.append("│" + " " * 40 + "│")
    
    # Distribution bars
    entities = get_all_entities()
    mood_counts = {m: 0 for m, _, _ in moods}
    for e in entities.values():
        if e.state.mood in mood_counts:
            mood_counts[e.state.mood] += 1
    
    total = sum(mood_counts.values()) or 1
    for mood, emoji, name in moods:
        count = mood_counts[mood]
        pct = count / total
        bar = "█" * int(pct * 20)
        lines.append("│" + f"  {emoji} {name:10} {bar}".ljust(40) + "│")
    
    lines.append("│" + " " * 40 + "│")
    lines.append("└" + "─" * 40 + "┘")
    
    return "\n".join(lines)


def _interaction_frame(frame_index: int, progress: float, config: AnimationConfig) -> str:
    """Generate entity interaction frame."""
    entities = list(get_all_entities().items())[:4]
    
    lines = []
    lines.append("╭" + "─" * 50 + "╮")
    lines.append("│" + " ENTITY INTERACTIONS ".center(50) + "│")
    lines.append("├" + "─" * 50 + "┤")
    
    # Show entities with pulsing connections
    pulse = (math.sin(progress * 4 * math.pi) + 1) / 2
    
    for i, (eid, entity) in enumerate(entities):
        # Pulse effect
        if pulse > 0.5:
            status = "◉"
        else:
            status = "○"
        
        mood_emoji = {
            EntityMood.DORMANT: "💤",
            EntityMood.RESTING: "😴",
            EntityMood.ACTIVE: "😊",
            EntityMood.AWAKENING: "😃",
            EntityMood.THRIVING: "🌟",
        }.get(entity.state.mood, "●")
        
        line = f"  {status} {entity.name[:20]:20} {mood_emoji} {entity.energy*100:5.1f}%"
        lines.append("│" + line.ljust(50) + "│")
        
        # Connection to next
        if i < len(entities) - 1:
            if progress > (i + 1) / len(entities):
                conn = "  ├────→ connected"
            else:
                conn = "  │"
            lines.append("│" + conn.ljust(50) + "│")
    
    lines.append("├" + "─" * 50 + "┤")
    lines.append("│" + f"  Interaction Progress: {progress*100:.0f}%".ljust(50) + "│")
    lines.append("╰" + "─" * 50 + "╯")
    
    return "\n".join(lines)


def _entity_card_frame(frame_index: int, progress: float, config: AnimationConfig) -> str:
    """Generate animated entity card."""
    entities = list(get_all_entities().items())
    entity_index = int(progress * len(entities)) % len(entities)
    eid, entity = entities[entity_index]
    
    # Animated border
    spinner = create_spinner_frame(frame_index, "stars")
    
    lines = []
    lines.append(f"{spinner}" + "═" * 38 + f"{spinner}")
    lines.append("")
    lines.append(f"  🎭 {entity.name}")
    lines.append(f"  " + "─" * 30)
    lines.append("")
    
    # Type
    lines.append(f"  Type: {entity.entity_type.value}")
    
    # Energy with bar
    energy_bar = "█" * int(entity.energy * 20) + "░" * (20 - int(entity.energy * 20))
    lines.append(f"  Energy: [{energy_bar}] {entity.energy*100:.0f}%")
    
    # Mood
    mood_emoji = {
        EntityMood.DORMANT: "💤",
        EntityMood.RESTING: "😴",
        EntityMood.ACTIVE: "😊",
        EntityMood.AWAKENING: "😃",
        EntityMood.THRIVING: "🌟",
    }.get(entity.state.mood, "●")
    lines.append(f"  Mood: {mood_emoji} {entity.state.mood.value}")
    
    # Animation state
    lines.append(f"  Animation: {entity.state.animation}")
    
    lines.append("")
    lines.append(f"{spinner}" + "═" * 38 + f"{spinner}")
    
    return "\n".join(lines)


def generate_energy_animation(
    output_dir: Optional[Path] = None,
    config: Optional[AnimationConfig] = None,
) -> AnimationSequence:
    """
    Generate energy bar animation.
    
    Args:
        output_dir: Optional directory to save frames
        config: Animation configuration
        
    Returns:
        AnimationSequence
    """
    config = config or AnimationConfig(fps=12, duration_seconds=5, loop=True)
    
    sequence = create_animation(
        name="entity_energy",
        generator=_energy_bar_frame,
        config=config,
    )
    
    if output_dir:
        save_animation_frames(sequence, Path(output_dir), "energy")
    
    return sequence


def generate_mood_animation(
    output_dir: Optional[Path] = None,
    config: Optional[AnimationConfig] = None,
) -> AnimationSequence:
    """
    Generate mood wheel animation.
    
    Args:
        output_dir: Optional directory to save frames
        config: Animation configuration
        
    Returns:
        AnimationSequence
    """
    config = config or AnimationConfig(fps=8, duration_seconds=5, loop=True)
    
    sequence = create_animation(
        name="mood_wheel",
        generator=_mood_wheel_frame,
        config=config,
    )
    
    if output_dir:
        save_animation_frames(sequence, Path(output_dir), "mood")
    
    return sequence


def generate_interaction_animation(
    output_dir: Optional[Path] = None,
    config: Optional[AnimationConfig] = None,
) -> AnimationSequence:
    """
    Generate interaction animation.
    
    Args:
        output_dir: Optional directory to save frames
        config: Animation configuration
        
    Returns:
        AnimationSequence
    """
    config = config or AnimationConfig(fps=10, duration_seconds=4, easing=EasingFunction.EASE_IN_OUT)
    
    sequence = create_animation(
        name="interactions",
        generator=_interaction_frame,
        config=config,
    )
    
    if output_dir:
        save_animation_frames(sequence, Path(output_dir), "interaction")
    
    return sequence


def generate_entity_animation(
    output_dir: Path,
    config: Optional[AnimationConfig] = None,
) -> dict[str, AnimationSequence]:
    """
    Generate all entity animations.
    
    Args:
        output_dir: Directory to save frames
        config: Animation configuration
        
    Returns:
        Dictionary of animation sequences
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    return {
        "energy": generate_energy_animation(output_dir / "energy", config),
        "mood": generate_mood_animation(output_dir / "mood", config),
        "interaction": generate_interaction_animation(output_dir / "interaction", config),
    }
