# Glyph Visualizer Example

This is a placeholder for the Jupyter notebook that will allow interactive glyph visualization.

```python
# Import required libraries
import sys
sys.path.append('..')
import numpy as np
from src.glyphs.generator import generate_glyph
from IPython.display import SVG, display

# Generate random attention matrix
attention = np.random.rand(12, 12)

# Generate glyph
sigil_path = generate_glyph(attention, theme="cosmic")

# Display the glyph
display(SVG(sigil_path))
