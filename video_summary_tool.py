#!/usr/bin/env python3
"""
Educational Video Summary Tool

This tool processes educational video content from multiple slides/tabs and generates
a structured summary with headings, lists, and explicit inclusion of:
- Text and explanations
- Formulae and equations
- Tables
- Key terms
- Graphs and visual elements

Usage:
    python video_summary_tool.py --input <input_file> --output <output_file>
"""

import json
import re
import argparse
from typing import List, Dict, Any
from dataclasses import dataclass, field
from enum import Enum


class ContentType(Enum):
    """Types of content that can be extracted from slides"""
    TEXT = "text"
    FORMULA = "formula"
    TABLE = "table"
    KEY_TERM = "key_term"
    GRAPH = "graph"
    EQUATION = "equation"
    EXAMPLE = "example"


@dataclass
class SlideContent:
    """Represents content from a single slide/tab"""
    slide_number: int
    title: str = ""
    text: List[str] = field(default_factory=list)
    formulae: List[str] = field(default_factory=list)
    equations: List[str] = field(default_factory=list)
    tables: List[Dict[str, Any]] = field(default_factory=list)
    key_terms: List[Dict[str, str]] = field(default_factory=list)
    graphs: List[str] = field(default_factory=list)
    examples: List[str] = field(default_factory=list)


@dataclass
class LessonSummary:
    """Represents a complete lesson summary"""
    lesson_title: str
    slides: List[SlideContent] = field(default_factory=list)


class VideoSummaryGenerator:
    """Generates structured summaries from educational video content"""
    
    def __init__(self):
        self.current_lesson = None
    
    def load_lesson_data(self, input_file: str) -> LessonSummary:
        """
        Load lesson data from a JSON file.
        
        Expected format:
        {
            "lesson_title": "Lesson Title",
            "slides": [
                {
                    "slide_number": 1,
                    "title": "Introduction",
                    "content": [
                        {"type": "text", "value": "..."},
                        {"type": "formula", "value": "E = mc²"},
                        {"type": "table", "headers": [...], "rows": [...]},
                        {"type": "key_term", "term": "...", "definition": "..."},
                        {"type": "graph", "description": "...", "image_path": "..."},
                        {"type": "equation", "value": "..."},
                        {"type": "example", "value": "..."}
                    ]
                },
                ...
            ]
        }
        """
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        lesson = LessonSummary(lesson_title=data.get('lesson_title', 'Untitled Lesson'))
        
        for slide_data in data.get('slides', []):
            slide = SlideContent(
                slide_number=slide_data.get('slide_number', 0),
                title=slide_data.get('title', '')
            )
            
            for item in slide_data.get('content', []):
                content_type = item.get('type', '').lower()
                
                if content_type == 'text':
                    slide.text.append(item.get('value', ''))
                elif content_type == 'formula':
                    slide.formulae.append(item.get('value', ''))
                elif content_type == 'equation':
                    slide.equations.append(item.get('value', ''))
                elif content_type == 'table':
                    slide.tables.append({
                        'headers': item.get('headers', []),
                        'rows': item.get('rows', [])
                    })
                elif content_type == 'key_term':
                    slide.key_terms.append({
                        'term': item.get('term', ''),
                        'definition': item.get('definition', '')
                    })
                elif content_type == 'graph':
                    slide.graphs.append({
                        'description': item.get('description', ''),
                        'image_path': item.get('image_path', '')
                    })
                elif content_type == 'example':
                    slide.examples.append(item.get('value', ''))
            
            lesson.slides.append(slide)
        
        return lesson
    
    def generate_markdown_summary(self, lesson: LessonSummary) -> str:
        """
        Generate a structured Markdown summary from lesson data.
        
        Structure:
        # Lesson Title (H1)
        ## Key Terms (H2)
        ## Summary by Section (H2)
        ### Section Title (H3)
        - Bullet points
        ### Formulae and Equations (H3)
        ### Tables (H3)
        ### Graphs and Visualizations (H3)
        ### Examples (H3)
        """
        output = []
        
        # H1: Lesson Title
        output.append(f"# {lesson.lesson_title}\n")
        
        # Collect all key terms across slides
        all_key_terms = []
        for slide in lesson.slides:
            all_key_terms.extend(slide.key_terms)
        
        if all_key_terms:
            output.append("## Key Terms\n")
            for term_dict in all_key_terms:
                term = term_dict.get('term', '')
                definition = term_dict.get('definition', '')
                output.append(f"**{term}**: {definition}\n")
            output.append("\n")
        
        # H2: Summary by Section
        output.append("## Lesson Overview\n")
        
        # Process each slide
        for slide in lesson.slides:
            if slide.title:
                # H3: Slide/Section Title
                output.append(f"### {slide.title}\n")
            else:
                output.append(f"### Slide {slide.slide_number}\n")
            
            # Text content
            if slide.text:
                for text in slide.text:
                    output.append(f"- {text}\n")
                output.append("\n")
            
            # Formulae and Equations
            if slide.formulae or slide.equations:
                output.append("#### Formulae and Equations\n")
                
                if slide.formulae:
                    for formula in slide.formulae:
                        output.append(f"```\n{formula}\n```\n")
                
                if slide.equations:
                    for equation in slide.equations:
                        output.append(f"```\n{equation}\n```\n")
                
                output.append("\n")
            
            # Tables
            if slide.tables:
                output.append("#### Tables\n")
                for table in slide.tables:
                    headers = table.get('headers', [])
                    rows = table.get('rows', [])
                    
                    if headers:
                        # Markdown table header
                        output.append("| " + " | ".join(headers) + " |\n")
                        output.append("| " + " | ".join(["---"] * len(headers)) + " |\n")
                        
                        # Table rows
                        for row in rows:
                            output.append("| " + " | ".join(str(cell) for cell in row) + " |\n")
                    
                    output.append("\n")
            
            # Graphs and Visualizations
            if slide.graphs:
                output.append("#### Graphs and Visualizations\n")
                for graph in slide.graphs:
                    description = graph.get('description', '')
                    image_path = graph.get('image_path', '')
                    
                    if description:
                        output.append(f"**{description}**\n")
                    
                    if image_path:
                        output.append(f"![Graph]({image_path})\n")
                    
                    output.append("\n")
            
            # Examples
            if slide.examples:
                output.append("#### Examples\n")
                for idx, example in enumerate(slide.examples, 1):
                    output.append(f"{idx}. {example}\n")
                output.append("\n")
        
        # Generate consolidated sections
        output.append("---\n\n")
        output.append("## Consolidated Reference\n")
        
        # All Formulae and Equations
        all_formulae = []
        all_equations = []
        for slide in lesson.slides:
            all_formulae.extend(slide.formulae)
            all_equations.extend(slide.equations)
        
        if all_formulae or all_equations:
            output.append("### All Formulae and Equations\n")
            
            if all_formulae:
                output.append("**Formulae:**\n")
                for formula in all_formulae:
                    output.append(f"- `{formula}`\n")
                output.append("\n")
            
            if all_equations:
                output.append("**Equations:**\n")
                for equation in all_equations:
                    output.append(f"- `{equation}`\n")
                output.append("\n")
        
        return "".join(output)
    
    def process_lesson(self, input_file: str, output_file: str):
        """
        Main processing function to load lesson data and generate summary.
        """
        lesson = self.load_lesson_data(input_file)
        summary = self.generate_markdown_summary(lesson)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(summary)
        
        print(f"Summary generated successfully!")
        print(f"Input: {input_file}")
        print(f"Output: {output_file}")
        print(f"Total slides processed: {len(lesson.slides)}")


def main():
    """Command-line interface for the video summary tool"""
    parser = argparse.ArgumentParser(
        description="Educational Video Summary Tool - Generate structured summaries from educational content"
    )
    parser.add_argument(
        '--input', '-i',
        required=True,
        help="Input JSON file containing lesson data"
    )
    parser.add_argument(
        '--output', '-o',
        required=True,
        help="Output Markdown file for the summary"
    )
    
    args = parser.parse_args()
    
    generator = VideoSummaryGenerator()
    generator.process_lesson(args.input, args.output)


if __name__ == "__main__":
    main()
