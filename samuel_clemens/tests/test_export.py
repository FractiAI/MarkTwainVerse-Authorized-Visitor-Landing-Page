"""
Tests for story export module.
"""

import pytest
import json
from pathlib import Path
from tempfile import TemporaryDirectory

from samuel_clemens.stories.generator import StoryGenerator, GeneratedStory
from samuel_clemens.stories.recombinator import StoryRecombinator, RecombinedStory
from samuel_clemens.stories.export import (
    export_to_markdown,
    export_to_html,
    export_to_json,
    export_to_text,
    export_story,
    export_anthology,
)


@pytest.fixture
def sample_story() -> GeneratedStory:
    """Generate a sample story for testing."""
    generator = StoryGenerator()
    return generator.generate()


@pytest.fixture
def sample_recombined() -> RecombinedStory:
    """Generate a sample recombined story for testing."""
    generator = StoryGenerator()
    recombinator = StoryRecombinator()
    stories = generator.generate_batch(2)
    return recombinator.blend(stories[0], stories[1])


class TestExportToMarkdown:
    """Tests for Markdown export."""

    def test_export_returns_string(self, sample_story: GeneratedStory) -> None:
        """export_to_markdown should return a string."""
        result = export_to_markdown(sample_story)
        assert isinstance(result, str)
        assert len(result) > 0

    def test_export_contains_title(self, sample_story: GeneratedStory) -> None:
        """Export should contain the story title."""
        result = export_to_markdown(sample_story)
        assert f"# {sample_story.title}" in result

    def test_export_contains_story_text(self, sample_story: GeneratedStory) -> None:
        """Export should contain the story text."""
        result = export_to_markdown(sample_story)
        assert sample_story.text in result

    def test_export_with_metadata(self, sample_story: GeneratedStory) -> None:
        """Export with metadata should include story details."""
        result = export_to_markdown(sample_story, include_metadata=True)
        assert "Word Count" in result
        assert "Template" in result

    def test_export_without_metadata(self, sample_story: GeneratedStory) -> None:
        """Export without metadata should omit details."""
        result = export_to_markdown(sample_story, include_metadata=False)
        assert "Word Count" not in result

    def test_export_to_file(self, sample_story: GeneratedStory) -> None:
        """Export should save to file when path provided."""
        with TemporaryDirectory() as tmpdir:
            filepath = Path(tmpdir) / "story.md"
            export_to_markdown(sample_story, filepath=filepath)
            assert filepath.exists()
            content = filepath.read_text()
            assert sample_story.title in content


class TestExportToHTML:
    """Tests for HTML export."""

    def test_export_returns_string(self, sample_story: GeneratedStory) -> None:
        """export_to_html should return a string."""
        result = export_to_html(sample_story)
        assert isinstance(result, str)

    def test_export_is_valid_html(self, sample_story: GeneratedStory) -> None:
        """Export should be valid HTML structure."""
        result = export_to_html(sample_story)
        assert "<!DOCTYPE html>" in result
        assert "<html" in result
        assert "</html>" in result

    def test_export_contains_title(self, sample_story: GeneratedStory) -> None:
        """Export should contain title in h1 tag."""
        result = export_to_html(sample_story)
        assert f"<title>{sample_story.title}</title>" in result

    def test_export_with_styles(self, sample_story: GeneratedStory) -> None:
        """Export with styles should include CSS."""
        result = export_to_html(sample_story, include_styles=True)
        assert "<style>" in result

    def test_export_without_styles(self, sample_story: GeneratedStory) -> None:
        """Export without styles should omit CSS."""
        result = export_to_html(sample_story, include_styles=False)
        assert "<style>" not in result

    def test_export_to_file(self, sample_story: GeneratedStory) -> None:
        """Export should save to file."""
        with TemporaryDirectory() as tmpdir:
            filepath = Path(tmpdir) / "story.html"
            export_to_html(sample_story, filepath=filepath)
            assert filepath.exists()


class TestExportToJSON:
    """Tests for JSON export."""

    def test_export_returns_string(self, sample_story: GeneratedStory) -> None:
        """export_to_json should return a string."""
        result = export_to_json(sample_story)
        assert isinstance(result, str)

    def test_export_is_valid_json(self, sample_story: GeneratedStory) -> None:
        """Export should be valid JSON."""
        result = export_to_json(sample_story)
        data = json.loads(result)
        assert isinstance(data, dict)

    def test_export_contains_required_fields(self, sample_story: GeneratedStory) -> None:
        """Export should contain all required fields."""
        result = export_to_json(sample_story)
        data = json.loads(result)
        assert "title" in data
        assert "text" in data
        assert "word_count" in data
        assert "generated_at" in data

    def test_export_generated_story_type(self, sample_story: GeneratedStory) -> None:
        """GeneratedStory should have type 'generated'."""
        result = export_to_json(sample_story)
        data = json.loads(result)
        assert data["type"] == "generated"

    def test_export_recombined_story_type(self, sample_recombined: RecombinedStory) -> None:
        """RecombinedStory should have type 'recombined'."""
        result = export_to_json(sample_recombined)
        data = json.loads(result)
        assert data["type"] == "recombined"

    def test_export_to_file(self, sample_story: GeneratedStory) -> None:
        """Export should save to file."""
        with TemporaryDirectory() as tmpdir:
            filepath = Path(tmpdir) / "story.json"
            export_to_json(sample_story, filepath=filepath)
            assert filepath.exists()
            
            # Verify JSON is valid
            content = filepath.read_text()
            data = json.loads(content)
            assert data["title"] == sample_story.title


class TestExportToText:
    """Tests for plain text export."""

    def test_export_returns_string(self, sample_story: GeneratedStory) -> None:
        """export_to_text should return a string."""
        result = export_to_text(sample_story)
        assert isinstance(result, str)

    def test_export_contains_title(self, sample_story: GeneratedStory) -> None:
        """Export should contain title."""
        result = export_to_text(sample_story)
        assert sample_story.title in result

    def test_export_contains_story_text(self, sample_story: GeneratedStory) -> None:
        """Export should contain story text."""
        result = export_to_text(sample_story)
        assert sample_story.text in result

    def test_export_to_file(self, sample_story: GeneratedStory) -> None:
        """Export should save to file."""
        with TemporaryDirectory() as tmpdir:
            filepath = Path(tmpdir) / "story.txt"
            export_to_text(sample_story, filepath=filepath)
            assert filepath.exists()


class TestExportStory:
    """Tests for auto-format export."""

    def test_auto_detect_markdown(self, sample_story: GeneratedStory) -> None:
        """Should auto-detect markdown from .md extension."""
        with TemporaryDirectory() as tmpdir:
            filepath = Path(tmpdir) / "story.md"
            result = export_story(sample_story, filepath)
            assert "# " in result

    def test_auto_detect_html(self, sample_story: GeneratedStory) -> None:
        """Should auto-detect HTML from .html extension."""
        with TemporaryDirectory() as tmpdir:
            filepath = Path(tmpdir) / "story.html"
            result = export_story(sample_story, filepath)
            assert "<!DOCTYPE html>" in result

    def test_auto_detect_json(self, sample_story: GeneratedStory) -> None:
        """Should auto-detect JSON from .json extension."""
        with TemporaryDirectory() as tmpdir:
            filepath = Path(tmpdir) / "story.json"
            result = export_story(sample_story, filepath)
            data = json.loads(result)
            assert "title" in data

    def test_explicit_format(self, sample_story: GeneratedStory) -> None:
        """Should use explicit format over extension."""
        with TemporaryDirectory() as tmpdir:
            filepath = Path(tmpdir) / "story.xyz"
            result = export_story(sample_story, filepath, format="json")
            data = json.loads(result)
            assert "title" in data


class TestExportAnthology:
    """Tests for anthology export."""

    def test_creates_files(self) -> None:
        """Should create files for each story."""
        generator = StoryGenerator()
        stories = generator.generate_batch(3)
        
        with TemporaryDirectory() as tmpdir:
            created = export_anthology(stories, Path(tmpdir))
            # 3 stories + 1 index
            assert len(created) == 4

    def test_creates_index(self) -> None:
        """Should create index file."""
        generator = StoryGenerator()
        stories = generator.generate_batch(2)
        
        with TemporaryDirectory() as tmpdir:
            created = export_anthology(stories, Path(tmpdir))
            index_path = Path(tmpdir) / "index.md"
            assert index_path.exists()

    def test_no_index(self) -> None:
        """Should skip index when disabled."""
        generator = StoryGenerator()
        stories = generator.generate_batch(2)
        
        with TemporaryDirectory() as tmpdir:
            created = export_anthology(stories, Path(tmpdir), create_index=False)
            # Only story files, no index
            assert len(created) == 2

    def test_different_formats(self) -> None:
        """Should respect format option."""
        generator = StoryGenerator()
        stories = generator.generate_batch(2)
        
        with TemporaryDirectory() as tmpdir:
            export_anthology(stories, Path(tmpdir), format="html")
            files = list(Path(tmpdir).glob("*.html"))
            # 2 stories + 1 index
            assert len(files) == 3
