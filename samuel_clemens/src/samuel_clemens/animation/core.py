"""
Animation Core - Base classes and utilities for animation generation.

Provides the foundation for frame-based animation creation.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Callable, Optional, Any
from enum import Enum

from rich.console import Console

console = Console()


class EasingFunction(Enum):
    """Animation easing functions."""
    LINEAR = "linear"
    EASE_IN = "ease_in"
    EASE_OUT = "ease_out"
    EASE_IN_OUT = "ease_in_out"
    BOUNCE = "bounce"
    ELASTIC = "elastic"


@dataclass
class AnimationConfig:
    """Configuration for an animation."""
    fps: int = 10
    duration_seconds: float = 3.0
    width: int = 80
    height: int = 24
    loop: bool = False
    easing: EasingFunction = EasingFunction.EASE_IN_OUT
    
    @property
    def total_frames(self) -> int:
        """Calculate total frames."""
        return int(self.fps * self.duration_seconds)


@dataclass
class AnimationFrame:
    """A single frame in an animation."""
    index: int
    timestamp: float
    content: str
    metadata: dict[str, Any] = field(default_factory=dict)
    
    def __post_init__(self) -> None:
        self.lines = self.content.split("\n")
    
    @property
    def width(self) -> int:
        """Maximum line width."""
        return max(len(line) for line in self.lines) if self.lines else 0
    
    @property
    def height(self) -> int:
        """Number of lines."""
        return len(self.lines)


@dataclass
class AnimationSequence:
    """A sequence of animation frames."""
    name: str
    frames: list[AnimationFrame] = field(default_factory=list)
    config: AnimationConfig = field(default_factory=AnimationConfig)
    created_at: datetime = field(default_factory=datetime.now)
    
    def add_frame(self, content: str, metadata: Optional[dict] = None) -> AnimationFrame:
        """Add a new frame to the sequence."""
        frame = AnimationFrame(
            index=len(self.frames),
            timestamp=len(self.frames) / self.config.fps,
            content=content,
            metadata=metadata or {},
        )
        self.frames.append(frame)
        return frame
    
    @property
    def duration(self) -> float:
        """Total duration in seconds."""
        return len(self.frames) / self.config.fps if self.frames else 0
    
    def get_frame_at_time(self, t: float) -> Optional[AnimationFrame]:
        """Get frame at specific time."""
        if not self.frames:
            return None
        
        frame_index = int(t * self.config.fps)
        if self.config.loop:
            frame_index = frame_index % len(self.frames)
        else:
            frame_index = min(frame_index, len(self.frames) - 1)
        
        return self.frames[frame_index]


def apply_easing(t: float, easing: EasingFunction) -> float:
    """
    Apply easing function to a 0-1 progress value.
    
    Args:
        t: Progress value (0 to 1)
        easing: Easing function to apply
        
    Returns:
        Eased progress value
    """
    t = max(0, min(1, t))
    
    if easing == EasingFunction.LINEAR:
        return t
    elif easing == EasingFunction.EASE_IN:
        return t * t
    elif easing == EasingFunction.EASE_OUT:
        return 1 - (1 - t) ** 2
    elif easing == EasingFunction.EASE_IN_OUT:
        if t < 0.5:
            return 2 * t * t
        else:
            return 1 - (-2 * t + 2) ** 2 / 2
    elif easing == EasingFunction.BOUNCE:
        if t < 1 / 2.75:
            return 7.5625 * t * t
        elif t < 2 / 2.75:
            t -= 1.5 / 2.75
            return 7.5625 * t * t + 0.75
        elif t < 2.5 / 2.75:
            t -= 2.25 / 2.75
            return 7.5625 * t * t + 0.9375
        else:
            t -= 2.625 / 2.75
            return 7.5625 * t * t + 0.984375
    elif easing == EasingFunction.ELASTIC:
        if t == 0 or t == 1:
            return t
        return -(2 ** (10 * t - 10)) * math.sin((t * 10 - 10.75) * (2 * math.pi / 3))
    
    return t


def create_animation(
    name: str,
    generator: Callable[[int, float, AnimationConfig], str],
    config: Optional[AnimationConfig] = None,
) -> AnimationSequence:
    """
    Create an animation sequence using a generator function.
    
    Args:
        name: Animation name
        generator: Function that generates frame content (frame_index, progress, config) -> content
        config: Animation configuration
        
    Returns:
        AnimationSequence with all frames
    """
    config = config or AnimationConfig()
    sequence = AnimationSequence(name=name, config=config)
    
    for i in range(config.total_frames):
        progress = i / max(config.total_frames - 1, 1)
        eased_progress = apply_easing(progress, config.easing)
        
        content = generator(i, eased_progress, config)
        sequence.add_frame(content, {"progress": progress, "eased": eased_progress})
    
    return sequence


def save_animation_frames(
    sequence: AnimationSequence,
    directory: Path,
    prefix: str = "frame",
) -> list[Path]:
    """
    Save animation frames to a directory.
    
    Args:
        sequence: Animation sequence to save
        directory: Output directory
        prefix: Filename prefix
        
    Returns:
        List of created file paths
    """
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    
    created = []
    
    # Save each frame
    for frame in sequence.frames:
        filepath = directory / f"{prefix}_{frame.index:04d}.txt"
        filepath.write_text(frame.content)
        created.append(filepath)
    
    # Save metadata
    import json
    metadata_path = directory / "animation.json"
    metadata = {
        "name": sequence.name,
        "frames": len(sequence.frames),
        "fps": sequence.config.fps,
        "duration": sequence.duration,
        "created_at": sequence.created_at.isoformat(),
        "config": {
            "width": sequence.config.width,
            "height": sequence.config.height,
            "loop": sequence.config.loop,
            "easing": sequence.config.easing.value,
        },
    }
    metadata_path.write_text(json.dumps(metadata, indent=2))
    created.append(metadata_path)
    
    return created


def render_animation_preview(
    sequence: AnimationSequence,
    frame_indices: Optional[list[int]] = None,
) -> None:
    """
    Render a preview of animation frames to console.
    
    Args:
        sequence: Animation sequence to preview
        frame_indices: Specific frames to show (default: first, middle, last)
    """
    from rich.panel import Panel
    from rich.columns import Columns
    
    if frame_indices is None:
        # Show first, middle, last
        n = len(sequence.frames)
        frame_indices = [0, n // 2, n - 1] if n > 2 else list(range(n))
    
    console.print(f"[bold cyan]Animation Preview: {sequence.name}[/bold cyan]")
    console.print(f"[dim]Frames: {len(sequence.frames)} | Duration: {sequence.duration:.2f}s | FPS: {sequence.config.fps}[/dim]\n")
    
    for idx in frame_indices:
        if 0 <= idx < len(sequence.frames):
            frame = sequence.frames[idx]
            console.print(Panel(
                frame.content,
                title=f"Frame {frame.index} @ {frame.timestamp:.2f}s",
                border_style="dim",
            ))


def interpolate_value(start: float, end: float, progress: float) -> float:
    """Linear interpolation between two values."""
    return start + (end - start) * progress


def interpolate_color(
    start: tuple[int, int, int],
    end: tuple[int, int, int],
    progress: float,
) -> tuple[int, int, int]:
    """Interpolate between two RGB colors."""
    return (
        int(interpolate_value(start[0], end[0], progress)),
        int(interpolate_value(start[1], end[1], progress)),
        int(interpolate_value(start[2], end[2], progress)),
    )


def create_progress_bar(
    progress: float,
    width: int = 40,
    filled_char: str = "█",
    empty_char: str = "░",
    show_percentage: bool = True,
) -> str:
    """Create an ASCII progress bar."""
    filled = int(progress * width)
    empty = width - filled
    
    bar = filled_char * filled + empty_char * empty
    
    if show_percentage:
        return f"[{bar}] {progress * 100:.1f}%"
    return f"[{bar}]"


def create_spinner_frame(frame_index: int, style: str = "dots") -> str:
    """Create a spinner frame."""
    spinners = {
        "dots": ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"],
        "line": ["-", "\\", "|", "/"],
        "blocks": ["▖", "▘", "▝", "▗"],
        "arrows": ["←", "↖", "↑", "↗", "→", "↘", "↓", "↙"],
        "stars": ["✶", "✷", "✸", "✹", "✺", "✹", "✸", "✷"],
    }
    
    frames = spinners.get(style, spinners["dots"])
    return frames[frame_index % len(frames)]
