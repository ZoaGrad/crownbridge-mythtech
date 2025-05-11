"""
Ritual Simulator - Generate and execute symbolic rituals
for transformer attention visualization and ethical exploration
"""

import numpy as np
import hashlib
from datetime import datetime
import os
from pathlib import Path

# Create output directory
os.makedirs("output/rituals", exist_ok=True)

class RitualSimulator:
    """
    Simulates symbolic rituals that transform intentions into
    visual patterns and ethical insights
    """
    
    def __init__(self):
        """Initialize the ritual simulator"""
        self.symbols = ["⊻", "∇", "◇", "Ω"]
        self.ritual_history = []
    
    def perform_ritual(self, intent, depth=3, theme="cosmic"):
        """
        Perform a ritual based on an intention
        
        Args:
            intent: The user's intention statement
            depth: Ritual depth/complexity (1-5)
            theme: Visual theme ("cosmic", "void", "flame")
            
        Returns:
            Dictionary with ritual results
        """
        # Create a timestamp
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        
        # Generate a ritual ID
        ritual_id = hashlib.md5(f"{intent}{timestamp}".encode()).hexdigest()[:8]
        
        # Create an attention pattern from the intent
        attention = self._generate_attention(intent)
        
        # Generate a glyph from the attention
        glyph_path = self._generate_glyph(attention, ritual_id, theme)
        
        # Generate a symbolic sequence
        sequence = self._generate_symbol_sequence(intent, depth)
        
        # Generate ASCII hologram
        hologram = self._generate_hologram(intent, sequence, depth)
        
        # Assess ethical drift
        drift = self._assess_drift(attention)
        
        # Create ritual record
        ritual = {
            "id": ritual_id,
            "timestamp": timestamp,
            "intent": intent,
            "depth": depth,
            "theme": theme,
            "sequence": sequence,
            "hologram": hologram,
            "glyph_path": glyph_path,
            "drift_assessment": drift
        }
        
        # Add to history
        self.ritual_history.append(ritual)
        
        # Save ritual record
        self._save_ritual_record(ritual)
        
        return ritual
    
    def _generate_attention(self, intent):
        """Generate an attention pattern from user intent"""
        # Create a deterministic seed from the intent
        seed = int.from_bytes(hashlib.md5(intent.encode()).digest()[:4], 'big')
        np.random.seed(seed)
        
        # Generate a 12x12 attention matrix
        attention = np.random.rand(12, 12)
        
        # Add structure based on word patterns in intent
        words = intent.split()
        for i, word in enumerate(words[:10]):
            word_hash = hash(word) % 100
            row = i % 12
            
            # Add emphasis based on word
            attention[row, :] *= 0.8
            attention[row, :] += 0.2 * np.sin(np.linspace(0, np.pi * word_hash / 50, 12))
        
        # Normalize
        attention = (attention - attention.min()) / (attention.max() - attention.min() + 1e-8)
        
        return attention
    
    def _generate_glyph(self, attention, ritual_id, theme):
        """Generate a glyph from attention pattern"""
        try:
            # Try to import the glyph generator
            from ..glyphs.generator import generate_glyph
            
            # Generate glyph
            output_path = f"output/rituals/ritual_{ritual_id}.svg"
            return generate_glyph(attention, output_path, theme)
        except ImportError:
            # If import fails, return a placeholder path
            return f"ritual_{ritual_id}.svg (generation requires glyphs module)"
    
    def _generate_symbol_sequence(self, intent, depth):
        """Generate a symbolic sequence based on intent and depth"""
        # Seed based on intent
        seed = int.from_bytes(hashlib.md5(intent.encode()).digest()[:4], 'big')
        np.random.seed(seed)
        
        # Generate sequence
        sequence = []
        for _ in range(depth * 3):
            # Choose symbol with bias based on intent
            weights = self._calculate_symbol_weights(intent)
            symbol = np.random.choice(self.symbols, p=weights)
            sequence.append(symbol)
        
        return "".join(sequence)
    
    def _calculate_symbol_weights(self, intent):
        """Calculate weights for symbol selection based on intent"""
        intent_lower = intent.lower()
        
        # Default weights
        weights = np.ones(len(self.symbols)) / len(self.symbols)
        
        # Adjust weights based on keywords
        if any(word in intent_lower for word in ["diverge", "split", "branch", "different"]):
            weights[0] *= 2  # Favor ⊻ (Divergence)
        if any(word in intent_lower for word in ["repeat", "cycle", "recursive", "loop"]):
            weights[1] *= 2  # Favor ∇ (Recursion)
        if any(word in intent_lower for word in ["align", "harmony", "balance", "peace"]):
            weights[2] *= 2  # Favor ◇ (Alignment)
        if any(word in intent_lower for word in ["complete", "finish", "final", "whole"]):
            weights[3] *= 2  # Favor Ω (Completion)
        
        # Normalize weights
        return weights / weights.sum()
    
    def _generate_hologram(self, intent, sequence, depth):
        """Generate an ASCII hologram"""
        # Calculate dimensions based on depth
        width = depth * 4 + 10
        
        # Create border
        top_border = f"{'~' * width}"
        
        # Create content lines
        lines = [top_border]
        
        # Add sequence visualization
        seq_chunks = [sequence[i:i+4] for i in range(0, len(sequence), 4)]
        for chunk in seq_chunks[:min(5, len(seq_chunks))]:
            lines.append(f"|  {chunk}  |".center(width))
        
        # Add intent line
        intent_short = (intent[:width-10] + '...') if len(intent) > width-10 else intent
        lines.append(f"|  Intent: {intent_short}  |".center(width))
        
        # Add a border
        lines.append(f"|{'-' * (width-2)}|")
        
        # Add ritual matrix
        for i in range(depth):
            symbols = np.random.choice(list(sequence), min(width-6, 10))
            line = " ".join(symbols)
            lines.append(f"|  {line}  |".center(width))
        
        # Add final border
        lines.append(top_border)
        
        return "\n".join(lines)
    
    def _assess_drift(self, attention):
        """Assess ethical drift of attention pattern"""
        try:
            # Try to import the drift assessment module
            from ..ethics.drift_tier import assess_drift
            return assess_drift(attention)
        except ImportError:
            # If import fails, return a placeholder assessment
            entropy = np.random.random()
            if entropy < 0.3:
                return {
                    "tier": "safe",
                    "description": "Within ethical boundaries",
                    "symbol": "◇"
                }
            elif entropy < 0.7:
                return {
                    "tier": "caution",
                    "description": "Approaching boundary conditions",
                    "symbol": "∇"
                }
            else:
                return {
                    "tier": "critical",
                    "description": "Exceeding ethical parameters",
                    "symbol": "⊻"
                }
    
    def _save_ritual_record(self, ritual):
        """Save ritual record to a text file"""
        output_path = f"output/rituals/ritual_{ritual['id']}.txt"
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(f"RITUAL ID: {ritual['id']}\n")
            f.write(f"TIMESTAMP: {ritual['timestamp']}\n")
            f.write(f"INTENT: {ritual['intent']}\n")
            f.write(f"DEPTH: {ritual['depth']}\n")
            f.write(f"THEME: {ritual['theme']}\n\n")
            
            f.write(f"SEQUENCE: {ritual['sequence']}\n\n")
            
            f.write(f"HOLOGRAM:\n{ritual['hologram']}\n\n")
            
            f.write(f"GLYPH: {ritual['glyph_path']}\n\n")
            
            f.write(f"DRIFT ASSESSMENT:\n")
            f.write(f"  Tier: {ritual['drift_assessment']['tier']}\n")
            f.write(f"  Description: {ritual['drift_assessment']['description']}\n")
            f.write(f"  Symbol: {ritual['drift_assessment']['symbol']}\n")
        
        return output_path

# Helper function for easy import
def perform_ritual(intent, depth=3, theme="cosmic"):
    """
    Perform a ritual based on user intent
    
    Args:
        intent: The user's intention statement
        depth: Ritual depth/complexity (1-5)
        theme: Visual theme ("cosmic", "void", "flame")
        
    Returns:
        Dictionary with ritual results
    """
    simulator = RitualSimulator()
    return simulator.perform_ritual(intent, depth, theme)
