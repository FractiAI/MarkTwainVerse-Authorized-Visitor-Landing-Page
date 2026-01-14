"""
Processing Module - Parse and analyze protocol files and text documents.

"The man who does not read has no advantage over the man who cannot read."
— Mark Twain

This module provides:
- Generic and protocol-specific file parsing
- Emoji analysis and extraction
- Structured section extraction
- Markdown conversion and export
- Obsidian [[wikilink]] vault export
- PDF document generation
- Bulk folder processing
"""

from samuel_clemens.processing.parser import (
    ParsedDocument,
    ProtocolDocument,
    parse_file,
    parse_folder,
    parse_protocol,
    parse_protocols_by_prefix,
    iter_protocol_files,
)
from samuel_clemens.processing.emoji import (
    EmojiInfo,
    extract_emojis,
    analyze_emoji_usage,
    emoji_to_text,
    count_emojis,
    get_emoji_categories,
    replace_emojis_with_text,
    strip_emojis,
)
from samuel_clemens.processing.sections import (
    Section,
    TableData,
    MetadataBlock,
    Quote,
    extract_sections,
    extract_metadata,
    extract_tables,
    extract_quotes,
    extract_conclusion,
    extract_checkmarks,
    extract_protocol_references,
)
from samuel_clemens.processing.export import (
    export_to_markdown,
    export_to_json,
    export_folder_summary,
    export_emoji_report,
    export_structure_analysis,
    export_protocol_index,
)
from samuel_clemens.processing.obsidian import (
    WikiLink,
    ObsidianPage,
    ObsidianVault,
    protocol_to_obsidian_page,
    export_obsidian_vault,
    create_entity_pages,
)
from samuel_clemens.processing.pdf_export import (
    PDFConfig,
    export_document_to_pdf,
    export_protocols_to_pdf,
    export_summary_pdf,
    export_story_to_pdf,
    export_anthology_to_pdf,
)

__all__ = [
    # Parser
    "ParsedDocument",
    "ProtocolDocument",
    "parse_file",
    "parse_folder",
    "parse_protocol",
    "parse_protocols_by_prefix",
    "iter_protocol_files",
    # Emoji
    "EmojiInfo",
    "extract_emojis",
    "analyze_emoji_usage",
    "emoji_to_text",
    "count_emojis",
    "get_emoji_categories",
    "replace_emojis_with_text",
    "strip_emojis",
    # Sections
    "Section",
    "TableData",
    "MetadataBlock",
    "Quote",
    "extract_sections",
    "extract_metadata",
    "extract_tables",
    "extract_quotes",
    "extract_conclusion",
    "extract_checkmarks",
    "extract_protocol_references",
    # Export
    "export_to_markdown",
    "export_to_json",
    "export_folder_summary",
    "export_emoji_report",
    "export_structure_analysis",
    "export_protocol_index",
    # Obsidian
    "WikiLink",
    "ObsidianPage",
    "ObsidianVault",
    "protocol_to_obsidian_page",
    "export_obsidian_vault",
    "create_entity_pages",
    # PDF
    "PDFConfig",
    "export_document_to_pdf",
    "export_protocols_to_pdf",
    "export_summary_pdf",
    "export_story_to_pdf",
    "export_anthology_to_pdf",
]


