"""
Config - Configuration management for MarkTwainVerse.

"Plan for what is difficult while it is easy." — Mark Twain
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Optional
import json


@dataclass
class VoiceConfig:
    """Voice narration configuration."""
    enabled: bool = True
    volume: float = 0.8
    speed: float = 1.0


@dataclass
class MediaConfig:
    """Media generation configuration."""
    art_enabled: bool = True
    images_enabled: bool = True
    video_enabled: bool = True
    quality: str = "standard"


@dataclass
class FSRConfig:
    """Full Sensory Reality configuration."""
    enabled: bool = True
    immersion_level: str = "moderate"  # minimal, moderate, full


@dataclass
class Config:
    """
    Main configuration for Samuel Clemens package.
    
    The town charter—all the rules and settings
    that govern how the frontier operates.
    """
    # Package info
    version: str = "0.1.0"
    debug: bool = False
    
    # Verse settings
    verse_name: str = "MarkTwainVerse"
    hero_host: str = "Mark Twain"
    
    # Day/night cycle (for demo: 2 min cycle, production: real time)
    demo_mode: bool = True
    day_cycle_duration_ms: int = 120000  # 2 minutes
    
    # Visitor settings
    default_visitor_name: str = "friend"
    
    # Media configuration
    voice: VoiceConfig = field(default_factory=VoiceConfig)
    media: MediaConfig = field(default_factory=MediaConfig)
    fsr: FSRConfig = field(default_factory=FSRConfig)
    
    # Logging
    log_level: str = "INFO"
    log_format: str = "frontier"  # frontier, standard, minimal

    def to_dict(self) -> dict[str, Any]:
        """Convert config to dictionary."""
        return {
            "version": self.version,
            "debug": self.debug,
            "verse_name": self.verse_name,
            "hero_host": self.hero_host,
            "demo_mode": self.demo_mode,
            "day_cycle_duration_ms": self.day_cycle_duration_ms,
            "default_visitor_name": self.default_visitor_name,
            "voice": {
                "enabled": self.voice.enabled,
                "volume": self.voice.volume,
                "speed": self.voice.speed,
            },
            "media": {
                "art_enabled": self.media.art_enabled,
                "images_enabled": self.media.images_enabled,
                "video_enabled": self.media.video_enabled,
                "quality": self.media.quality,
            },
            "fsr": {
                "enabled": self.fsr.enabled,
                "immersion_level": self.fsr.immersion_level,
            },
            "log_level": self.log_level,
            "log_format": self.log_format,
        }
    
    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Config":
        """Create config from dictionary."""
        voice = VoiceConfig(**data.get("voice", {})) if "voice" in data else VoiceConfig()
        media = MediaConfig(**data.get("media", {})) if "media" in data else MediaConfig()
        fsr = FSRConfig(**data.get("fsr", {})) if "fsr" in data else FSRConfig()
        
        return cls(
            version=data.get("version", "0.1.0"),
            debug=data.get("debug", False),
            verse_name=data.get("verse_name", "MarkTwainVerse"),
            hero_host=data.get("hero_host", "Mark Twain"),
            demo_mode=data.get("demo_mode", True),
            day_cycle_duration_ms=data.get("day_cycle_duration_ms", 120000),
            default_visitor_name=data.get("default_visitor_name", "friend"),
            voice=voice,
            media=media,
            fsr=fsr,
            log_level=data.get("log_level", "INFO"),
            log_format=data.get("log_format", "frontier"),
        )


# Global config instance
_config: Optional[Config] = None


def get_config() -> Config:
    """
    Get the global configuration instance.
    
    Returns:
        The singleton Config
    """
    global _config
    if _config is None:
        _config = Config()
    return _config


def load_config(path: Path | str) -> Config:
    """
    Load configuration from a JSON file.
    
    Args:
        path: Path to configuration file
        
    Returns:
        Loaded Config instance
    """
    global _config
    
    path = Path(path)
    if path.exists():
        with open(path) as f:
            data = json.load(f)
        _config = Config.from_dict(data)
    else:
        _config = Config()
    
    return _config


def save_config(path: Path | str, config: Optional[Config] = None) -> None:
    """
    Save configuration to a JSON file.
    
    Args:
        path: Path to save configuration
        config: Config to save (uses global if not provided)
    """
    path = Path(path)
    config = config or get_config()
    
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        json.dump(config.to_dict(), f, indent=2)


def reset_config() -> Config:
    """
    Reset configuration to defaults.
    
    Returns:
        Fresh Config instance
    """
    global _config
    _config = Config()
    return _config
