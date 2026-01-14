"""
Tests for CLI module.
"""

import pytest
from click.testing import CliRunner

from samuel_clemens.cli.main import cli


@pytest.fixture
def runner() -> CliRunner:
    """Create CLI test runner."""
    return CliRunner()


class TestCLI:
    """Tests for CLI commands."""

    def test_cli_help(self, runner: CliRunner) -> None:
        """CLI should show help."""
        result = runner.invoke(cli, ["--help"])
        assert result.exit_code == 0
        assert "Samuel Clemens" in result.output

    def test_cli_version(self, runner: CliRunner) -> None:
        """CLI should show version."""
        result = runner.invoke(cli, ["--version"])
        assert result.exit_code == 0
        assert "0.2.0" in result.output

    def test_greet_command(self, runner: CliRunner) -> None:
        """greet command should work."""
        result = runner.invoke(cli, ["greet"])
        assert result.exit_code == 0
        assert "Mark Twain" in result.output

    def test_greet_with_name(self, runner: CliRunner) -> None:
        """greet command should accept name."""
        result = runner.invoke(cli, ["greet", "--name", "Partner"])
        assert result.exit_code == 0

    def test_farewell_command(self, runner: CliRunner) -> None:
        """farewell command should work."""
        result = runner.invoke(cli, ["farewell"])
        assert result.exit_code == 0

    def test_story_command(self, runner: CliRunner) -> None:
        """story command should work."""
        result = runner.invoke(cli, ["story"])
        assert result.exit_code == 0
        assert "Story" in result.output

    def test_story_with_topic(self, runner: CliRunner) -> None:
        """story command should accept topic."""
        result = runner.invoke(cli, ["story", "--topic", "adventure"])
        assert result.exit_code == 0
        assert "Adventure" in result.output

    def test_wisdom_command(self, runner: CliRunner) -> None:
        """wisdom command should work."""
        result = runner.invoke(cli, ["wisdom"])
        assert result.exit_code == 0
        assert "Wisdom" in result.output

    def test_status_command(self, runner: CliRunner) -> None:
        """status command should work."""
        result = runner.invoke(cli, ["status"])
        assert result.exit_code == 0
        assert "MarkTwainVerse" in result.output

    def test_expedition_command(self, runner: CliRunner) -> None:
        """expedition command should work."""
        result = runner.invoke(cli, ["expedition"])
        assert result.exit_code == 0
        assert "Expedition" in result.output

    def test_expedition_with_type(self, runner: CliRunner) -> None:
        """expedition command should accept type."""
        result = runner.invoke(cli, ["expedition", "--type", "fishing"])
        assert result.exit_code == 0
        assert "Fishing" in result.output

    def test_cycles_command(self, runner: CliRunner) -> None:
        """cycles command should work."""
        result = runner.invoke(cli, ["cycles"])
        assert result.exit_code == 0
        assert "Natural Cycles" in result.output

    def test_entities_command(self, runner: CliRunner) -> None:
        """entities command should work."""
        result = runner.invoke(cli, ["entities"])
        assert result.exit_code == 0
        assert "Living Entities" in result.output

    def test_quotes_command(self, runner: CliRunner) -> None:
        """quotes command should work."""
        result = runner.invoke(cli, ["quotes"])
        assert result.exit_code == 0
        assert "Twain Quotes" in result.output

    def test_interact_command(self, runner: CliRunner) -> None:
        """interact command should work."""
        result = runner.invoke(cli, ["interact", "hero-host-mark-twain"])
        assert result.exit_code == 0
        assert "Mark Twain" in result.output

    def test_interact_not_found(self, runner: CliRunner) -> None:
        """interact command should handle not found."""
        result = runner.invoke(cli, ["interact", "nonexistent"])
        assert result.exit_code == 0
        assert "not found" in result.output
