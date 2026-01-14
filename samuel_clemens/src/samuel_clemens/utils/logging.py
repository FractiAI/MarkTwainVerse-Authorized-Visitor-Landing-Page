"""
Logging - Frontier-themed logging for MarkTwainVerse.

"The difference between the right word and the almost right word is 
the difference between lightning and a lightning bug." — Mark Twain

Provides rich console output with frontier-appropriate styling.
"""

from __future__ import annotations

import logging
from datetime import datetime
from typing import Optional

from rich.console import Console
from rich.logging import RichHandler
from rich.theme import Theme

# Frontier theme for Rich console
FRONTIER_THEME = Theme({
    "info": "cyan",
    "warning": "yellow",
    "error": "red bold",
    "success": "green",
    "story": "magenta italic",
    "event": "blue bold",
    "frontier": "yellow bold",
    "wisdom": "green italic",
})

# Create themed console
console = Console(theme=FRONTIER_THEME)


class FrontierLogger:
    """
    A frontier-themed logger with Rich console output.
    
    Each log entry comes with frontier flair—because even
    system messages should tell a story.
    """
    
    def __init__(self, name: str = "samuel_clemens", level: int = logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        
        # Add Rich handler if not already added
        if not any(isinstance(h, RichHandler) for h in self.logger.handlers):
            handler = RichHandler(
                console=console,
                show_time=True,
                show_path=False,
                rich_tracebacks=True,
            )
            handler.setFormatter(logging.Formatter("%(message)s"))
            self.logger.addHandler(handler)
    
    def info(self, message: str) -> None:
        """Log an info message."""
        self.logger.info(message)
    
    def warning(self, message: str) -> None:
        """Log a warning message."""
        self.logger.warning(message)
    
    def error(self, message: str) -> None:
        """Log an error message."""
        self.logger.error(message)
    
    def debug(self, message: str) -> None:
        """Log a debug message."""
        self.logger.debug(message)
    
    def frontier(self, message: str) -> None:
        """Log a frontier-styled message."""
        console.print(f"🏔️  [frontier]{message}[/frontier]")
    
    def story(self, message: str) -> None:
        """Log a story-styled message."""
        console.print(f"📖 [story]{message}[/story]")
    
    def event(self, message: str) -> None:
        """Log an event-styled message."""
        console.print(f"⚡ [event]{message}[/event]")
    
    def wisdom(self, message: str) -> None:
        """Log a wisdom-styled message."""
        console.print(f"💡 [wisdom]{message}[/wisdom]")
    
    def success(self, message: str) -> None:
        """Log a success message."""
        console.print(f"✅ [success]{message}[/success]")


# Global logger instance
_logger: Optional[FrontierLogger] = None


def get_logger() -> FrontierLogger:
    """
    Get the global FrontierLogger instance.
    
    Returns:
        The singleton FrontierLogger
    """
    global _logger
    if _logger is None:
        _logger = FrontierLogger()
    return _logger


def frontier_log(message: str) -> None:
    """
    Log a frontier dispatch.
    
    Standard logging with frontier flair—for general
    operational messages.
    
    Args:
        message: The message to log
    """
    get_logger().frontier(message)


def story_log(message: str) -> None:
    """
    Log a narrative event.
    
    For storytelling moments—when the verse
    speaks through its methods.
    
    Args:
        message: The narrative message
    """
    get_logger().story(message)


def event_log(message: str) -> None:
    """
    Log an autonomous event.
    
    For spontaneous happenings in the verse—
    when the world moves on its own.
    
    Args:
        message: The event message
    """
    get_logger().event(message)


def wisdom_log(message: str) -> None:
    """
    Log a piece of wisdom.
    
    For insights and sage observations—
    Twain-worthy nuggets of truth.
    
    Args:
        message: The wisdom to share
    """
    get_logger().wisdom(message)


def success_log(message: str) -> None:
    """
    Log a successful operation.
    
    Args:
        message: The success message
    """
    get_logger().success(message)


def format_timestamp() -> str:
    """
    Format the current time in frontier style.
    
    Returns:
        Formatted timestamp string
    """
    now = datetime.now()
    hour = now.hour
    
    if 5 <= hour < 12:
        time_of_day = "morning"
    elif 12 <= hour < 17:
        time_of_day = "afternoon"
    elif 17 <= hour < 21:
        time_of_day = "evening"
    else:
        time_of_day = "night"
    
    return f"{now.strftime('%H:%M:%S')} ({time_of_day})"
