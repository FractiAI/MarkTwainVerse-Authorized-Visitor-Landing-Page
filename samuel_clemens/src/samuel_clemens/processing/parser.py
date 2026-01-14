"""
Parser - Generic and protocol-specific document parsing.

"The difference between the right word and the almost right word is the
difference between lightning and a lightning bug." — Mark Twain
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional, Iterator
from datetime import datetime

from samuel_clemens.processing.emoji import extract_emojis, EmojiInfo, analyze_emoji_usage
from samuel_clemens.processing.sections import (
    Section,
    MetadataBlock,
    TableData,
    Quote,
    extract_sections,
    extract_metadata,
    extract_tables,
    extract_quotes,
    extract_conclusion,
    extract_checkmarks,
    extract_protocol_references,
)


@dataclass
class ParsedDocument:
    """A parsed document with extracted structure."""
    filepath: Path
    filename: str
    content: str
    
    # Structure
    title: Optional[str] = None
    subtitle: Optional[str] = None
    sections: list[Section] = field(default_factory=list)
    tables: list[TableData] = field(default_factory=list)
    quotes: list[Quote] = field(default_factory=list)
    
    # Analysis
    emojis: list[EmojiInfo] = field(default_factory=list)
    word_count: int = 0
    line_count: int = 0
    
    # Parsing metadata
    parsed_at: datetime = field(default_factory=datetime.now)
    
    @property
    def has_tables(self) -> bool:
        return len(self.tables) > 0
    
    @property
    def has_quotes(self) -> bool:
        return len(self.quotes) > 0
    
    @property
    def emoji_count(self) -> int:
        return sum(e.count for e in self.emojis)
    
    def get_section(self, title: str) -> Optional[Section]:
        """Get section by title (case-insensitive partial match)."""
        title_lower = title.lower()
        for section in self.sections:
            if title_lower in section.title.lower():
                return section
            for sub in section.subsections:
                if title_lower in sub.title.lower():
                    return sub
        return None
    
    def get_all_text(self) -> str:
        """Get all text content."""
        return self.content


@dataclass
class ProtocolDocument(ParsedDocument):
    """A parsed NSPFRP protocol document with protocol-specific fields."""
    
    # Protocol metadata
    metadata: MetadataBlock = field(default_factory=MetadataBlock)
    protocol_number: Optional[int] = None
    protocol_id: Optional[str] = None  # e.g., "P92"
    category: Optional[str] = None
    status: Optional[str] = None
    discovery_date: Optional[str] = None
    protocol_type: Optional[str] = None
    
    # Protocol structure
    emergent_observation: Optional[Section] = None
    conclusion: Optional[Section] = None
    checkmarks: list[str] = field(default_factory=list)
    protocol_references: list[tuple[int, str]] = field(default_factory=list)
    
    # Footer
    footer_emojis: list[str] = field(default_factory=list)
    
    @property
    def is_operational(self) -> bool:
        """Check if protocol is marked operational."""
        if self.status:
            return "OPERATIONAL" in self.status.upper()
        return False
    
    @property
    def is_emergent(self) -> bool:
        """Check if protocol is emergent observation."""
        if self.status:
            return "EMERGENT" in self.status.upper()
        return False


def parse_file(filepath: Path | str) -> ParsedDocument:
    """
    Parse any text/markdown file.
    
    Args:
        filepath: Path to file
        
    Returns:
        ParsedDocument
    """
    filepath = Path(filepath)
    
    if not filepath.exists():
        raise FileNotFoundError(f"File not found: {filepath}")
    
    content = filepath.read_text(encoding="utf-8")
    
    # Basic parsing
    lines = content.split("\n")
    
    # Extract title (first H1)
    title = None
    subtitle = None
    for i, line in enumerate(lines):
        if line.startswith("# "):
            title = line[2:].strip()
            # Check for subtitle on next line
            if i + 1 < len(lines) and lines[i + 1].startswith("## "):
                subtitle = lines[i + 1][3:].strip()
            break
    
    # Extract structure
    sections = extract_sections(content)
    tables = extract_tables(content)
    quotes = extract_quotes(content)
    emojis = extract_emojis(content)
    
    # Count words
    word_count = len(re.findall(r"\w+", content))
    
    return ParsedDocument(
        filepath=filepath,
        filename=filepath.name,
        content=content,
        title=title,
        subtitle=subtitle,
        sections=sections,
        tables=tables,
        quotes=quotes,
        emojis=emojis,
        word_count=word_count,
        line_count=len(lines),
    )


def parse_protocol(filepath: Path | str) -> ProtocolDocument:
    """
    Parse an NSPFRP protocol file with protocol-specific extraction.
    
    Args:
        filepath: Path to protocol file
        
    Returns:
        ProtocolDocument with full protocol analysis
    """
    filepath = Path(filepath)
    
    if not filepath.exists():
        raise FileNotFoundError(f"File not found: {filepath}")
    
    content = filepath.read_text(encoding="utf-8")
    lines = content.split("\n")
    
    # Basic parsing
    title = None
    subtitle = None
    for i, line in enumerate(lines):
        if line.startswith("# "):
            title = line[2:].strip()
            if i + 1 < len(lines) and lines[i + 1].startswith("## "):
                subtitle = lines[i + 1][3:].strip()
            break
    
    # Extract protocol number from title
    protocol_number = None
    protocol_id = None
    if title:
        match = re.search(r"PROTOCOL\s+(\d+)", title, re.IGNORECASE)
        if match:
            protocol_number = int(match.group(1))
            protocol_id = f"P{protocol_number}"
    
    # Extract structure
    sections = extract_sections(content)
    tables = extract_tables(content)
    quotes = extract_quotes(content)
    emojis = extract_emojis(content)
    metadata = extract_metadata(content)
    conclusion = extract_conclusion(content)
    checkmarks = extract_checkmarks(content)
    protocol_refs = extract_protocol_references(content)
    
    # Find emergent observation section
    emergent = None
    for section in sections:
        if "EMERGENT" in section.title.upper():
            emergent = section
            break
    
    # Extract footer emojis (last non-empty line with only emojis)
    footer_emojis = []
    for line in reversed(lines):
        line = line.strip()
        if not line:
            continue
        # Check if line is mostly emojis
        emoji_analysis = analyze_emoji_usage(line)
        if emoji_analysis["emoji_density"] > 0.5:
            footer_emojis = [e.char for e in emoji_analysis["emojis"]]
        break
    
    # Word count
    word_count = len(re.findall(r"\w+", content))
    
    return ProtocolDocument(
        filepath=filepath,
        filename=filepath.name,
        content=content,
        title=title,
        subtitle=subtitle,
        sections=sections,
        tables=tables,
        quotes=quotes,
        emojis=emojis,
        word_count=word_count,
        line_count=len(lines),
        metadata=metadata,
        protocol_number=protocol_number,
        protocol_id=protocol_id,
        category=metadata.category,
        status=metadata.status,
        discovery_date=metadata.discovery_date,
        protocol_type=metadata.document_type,
        emergent_observation=emergent,
        conclusion=conclusion,
        checkmarks=checkmarks,
        protocol_references=protocol_refs,
        footer_emojis=footer_emojis,
    )


def parse_folder(
    folder_path: Path | str,
    pattern: str = "*.md",
    recursive: bool = False,
    as_protocols: bool = False,
) -> list[ParsedDocument | ProtocolDocument]:
    """
    Parse all matching files in a folder.
    
    Args:
        folder_path: Directory to scan
        pattern: Glob pattern for files (default: *.md)
        recursive: Search recursively
        as_protocols: Parse as protocol documents
        
    Returns:
        List of parsed documents
    """
    folder_path = Path(folder_path)
    
    if not folder_path.exists():
        raise FileNotFoundError(f"Folder not found: {folder_path}")
    
    if not folder_path.is_dir():
        raise ValueError(f"Not a directory: {folder_path}")
    
    # Find files
    if recursive:
        files = list(folder_path.rglob(pattern))
    else:
        files = list(folder_path.glob(pattern))
    
    # Sort by name
    files.sort()
    
    # Parse each file
    documents = []
    for filepath in files:
        try:
            if as_protocols:
                doc = parse_protocol(filepath)
            else:
                doc = parse_file(filepath)
            documents.append(doc)
        except Exception as e:
            print(f"Warning: Failed to parse {filepath}: {e}")
    
    return documents


def parse_protocols_by_prefix(
    folder_path: Path | str,
    prefixes: list[str] = None,
) -> list[ProtocolDocument]:
    """
    Parse protocol files matching common prefixes.
    
    Args:
        folder_path: Directory to scan
        prefixes: List of prefixes (default: NSPFRP_, PROTOCOL_, etc.)
        
    Returns:
        List of ProtocolDocument objects
    """
    if prefixes is None:
        prefixes = ["NSPFRP_", "PROTOCOL_", "P_", "NSP_"]
    
    folder_path = Path(folder_path)
    
    all_protocols = []
    for prefix in prefixes:
        pattern = f"{prefix}*.md"
        protocols = parse_folder(folder_path, pattern=pattern, as_protocols=True)
        all_protocols.extend(protocols)
    
    # Deduplicate by filepath
    seen = set()
    unique = []
    for doc in all_protocols:
        if doc.filepath not in seen:
            seen.add(doc.filepath)
            unique.append(doc)
    
    # Sort by protocol number
    unique.sort(key=lambda d: d.protocol_number or 0)
    
    return unique


def iter_protocol_files(folder_path: Path | str) -> Iterator[Path]:
    """
    Iterate over protocol files in a folder.
    
    Args:
        folder_path: Directory to scan
        
    Yields:
        Paths to protocol files
    """
    folder_path = Path(folder_path)
    
    prefixes = ["NSPFRP_", "PROTOCOL_", "P_", "NSP_"]
    
    for prefix in prefixes:
        for filepath in folder_path.glob(f"{prefix}*.md"):
            yield filepath
