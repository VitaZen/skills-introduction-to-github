# Quick Start Guide - Educational Video Summary Tool

## Getting Started in 5 Minutes

### Step 1: Verify Python Installation

```bash
python3 --version
```

You should see Python 3.7 or higher.

### Step 2: Prepare Your Lesson Data

You have two options:

**Option A: Use the Template**
```bash
cp lesson_template.json my_lesson.json
```
Then edit `my_lesson.json` with your lesson content.

**Option B: Start with the Example**
```bash
cp example_lesson.json my_lesson.json
```
Then modify it to match your content.

### Step 3: Run the Tool

```bash
python3 video_summary_tool.py --input my_lesson.json --output my_summary.md
```

### Step 4: View Your Summary

Open `my_summary.md` in any text editor or Markdown viewer.

## Creating Your Lesson JSON File

### Basic Structure

Every lesson needs:
1. A `lesson_title`
2. An array of `slides`
3. Each slide has a `slide_number`, `title`, and `content` array

### Adding Content to Slides

#### Text Content
```json
{
  "type": "text",
  "value": "Your explanation here"
}
```

#### Formulae
```json
{
  "type": "formula",
  "value": "E = mc²"
}
```

#### Equations
```json
{
  "type": "equation",
  "value": "ax² + bx + c = 0"
}
```

#### Tables
```json
{
  "type": "table",
  "headers": ["Header 1", "Header 2"],
  "rows": [
    ["Data 1", "Data 2"],
    ["Data 3", "Data 4"]
  ]
}
```

#### Key Terms
```json
{
  "type": "key_term",
  "term": "Photosynthesis",
  "definition": "The process by which plants convert light energy into chemical energy"
}
```

#### Graphs/Images
```json
{
  "type": "graph",
  "description": "Graph showing exponential growth",
  "image_path": "images/graph1.png"
}
```

#### Examples
```json
{
  "type": "example",
  "value": "Example: Calculate the area of a circle with radius 5cm"
}
```

## Tips for Educational Videos

### While Watching the Video

1. **Pause at each slide** - Take time to capture all content
2. **Note slide numbers** - Keep track of the sequence
3. **Capture everything** - Text, formulae, tables, graphs
4. **Screenshot graphs** - Save visual elements to reference later
5. **Write definitions** - Define all key terms as they appear

### Organizing Your Notes

1. **Give descriptive titles** - Make each slide title clear and specific
2. **Group related concepts** - Keep similar topics together
3. **Tag content correctly** - Use the right type for each element
4. **Add context** - Include explanatory text around formulae and tables
5. **Number examples** - Keep examples in order

### Typical 12-Slide Lesson Structure

1. **Slide 1**: Introduction and Overview
2. **Slides 2-3**: Background and Prerequisites
3. **Slides 4-7**: Main Concepts (with formulae, examples, tables)
4. **Slides 8-9**: Applications and Advanced Topics
5. **Slides 10-11**: Practice Problems or Case Studies
6. **Slide 12**: Summary and Key Takeaways

## Example Workflow

### 1. Watch and Capture
- Open video
- Open `lesson_template.json` in your editor
- Pause at each slide and fill in the content

### 2. Structure Your Data
```json
{
  "lesson_title": "Introduction to Algebra",
  "slides": [
    {
      "slide_number": 1,
      "title": "What is Algebra?",
      "content": [
        {"type": "text", "value": "Algebra uses symbols to represent numbers"},
        {"type": "key_term", "term": "Variable", "definition": "A symbol that represents an unknown value"}
      ]
    }
    // ... more slides
  ]
}
```

### 3. Generate Summary
```bash
python3 video_summary_tool.py -i algebra_lesson.json -o algebra_summary.md
```

### 4. Study from Your Notes
- Review the structured summary
- Use the consolidated reference for quick lookup
- Share with study group

## Common Use Cases

### Mathematics Lessons
- Focus on formulae and equations
- Include worked examples
- Add graphs for function visualization

### Science Lessons
- Document key terms and definitions
- Include tables for data and constants
- Add diagrams and experimental setups

### Business/Economics
- Use tables for financial data
- Include graphs for trends
- Add real-world examples

### History/Literature
- Focus on key terms and dates
- Use bullet points for events
- Include quotes as examples

## Troubleshooting

**Q: My JSON won't parse**
- Use a JSON validator (jsonlint.com)
- Check for missing commas and quotes
- Ensure brackets are balanced

**Q: Formulae look wrong**
- Make sure special characters are properly escaped
- Use plain text, not rich text
- Consider using LaTeX notation

**Q: Missing content in output**
- Verify content type matches supported types
- Check for typos in type names
- Ensure value fields are present

**Q: Table formatting issues**
- Ensure headers and rows have same column count
- Use simple text, avoid special formatting
- Check for extra/missing commas

## Next Steps

1. ✅ Try the example lesson
2. ✅ Create your first lesson from a video
3. ✅ Customize the template for your subject
4. ✅ Build a library of structured notes
5. ✅ Share with classmates

## Resources

- Full documentation: `TOOL_README.md`
- Example lesson: `example_lesson.json`
- Template: `lesson_template.json`
- Sample output: Run the example to generate `example_output.md`

---

**Happy Learning! 📚✨**
