"""
Export - Convert parsed documents to various formats.

"I haven't any right to criticize books, and I don't do it except
when I hate them." — Mark Twain
"""

from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path
from typing import Optional, Any
from datetime import datetime

from samuel_clemens.processing.parser import ParsedDocument, ProtocolDocument
from samuel_clemens.processing.emoji import EmojiInfo, analyze_emoji_usage


def _serialize_for_json(obj: Any) -> Any:
    """Make objects JSON serializable."""
    if isinstance(obj, Path):
        return str(obj)
    if isinstance(obj, datetime):
        return obj.isoformat()
    if hasattr(obj, "__dict__"):
        return {k: _serialize_for_json(v) for k, v in obj.__dict__.items()}
    if isinstance(obj, list):
        return [_serialize_for_json(i) for i in obj]
    if isinstance(obj, dict):
        return {k: _serialize_for_json(v) for k, v in obj.items()}
    return obj


def export_to_markdown(
    doc: ParsedDocument | ProtocolDocument,
    output_path: Path | str,
    include_analysis: bool = True,
) -> Path:
    """
    Export parsed document to markdown with analysis.
    
    Args:
        doc: Parsed document
        output_path: Output file path
        include_analysis: Include analysis section
        
    Returns:
        Path to created file
    """
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    lines = []
    
    # Header
    lines.append(f"# {doc.title or doc.filename}")
    if doc.subtitle:
        lines.append(f"## {doc.subtitle}")
    lines.append("")
    
    # Metadata (for protocols)
    if isinstance(doc, ProtocolDocument):
        lines.append("## 📋 Protocol Metadata")
        lines.append("")
        lines.append(f"- **Protocol ID:** {doc.protocol_id}")
        lines.append(f"- **Category:** {doc.category}")
        lines.append(f"- **Status:** {doc.status}")
        lines.append(f"- **Discovery Date:** {doc.discovery_date}")
        lines.append(f"- **Type:** {doc.protocol_type}")
        lines.append("")
    
    # Analysis section
    if include_analysis:
        lines.append("## 📊 Document Analysis")
        lines.append("")
        lines.append(f"- **File:** `{doc.filename}`")
        lines.append(f"- **Words:** {doc.word_count:,}")
        lines.append(f"- **Lines:** {doc.line_count:,}")
        lines.append(f"- **Sections:** {len(doc.sections)}")
        lines.append(f"- **Tables:** {len(doc.tables)}")
        lines.append(f"- **Quotes:** {len(doc.quotes)}")
        lines.append(f"- **Emojis:** {doc.emoji_count}")
        lines.append("")
        
        if doc.emojis:
            lines.append("### Emoji Usage")
            lines.append("")
            for emoji in sorted(doc.emojis, key=lambda e: -e.count)[:10]:
                lines.append(f"- {emoji.char} ({emoji.name}): {emoji.count}×")
            lines.append("")
    
    # Sections outline
    lines.append("## 📑 Document Structure")
    lines.append("")
    for section in doc.sections:
        prefix = "#" * section.level
        lines.append(f"- {prefix} {section.title}")
        for sub in section.subsections:
            subprefix = "#" * sub.level
            lines.append(f"  - {subprefix} {sub.title}")
    lines.append("")
    
    # Protocol-specific sections
    if isinstance(doc, ProtocolDocument):
        if doc.emergent_observation:
            lines.append("## 🎯 Emergent Observation")
            lines.append("")
            lines.append(doc.emergent_observation.content[:500])
            if len(doc.emergent_observation.content) > 500:
                lines.append("...")
            lines.append("")
        
        if doc.checkmarks:
            lines.append("## ✅ Checkmarks")
            lines.append("")
            for item in doc.checkmarks[:10]:
                lines.append(f"- ✅ {item}")
            if len(doc.checkmarks) > 10:
                lines.append(f"- ... and {len(doc.checkmarks) - 10} more")
            lines.append("")
        
        if doc.protocol_references:
            lines.append("## 🔗 Protocol References")
            lines.append("")
            for num, desc in doc.protocol_references:
                lines.append(f"- Protocol {num}: {desc}" if desc else f"- Protocol {num}")
            lines.append("")
        
        if doc.footer_emojis:
            lines.append(f"**Footer:** {''.join(doc.footer_emojis)}")
            lines.append("")
    
    # Write
    content = "\n".join(lines)
    output_path.write_text(content, encoding="utf-8")
    
    return output_path


def export_to_json(
    doc: ParsedDocument | ProtocolDocument,
    output_path: Path | str,
    pretty: bool = True,
) -> Path:
    """
    Export parsed document to JSON.
    
    Args:
        doc: Parsed document
        output_path: Output file path
        pretty: Pretty-print JSON
        
    Returns:
        Path to created file
    """
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Build data dict
    data = {
        "filename": doc.filename,
        "filepath": str(doc.filepath),
        "title": doc.title,
        "subtitle": doc.subtitle,
        "word_count": doc.word_count,
        "line_count": doc.line_count,
        "emoji_count": doc.emoji_count,
        "parsed_at": doc.parsed_at.isoformat(),
        "sections": [
            {
                "title": s.title,
                "level": s.level,
                "emoji": s.emoji,
                "start_line": s.start_line,
                "end_line": s.end_line,
                "subsection_count": len(s.subsections),
            }
            for s in doc.sections
        ],
        "tables": [
            {
                "headers": t.headers,
                "row_count": t.num_rows,
                "start_line": t.start_line,
            }
            for t in doc.tables
        ],
        "quotes": [
            {
                "text": q.text[:200],
                "attribution": q.attribution,
            }
            for q in doc.quotes
        ],
        "emojis": [
            {
                "char": e.char,
                "name": e.name,
                "category": e.category,
                "count": e.count,
            }
            for e in doc.emojis
        ],
    }
    
    # Add protocol-specific fields
    if isinstance(doc, ProtocolDocument):
        data["protocol"] = {
            "number": doc.protocol_number,
            "id": doc.protocol_id,
            "category": doc.category,
            "status": doc.status,
            "discovery_date": doc.discovery_date,
            "type": doc.protocol_type,
            "is_operational": doc.is_operational,
            "is_emergent": doc.is_emergent,
            "checkmarks": doc.checkmarks,
            "references": [{"number": n, "description": d} for n, d in doc.protocol_references],
            "footer_emojis": doc.footer_emojis,
        }
    
    # Write
    indent = 2 if pretty else None
    output_path.write_text(json.dumps(data, indent=indent, ensure_ascii=False), encoding="utf-8")
    
    return output_path


def export_folder_summary(
    documents: list[ParsedDocument | ProtocolDocument],
    output_path: Path | str,
    format: str = "markdown",
) -> Path:
    """
    Export summary of all documents in a folder.
    
    Args:
        documents: List of parsed documents
        output_path: Output file path
        format: 'markdown' or 'json'
        
    Returns:
        Path to created file
    """
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    if format == "json":
        data = {
            "total_documents": len(documents),
            "total_words": sum(d.word_count for d in documents),
            "total_lines": sum(d.line_count for d in documents),
            "total_emojis": sum(d.emoji_count for d in documents),
            "documents": [
                {
                    "filename": d.filename,
                    "title": d.title,
                    "word_count": d.word_count,
                    "emoji_count": d.emoji_count,
                    "protocol_number": d.protocol_number if isinstance(d, ProtocolDocument) else None,
                }
                for d in documents
            ],
        }
        output_path.write_text(json.dumps(data, indent=2, ensure_ascii=False))
    else:
        lines = []
        lines.append("# Document Summary")
        lines.append("")
        lines.append(f"**Generated:** {datetime.now().isoformat()}")
        lines.append(f"**Total Documents:** {len(documents)}")
        lines.append(f"**Total Words:** {sum(d.word_count for d in documents):,}")
        lines.append(f"**Total Emojis:** {sum(d.emoji_count for d in documents):,}")
        lines.append("")
        
        # Table
        lines.append("| # | File | Title | Words | Emojis |")
        lines.append("|---|------|-------|-------|--------|")
        
        for i, doc in enumerate(documents, 1):
            title = (doc.title or "")[:40]
            lines.append(f"| {i} | `{doc.filename}` | {title} | {doc.word_count:,} | {doc.emoji_count} |")
        
        lines.append("")
        output_path.write_text("\n".join(lines), encoding="utf-8")
    
    return output_path


def export_emoji_report(
    documents: list[ParsedDocument | ProtocolDocument],
    output_path: Path | str,
) -> Path:
    """
    Export emoji usage report across all documents.
    
    Args:
        documents: List of parsed documents
        output_path: Output file path
        
    Returns:
        Path to created file
    """
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Aggregate emoji data
    emoji_totals: dict[str, dict] = {}
    
    for doc in documents:
        for emoji in doc.emojis:
            if emoji.char not in emoji_totals:
                emoji_totals[emoji.char] = {
                    "name": emoji.name,
                    "category": emoji.category,
                    "count": 0,
                    "documents": [],
                }
            emoji_totals[emoji.char]["count"] += emoji.count
            emoji_totals[emoji.char]["documents"].append(doc.filename)
    
    # Sort by count
    sorted_emojis = sorted(emoji_totals.items(), key=lambda x: -x[1]["count"])
    
    lines = []
    lines.append("# Emoji Usage Report")
    lines.append("")
    lines.append(f"**Generated:** {datetime.now().isoformat()}")
    lines.append(f"**Documents Analyzed:** {len(documents)}")
    lines.append(f"**Unique Emojis:** {len(emoji_totals)}")
    lines.append(f"**Total Emoji Uses:** {sum(e['count'] for e in emoji_totals.values()):,}")
    lines.append("")
    
    # Table
    lines.append("## Emoji Frequency")
    lines.append("")
    lines.append("| Emoji | Name | Category | Count | Documents |")
    lines.append("|-------|------|----------|-------|-----------|")
    
    for emoji_char, data in sorted_emojis[:50]:
        doc_count = len(set(data["documents"]))
        lines.append(f"| {emoji_char} | {data['name']} | {data['category']} | {data['count']} | {doc_count} |")
    
    lines.append("")
    
    # Category breakdown
    lines.append("## By Category")
    lines.append("")
    
    category_counts: dict[str, int] = {}
    for data in emoji_totals.values():
        cat = data["category"]
        category_counts[cat] = category_counts.get(cat, 0) + data["count"]
    
    for cat, count in sorted(category_counts.items(), key=lambda x: -x[1]):
        lines.append(f"- **{cat}:** {count:,}")
    
    lines.append("")
    output_path.write_text("\n".join(lines), encoding="utf-8")
    
    return output_path


def export_structure_analysis(
    documents: list[ParsedDocument | ProtocolDocument],
    output_path: Path | str,
) -> Path:
    """
    Export document structure analysis.
    
    Args:
        documents: List of parsed documents
        output_path: Output file path
        
    Returns:
        Path to created file
    """
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    lines = []
    lines.append("# Document Structure Analysis")
    lines.append("")
    lines.append(f"**Generated:** {datetime.now().isoformat()}")
    lines.append(f"**Documents:** {len(documents)}")
    lines.append("")
    
    # Common section patterns
    all_sections: dict[str, int] = {}
    for doc in documents:
        for section in doc.sections:
            # Normalize title
            title = section.plain_title.upper()
            all_sections[title] = all_sections.get(title, 0) + 1
    
    lines.append("## Common Section Titles")
    lines.append("")
    for title, count in sorted(all_sections.items(), key=lambda x: -x[1])[:20]:
        lines.append(f"- **{title}**: {count} documents")
    lines.append("")
    
    # Protocol-specific analysis
    protocol_docs = [d for d in documents if isinstance(d, ProtocolDocument)]
    if protocol_docs:
        lines.append("## Protocol Analysis")
        lines.append("")
        lines.append(f"**Total Protocols:** {len(protocol_docs)}")
        lines.append(f"**Operational:** {sum(1 for d in protocol_docs if d.is_operational)}")
        lines.append(f"**Emergent:** {sum(1 for d in protocol_docs if d.is_emergent)}")
        lines.append("")
        
        # Protocol numbers
        protocol_numbers = [d.protocol_number for d in protocol_docs if d.protocol_number]
        if protocol_numbers:
            lines.append(f"**Protocol Range:** P{min(protocol_numbers)} - P{max(protocol_numbers)}")
            
            # Find gaps
            all_nums = set(range(min(protocol_numbers), max(protocol_numbers) + 1))
            missing = sorted(all_nums - set(protocol_numbers))
            if missing:
                lines.append(f"**Missing Numbers:** {', '.join(str(n) for n in missing[:10])}")
                if len(missing) > 10:
                    lines.append(f"  ... and {len(missing) - 10} more")
        lines.append("")
        
        # Cross-references
        lines.append("## Protocol Cross-References")
        lines.append("")
        for doc in protocol_docs[:10]:
            if doc.protocol_references:
                refs = ", ".join(f"P{n}" for n, _ in doc.protocol_references[:5])
                lines.append(f"- **{doc.protocol_id}** references: {refs}")
        lines.append("")
    
    output_path.write_text("\n".join(lines), encoding="utf-8")
    
    return output_path


def export_protocol_index(
    protocols: list[ProtocolDocument],
    output_path: Path | str,
) -> Path:
    """
    Export a protocol index with links and metadata.
    
    Args:
        protocols: List of protocol documents
        output_path: Output file path
        
    Returns:
        Path to created file
    """
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Sort by protocol number
    protocols = sorted(protocols, key=lambda p: p.protocol_number or 0)
    
    lines = []
    lines.append("# Protocol Index")
    lines.append("")
    lines.append(f"**Generated:** {datetime.now().isoformat()}")
    lines.append(f"**Total Protocols:** {len(protocols)}")
    lines.append("")
    
    # Group by category
    categories: dict[str, list] = {}
    for p in protocols:
        cat = p.category or "Uncategorized"
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(p)
    
    lines.append("## By Category")
    lines.append("")
    for cat in sorted(categories.keys()):
        lines.append(f"### {cat}")
        lines.append("")
        for p in categories[cat]:
            status_emoji = "✅" if p.is_operational else "⚠️"
            lines.append(f"- {status_emoji} **{p.protocol_id}**: {p.title}")
        lines.append("")
    
    # Full table
    lines.append("## Full Index")
    lines.append("")
    lines.append("| P# | Title | Category | Status |")
    lines.append("|---|-------|----------|--------|")
    
    for p in protocols:
        status = "✅" if p.is_operational else "⚠️"
        title = (p.title or "")[:50]
        lines.append(f"| {p.protocol_number} | {title} | {p.category or '-'} | {status} |")
    
    lines.append("")
    output_path.write_text("\n".join(lines), encoding="utf-8")
    
    return output_path
