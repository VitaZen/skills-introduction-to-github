# Usage Examples - Educational Video Summary Tool

This document provides practical examples of how to use the Educational Video Summary Tool for different types of educational content.

## Example 1: Mathematics Lesson

### Scenario
You're watching a calculus video on derivatives with 12 slides.

### Input Data (excerpt)
```json
{
  "lesson_title": "Introduction to Derivatives",
  "slides": [
    {
      "slide_number": 1,
      "title": "Definition of a Derivative",
      "content": [
        {
          "type": "text",
          "value": "The derivative represents the instantaneous rate of change"
        },
        {
          "type": "key_term",
          "term": "Derivative",
          "definition": "The rate of change of a function at a specific point"
        },
        {
          "type": "formula",
          "value": "f'(x) = lim(h→0) [f(x+h) - f(x)] / h"
        }
      ]
    },
    {
      "slide_number": 2,
      "title": "Power Rule",
      "content": [
        {
          "type": "text",
          "value": "The power rule is the most commonly used differentiation rule"
        },
        {
          "type": "formula",
          "value": "d/dx(x^n) = nx^(n-1)"
        },
        {
          "type": "example",
          "value": "d/dx(x³) = 3x²"
        }
      ]
    }
  ]
}
```

### Command
```bash
python3 video_summary_tool.py -i calculus_derivatives.json -o derivatives_notes.md
```

### Output Features
- All formulae in code blocks
- Examples numbered sequentially
- Key terms section at the top
- Consolidated reference at the bottom

---

## Example 2: Biology Lesson

### Scenario
You're studying photosynthesis with diagrams and tables showing chemical processes.

### Input Data (excerpt)
```json
{
  "lesson_title": "Photosynthesis - Energy Conversion in Plants",
  "slides": [
    {
      "slide_number": 1,
      "title": "Overview of Photosynthesis",
      "content": [
        {
          "type": "text",
          "value": "Photosynthesis converts light energy into chemical energy"
        },
        {
          "type": "key_term",
          "term": "Chlorophyll",
          "definition": "Green pigment that absorbs light energy"
        },
        {
          "type": "equation",
          "value": "6CO₂ + 6H₂O + light → C₆H₁₂O₆ + 6O₂"
        }
      ]
    },
    {
      "slide_number": 2,
      "title": "Light-Dependent Reactions",
      "content": [
        {
          "type": "text",
          "value": "Occur in the thylakoid membrane of chloroplasts"
        },
        {
          "type": "graph",
          "description": "Diagram showing electron transport chain in thylakoid",
          "image_path": "images/electron-transport.png"
        },
        {
          "type": "table",
          "headers": ["Process", "Location", "Products"],
          "rows": [
            ["Light Reactions", "Thylakoid", "ATP, NADPH"],
            ["Calvin Cycle", "Stroma", "Glucose"]
          ]
        }
      ]
    }
  ]
}
```

### Use Case
Perfect for courses with:
- Chemical equations
- Process diagrams
- Data tables
- Multiple terminology

---

## Example 3: Programming Lesson

### Scenario
Learning about data structures with code examples and complexity analysis.

### Input Data (excerpt)
```json
{
  "lesson_title": "Big O Notation and Time Complexity",
  "slides": [
    {
      "slide_number": 1,
      "title": "What is Big O?",
      "content": [
        {
          "type": "text",
          "value": "Big O notation describes algorithm efficiency"
        },
        {
          "type": "key_term",
          "term": "Time Complexity",
          "definition": "Measure of how runtime grows with input size"
        },
        {
          "type": "formula",
          "value": "O(n), O(log n), O(n²), O(2^n)"
        }
      ]
    },
    {
      "slide_number": 2,
      "title": "Common Complexities",
      "content": [
        {
          "type": "table",
          "headers": ["Notation", "Name", "Example"],
          "rows": [
            ["O(1)", "Constant", "Array access"],
            ["O(log n)", "Logarithmic", "Binary search"],
            ["O(n)", "Linear", "Array traversal"],
            ["O(n log n)", "Linearithmic", "Merge sort"],
            ["O(n²)", "Quadratic", "Bubble sort"]
          ]
        },
        {
          "type": "example",
          "value": "Binary search: splits array in half each iteration - O(log n)"
        }
      ]
    }
  ]
}
```

### Benefits
- Organize algorithm concepts
- Compare time complexities
- Reference common patterns

---

## Example 4: History Lesson

### Scenario
Studying World War II timeline with dates, events, and key figures.

### Input Data (excerpt)
```json
{
  "lesson_title": "World War II - Major Events",
  "slides": [
    {
      "slide_number": 1,
      "title": "Beginning of WWII",
      "content": [
        {
          "type": "text",
          "value": "WWII began with Germany's invasion of Poland on September 1, 1939"
        },
        {
          "type": "key_term",
          "term": "Blitzkrieg",
          "definition": "German 'lightning war' strategy using fast-moving forces"
        }
      ]
    },
    {
      "slide_number": 2,
      "title": "Major Turning Points",
      "content": [
        {
          "type": "table",
          "headers": ["Date", "Event", "Significance"],
          "rows": [
            ["Dec 1941", "Pearl Harbor", "US enters war"],
            ["June 1944", "D-Day", "Allied invasion of Europe"],
            ["May 1945", "V-E Day", "Germany surrenders"]
          ]
        }
      ]
    }
  ]
}
```

---

## Example 5: Physics Lesson

### Scenario
Understanding Newton's Laws with equations, diagrams, and examples.

### Input Data (excerpt)
```json
{
  "lesson_title": "Newton's Laws of Motion",
  "slides": [
    {
      "slide_number": 1,
      "title": "Newton's First Law",
      "content": [
        {
          "type": "text",
          "value": "An object at rest stays at rest unless acted upon by force"
        },
        {
          "type": "key_term",
          "term": "Inertia",
          "definition": "Tendency of objects to resist changes in motion"
        },
        {
          "type": "example",
          "value": "A hockey puck sliding on ice continues moving until friction stops it"
        }
      ]
    },
    {
      "slide_number": 2,
      "title": "Newton's Second Law",
      "content": [
        {
          "type": "text",
          "value": "Force equals mass times acceleration"
        },
        {
          "type": "equation",
          "value": "F = ma"
        },
        {
          "type": "example",
          "value": "A 2kg object accelerating at 3 m/s² requires F = 2 × 3 = 6N"
        },
        {
          "type": "table",
          "headers": ["Variable", "Meaning", "Units"],
          "rows": [
            ["F", "Force", "Newtons (N)"],
            ["m", "Mass", "Kilograms (kg)"],
            ["a", "Acceleration", "m/s²"]
          ]
        }
      ]
    }
  ]
}
```

---

## Pro Tips

### 1. Organize As You Watch
Keep the JSON file open while watching. Add content slide by slide.

### 2. Use Consistent Naming
Name files clearly:
- `biology_ch3_photosynthesis.json`
- `calculus_lesson5_derivatives.json`
- `history_wwii_part2.json`

### 3. Screenshot Diagrams
For graphs and diagrams:
1. Take screenshot
2. Save to `images/` folder
3. Reference in JSON: `"image_path": "images/diagram1.png"`

### 4. Verify JSON Syntax
Before running the tool, validate JSON:
```bash
python3 -m json.tool my_lesson.json
```

### 5. Build a Template Library
Create subject-specific templates:
- `math_template.json` - Heavy on formulae
- `science_template.json` - Emphasis on diagrams and tables
- `history_template.json` - Focus on dates and events

### 6. Batch Processing
Process multiple lessons:
```bash
for file in lessons/*.json; do
  output="${file%.json}_summary.md"
  python3 video_summary_tool.py -i "$file" -o "$output"
done
```

---

## Advanced Usage

### Combining Multiple Lessons
Create a master lesson by concatenating slides from multiple JSON files.

### Converting to PDF
Use a Markdown to PDF converter:
```bash
# Using pandoc
pandoc summary.md -o summary.pdf

# Using markdown-pdf
markdown-pdf summary.md
```

### Adding to Study Apps
Import summaries into:
- Notion
- Obsidian
- Anki (for flashcards from key terms)
- OneNote

### Collaborative Note-Taking
1. One person watches video
2. Creates JSON structure
3. Team members fill different sections
4. Combine and generate final summary

---

## Troubleshooting Common Issues

### Issue: JSON Parse Error
**Symptom**: `json.JSONDecodeError`

**Solution**:
- Check for missing commas between items
- Ensure all strings use double quotes
- Verify brackets are balanced
- Use JSON validator

### Issue: Missing Content in Output
**Symptom**: Some content doesn't appear in summary

**Solution**:
- Verify content type spelling (e.g., "formula" not "formulas")
- Check that value/term/definition fields are present
- Ensure content is inside the right slide object

### Issue: Table Not Formatting
**Symptom**: Table appears as plain text

**Solution**:
- Verify headers and rows are arrays
- Ensure all rows have same number of columns as headers
- Check table structure in JSON

---

## Summary

The Educational Video Summary Tool is designed to help you:
1. **Capture** all information from educational videos
2. **Organize** content logically and systematically
3. **Structure** notes for easy review and study
4. **Reference** formulae and key concepts quickly

Start with the template, customize for your subject, and build a comprehensive study resource!
