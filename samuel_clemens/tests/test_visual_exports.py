"""
Tests for visualization exports (PNG and PDF).
"""

import pytest
from pathlib import Path
import shutil
import tempfile
from PIL import Image

from samuel_clemens.visualization.image_export import (
    render_story_card_image,
    render_protocol_card_image,
    render_ascii_to_image,
    ImageConfig,
)
from samuel_clemens.processing.pdf_export import (
    export_story_to_pdf,
    export_anthology_to_pdf,
    PDFConfig,
)
from samuel_clemens.stories.generator import GeneratedStory
from samuel_clemens.processing import ProtocolDocument, Quote

@pytest.fixture
def sample_story():
    return GeneratedStory(
        title="Test Story",
        text="# Chapter 1\n\nOnce upon a time...",
        template_used="frontier_tale",
        quote=Quote(text="Test quote", attribution="Mark Twain"),
    )

@pytest.fixture
def sample_protocol():
    return ProtocolDocument(
        filepath=Path("PROTOCOL_99.md"),
        filename="PROTOCOL_99.md",
        content="# Protocol 99",
        protocol_number=99,
        protocol_id="P99",
        title="Test Protocol",
        checkmarks=["Point 1", "Point 2"],
        # emoji_count is a property, provide emojis list to populate it
        emojis=[], 
        word_count=100,
        sections=[],
        metadata=None # Optional
    )

class TestImageExport:
    """Test PNG generation."""
    
    def test_render_story_card(self, sample_story, tmp_path):
        output = tmp_path / "story_card.png"
        render_story_card_image(sample_story, output)
        
        assert output.exists()
        img = Image.open(output)
        assert img.format == "PNG"
        assert img.size == (1200, 630)
    
    def test_render_protocol_card(self, sample_protocol, tmp_path):
        output = tmp_path / "protocol_card.png"
        render_protocol_card_image(sample_protocol, output)
        
        assert output.exists()
        img = Image.open(output)
        assert img.size[0] == 1200
        
    def test_render_ascii_art(self, tmp_path):
        ascii_art = "  /\\\n /  \\\n/____\\"
        output = tmp_path / "ascii.png"
        render_ascii_to_image(ascii_art, output)
        
        assert output.exists()
        img = Image.open(output)
        assert img.size[0] > 0
        assert img.size[1] > 0

class TestPDFExportExtensions:
    """Test extended PDF features."""
    
    def test_export_story_pdf(self, sample_story, tmp_path):
        output = tmp_path / "story.pdf"
        export_story_to_pdf(sample_story, output)
        assert output.exists()
        assert output.stat().st_size > 0
        
    def test_export_anthology_pdf(self, tmp_path):
        # Create fake anthology dir
        anthology_dir = tmp_path / "anthology"
        anthology_dir.mkdir()
        (anthology_dir / "story1.md").write_text("# Story 1\nContent")
        (anthology_dir / "story2.md").write_text("# Story 2\nContent")
        
        output = tmp_path / "anthology.pdf"
        export_anthology_to_pdf(anthology_dir, output)
        assert output.exists()
