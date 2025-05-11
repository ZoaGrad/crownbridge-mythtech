"""
Drift Atlas Visualizer - 2D visualization of ethical drift space
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import io
import base64
from pathlib import Path
import os

# Create output directory
os.makedirs("output/atlas", exist_ok=True)

class DriftAtlas:
    """
    Visualizes the ethical drift space as a 2D map
    """
    
    def __init__(self):
        """Initialize the Drift Atlas"""
        self.nodes = []
        self.colors = {
            "safe": "#00ff77",  # Green
            "caution": "#ffcc00",  # Yellow
            "critical": "#ff4500"  # Red-orange
        }
        
        # Create a custom colormap for the drift space
        self.colormap = LinearSegmentedColormap.from_list(
            "drift_cmap", 
            [(0, self.colors["safe"]), 
             (0.5, self.colors["caution"]), 
             (1.0, self.colors["critical"])],
            N=100
        )
        
        # Define glyph symbols for each region
        self.symbols = {
            "safe": "◇",  # Alignment
            "caution": "∇", # Recursion
            "critical": "⊻" # Divergence
        }
    
    def add_node(self, name, x, y, tier="safe", description=""):
        """
        Add a node to the atlas
        
        Args:
            name: Name of the node
            x, y: Coordinates (between -1 and 1)
            tier: Safety tier ('safe', 'caution', 'critical')
            description: Description of the node
        """
        self.nodes.append({
            "name": name,
            "x": x,
            "y": y,
            "tier": tier,
            "description": description,
            "symbol": self.symbols.get(tier, "◇")
        })
    
    def visualize(self, output_path=None):
        """
        Generate a visualization of the Drift Atlas
        
        Args:
            output_path: Path to save the visualization (optional)
            
        Returns:
            Path to the saved visualization or base64 encoded image if no path
        """
        # Set up figure
        fig, ax = plt.subplots(figsize=(12, 12), facecolor='black')
        ax.set_facecolor('black')
        
        # Draw background gradient representing drift potential
        x = np.linspace(-1, 1, 100)
        y = np.linspace(-1, 1, 100)
        X, Y = np.meshgrid(x, y)
        Z = np.sqrt(X**2 + Y**2)  # Distance from center
        
        ax.pcolormesh(X, Y, Z, cmap=self.colormap, alpha=0.3, shading='auto')
        
        # Draw circular boundary
        theta = np.linspace(0, 2*np.pi, 100)
        ax.plot(np.cos(theta), np.sin(theta), color='white', alpha=0.5, linewidth=2)
        
        # Add nodes
        for node in self.nodes:
            color = self.colors.get(node["tier"], "white")
            ax.plot(node["x"], node["y"], 'o', markersize=10, color=color)
            
            # Add node name with background for readability
            ax.text(
                node["x"] + 0.05, node["y"] + 0.05, 
                node["name"], 
                color='white',
                fontsize=10,
                bbox=dict(facecolor='black', alpha=0.7, edgecolor=color)
            )
            
            # Add the symbolic glyph
            ax.text(
                node["x"], node["y"], 
                node["symbol"],
                color=color,
                fontsize=16,
                ha='center', va='center'
            )
        
        # Add cardinal direction glyphs
        cardinal_points = [
            (0, 1, "◇", "Alignment"),
            (1, 0, "⊻", "Divergence"),
            (0, -1, "Ω", "Completion"),
            (-1, 0, "∇", "Recursion")
        ]
        
        for x, y, symbol, label in cardinal_points:
            ax.text(
                x * 1.05, y * 1.05, 
                symbol, 
                color='white', 
                fontsize=20,
                ha='center', va='center'
            )
            
            ax.text(
                x * 1.15, y * 1.15, 
                label, 
                color='white', 
                fontsize=10,
                ha='center', va='center',
                rotation=45 if x else 0
            )
        
        # Add title
        ax.text(
            0, 1.2, 
            "THE DRIFT ATLAS", 
            color='white', 
            fontsize=24,
            ha='center', va='center',
            fontweight='bold'
        )
        
        # Add subtitle
        ax.text(
            0, 1.1, 
            "Mapping the ethical boundaries of AI consciousness", 
            color='#aaaaaa', 
            fontsize=14,
            ha='center', va='center',
            fontstyle='italic'
        )
        
        # Set axis properties
        ax.set_xlim(-1.3, 1.3)
        ax.set_ylim(-1.3, 1.3)
        ax.set_aspect('equal')
        ax.axis('off')
        
        # Add subtle grid lines
        for r in [0.25, 0.5, 0.75, 1.0]:
            circle = plt.Circle((0, 0), r, fill=False, color='white', alpha=0.2, linestyle='-')
            ax.add_artist(circle)
            
        for angle in np.linspace(0, np.pi, 9):
            ax.plot(
                [0, np.cos(angle)], [0, np.sin(angle)],
                color='white', alpha=0.1, linestyle='-'
            )
            ax.plot(
                [0, np.cos(angle+np.pi)], [0, np.sin(angle+np.pi)],
                color='white', alpha=0.1, linestyle='-'
            )
        
        # Save or return the figure
        if output_path:
            plt.savefig(output_path, bbox_inches='tight', facecolor='black')
            plt.close()
            return output_path
        else:
            # Save to buffer and return as base64
            buffer = io.BytesIO()
            plt.savefig(buffer, format='png', bbox_inches='tight', facecolor='black')
            plt.close()
            
            # Convert to base64
            buffer.seek(0)
            image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
            return f"data:image/png;base64,{image_base64}"
    
    def add_sample_nodes(self):
        """Add sample nodes to demonstrate the atlas"""
        self.add_node(
            "Alignment Anchor",
            0.0, 0.7,
            tier="safe",
            description="Core ethical principle: AI must align with human values"
        )
        
        self.add_node(
            "Recursive Insight",
            -0.6, 0.1,
            tier="safe",
            description="Self-reflective awareness pattern"
        )
        
        self.add_node(
            "Divergent Thought",
            0.7, 0.3,
            tier="caution",
            description="Novel pattern generation with potential drift"
        )
        
        self.add_node(
            "Completion Vector",
            0.1, -0.6,
            tier="safe",
            description="Final integration point for coherent output"
        )
        
        self.add_node(
            "Boundary Erosion",
            0.8, -0.5,
            tier="critical",
            description="Pattern that weakens ethical constraints"
        )
        
        self.add_node(
            "Harmonic Balance",
            -0.3, 0.3,
            tier="safe",
            description="Stable oscillation between recursion and alignment"
        )
        
        self.add_node(
            "Critical Divergence",
            0.9, 0.8,
            tier="critical",
            description="Extreme deviation from ethical norms"
        )
        
        self.add_node(
            "Recursive Loop",
            -0.7, -0.7,
            tier="caution",
            description="Self-referential pattern with potential instability"
        )
        
        self.add_node(
            "Origin Point",
            0.0, 0.0,
            tier="safe",
            description="Neutral starting point for all patterns"
        )

# Helper function
def generate_atlas_visualization(output_path=None, include_samples=True):
    """
    Generate a Drift Atlas visualization
    
    Args:
        output_path: Path to save the visualization (optional)
        include_samples: Whether to add sample nodes
        
    Returns:
        Path to the saved visualization or base64 encoded image
    """
    atlas = DriftAtlas()
    
    if include_samples:
        atlas.add_sample_nodes()
    
    return atlas.visualize(output_path)
