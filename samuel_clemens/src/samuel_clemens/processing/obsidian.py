"""
Obsidian Export - Generate Obsidian-compatible markdown with [[wikilinks]].

"I have never let my schooling interfere with my education." — Mark Twain

Features:
- [[Wikilink]] style internal links
- Entity cross-referencing
- Backlink tracking
- Vault structure with folders
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional, Iterator
from datetime import datetime

from samuel_clemens.processing.parser import ParsedDocument, ProtocolDocument


@dataclass
class WikiLink:
    """Represents an Obsidian [[wikilink]]."""
    target: str  # Target page name
    display: Optional[str] = None  # Optional display text
    
    def __str__(self) -> str:
        if self.display:
            return f"[[{self.target}|{self.display}]]"
        return f"[[{self.target}]]"


@dataclass 
class ObsidianPage:
    """A page in the Obsidian vault."""
    filename: str
    title: str
    content: str
    frontmatter: dict = field(default_factory=dict)
    outgoing_links: list[WikiLink] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)
    
    def render(self) -> str:
        """Render page with YAML frontmatter."""
        lines = []
        
        # YAML frontmatter
        lines.append("---")
        lines.append(f"title: \"{self.title}\"")
        lines.append(f"created: {datetime.now().isoformat()}")
        
        if self.tags:
            lines.append(f"tags: [{', '.join(self.tags)}]")
        
        for key, value in self.frontmatter.items():
            if isinstance(value, list):
                lines.append(f"{key}: [{', '.join(str(v) for v in value)}]")
            else:
                lines.append(f"{key}: {value}")
        
        lines.append("---")
        lines.append("")
        lines.append(self.content)
        
        return "\n".join(lines)


@dataclass
class ObsidianVault:
    """An Obsidian vault structure."""
    name: str
    root_path: Path
    pages: dict[str, ObsidianPage] = field(default_factory=dict)
    
    def add_page(self, page: ObsidianPage, folder: str = "") -> None:
        """Add a page to the vault."""
        key = f"{folder}/{page.filename}" if folder else page.filename
        self.pages[key] = page
    
    def get_page(self, name: str) -> Optional[ObsidianPage]:
        """Get page by name."""
        return self.pages.get(name)
    
    def get_all_links(self) -> dict[str, list[str]]:
        """Get all links (target -> sources)."""
        backlinks: dict[str, list[str]] = {}
        
        for page_path, page in self.pages.items():
            for link in page.outgoing_links:
                target = link.target
                if target not in backlinks:
                    backlinks[target] = []
                backlinks[target].append(page_path)
        
        return backlinks
    
    def export(self) -> int:
        """Export vault to filesystem."""
        self.root_path.mkdir(parents=True, exist_ok=True)
        
        count = 0
        for page_path, page in self.pages.items():
            filepath = self.root_path / page_path
            filepath.parent.mkdir(parents=True, exist_ok=True)
            filepath.write_text(page.render(), encoding="utf-8")
            count += 1
        
        return count


def _slugify(text: str) -> str:
    """Convert text to valid filename."""
    # Remove special chars, replace spaces with underscores
    slug = re.sub(r"[^\w\s-]", "", text)
    slug = re.sub(r"\s+", "_", slug)
    return slug[:50]  # Limit length


def _extract_entities(text: str) -> list[str]:
    """Extract entity names from text for linking."""
    entities = []
    
    # Protocol references
    protocol_pattern = r"Protocol\s+(\d+)(?::\s*([^,\n]+))?"
    for match in re.finditer(protocol_pattern, text, re.IGNORECASE):
        num = match.group(1)
        name = match.group(2) if match.group(2) else f"Protocol_{num}"
        entities.append(f"Protocol_{num}")
    
    # Known entity types
    known_entities = [
        "Mark Twain", "Samuel Clemens",
        "Lewis & Clark", "Marco Polo", "John Muir",
        "Nikola Tesla", "Alexander von Humboldt",
        "NSPFRP", "HHF-AI MRI", "Syntheverse",
        "Hero Host", "Gold Nugget", "Expedition",
    ]
    
    for entity in known_entities:
        if entity.lower() in text.lower():
            entities.append(entity.replace(" ", "_"))
    
    return list(set(entities))


def _add_wikilinks(text: str, entities: list[str]) -> tuple[str, list[WikiLink]]:
    """Add [[wikilinks]] to text for known entities."""
    result = text
    links = []
    
    for entity in entities:
        # Convert entity back to readable form
        readable = entity.replace("_", " ")
        
        # Pattern to find entity (not already in wikilink)
        pattern = rf"(?<!\[\[)\b{re.escape(readable)}\b(?!\]\])"
        
        if re.search(pattern, result, re.IGNORECASE):
            # Replace first occurrence
            match = re.search(pattern, result, re.IGNORECASE)
            if match:
                original = match.group(0)
                result = result[:match.start()] + f"[[{entity}|{original}]]" + result[match.end():]
                links.append(WikiLink(target=entity, display=original))
    
    return result, links


def protocol_to_obsidian_page(
    protocol: ProtocolDocument,
    add_links: bool = True,
) -> ObsidianPage:
    """
    Convert a protocol document to an Obsidian page.
    
    Args:
        protocol: Protocol document
        add_links: Add [[wikilinks]] for entities
        
    Returns:
        ObsidianPage
    """
    # Build content
    lines = []
    
    # Title (already in frontmatter, but add for readability)
    lines.append(f"# {protocol.title}")
    if protocol.subtitle:
        lines.append(f"## {protocol.subtitle}")
    lines.append("")
    
    # Metadata callout
    lines.append("> [!info] Protocol Metadata")
    lines.append(f"> - **Number:** {protocol.protocol_id}")
    lines.append(f"> - **Category:** {protocol.category}")
    lines.append(f"> - **Status:** {protocol.status}")
    lines.append(f"> - **Date:** {protocol.discovery_date}")
    lines.append("")
    
    # Main content (simplified - first few sections)
    if protocol.emergent_observation:
        lines.append("## 🎯 Emergent Observation")
        lines.append("")
        lines.append(protocol.emergent_observation.content[:1000])
        lines.append("")
    
    # Checkmarks
    if protocol.checkmarks:
        lines.append("## ✅ Key Points")
        lines.append("")
        for check in protocol.checkmarks[:10]:
            lines.append(f"- ✅ {check}")
        lines.append("")
    
    # Protocol references as links
    if protocol.protocol_references:
        lines.append("## 🔗 Related Protocols")
        lines.append("")
        for num, desc in protocol.protocol_references:
            link = f"[[Protocol_{num}|Protocol {num}]]"
            if desc:
                lines.append(f"- {link}: {desc}")
            else:
                lines.append(f"- {link}")
        lines.append("")
    
    # Footer
    if protocol.footer_emojis:
        lines.append("")
        lines.append("---")
        lines.append("".join(protocol.footer_emojis))
    
    content = "\n".join(lines)
    
    # Add entity links
    outgoing_links = []
    if add_links:
        entities = _extract_entities(content)
        content, outgoing_links = _add_wikilinks(content, entities)
    
    # Build tags
    tags = ["protocol", "nspfrp"]
    if protocol.category:
        tags.append(_slugify(protocol.category.split("/")[0].strip()).lower())
    if protocol.is_operational:
        tags.append("operational")
    if protocol.is_emergent:
        tags.append("emergent")
    
    # Frontmatter
    frontmatter = {
        "protocol_number": protocol.protocol_number,
        "category": protocol.category,
        "status": protocol.status,
    }
    
    filename = f"Protocol_{protocol.protocol_number}.md" if protocol.protocol_number else f"{_slugify(protocol.title)}.md"
    
    return ObsidianPage(
        filename=filename,
        title=protocol.title or filename,
        content=content,
        frontmatter=frontmatter,
        outgoing_links=outgoing_links,
        tags=tags,
    )


def export_obsidian_vault(
    documents: list[ParsedDocument | ProtocolDocument],
    output_path: Path | str,
    vault_name: str = "MarkTwainVerse",
) -> ObsidianVault:
    """
    Export documents as an Obsidian vault.
    
    Args:
        documents: Documents to export
        output_path: Vault root path
        vault_name: Name of the vault
        
    Returns:
        ObsidianVault
    """
    output_path = Path(output_path)
    vault = ObsidianVault(name=vault_name, root_path=output_path)
    
    # Convert each document
    for doc in documents:
        if isinstance(doc, ProtocolDocument):
            page = protocol_to_obsidian_page(doc)
            vault.add_page(page, folder="Protocols")
        else:
            # Generic document
            content = f"# {doc.title or doc.filename}\n\n{doc.content[:2000]}"
            page = ObsidianPage(
                filename=f"{_slugify(doc.title or doc.filename)}.md",
                title=doc.title or doc.filename,
                content=content,
                tags=["document"],
            )
            vault.add_page(page, folder="Documents")
    
    # Create index pages
    _create_vault_index(vault, documents)
    
    # Export to filesystem
    vault.export()
    
    return vault


def _create_vault_index(vault: ObsidianVault, documents: list) -> None:
    """Create index pages for the vault."""
    
    # Main index
    lines = []
    lines.append("# MarkTwainVerse Knowledge Base")
    lines.append("")
    lines.append(f"**Generated:** {datetime.now().isoformat()}")
    lines.append(f"**Total Documents:** {len(documents)}")
    lines.append("")
    
    # Protocol section
    protocols = [d for d in documents if isinstance(d, ProtocolDocument)]
    if protocols:
        lines.append("## 📜 Protocols")
        lines.append("")
        for p in sorted(protocols, key=lambda x: x.protocol_number or 0):
            status = "✅" if p.is_operational else "⚠️"
            lines.append(f"- {status} [[Protocol_{p.protocol_number}|{p.title}]]")
        lines.append("")
    
    # Navigation
    lines.append("## 🗺️ Navigation")
    lines.append("")
    lines.append("- [[Protocol_Index|Protocol Index]]")
    lines.append("- [[Entity_Index|Entity Index]]")
    lines.append("- [[Tag_Index|Tags]]")
    
    vault.add_page(ObsidianPage(
        filename="README.md",
        title="MarkTwainVerse Knowledge Base",
        content="\n".join(lines),
        tags=["index"],
    ))
    
    # Protocol index
    if protocols:
        index_lines = ["# Protocol Index", ""]
        
        # Group by category
        by_category: dict[str, list] = {}
        for p in protocols:
            cat = p.category or "Uncategorized"
            if cat not in by_category:
                by_category[cat] = []
            by_category[cat].append(p)
        
        for cat, protos in sorted(by_category.items()):
            index_lines.append(f"## {cat}")
            index_lines.append("")
            for p in sorted(protos, key=lambda x: x.protocol_number or 0):
                index_lines.append(f"- [[Protocol_{p.protocol_number}]]")
            index_lines.append("")
        
        vault.add_page(ObsidianPage(
            filename="Protocol_Index.md",
            title="Protocol Index",
            content="\n".join(index_lines),
            tags=["index", "protocols"],
        ))
    
    # Entity index
    all_entities = set()
    for doc in documents:
        if isinstance(doc, ProtocolDocument):
            all_entities.update(_extract_entities(doc.content))
    
    entity_lines = ["# Entity Index", ""]
    for entity in sorted(all_entities):
        entity_lines.append(f"- [[{entity}]]")
    
    vault.add_page(ObsidianPage(
        filename="Entity_Index.md",
        title="Entity Index",
        content="\n".join(entity_lines),
        tags=["index", "entities"],
    ))


def create_entity_pages(
    vault: ObsidianVault,
    documents: list[ProtocolDocument],
) -> None:
    """
    Create stub pages for all referenced entities.
    
    Args:
        vault: Vault to add pages to
        documents: Source documents
    """
    # Collect all entities and their references
    entity_refs: dict[str, list[str]] = {}
    
    for doc in documents:
        if not isinstance(doc, ProtocolDocument):
            continue
        
        entities = _extract_entities(doc.content)
        for entity in entities:
            if entity not in entity_refs:
                entity_refs[entity] = []
            if doc.protocol_id:
                entity_refs[entity].append(doc.protocol_id)
    
    # Create pages
    for entity, refs in entity_refs.items():
        lines = [f"# {entity.replace('_', ' ')}", ""]
        
        lines.append("## Referenced In")
        lines.append("")
        for ref in set(refs):
            lines.append(f"- [[{ref}]]")
        
        vault.add_page(ObsidianPage(
            filename=f"{entity}.md",
            title=entity.replace("_", " "),
            content="\n".join(lines),
            tags=["entity"],
        ), folder="Entities")
