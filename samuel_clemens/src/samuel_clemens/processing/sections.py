"""
Section Extraction - Parse structured sections from protocol documents.

"Get your facts first, then you can distort them as you please."
— Mark Twain
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Optional, Any


@dataclass
class Section:
    """Represents a section in a document."""
    title: str
    level: int  # 1 for H1, 2 for H2, etc.
    content: str
    start_line: int
    end_line: int
    emoji: Optional[str] = None
    subsections: list["Section"] = field(default_factory=list)
    
    @property
    def plain_title(self) -> str:
        """Title without emoji prefix."""
        # Remove emoji prefix if present
        if self.emoji and self.title.startswith(self.emoji):
            return self.title[len(self.emoji):].strip()
        return self.title
    
    def get_text(self) -> str:
        """Get full section text including subsections."""
        return self.content


@dataclass
class TableData:
    """Represents a parsed markdown table."""
    headers: list[str]
    rows: list[list[str]]
    start_line: int
    end_line: int
    
    @property
    def num_columns(self) -> int:
        return len(self.headers)
    
    @property
    def num_rows(self) -> int:
        return len(self.rows)


@dataclass
class MetadataBlock:
    """Protocol metadata extracted from header."""
    protocol_number: Optional[str] = None
    category: Optional[str] = None
    status: Optional[str] = None
    discovery_date: Optional[str] = None
    document_type: Optional[str] = None
    raw_fields: dict[str, str] = field(default_factory=dict)
    
    @classmethod
    def from_text(cls, text: str) -> "MetadataBlock":
        """Parse metadata from text block."""
        metadata = cls()
        
        # Pattern for **Field:** Value or **Field:** Value
        pattern = r"\*\*([^:*]+):\*\*\s*(.+)"
        
        for match in re.finditer(pattern, text):
            field_name = match.group(1).strip().lower()
            value = match.group(2).strip()
            
            metadata.raw_fields[match.group(1).strip()] = value
            
            if "protocol" in field_name and "number" in field_name:
                metadata.protocol_number = value
            elif "category" in field_name:
                metadata.category = value
            elif "status" in field_name:
                metadata.status = value
            elif "date" in field_name:
                metadata.discovery_date = value
            elif "type" in field_name:
                metadata.document_type = value
        
        return metadata


@dataclass
class Quote:
    """Represents a blockquote."""
    text: str
    attribution: Optional[str] = None
    line_number: int = 0


def extract_sections(text: str) -> list[Section]:
    """
    Extract all sections from markdown text.
    
    Args:
        text: Markdown text
        
    Returns:
        List of Section objects (hierarchical)
    """
    lines = text.split("\n")
    sections: list[Section] = []
    current_sections: dict[int, Section] = {}  # level -> current section
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Check for heading
        heading_match = re.match(r"^(#{1,6})\s+(.+)$", line)
        
        if heading_match:
            level = len(heading_match.group(1))
            title = heading_match.group(2).strip()
            
            # Extract emoji if present
            emoji = None
            emoji_match = re.match(r"^([^\w\s])\s*(.+)$", title)
            if emoji_match:
                potential_emoji = emoji_match.group(1)
                # Check if it's an emoji (simplified check)
                if ord(potential_emoji[0]) > 127:
                    emoji = potential_emoji
            
            # Find section content (until next heading of same or higher level)
            content_lines = []
            j = i + 1
            while j < len(lines):
                next_line = lines[j]
                next_heading = re.match(r"^(#{1,6})\s+", next_line)
                if next_heading and len(next_heading.group(1)) <= level:
                    break
                content_lines.append(next_line)
                j += 1
            
            section = Section(
                title=title,
                level=level,
                content="\n".join(content_lines),
                start_line=i + 1,  # 1-indexed
                end_line=j,
                emoji=emoji,
            )
            
            # Add to hierarchy
            if level == 1:
                sections.append(section)
            else:
                # Find parent section
                for parent_level in range(level - 1, 0, -1):
                    if parent_level in current_sections:
                        current_sections[parent_level].subsections.append(section)
                        break
                else:
                    # No parent found, add as top-level
                    sections.append(section)
            
            current_sections[level] = section
            i = j
        else:
            i += 1
    
    return sections


def extract_metadata(text: str) -> MetadataBlock:
    """
    Extract metadata block from protocol document.
    
    Args:
        text: Document text
        
    Returns:
        MetadataBlock with extracted fields
    """
    lines = text.split("\n")
    
    # Find metadata section (typically after title, before first major section)
    metadata_text = ""
    in_metadata = False
    
    for i, line in enumerate(lines):
        # Skip title
        if line.startswith("# "):
            in_metadata = True
            continue
        
        # Stop at first section or horizontal rule preceded by blank line
        if in_metadata:
            if line.startswith("## "):
                break
            if line.strip() == "---" and i > 0 and lines[i-1].strip() == "":
                break
            metadata_text += line + "\n"
    
    return MetadataBlock.from_text(metadata_text)


def extract_tables(text: str) -> list[TableData]:
    """
    Extract all tables from markdown text.
    
    Args:
        text: Markdown text
        
    Returns:
        List of TableData objects
    """
    tables = []
    lines = text.split("\n")
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Check for table header (contains |)
        if "|" in line and i + 1 < len(lines) and re.match(r"^\|[-:\s|]+\|$", lines[i + 1].strip()):
            # Found table
            start_line = i
            
            # Parse header
            headers = [cell.strip() for cell in line.split("|") if cell.strip()]
            
            # Skip separator
            i += 2
            
            # Parse rows
            rows = []
            while i < len(lines) and "|" in lines[i]:
                row = [cell.strip() for cell in lines[i].split("|") if cell.strip()]
                if row:
                    rows.append(row)
                i += 1
            
            tables.append(TableData(
                headers=headers,
                rows=rows,
                start_line=start_line + 1,
                end_line=i,
            ))
        else:
            i += 1
    
    return tables


def extract_quotes(text: str) -> list[Quote]:
    """
    Extract all blockquotes from markdown text.
    
    Args:
        text: Markdown text
        
    Returns:
        List of Quote objects
    """
    quotes = []
    lines = text.split("\n")
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        if line.startswith(">"):
            # Found quote
            quote_lines = []
            start_line = i
            
            while i < len(lines) and (lines[i].startswith(">") or lines[i].strip() == ""):
                content = lines[i].lstrip("> ").strip()
                if content:
                    quote_lines.append(content)
                i += 1
                if lines[i - 1].strip() == "" and i < len(lines) and not lines[i].startswith(">"):
                    break
            
            quote_text = " ".join(quote_lines)
            
            # Check for attribution
            attribution = None
            attr_match = re.search(r"[-—]\s*(.+)$", quote_text)
            if attr_match:
                attribution = attr_match.group(1).strip()
                quote_text = quote_text[:attr_match.start()].strip()
            
            quotes.append(Quote(
                text=quote_text,
                attribution=attribution,
                line_number=start_line + 1,
            ))
        else:
            i += 1
    
    return quotes


def extract_conclusion(text: str) -> Optional[Section]:
    """
    Extract conclusion section from protocol document.
    
    Args:
        text: Document text
        
    Returns:
        Conclusion Section if found
    """
    sections = extract_sections(text)
    
    for section in sections:
        if "CONCLUSION" in section.title.upper():
            return section
        
        # Check subsections
        for sub in section.subsections:
            if "CONCLUSION" in sub.title.upper():
                return sub
    
    return None


def extract_checkmarks(text: str) -> list[str]:
    """
    Extract all checkmark items from text.
    
    Args:
        text: Document text
        
    Returns:
        List of items with checkmarks
    """
    pattern = r"[✅✓☑]\s*\*?\*?([^*\n]+)"
    matches = re.findall(pattern, text)
    return [m.strip() for m in matches]


def extract_protocol_references(text: str) -> list[tuple[int, str]]:
    """
    Extract references to other protocols.
    
    Args:
        text: Document text
        
    Returns:
        List of (protocol_number, description) tuples
    """
    references = []
    
    # Pattern: Protocol XX: Description or PROTOCOL XX or P+number
    patterns = [
        r"Protocol\s+(\d+):\s*([^\n]+)",
        r"PROTOCOL\s+(\d+):\s*([^\n]+)",
        r"Protocol\s+(\d+)",
        r"P(\d+)",
    ]
    
    for pattern in patterns:
        for match in re.finditer(pattern, text, re.IGNORECASE):
            num = int(match.group(1))
            desc = match.group(2).strip() if len(match.groups()) > 1 else ""
            references.append((num, desc))
    
    # Deduplicate
    seen = set()
    unique = []
    for num, desc in references:
        if num not in seen:
            seen.add(num)
            unique.append((num, desc))
    
    return sorted(unique, key=lambda x: x[0])


def get_section_by_emoji(sections: list[Section], emoji: str) -> Optional[Section]:
    """
    Find a section by its emoji prefix.
    
    Args:
        sections: List of sections
        emoji: Emoji to search for
        
    Returns:
        Section if found
    """
    for section in sections:
        if section.emoji == emoji:
            return section
        for sub in section.subsections:
            if sub.emoji == emoji:
                return sub
    return None


def get_all_section_titles(sections: list[Section]) -> list[str]:
    """
    Get all section titles (flattened).
    
    Args:
        sections: List of sections
        
    Returns:
        List of all titles
    """
    titles = []
    for section in sections:
        titles.append(section.title)
        for sub in section.subsections:
            titles.append(sub.title)
    return titles
