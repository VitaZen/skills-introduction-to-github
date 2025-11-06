#!/usr/bin/env python3
"""
Unit tests for the Educational Video Summary Tool

Run with: python3 test_video_summary_tool.py
"""

import unittest
import json
import os
import tempfile
from video_summary_tool import (
    VideoSummaryGenerator, 
    SlideContent, 
    LessonSummary,
    ContentType
)


class TestVideoSummaryGenerator(unittest.TestCase):
    """Test cases for the VideoSummaryGenerator class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.generator = VideoSummaryGenerator()
        self.temp_dir = tempfile.mkdtemp()
    
    def tearDown(self):
        """Clean up temporary files"""
        import shutil
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)
    
    def test_load_simple_lesson(self):
        """Test loading a simple lesson with basic content"""
        lesson_data = {
            "lesson_title": "Test Lesson",
            "slides": [
                {
                    "slide_number": 1,
                    "title": "Introduction",
                    "content": [
                        {"type": "text", "value": "Test text"}
                    ]
                }
            ]
        }
        
        # Write test data to file
        test_file = os.path.join(self.temp_dir, "test_lesson.json")
        with open(test_file, 'w') as f:
            json.dump(lesson_data, f)
        
        # Load lesson
        lesson = self.generator.load_lesson_data(test_file)
        
        # Assertions
        self.assertEqual(lesson.lesson_title, "Test Lesson")
        self.assertEqual(len(lesson.slides), 1)
        self.assertEqual(lesson.slides[0].slide_number, 1)
        self.assertEqual(lesson.slides[0].title, "Introduction")
        self.assertEqual(len(lesson.slides[0].text), 1)
        self.assertEqual(lesson.slides[0].text[0], "Test text")
    
    def test_load_lesson_with_formulae(self):
        """Test loading lessons with formulae and equations"""
        lesson_data = {
            "lesson_title": "Math Lesson",
            "slides": [
                {
                    "slide_number": 1,
                    "title": "Formulae",
                    "content": [
                        {"type": "formula", "value": "E = mc²"},
                        {"type": "equation", "value": "ax² + bx + c = 0"}
                    ]
                }
            ]
        }
        
        test_file = os.path.join(self.temp_dir, "math_lesson.json")
        with open(test_file, 'w') as f:
            json.dump(lesson_data, f)
        
        lesson = self.generator.load_lesson_data(test_file)
        
        self.assertEqual(len(lesson.slides[0].formulae), 1)
        self.assertEqual(len(lesson.slides[0].equations), 1)
        self.assertEqual(lesson.slides[0].formulae[0], "E = mc²")
        self.assertEqual(lesson.slides[0].equations[0], "ax² + bx + c = 0")
    
    def test_load_lesson_with_tables(self):
        """Test loading lessons with tables"""
        lesson_data = {
            "lesson_title": "Table Lesson",
            "slides": [
                {
                    "slide_number": 1,
                    "title": "Data",
                    "content": [
                        {
                            "type": "table",
                            "headers": ["A", "B"],
                            "rows": [["1", "2"], ["3", "4"]]
                        }
                    ]
                }
            ]
        }
        
        test_file = os.path.join(self.temp_dir, "table_lesson.json")
        with open(test_file, 'w') as f:
            json.dump(lesson_data, f)
        
        lesson = self.generator.load_lesson_data(test_file)
        
        self.assertEqual(len(lesson.slides[0].tables), 1)
        table = lesson.slides[0].tables[0]
        self.assertEqual(table['headers'], ["A", "B"])
        self.assertEqual(len(table['rows']), 2)
    
    def test_load_lesson_with_key_terms(self):
        """Test loading lessons with key terms"""
        lesson_data = {
            "lesson_title": "Vocabulary Lesson",
            "slides": [
                {
                    "slide_number": 1,
                    "title": "Terms",
                    "content": [
                        {
                            "type": "key_term",
                            "term": "Algorithm",
                            "definition": "A step-by-step procedure"
                        }
                    ]
                }
            ]
        }
        
        test_file = os.path.join(self.temp_dir, "vocab_lesson.json")
        with open(test_file, 'w') as f:
            json.dump(lesson_data, f)
        
        lesson = self.generator.load_lesson_data(test_file)
        
        self.assertEqual(len(lesson.slides[0].key_terms), 1)
        term = lesson.slides[0].key_terms[0]
        self.assertEqual(term['term'], "Algorithm")
        self.assertEqual(term['definition'], "A step-by-step procedure")
    
    def test_load_lesson_with_graphs(self):
        """Test loading lessons with graphs"""
        lesson_data = {
            "lesson_title": "Graph Lesson",
            "slides": [
                {
                    "slide_number": 1,
                    "title": "Visualization",
                    "content": [
                        {
                            "type": "graph",
                            "description": "Test graph",
                            "image_path": "test.png"
                        }
                    ]
                }
            ]
        }
        
        test_file = os.path.join(self.temp_dir, "graph_lesson.json")
        with open(test_file, 'w') as f:
            json.dump(lesson_data, f)
        
        lesson = self.generator.load_lesson_data(test_file)
        
        self.assertEqual(len(lesson.slides[0].graphs), 1)
        graph = lesson.slides[0].graphs[0]
        self.assertEqual(graph['description'], "Test graph")
        self.assertEqual(graph['image_path'], "test.png")
    
    def test_load_lesson_with_examples(self):
        """Test loading lessons with examples"""
        lesson_data = {
            "lesson_title": "Example Lesson",
            "slides": [
                {
                    "slide_number": 1,
                    "title": "Examples",
                    "content": [
                        {"type": "example", "value": "Example 1"},
                        {"type": "example", "value": "Example 2"}
                    ]
                }
            ]
        }
        
        test_file = os.path.join(self.temp_dir, "example_lesson.json")
        with open(test_file, 'w') as f:
            json.dump(lesson_data, f)
        
        lesson = self.generator.load_lesson_data(test_file)
        
        self.assertEqual(len(lesson.slides[0].examples), 2)
        self.assertEqual(lesson.slides[0].examples[0], "Example 1")
    
    def test_generate_markdown_basic(self):
        """Test basic markdown generation"""
        lesson = LessonSummary(lesson_title="Test Lesson")
        slide = SlideContent(slide_number=1, title="Intro")
        slide.text.append("Test content")
        lesson.slides.append(slide)
        
        markdown = self.generator.generate_markdown_summary(lesson)
        
        self.assertIn("# Test Lesson", markdown)
        self.assertIn("## Lesson Overview", markdown)
        self.assertIn("### Intro", markdown)
        self.assertIn("- Test content", markdown)
    
    def test_generate_markdown_with_formulae(self):
        """Test markdown generation with formulae"""
        lesson = LessonSummary(lesson_title="Math")
        slide = SlideContent(slide_number=1, title="Formulae")
        slide.formulae.append("a + b = c")
        lesson.slides.append(slide)
        
        markdown = self.generator.generate_markdown_summary(lesson)
        
        self.assertIn("#### Formulae and Equations", markdown)
        self.assertIn("```", markdown)
        self.assertIn("a + b = c", markdown)
        self.assertIn("## Consolidated Reference", markdown)
    
    def test_generate_markdown_with_tables(self):
        """Test markdown generation with tables"""
        lesson = LessonSummary(lesson_title="Data")
        slide = SlideContent(slide_number=1, title="Table")
        slide.tables.append({
            'headers': ['X', 'Y'],
            'rows': [['1', '2']]
        })
        lesson.slides.append(slide)
        
        markdown = self.generator.generate_markdown_summary(lesson)
        
        self.assertIn("#### Tables", markdown)
        self.assertIn("| X | Y |", markdown)
        self.assertIn("| --- | --- |", markdown)
        self.assertIn("| 1 | 2 |", markdown)
    
    def test_generate_markdown_with_key_terms(self):
        """Test markdown generation with key terms"""
        lesson = LessonSummary(lesson_title="Vocab")
        slide = SlideContent(slide_number=1, title="Terms")
        slide.key_terms.append({
            'term': 'Term1',
            'definition': 'Def1'
        })
        lesson.slides.append(slide)
        
        markdown = self.generator.generate_markdown_summary(lesson)
        
        self.assertIn("## Key Terms", markdown)
        self.assertIn("**Term1**: Def1", markdown)
    
    def test_multiple_slides(self):
        """Test handling multiple slides"""
        lesson_data = {
            "lesson_title": "Multi-Slide Lesson",
            "slides": [
                {
                    "slide_number": i,
                    "title": f"Slide {i}",
                    "content": [
                        {"type": "text", "value": f"Content {i}"}
                    ]
                }
                for i in range(1, 13)  # 12 slides
            ]
        }
        
        test_file = os.path.join(self.temp_dir, "multi_lesson.json")
        with open(test_file, 'w') as f:
            json.dump(lesson_data, f)
        
        lesson = self.generator.load_lesson_data(test_file)
        
        self.assertEqual(len(lesson.slides), 12)
        for i, slide in enumerate(lesson.slides, 1):
            self.assertEqual(slide.slide_number, i)
            self.assertEqual(slide.title, f"Slide {i}")
    
    def test_process_lesson_end_to_end(self):
        """Test complete process from input to output"""
        lesson_data = {
            "lesson_title": "Complete Test",
            "slides": [
                {
                    "slide_number": 1,
                    "title": "Test",
                    "content": [
                        {"type": "text", "value": "Test text"},
                        {"type": "formula", "value": "f(x) = x²"}
                    ]
                }
            ]
        }
        
        input_file = os.path.join(self.temp_dir, "input.json")
        output_file = os.path.join(self.temp_dir, "output.md")
        
        with open(input_file, 'w') as f:
            json.dump(lesson_data, f)
        
        self.generator.process_lesson(input_file, output_file)
        
        # Verify output file was created
        self.assertTrue(os.path.exists(output_file))
        
        # Verify output content
        with open(output_file, 'r') as f:
            content = f.read()
            self.assertIn("# Complete Test", content)
            self.assertIn("Test text", content)
            self.assertIn("f(x) = x²", content)
    
    def test_empty_slides(self):
        """Test handling of slides with no content"""
        lesson_data = {
            "lesson_title": "Empty Lesson",
            "slides": [
                {
                    "slide_number": 1,
                    "title": "Empty",
                    "content": []
                }
            ]
        }
        
        test_file = os.path.join(self.temp_dir, "empty_lesson.json")
        with open(test_file, 'w') as f:
            json.dump(lesson_data, f)
        
        lesson = self.generator.load_lesson_data(test_file)
        markdown = self.generator.generate_markdown_summary(lesson)
        
        # Should still generate valid markdown
        self.assertIn("# Empty Lesson", markdown)
        self.assertIn("### Empty", markdown)


class TestSlideContent(unittest.TestCase):
    """Test cases for the SlideContent class"""
    
    def test_slide_initialization(self):
        """Test SlideContent initialization"""
        slide = SlideContent(slide_number=1, title="Test")
        
        self.assertEqual(slide.slide_number, 1)
        self.assertEqual(slide.title, "Test")
        self.assertEqual(len(slide.text), 0)
        self.assertEqual(len(slide.formulae), 0)
        self.assertEqual(len(slide.equations), 0)
        self.assertEqual(len(slide.tables), 0)
        self.assertEqual(len(slide.key_terms), 0)
        self.assertEqual(len(slide.graphs), 0)
        self.assertEqual(len(slide.examples), 0)
    
    def test_slide_content_addition(self):
        """Test adding content to slides"""
        slide = SlideContent(slide_number=1)
        
        slide.text.append("Text 1")
        slide.formulae.append("Formula 1")
        slide.key_terms.append({'term': 'T1', 'definition': 'D1'})
        
        self.assertEqual(len(slide.text), 1)
        self.assertEqual(len(slide.formulae), 1)
        self.assertEqual(len(slide.key_terms), 1)


class TestLessonSummary(unittest.TestCase):
    """Test cases for the LessonSummary class"""
    
    def test_lesson_initialization(self):
        """Test LessonSummary initialization"""
        lesson = LessonSummary(lesson_title="Test Lesson")
        
        self.assertEqual(lesson.lesson_title, "Test Lesson")
        self.assertEqual(len(lesson.slides), 0)
    
    def test_adding_slides(self):
        """Test adding slides to lesson"""
        lesson = LessonSummary(lesson_title="Test")
        
        for i in range(12):
            slide = SlideContent(slide_number=i+1)
            lesson.slides.append(slide)
        
        self.assertEqual(len(lesson.slides), 12)


def run_tests():
    """Run all tests"""
    print("Running Educational Video Summary Tool Tests...")
    print("=" * 70)
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add test classes
    suite.addTests(loader.loadTestsFromTestCase(TestVideoSummaryGenerator))
    suite.addTests(loader.loadTestsFromTestCase(TestSlideContent))
    suite.addTests(loader.loadTestsFromTestCase(TestLessonSummary))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("\n" + "=" * 70)
    print(f"Tests run: {result.testsRun}")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    return result.wasSuccessful()


if __name__ == '__main__':
    success = run_tests()
    exit(0 if success else 1)
