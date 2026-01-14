"""
Image Export - Generate PNG visualizations using Pillow.

"The public is the only critic whose opinion is worth anything at all."
— Mark Twain

Features:
- Story Cards (Title, Quote, Summary)
- Protocol Cards (Status, Emojis, Stats)
- ASCII Art Rendering
- Statistical Dashboards
"""

from __future__ import annotations

import textwrap
from pathlib import Path
from typing import Optional, Any
from dataclasses import dataclass

from PIL import Image, ImageDraw, ImageFont

from samuel_clemens.processing.parser import ProtocolDocument
from samuel_clemens.stories.generator import Story

# Default font paths (system dependent - fallback strategies needed)
# For macOS, we can look in /System/Library/Fonts or /Library/Fonts
FONT_PATHS = [
    "/System/Library/Fonts/Helvetica.ttc",
    "/System/Library/Fonts/Monaco.ttf",
    "/Library/Fonts/Arial.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",  # Linux
    "C:\\Windows\\Fonts\\arial.ttf",  # Windows
]

def _get_font(name: str = "sans", size: int = 20) -> ImageFont.FreeTypeFont:
    """Load a font or fallback to default."""
    # Try to find a valid font path
    font_path = None
    for path in FONT_PATHS:
        if Path(path).exists():
            font_path = path
            break
    
    try:
        if font_path:
            return ImageFont.truetype(font_path, size)
        return ImageFont.load_default()
    except Exception:
        return ImageFont.load_default()


@dataclass
class ImageConfig:
    """Configuration for image generation."""
    width: int = 1200
    height: int = 630  # Standard social media card size
    bg_color: str = "#1a1a1a"
    text_color: str = "#ffffff"
    accent_color: str = "#f1c40f"
    font_size_title: int = 60
    font_size_body: int = 24
    padding: int = 60


def _draw_text_centered(
    draw: ImageDraw.ImageDraw,
    text: str,
    y: int,
    width: int,
    font: ImageFont.FreeTypeFont,
    color: str,
) -> int:
    """Draw centered text and return bottom Y coordinate."""
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (width - text_width) // 2
    draw.text((x, y), text, font=font, fill=color)
    
    return y + text_height


def _wrap_text(text: str, font: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
    """Wrap text to fit width."""
    lines = []
    # Approximate chars per line
    avg_char_width = font.getlength("x")
    chars_per_line = int(max_width / avg_char_width)
    
    wrapper = textwrap.TextWrapper(width=chars_per_line)
    lines = wrapper.wrap(text)
    
    return lines


def render_story_card_image(
    story: Story,
    output_path: Path | str,
    config: Optional[ImageConfig] = None,
) -> Path:
    """
    Render a story card to PNG.
    
    Args:
        story: Story object
        output_path: Output file path
        config: Image configuration
        
    Returns:
        Path to created image
    """
    config = config or ImageConfig()
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Create image
    img = Image.new("RGB", (config.width, config.height), config.bg_color)
    draw = ImageDraw.Draw(img)
    
    # Fonts
    title_font = _get_font(size=config.font_size_title)
    body_font = _get_font(size=config.font_size_body)
    meta_font = _get_font(size=int(config.font_size_body * 0.8))
    
    current_y = config.padding
    
    # Border
    draw.rectangle(
        [
            (config.padding // 2, config.padding // 2), 
            (config.width - config.padding // 2, config.height - config.padding // 2)
        ],
        outline=config.accent_color,
        width=4
    )
    
    # Title
    current_y = _draw_text_centered(
        draw, story.title, current_y, config.width, title_font, config.accent_color
    )
    current_y += 40
    
    # Quote
    quote = f'"{story.quote.text}"'
    quote_lines = _wrap_text(quote, body_font, config.width - config.padding * 4)
    for line in quote_lines:
        current_y = _draw_text_centered(
            draw, line, current_y, config.width, body_font, "#dddddd"
        )
        current_y += 10
    
    # Attribution
    current_y += 10
    source = getattr(story.quote, "source", getattr(story.quote, "attribution", "Unknown"))
    _draw_text_centered(
        draw, f"— {source}", current_y, config.width, meta_font, "#aaaaaa"
    )
    
    # Footer metadata
    template = getattr(story, "template_name", getattr(story, "template_used", "Story"))
    footer_text = f"MarkTwainVerse • {template}"
    bbox = draw.textbbox((0, 0), footer_text, font=meta_font)
    footer_width = bbox[2] - bbox[0]
    draw.text(
        ((config.width - footer_width) // 2, config.height - config.padding - 20),
        footer_text,
        font=meta_font,
        fill=config.accent_color
    )
    
    img.save(output_path)
    return output_path


def render_protocol_card_image(
    protocol: ProtocolDocument,
    output_path: Path | str,
    config: Optional[ImageConfig] = None,
) -> Path:
    """
    Render a protocol status card to PNG.
    
    Args:
        protocol: Protocol document
        output_path: Output file path
        
    Returns:
        Path to created image
    """
    config = config or ImageConfig(bg_color="#0f2b3e", accent_color="#00ff9d")
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    img = Image.new("RGB", (config.width, config.height), config.bg_color)
    draw = ImageDraw.Draw(img)
    
    title_font = _get_font(size=config.font_size_title)
    heading_font = _get_font(size=40)
    body_font = _get_font(size=config.font_size_body)
    
    current_y = config.padding
    
    # Protocol ID
    if protocol.protocol_id:
        draw.text(
            (config.padding, current_y), 
            protocol.protocol_id, 
            font=heading_font, 
            fill=config.accent_color
        )
    
    # Status
    status = protocol.status or "UNKNOWN"
    status_bbox = draw.textbbox((0, 0), status, font=body_font)
    status_width = status_bbox[2] - status_bbox[0]
    draw.text(
        (config.width - config.padding - status_width, current_y + 10),
        status,
        font=body_font,
        fill="#ff4444" if "ALERT" in status else "#00ff9d"
    )
    
    current_y += 80
    
    # Title
    title_lines = _wrap_text(
        protocol.title or "Untitled", 
        title_font, 
        config.width - config.padding * 2
    )
    for line in title_lines:
        draw.text(
            (config.padding, current_y), 
            line, 
            font=title_font, 
            fill=config.text_color
        )
        current_y += config.font_size_title + 10
    
    current_y += 40
    
    # Stats Grid
    stats = [
        ("Words", str(protocol.word_count)),
        ("Emojis", str(protocol.emoji_count)),
        ("Sections", str(len(protocol.sections))),
        ("Checks", str(len(protocol.checkmarks))),
    ]
    
    grid_x = config.padding
    for label, value in stats:
        draw.text((grid_x, current_y), label, font=body_font, fill="#aaaaaa")
        draw.text(
            (grid_x, current_y + 30), 
            value, 
            font=heading_font, 
            fill=config.text_color
        )
        grid_x += 200
    
    # Footer Emojis
    if protocol.footer_emojis:
        emoji_str = " ".join(protocol.footer_emojis)
        draw.text(
            (config.padding, config.height - config.padding - 40),
            emoji_str,
            font=heading_font,  # Might not render colored emojis correctly without special font
            fill="#ffffff"
        )
    
    img.save(output_path)
    return output_path


def render_ascii_to_image(
    ascii_art: str,
    output_path: Path | str,
    bg_color: str = "#000000",
    text_color: str = "#00ff00",
) -> Path:
    """
    Render ASCII art string to an image.
    
    Args:
        ascii_art: String containing ASCII art
        output_path: Output file path
        
    Returns:
        Path to created image
    """
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    lines = ascii_art.split("\n")
    max_len = max(len(line) for line in lines) if lines else 0
    line_count = len(lines)
    
    # Try to find a monospace font
    font = _get_font("mono", size=14)
    
    # Calculate size
    char_width = font.getlength("A")
    # Approximate height
    bbox = font.getbbox("Tg")
    char_height = bbox[3] - bbox[1] + 4
    
    width = int(max_len * char_width) + 40
    height = int(line_count * char_height) + 40
    
    img = Image.new("RGB", (width, height), bg_color)
    draw = ImageDraw.Draw(img)
    
    y = 20
    for line in lines:
        draw.text((20, y), line, font=font, fill=text_color)
        y += char_height
    
    img.save(output_path)
    return output_path
