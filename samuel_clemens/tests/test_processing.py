"""
Tests for the processing module - Obsidian and PDF export.
"""

import pytest
from pathlib import Path
import tempfile
import shutil

from samuel_clemens.processing import (
    # Parser
    parse_file,
    parse_protocol,
    ParsedDocument,
    ProtocolDocument,
    # Sections
    extract_sections,
    extract_metadata,
    extract_tables,
    # Emoji
    extract_emojis,
    analyze_emoji_usage,
    emoji_to_text,
    # Obsidian
    WikiLink,
    ObsidianPage,
    ObsidianVault,
    protocol_to_obsidian_page,
    export_obsidian_vault,
    # PDF
    PDFConfig,
    export_document_to_pdf,
    export_protocols_to_pdf,
)


class TestEmojiProcessing:
    """Test emoji extraction and analysis."""
    
    def test_extract_emojis_basic(self):
        text = "Hello ✅ World 🎯 Test ✨"
        emojis = extract_emojis(text)
        assert len(emojis) == 3
        chars = [e.char for e in emojis]
        assert "✅" in chars
        assert "🎯" in chars
        assert "✨" in chars
    
    def test_extract_emojis_with_counts(self):
        text = "✅ First ✅ Second ✅ Third"
        emojis = extract_emojis(text)
        assert len(emojis) == 1  # One unique emoji
        assert emojis[0].count == 3  # Appears 3 times
    
    def test_analyze_emoji_usage(self):
        text = "Status: ✅ Target: 🎯 Symbol: 💎✨"
        analysis = analyze_emoji_usage(text)
        assert analysis["total_count"] == 4
        assert analysis["unique_count"] == 4
        assert "status" in analysis["by_category"]
    
    def test_emoji_to_text(self):
        assert emoji_to_text("✅") == "checkmark"
        assert emoji_to_text("🎯") == "target"
        assert emoji_to_text("💎") == "gem"


class TestSectionExtraction:
    """Test markdown section extraction."""
    
    def test_extract_sections_basic(self):
        text = """# Title
        
## Section 1

Content here.

## Section 2

More content.
"""
        sections = extract_sections(text)
        assert len(sections) >= 1
    
    def test_extract_sections_with_emoji(self):
        text = """# Protocol

## 🎯 Emergent Observation

This is important.

## 🔗 Links

References here.
"""
        sections = extract_sections(text)
        assert len(sections) >= 1
    
    def test_extract_metadata(self):
        text = """# Protocol 42

**Protocol Number:** P42  
**Category:** Test / Demo  
**Status:** ✅ OPERATIONAL
"""
        metadata = extract_metadata(text)
        assert metadata.protocol_number == "P42"
        assert metadata.category == "Test / Demo"
    
    def test_extract_tables(self):
        text = """
| Header1 | Header2 |
|---------|---------|
| Cell1   | Cell2   |
| Cell3   | Cell4   |
"""
        tables = extract_tables(text)
        assert len(tables) == 1
        assert tables[0].num_columns == 2
        assert tables[0].num_rows == 2


class TestObsidianExport:
    """Test Obsidian vault export."""
    
    def test_wikilink_creation(self):
        link = WikiLink(target="Protocol_42")
        assert str(link) == "[[Protocol_42]]"
        
        link_with_display = WikiLink(target="Protocol_42", display="P42")
        assert str(link_with_display) == "[[Protocol_42|P42]]"
    
    def test_obsidian_page_creation(self):
        page = ObsidianPage(
            filename="test.md",
            title="Test Page",
            content="# Test\n\nContent here.",
            tags=["test", "demo"],
        )
        rendered = page.render()
        assert "---" in rendered
        assert 'title: "Test Page"' in rendered
        assert "tags: [test, demo]" in rendered
        assert "# Test" in rendered
    
    def test_obsidian_vault_creation(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            vault = ObsidianVault(
                name="TestVault",
                root_path=Path(tmpdir) / "vault",
            )
            
            page = ObsidianPage(
                filename="index.md",
                title="Index",
                content="# Index",
            )
            vault.add_page(page)
            
            count = vault.export()
            assert count == 1
            assert (Path(tmpdir) / "vault" / "index.md").exists()


class TestPDFExport:
    """Test PDF export functionality."""
    
    def test_pdf_config_defaults(self):
        config = PDFConfig()
        assert config.title_size == 24
        assert config.body_size == 11
        assert config.include_toc is True
    
    def test_pdf_config_custom(self):
        config = PDFConfig(
            title_size=30,
            include_toc=False,
        )
        assert config.title_size == 30
        assert config.include_toc is False


class TestDocumentParsing:
    """Test document parsing."""
    
    def test_parsed_document_properties(self):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
            f.write("# Test Title\n\nSome content ✅ here.")
            f.flush()
            
            doc = parse_file(f.name)
            assert doc.title == "Test Title"
            assert doc.word_count > 0
            assert doc.emoji_count == 1
            
            Path(f.name).unlink()
    
    def test_protocol_document_parsing(self):
        content = """# PROTOCOL 99: TEST PROTOCOL
## Test Subtitle

**Protocol Number:** P99  
**Category:** Test  
**Status:** ✅ OPERATIONAL

## 🎯 EMERGENT OBSERVATION

This is a test protocol.

## 🌟 CONCLUSION

- ✅ First point
- ✅ Second point

💎✨
"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
            f.write(content)
            f.flush()
            
            doc = parse_protocol(f.name)
            assert doc.protocol_number == 99
            assert doc.protocol_id == "P99"
            assert len(doc.checkmarks) >= 2
            assert len(doc.footer_emojis) >= 1
            
            Path(f.name).unlink()


class TestIntegration:
    """Integration tests for full workflow."""
    
    def test_full_obsidian_export_workflow(self):
        """Test complete Obsidian export from parsed documents."""
        content = """# PROTOCOL 1: TEST
## Subtitle

**Protocol Number:** P1
**Status:** ✅ OPERATIONAL

## 🎯 Observation

Test content with [[Entity_Link]].
"""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create test file
            test_file = Path(tmpdir) / "PROTOCOL_1.md"
            test_file.write_text(content)
            
            # Parse
            doc = parse_protocol(test_file)
            
            # Convert to Obsidian
            page = protocol_to_obsidian_page(doc)
            assert page.filename == "Protocol_1.md"
            assert "protocol" in page.tags
            
            # Export vault
            vault_path = Path(tmpdir) / "vault"
            vault = export_obsidian_vault([doc], vault_path)
            
            assert len(vault.pages) >= 1
            assert vault_path.exists()
