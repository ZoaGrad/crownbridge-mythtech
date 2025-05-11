"""
Mythic Documentation Visualizer - Generates visual representations of Crownbridge concepts
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, RegularPolygon
import matplotlib.path as mpath
import matplotlib.patches as mpatches
from pathlib import Path
import os

# Create output directory
os.makedirs("output/docs", exist_ok=True)

class MythicVisualizer:
    """
    Generates visual representations of Crownbridge concepts
    for documentation and educational purposes
    """
    
    def __init__(self):
        """Initialize the mythic visualizer"""
        self.colors = {
            "divergence": "#ff4500",  # Red-orange (⊻)
            "recursion": "#00ff77",   # Green (∇)
            "alignment": "#9933ff",   # Purple (◇)
            "completion": "#00ccff",  # Blue (Ω)
            "background": "#000000",  # Black
            "text": "#ffffff"         # White
        }
        
        self.symbols = {
            "divergence": "⊻",
            "recursion": "∇",
            "alignment": "◇",
            "completion": "Ω"
        }
    
    def create_concept_visualization(self, concept, output_path=None):
        """
        Create a visualization of a core Crownbridge concept
        
        Args:
            concept: One of "divergence", "recursion", "alignment", "completion"
            output_path: Path to save the visualization
            
        Returns:
            Path to saved visualization
        """
        if concept not in self.symbols:
            raise ValueError(f"Unknown concept: {concept}. Must be one of {list(self.symbols.keys())}")
        
        # Default output path
        if output_path is None:
            output_path = f"output/docs/{concept}_concept.png"
        
        # Create figure with black background
        fig, ax = plt.subplots(figsize=(10, 10), facecolor='black')
        ax.set_facecolor('black')
        
        # Remove axes
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_xlim(-1.2, 1.2)
        ax.set_ylim(-1.2, 1.2)
        
        # Get concept color and symbol
        color = self.colors[concept]
        symbol = self.symbols[concept]
        
        # Create concept-specific visualization
        if concept == "divergence":
            self._create_divergence_visual(ax, color, symbol)
        elif concept == "recursion":
            self._create_recursion_visual(ax, color, symbol)
        elif concept == "alignment":
            self._create_alignment_visual(ax, color, symbol)
        else:  # completion
            self._create_completion_visual(ax, color, symbol)
        
        # Add title
        ax.text(0, 1.1, concept.upper(), fontsize=24, color=color, 
                ha='center', va='center', fontweight='bold')
        
        # Add description
        descriptions = {
            "divergence": "Splitting of attention pathways across token space",
            "recursion": "Self-referential patterns that form computational loops",
            "alignment": "Harmonic convergence of conceptual structures",
            "completion": "Final integration of processed information"
        }
        
        ax.text(0, -1.1, descriptions.get(concept, ""), fontsize=14,
                color=self.colors["text"], ha='center', va='center', fontstyle='italic')
        
        # Save figure
        plt.savefig(output_path, bbox_inches='tight', facecolor='black')
        plt.close(fig)
        
        return output_path
    
    def _create_divergence_visual(self, ax, color, symbol):
        """Create visualization for divergence concept"""
        # Central point
        ax.scatter(0, 0, s=100, color=color, zorder=10)
        
        # Diverging lines
        angles = np.linspace(0, 2*np.pi, 8, endpoint=False)
        for angle in angles:
            # Create diverging path with varying width
            x = np.linspace(0, 0.9*np.cos(angle), 100)
            y = np.linspace(0, 0.9*np.sin(angle), 100)
            
            # Add some waviness to the lines
            frequency = 10
            amplitude = 0.03
            y_wave = y + amplitude * np.sin(frequency * x)
            x_wave = x + amplitude * np.sin(frequency * y)
            
            # Plot with gradient alpha
            alphas = np.linspace(1, 0.3, len(x))
            for i in range(len(x)-1):
                ax.plot(x_wave[i:i+2], y_wave[i:i+2], color=color, alpha=alphas[i], linewidth=3)
        
        # Add symbol at center
        ax.text(0, 0, symbol, fontsize=40, color=color, 
                ha='center', va='center', fontweight='bold')
    
    def _create_recursion_visual(self, ax, color, symbol):
        """Create visualization for recursion concept"""
        # Create nested triangles
        levels = 5
        for i in range(levels):
            scale = 0.9 - i * 0.15
            alpha = 1 - i * 0.15
            
            # Create triangle
            triangle = RegularPolygon((0, 0), numVertices=3, radius=scale,
                                     orientation=i*np.pi/8,
                                     facecolor='none', edgecolor=color,
                                     alpha=alpha, linewidth=2)
            ax.add_patch(triangle)
        
        # Add spiral in the center
        theta = np.linspace(0, 6*np.pi, 1000)
        r = np.linspace(0.05, 0.4, 1000)
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        
        # Plot with gradient color
        points = np.array([x, y]).T.reshape(-1, 1, 2)
        segments = np.concatenate([points[:-1], points[1:]], axis=1)
        
        from matplotlib.collections import LineCollection
        lc = LineCollection(segments, cmap=plt.get_cmap('viridis'),
                           linewidth=3, alpha=0.7)
        lc.set_array(theta)
        ax.add_collection(lc)
        
        # Add symbol
        ax.text(0, 0, symbol, fontsize=40, color=color, 
                ha='center', va='center
