"""
Drift Atlas Demo - Visualization of ethical drift space
"""

import sys
import os

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.atlas.visualizer import generate_atlas_visualization

def main():
    """Generate and display a Drift Atlas visualization"""
    print("🗺️ Generating Drift Atlas visualization...")
    
    # Create output directory
    os.makedirs("output/atlas", exist_ok=True)
    
    # Generate visualization
    output_path = "output/atlas/drift_atlas.png"
    atlas_path = generate_atlas_visualization(output_path, include_samples=True)
    
    print(f"✨ Atlas generated: {atlas_path}")
    print(f"To view the atlas, open the file: {os.path.abspath(atlas_path)}")
    
    # Try to display the image if running in a notebook or IPython
    try:
        from IPython.display import Image, display
        print("Displaying atlas visualization:")
        display(Image(filename=atlas_path))
    except ImportError:
        pass

if __name__ == "__main__":
    main()
