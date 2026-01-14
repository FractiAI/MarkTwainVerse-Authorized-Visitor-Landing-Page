"""
ASCII Art - Frontier-themed ASCII art for MarkTwainVerse.

Classic terminal art for banners, portraits, and maps.
"""

from __future__ import annotations

from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()


# Mark Twain ASCII portrait
TWAIN_PORTRAIT = r"""
        .--.
       /    \
      | o  o |
      |  __  |
      | /  \ |
       \    /
    ____\||/____
   /    |  |    \
  /     |  |     \
 |  .-. |  | .-.  |
 | (   )|  |(   ) |
  \ `-' |  | `-' /
   \____|  |____/
        |__|
    Mark Twain
"""

TWAIN_PORTRAIT_SMALL = r"""
   .---.
  ( o o )
   \ = /
   /   \
  /_____\
  M.Twain
"""

# Frontier banner
FRONTIER_BANNER = r"""
╔═══════════════════════════════════════════════════════════════════╗
║  ███╗   ███╗ █████╗ ██████╗ ██╗  ██╗    ████████╗██╗    ██╗       ║
║  ████╗ ████║██╔══██╗██╔══██╗██║ ██╔╝    ╚══██╔══╝██║    ██║       ║
║  ██╔████╔██║███████║██████╔╝█████╔╝        ██║   ██║ █╗ ██║       ║
║  ██║╚██╔╝██║██╔══██║██╔══██╗██╔═██╗        ██║   ██║███╗██║       ║
║  ██║ ╚═╝ ██║██║  ██║██║  ██║██║  ██╗       ██║   ╚███╔███╔╝       ║
║  ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝       ╚═╝    ╚══╝╚══╝        ║
║                                                                    ║
║  ██╗   ██╗███████╗██████╗ ███████╗███████╗                        ║
║  ██║   ██║██╔════╝██╔══██╗██╔════╝██╔════╝                        ║
║  ██║   ██║█████╗  ██████╔╝███████╗█████╗                          ║
║  ╚██╗ ██╔╝██╔══╝  ██╔══██╗╚════██║██╔══╝                          ║
║   ╚████╔╝ ███████╗██║  ██║███████║███████╗                        ║
║    ╚═══╝  ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝                        ║
╚═══════════════════════════════════════════════════════════════════╝
"""

FRONTIER_BANNER_SMALL = r"""
╔════════════════════════════════╗
║   MARK TWAIN VERSE             ║
║   ~~~~~~~~~~~~~~~~~~~~~~~~     ║
║   Frontier • Stories • Life    ║
╚════════════════════════════════╝
"""

# Steamboat art
STEAMBOAT = r"""
                                        |
                                       _|_
                                      /   \
                                     |     |
                        ___________  |  _  |  ___________
                       /           \ |_/ \_| /           \
          ~~~~~~~~~~~~|   TWAIN    |~~~~~~~~|  EXPRESS   |~~~~~~~~~~~~
           ~~~~~~~~~~~|___________|~~~~~~~~~|___________|~~~~~~~~~~~
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

STEAMBOAT_SMALL = r"""
        |_
       /  \
   ~~~|TWAIN|~~~
   ~~~~~~~~~~~~~
"""

# Frontier map
FRONTIER_MAP = r"""
    ╔═══════════════════════════════════════════════════════════╗
    ║                    SYNTHEVERSE FRONTIER                    ║
    ╠═══════════════════════════════════════════════════════════╣
    ║                                                            ║
    ║        🏔️ Alpine Heights          ⛺ Wilderness Preserve   ║
    ║           \                              /                 ║
    ║            \                            /                  ║
    ║             \    🌲🌲🌲🌲🌲🌲🌲    /                   ║
    ║              \                        /                    ║
    ║               ╔══════════════════════╗                     ║
    ║  🎣 Crystal   ║   🏛️ TOWN CENTER    ║    🏠 Frontier     ║
    ║     Lake  ~~~~║                      ║~~~~  Colony        ║
    ║               ║    🎩 Mark Twain     ║                     ║
    ║               ╚══════════════════════╝                     ║
    ║              /                        \                    ║
    ║             /                          \                   ║
    ║   🚀 Innovation                    🌴 Tropical            ║
    ║      Hub                              Beach               ║
    ║                                                            ║
    ╚═══════════════════════════════════════════════════════════╝
"""

# Campfire scene
CAMPFIRE = r"""
                          (  )   (   )  )
                           ) (   )  (  (
                           ( )  (    ) )
                           _____________
                          <_____________> ___
                          |             |/ _ \
                          |               | | |
                          |               |_| |
                       ___|             |\___/
                      /    \___________/    \
                     /                        \
                    /__________________________\
                    
       🌙  Gather 'round for fireside tales...  ⭐
"""

# Book/Story art
BOOK_ART = r"""
        _______________________
       /                       /|
      /_______________________/ |
     |   ___________________   | |
     |  |                   |  | |
     |  |   📖 A TALE FROM  |  | |
     |  |   THE FRONTIER    |  | |
     |  |                   |  | |
     |  |   By Mark Twain   |  | |
     |  |___________________|  | |
     |_________________________|/
"""


def render_frontier_banner(size: str = "large") -> str:
    """
    Render the MarkTwainVerse frontier banner.
    
    Args:
        size: Banner size (large, small)
        
    Returns:
        The banner string
    """
    banner = FRONTIER_BANNER if size == "large" else FRONTIER_BANNER_SMALL
    console.print(Panel(
        Text(banner, style="yellow"),
        border_style="yellow",
    ))
    return banner


def render_twain_portrait(size: str = "large") -> str:
    """
    Render Mark Twain's ASCII portrait.
    
    Args:
        size: Portrait size (large, small)
        
    Returns:
        The portrait string
    """
    portrait = TWAIN_PORTRAIT if size == "large" else TWAIN_PORTRAIT_SMALL
    console.print(Panel(
        Text(portrait, style="cyan"),
        title="🎩 Samuel Clemens",
        subtitle="a.k.a. Mark Twain",
        border_style="yellow",
    ))
    return portrait


def render_map_art() -> str:
    """
    Render the frontier map.
    
    Returns:
        The map string
    """
    console.print(Panel(
        Text(FRONTIER_MAP, style="green"),
        border_style="green",
    ))
    return FRONTIER_MAP


def render_steamboat(size: str = "large") -> str:
    """
    Render a Mississippi steamboat.
    
    Args:
        size: Art size (large, small)
        
    Returns:
        The steamboat string
    """
    boat = STEAMBOAT if size == "large" else STEAMBOAT_SMALL
    console.print(Panel(
        Text(boat, style="cyan"),
        title="🚢 Mississippi Steamboat",
        border_style="blue",
    ))
    return boat


def render_campfire() -> None:
    """
    Render a campfire scene for storytelling.
    """
    console.print(Panel(
        Text(CAMPFIRE, style="yellow"),
        title="🔥 Fireside Tales",
        border_style="red",
    ))


def render_book() -> None:
    """
    Render a book for story display.
    """
    console.print(Panel(
        Text(BOOK_ART, style="magenta"),
        border_style="magenta",
    ))


def render_welcome_scene() -> None:
    """
    Render a complete welcome scene with banner and portrait.
    """
    console.print()
    render_frontier_banner(size="small")
    console.print()
    render_twain_portrait(size="small")
    console.print()
    console.print("[italic]Welcome to the frontier, friend...[/italic]")
    console.print()


def render_goodbye_scene() -> None:
    """
    Render a goodbye scene with steamboat.
    """
    console.print()
    render_steamboat(size="small")
    console.print()
    console.print("[italic]Safe travels on the river of life...[/italic]")
    console.print()


def get_mood_emoji(mood: str) -> str:
    """
    Get an emoji for a mood state.
    
    Args:
        mood: Mood name
        
    Returns:
        Corresponding emoji
    """
    mood_emojis = {
        "dormant": "💤",
        "awakening": "🌅",
        "active": "⭐",
        "thriving": "🌟",
        "resting": "🌙",
    }
    return mood_emojis.get(mood.lower(), "●")


def get_weather_art(weather: str) -> str:
    """
    Get ASCII art for weather conditions.
    
    Args:
        weather: Weather condition
        
    Returns:
        ASCII art string
    """
    weather_art = {
        "sunny": "  \\  |  /\n   \\ | /\n ----⊙----\n   / | \\\n  /  |  \\",
        "cloudy": "   .-~~~-.\n .-~       ~-.\n(    ☁️     )\n `-._____.-'",
        "rainy": "   ☁️☁️☁️\n  /  /  /\n /  /  /\n/  /  /",
        "stormy": "  ⚡☁️⚡\n  /  /  /\n /⚡/  /\n/  /⚡/",
        "night": "  ✦  ✦  ✦\n    🌙\n  ✦    ✦",
    }
    return weather_art.get(weather.lower(), "")
