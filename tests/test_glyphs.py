"""
Tests for the glyph generation system
"""

import sys
import os
import unittest
import numpy as np

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.glyphs.generator import generate_glyph

class TestGlyphGenerator(unittest.TestCase):
    """Test cases for the glyph generator"""

    def test_glyph_generation(self):
        """Test that glyphs can be generated from attention matrices"""
        # Create test attention matrix
        attention = np.random.rand(12, 12)
        
        # Generate glyph
        output_path = "test_glyph.svg"
        result_path = generate_glyph(attention, output_path)
        
        # Check that file was created
        self.assertTrue(os.path.exists(result_path))
        
        # Check that it's a valid SVG file
        with open(result_path, 'r') as f:
            content = f.read()
            self.assertTrue(content.startswith('<?xml') or '<svg' in content)
        
        # Clean up
        if os.path.exists(output_path):
            os.remove(output_path)

    def test_different_themes(self):
        """Test that different themes produce different outputs"""
        attention = np.random.rand(12, 12)
        
        # Generate glyphs with different themes
        cosmic_path = generate_glyph(attention, "cosmic_test.svg", theme="cosmic")
        void_path = generate_glyph(attention, "void_test.svg", theme="void")
        
        # Check that files exist
        self.assertTrue(os.path.exists(cosmic_path))
        self.assertTrue(os.path.exists(void_path))
        
        # Load content
        with open(cosmic_path, 'r') as f:
            cosmic_content = f.read()
        with open(void_path, 'r') as f:
            void_content = f.read()
            
        # They should be different
        self.assertNotEqual(cosmic_content, void_content)
        
        # Clean up
        for path in [cosmic_path, void_path]:
            if os.path.exists(path):
                os.remove(path)

if __name__ == '__main__':
    unittest.main()
