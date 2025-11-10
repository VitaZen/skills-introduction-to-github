# Educational Video Summary Tool

A comprehensive tool for processing educational video content and generating structured, well-organized summaries with proper formatting of formulae, tables, graphs, and key concepts.

## Overview

This tool is designed to help students and educators create high-quality notes from educational videos. It processes content from multiple slides/tabs (typically ~12 per lesson) and generates a logical, well-structured summary document in Markdown format.

## Features

- ✅ **Multi-slide Processing**: Handles lessons with multiple slides/tabs (supports 12+ slides per lesson)
- ✅ **Content Extraction**: Extracts and organizes:
  - Text explanations
  - Mathematical formulae and equations
  - Tables and data
  - Key terms and definitions
  - Graphs and visualizations
  - Examples and demonstrations
- ✅ **Structured Output**: Generates summaries with:
  - H1, H2, H3 hierarchical headings
  - Bullet points and numbered lists
  - Properly formatted tables
  - Code blocks for formulae
  - Image references for graphs
- ✅ **Consolidated Reference**: Creates a quick reference section with all formulae and key terms

## Installation

### Requirements

- Python 3.7 or higher
- No external dependencies required (uses only Python standard library)

### Setup

1. Clone or download this repository
2. Ensure Python 3.7+ is installed:
   ```bash
   python3 --version
   ```

3. Make the script executable (optional):
   ```bash
   chmod +x video_summary_tool.py
   ```

## Usage

### Command Line Interface

```bash
python3 video_summary_tool.py --input <input_file.json> --output <output_file.md>
```

#### Arguments

- `--input` or `-i`: Path to the input JSON file containing lesson data (required)
- `--output` or `-o`: Path to the output Markdown file for the summary (required)

### Example

```bash
python3 video_summary_tool.py --input example_lesson.json --output lesson_summary.md
```

## Input Format

The tool expects a JSON file with the following structure:

```json
{
  "lesson_title": "Lesson Title",
  "slides": [
    {
      "slide_number": 1,
      "title": "Slide Title",
      "content": [
        {
          "type": "text",
          "value": "Explanatory text content"
        },
        {
          "type": "formula",
          "value": "E = mc²"
        },
        {
          "type": "equation",
          "value": "ax² + bx + c = 0"
        },
        {
          "type": "table",
          "headers": ["Column 1", "Column 2"],
          "rows": [
            ["Data 1", "Data 2"],
            ["Data 3", "Data 4"]
          ]
        },
        {
          "type": "key_term",
          "term": "Terminology",
          "definition": "Definition of the term"
        },
        {
          "type": "graph",
          "description": "Graph description",
          "image_path": "path/to/image.png"
        },
        {
          "type": "example",
          "value": "Example problem or demonstration"
        }
      ]
    }
  ]
}
```

### Content Types

The tool supports the following content types:

1. **text**: Plain text explanations and descriptions
2. **formula**: Mathematical formulae (displayed in code blocks)
3. **equation**: Mathematical equations (displayed in code blocks)
4. **table**: Tabular data with headers and rows
5. **key_term**: Important terminology with definitions
6. **graph**: Visual elements with descriptions and image paths
7. **example**: Example problems, demonstrations, or applications

## Output Format

The tool generates a structured Markdown document with:

### 1. Lesson Title (H1)
The main title of the lesson

### 2. Key Terms Section (H2)
All key terms and their definitions collected from all slides

### 3. Lesson Overview (H2)
Detailed content organized by slide:
- **Slide Titles (H3)**: Each slide becomes a subsection
- **Content**: Bullet points for text content
- **Formulae and Equations (H4)**: Mathematical content in code blocks
- **Tables (H4)**: Markdown-formatted tables
- **Graphs and Visualizations (H4)**: Descriptions and image links
- **Examples (H4)**: Numbered lists of examples

### 4. Consolidated Reference (H2)
Quick reference section with:
- All formulae from the lesson
- All equations from the lesson

## Example Output Structure

```markdown
# Introduction to Calculus - Derivatives

## Key Terms

**Derivative**: The instantaneous rate of change of a function at a point
**Composite Function**: A function formed by combining two or more functions

## Lesson Overview

### What is a Derivative?

- A derivative represents the rate of change of a function
- The derivative is the slope of the tangent line

#### Formulae and Equations

```
f'(x) = lim(h→0) [f(x+h) - f(x)] / h
```

### Basic Derivative Rules

- There are several fundamental rules for computing derivatives

#### Formulae and Equations

```
Power Rule: d/dx(x^n) = nx^(n-1)
```

---

## Consolidated Reference

### All Formulae and Equations

**Formulae:**
- `f'(x) = lim(h→0) [f(x+h) - f(x)] / h`
- `Power Rule: d/dx(x^n) = nx^(n-1)`
```

## Workflow

1. **Prepare Input Data**: Create a JSON file with your lesson content
   - Organize content by slides (recommend 12 slides per lesson)
   - Tag each content item with its type (text, formula, table, etc.)
   - Include all relevant information from each tab/slide

2. **Run the Tool**: Execute the script with your input file
   ```bash
   python3 video_summary_tool.py -i my_lesson.json -o my_summary.md
   ```

3. **Review Output**: Open the generated Markdown file
   - Verify all content is properly formatted
   - Check that formulae, tables, and graphs are correctly displayed
   - Review the structure and organization

4. **Use Your Summary**: 
   - Study from the structured summary
   - Convert to PDF if needed
   - Share with classmates
   - Use as a study guide

## Tips for Best Results

1. **Organize by Concepts**: Group related slides together with clear titles
2. **Tag Accurately**: Use the correct content type for each item
3. **Include Context**: Add descriptions to graphs and visualizations
4. **Define Terms**: Include definitions for all key terms
5. **Add Examples**: Include worked examples to illustrate concepts
6. **Use Clear Titles**: Give each slide a descriptive title

## Customization

The tool is designed to be easily customizable:

- **Modify Output Format**: Edit the `generate_markdown_summary()` method
- **Add Content Types**: Extend the `ContentType` enum and update parsing logic
- **Change Structure**: Adjust heading levels and organization in the generator
- **Add Export Formats**: Implement additional output formats (HTML, PDF, etc.)

## Troubleshooting

### Common Issues

**Issue**: `FileNotFoundError`
- **Solution**: Check that the input file path is correct and the file exists

**Issue**: `json.JSONDecodeError`
- **Solution**: Validate your JSON syntax using a JSON validator

**Issue**: Missing content in output
- **Solution**: Verify that content types in your JSON match the supported types

**Issue**: Formatting issues
- **Solution**: Ensure special characters in formulae are properly escaped in JSON

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues, questions, or suggestions:
- Open an issue in the GitHub repository
- Review existing issues for solutions
- Check the example files for reference

## Changelog

### Version 1.0.0
- Initial release
- Support for 7 content types
- Markdown output generation
- Structured summary with H1/H2/H3 headings
- Consolidated reference sections
- Example lesson included
