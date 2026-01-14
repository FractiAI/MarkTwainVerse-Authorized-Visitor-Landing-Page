"""
PDF Export - Generate PDF documents from parsed content.

"Always do right. This will gratify some people and astonish the rest."
— Mark Twain

Features:
- Story export to PDF
- Protocol documentation PDFs
- Visualization PDFs with embedded charts
- Report compilation
"""

from __future__ import annotations

import io
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Any
from datetime import datetime

try:
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.platypus import (
        SimpleDocTemplate,
        Paragraph,
        Spacer,
        PageBreak,
        Table,
        TableStyle,
        Image,
        ListFlowable,
        ListItem,
    )
    from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
    HAS_REPORTLAB = True
except ImportError:
    HAS_REPORTLAB = False
    letter = (612.0, 792.0)
    A4 = (595.27, 841.89)

from samuel_clemens.processing.parser import ParsedDocument, ProtocolDocument


@dataclass
class PDFConfig:
    """Configuration for PDF export."""
    page_size: tuple = letter
    margin_left: float = 1.0  # inches
    margin_right: float = 1.0
    margin_top: float = 1.0
    margin_bottom: float = 1.0
    title_font: str = "Helvetica-Bold"
    body_font: str = "Helvetica"
    title_size: int = 24
    heading_size: int = 16
    body_size: int = 11
    include_toc: bool = True
    include_header: bool = True
    include_footer: bool = True


def _check_reportlab():
    """Check if reportlab is available."""
    if not HAS_REPORTLAB:
        raise ImportError(
            "reportlab is required for PDF export. "
            "Install with: pip install reportlab"
        )


def _get_styles(config: PDFConfig) -> dict:
    """Get paragraph styles for PDF."""
    styles = getSampleStyleSheet()
    
    # Custom styles
    styles.add(ParagraphStyle(
        name='CustomTitle',
        parent=styles['Title'],
        fontSize=config.title_size,
        spaceAfter=20,
        alignment=TA_CENTER,
    ))
    
    styles.add(ParagraphStyle(
        name='CustomHeading',
        parent=styles['Heading1'],
        fontSize=config.heading_size,
        spaceAfter=12,
        spaceBefore=16,
    ))
    
    styles.add(ParagraphStyle(
        name='CustomBody',
        parent=styles['Normal'],
        fontSize=config.body_size,
        alignment=TA_JUSTIFY,
        spaceAfter=8,
    ))
    
    styles.add(ParagraphStyle(
        name='Metadata',
        parent=styles['Normal'],
        fontSize=9,
        textColor=colors.grey,
        spaceAfter=4,
    ))
    
    styles.add(ParagraphStyle(
        name='Quote',
        parent=styles['Normal'],
        fontSize=config.body_size,
        leftIndent=20,
        rightIndent=20,
        fontName='Helvetica-Oblique',
        textColor=colors.darkgrey,
        spaceAfter=12,
    ))
    
    return styles


def _clean_text(text: str) -> str:
    """Clean text for PDF rendering."""
    # Remove or replace problematic characters
    replacements = {
        '✅': '[OK]',
        '❌': '[X]',
        '⚠️': '[!]',
        '🚨': '[!]',
        '🎯': '*',
        '📊': '',
        '🌟': '*',
        '✨': '*',
        '🔄': '',
        '🔗': '',
        '🏗️': '',
        '💎': '*',
        '📝': '',
        '📖': '',
        '📚': '',
        '🚀': '',
        '🌐': '',
        '🎬': '',
        '🎩': '',
        '⭐': '*',
        '💡': '',
        '🔘': 'o',
        '—': '-',
        '–': '-',
        '"': '"',
        '"': '"',
        ''': "'",
        ''': "'",
    }
    
    for old, new in replacements.items():
        text = text.replace(old, new)
    
    # Escape XML special chars
    text = text.replace('&', '&amp;')
    text = text.replace('<', '&lt;')
    text = text.replace('>', '&gt;')
    
    return text


def _markdown_to_paragraphs(text: str, styles: dict) -> list:
    """Convert markdown text to PDF paragraphs."""
    elements = []
    current_style = styles['CustomBody']
    
    lines = text.split('\n')
    buffer = []
    
    for line in lines:
        line = line.strip()
        
        if not line:
            if buffer:
                para_text = ' '.join(buffer)
                elements.append(Paragraph(_clean_text(para_text), current_style))
                buffer = []
            elements.append(Spacer(1, 6))
            continue
        
        # Headers
        if line.startswith('# '):
            if buffer:
                elements.append(Paragraph(_clean_text(' '.join(buffer)), current_style))
                buffer = []
            elements.append(Paragraph(_clean_text(line[2:]), styles['CustomTitle']))
            continue
        
        if line.startswith('## '):
            if buffer:
                elements.append(Paragraph(_clean_text(' '.join(buffer)), current_style))
                buffer = []
            elements.append(Paragraph(_clean_text(line[3:]), styles['CustomHeading']))
            continue
        
        if line.startswith('### '):
            if buffer:
                elements.append(Paragraph(_clean_text(' '.join(buffer)), current_style))
                buffer = []
            elements.append(Paragraph(f"<b>{_clean_text(line[4:])}</b>", styles['CustomBody']))
            continue
        
        # Blockquotes
        if line.startswith('>'):
            if buffer:
                elements.append(Paragraph(_clean_text(' '.join(buffer)), current_style))
                buffer = []
            quote_text = line.lstrip('> ')
            elements.append(Paragraph(_clean_text(quote_text), styles['Quote']))
            continue
        
        # List items
        if line.startswith('- ') or line.startswith('* '):
            if buffer:
                elements.append(Paragraph(_clean_text(' '.join(buffer)), current_style))
                buffer = []
            bullet_text = line[2:]
            elements.append(Paragraph(f"• {_clean_text(bullet_text)}", styles['CustomBody']))
            continue
        
        # Regular text
        buffer.append(line)
    
    if buffer:
        elements.append(Paragraph(_clean_text(' '.join(buffer)), current_style))
    
    return elements


def export_document_to_pdf(
    doc: ParsedDocument | ProtocolDocument,
    output_path: Path | str,
    config: Optional[PDFConfig] = None,
) -> Path:
    """
    Export a document to PDF.
    
    Args:
        doc: Document to export
        output_path: Output file path
        config: PDF configuration
        
    Returns:
        Path to created PDF
    """
    _check_reportlab()
    
    config = config or PDFConfig()
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    styles = _get_styles(config)
    
    # Create document
    pdf = SimpleDocTemplate(
        str(output_path),
        pagesize=config.page_size,
        leftMargin=config.margin_left * inch,
        rightMargin=config.margin_right * inch,
        topMargin=config.margin_top * inch,
        bottomMargin=config.margin_bottom * inch,
    )
    
    elements = []
    
    # Title
    title = doc.title or doc.filename
    elements.append(Paragraph(_clean_text(title), styles['CustomTitle']))
    
    if doc.subtitle:
        elements.append(Paragraph(_clean_text(doc.subtitle), styles['Heading2']))
    
    elements.append(Spacer(1, 20))
    
    # Protocol metadata
    if isinstance(doc, ProtocolDocument):
        meta_lines = [
            f"Protocol: {doc.protocol_id}",
            f"Category: {doc.category}",
            f"Status: {_clean_text(doc.status or 'N/A')}",
            f"Date: {doc.discovery_date}",
        ]
        for line in meta_lines:
            elements.append(Paragraph(line, styles['Metadata']))
        elements.append(Spacer(1, 20))
    
    # Content
    content_elements = _markdown_to_paragraphs(doc.content, styles)
    elements.extend(content_elements)
    
    # Footer
    elements.append(Spacer(1, 30))
    elements.append(Paragraph(
        f"Generated by Samuel Clemens | {datetime.now().strftime('%Y-%m-%d')}",
        styles['Metadata']
    ))
    
    # Build PDF
    pdf.build(elements)
    
    return output_path


def export_protocols_to_pdf(
    protocols: list[ProtocolDocument],
    output_path: Path | str,
    config: Optional[PDFConfig] = None,
) -> Path:
    """
    Export multiple protocols to a single PDF.
    
    Args:
        protocols: Protocols to export
        output_path: Output file path
        config: PDF configuration
        
    Returns:
        Path to created PDF
    """
    _check_reportlab()
    
    config = config or PDFConfig()
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    styles = _get_styles(config)
    
    pdf = SimpleDocTemplate(
        str(output_path),
        pagesize=config.page_size,
        leftMargin=config.margin_left * inch,
        rightMargin=config.margin_right * inch,
        topMargin=config.margin_top * inch,
        bottomMargin=config.margin_bottom * inch,
    )
    
    elements = []
    
    # Cover page
    elements.append(Spacer(1, 2 * inch))
    elements.append(Paragraph("NSPFRP Protocol Documentation", styles['CustomTitle']))
    elements.append(Spacer(1, 0.5 * inch))
    elements.append(Paragraph(
        f"{len(protocols)} Protocols",
        styles['CustomHeading']
    ))
    elements.append(Spacer(1, inch))
    elements.append(Paragraph(
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        styles['Metadata']
    ))
    elements.append(PageBreak())
    
    # Table of Contents
    if config.include_toc:
        elements.append(Paragraph("Table of Contents", styles['CustomHeading']))
        elements.append(Spacer(1, 20))
        
        for i, p in enumerate(sorted(protocols, key=lambda x: x.protocol_number or 0), 1):
            toc_line = f"{i}. Protocol {p.protocol_number}: {_clean_text(p.title or 'Untitled')}"
            elements.append(Paragraph(toc_line, styles['CustomBody']))
        
        elements.append(PageBreak())
    
    # Each protocol
    for protocol in sorted(protocols, key=lambda x: x.protocol_number or 0):
        # Title
        elements.append(Paragraph(
            _clean_text(protocol.title or f"Protocol {protocol.protocol_number}"),
            styles['CustomTitle']
        ))
        
        if protocol.subtitle:
            elements.append(Paragraph(_clean_text(protocol.subtitle), styles['Heading2']))
        
        elements.append(Spacer(1, 10))
        
        # Metadata table
        meta_data = [
            ["Protocol", protocol.protocol_id or "N/A"],
            ["Category", protocol.category or "N/A"],
            ["Status", _clean_text(protocol.status or "N/A")],
            ["Date", protocol.discovery_date or "N/A"],
        ]
        
        meta_table = Table(meta_data, colWidths=[1.5 * inch, 4 * inch])
        meta_table.setStyle(TableStyle([
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 9),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.darkgrey),
            ('ALIGN', (0, 0), (0, -1), 'RIGHT'),
            ('ALIGN', (1, 0), (1, -1), 'LEFT'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ]))
        elements.append(meta_table)
        elements.append(Spacer(1, 20))
        
        # Content (limited)
        if protocol.emergent_observation:
            elements.append(Paragraph("Emergent Observation", styles['CustomHeading']))
            content = protocol.emergent_observation.content[:2000]
            content_elements = _markdown_to_paragraphs(content, styles)
            elements.extend(content_elements)
        
        # Checkmarks
        if protocol.checkmarks:
            elements.append(Paragraph("Key Points", styles['CustomHeading']))
            for check in protocol.checkmarks[:8]:
                elements.append(Paragraph(f"[OK] {_clean_text(check)}", styles['CustomBody']))
        
        elements.append(PageBreak())
    
    # Build
    pdf.build(elements)
    
    return output_path


def export_summary_pdf(
    protocols: list[ProtocolDocument],
    output_path: Path | str,
    title: str = "Protocol Summary Report",
) -> Path:
    """
    Export a summary PDF with protocol overview.
    
    Args:
        protocols: Protocols to summarize
        output_path: Output file path
        title: Report title
        
    Returns:
        Path to created PDF
    """
    _check_reportlab()
    
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    styles = _get_styles(PDFConfig())
    
    pdf = SimpleDocTemplate(str(output_path), pagesize=letter)
    elements = []
    
    # Title
    elements.append(Paragraph(title, styles['CustomTitle']))
    elements.append(Spacer(1, 20))
    elements.append(Paragraph(
        f"Generated: {datetime.now().strftime('%Y-%m-%d')} | "
        f"Protocols: {len(protocols)}",
        styles['Metadata']
    ))
    elements.append(Spacer(1, 30))
    
    # Summary table
    table_data = [["#", "Protocol", "Category", "Status"]]
    
    for p in sorted(protocols, key=lambda x: x.protocol_number or 0):
        status = "OK" if p.is_operational else "?"
        table_data.append([
            str(p.protocol_number or "?"),
            _clean_text(p.title or "Untitled")[:40],
            (p.category or "N/A")[:25],
            status,
        ])
    
    table = Table(table_data, colWidths=[0.5 * inch, 3 * inch, 2 * inch, 0.5 * inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkgrey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ]))
    elements.append(table)
    
    # Build
    pdf.build(elements)
    
    return output_path


def export_story_to_pdf(
    story: Any,  # Story type
    output_path: Path | str,
    config: Optional[PDFConfig] = None,
) -> Path:
    """
    Export a story object to PDF.
    
    Args:
        story: Story object (duck typing)
        output_path: Output file path
        config: PDF configuration
        
    Returns:
        Path to created PDF
    """
    _check_reportlab()
    
    config = config or PDFConfig()
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    styles = _get_styles(config)
    
    pdf = SimpleDocTemplate(
        str(output_path),
        pagesize=config.page_size,
        leftMargin=config.margin_left * inch,
        rightMargin=config.margin_right * inch,
        topMargin=config.margin_top * inch,
        bottomMargin=config.margin_bottom * inch,
    )
    
    elements = []
    
    # Title
    elements.append(Paragraph(_clean_text(story.title), styles['CustomTitle']))
    
    template = getattr(story, "template_name", getattr(story, "template_used", None))
    if template:
        elements.append(Paragraph(
            f"A {template}", 
            styles['Metadata']
        ))
    
    elements.append(Spacer(1, 40))
    
    # Quote
    if story.quote:
        quote_text = story.quote.text
        source = getattr(story.quote, "source", getattr(story.quote, "attribution", "Unknown"))
        elements.append(Paragraph(f'"{_clean_text(quote_text)}"', styles['Quote']))
        elements.append(Paragraph(f"— {_clean_text(source)}", styles['Metadata']))
        elements.append(Spacer(1, 30))
    
    # Content
    content_text = getattr(story, "content", getattr(story, "text", ""))
    content_elements = _markdown_to_paragraphs(content_text, styles)
    elements.extend(content_elements)
    
    # Footer
    elements.append(Spacer(1, 30))
    elements.append(Paragraph(
        "MarkTwainVerse Authorized Visitor Log",
        styles['Metadata']
    ))
    
    # Build
    pdf.build(elements)
    
    return output_path


def export_anthology_to_pdf(
    anthology_path: Path | str,
    output_path: Path | str,
    title: str = "Frontier Anthology",
    config: Optional[PDFConfig] = None,
) -> Path:
    """
    Export an authorized anthology folder to a single PDF.
    
    Args:
        anthology_path: Path to anthology folder
        output_path: Output file path
        title: Anthology title
        config: PDF configuration
        
    Returns:
        Path to created PDF
    """
    _check_reportlab()
    
    config = config or PDFConfig()
    anthology_path = Path(anthology_path)
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    styles = _get_styles(config)
    
    pdf = SimpleDocTemplate(
        str(output_path),
        pagesize=config.page_size,
        leftMargin=config.margin_left * inch,
        rightMargin=config.margin_right * inch,
        topMargin=config.margin_top * inch,
        bottomMargin=config.margin_bottom * inch,
    )
    
    elements = []
    
    # Find markdown files
    md_files = sorted(list(anthology_path.glob("*.md")))
    
    # Cover
    elements.append(Spacer(1, 2 * inch))
    elements.append(Paragraph(title, styles['CustomTitle']))
    elements.append(Spacer(1, 0.5 * inch))
    elements.append(Paragraph(
        f"{len(md_files)} Tales from the Frontier",
        styles['CustomHeading']
    ))
    elements.append(Spacer(1, inch))
    elements.append(Paragraph(
        f"Generated: {datetime.now().strftime('%Y-%m-%d')}",
        styles['Metadata']
    ))
    elements.append(PageBreak())
    
    # TOC
    elements.append(Paragraph("Table of Contents", styles['CustomHeading']))
    elements.append(Spacer(1, 20))
    for i, md in enumerate(md_files, 1):
        # Extract title from first line
        try:
            content = md.read_text()
            first_line = content.split('\n')[0].replace('#', '').strip()
            elements.append(Paragraph(f"{i}. {first_line}", styles['CustomBody']))
        except Exception:
            elements.append(Paragraph(f"{i}. {md.stem}", styles['CustomBody']))
    elements.append(PageBreak())
    
    # Stories
    for md in md_files:
        content = md.read_text()
        
        # New chapter
        content_elements = _markdown_to_paragraphs(content, styles)
        elements.extend(content_elements)
        elements.append(PageBreak())
    
    # Build
    pdf.build(elements)
    
    return output_path
