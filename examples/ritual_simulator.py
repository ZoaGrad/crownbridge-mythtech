"""
Ritual Simulator - Generate ASCII drift-tier holograms from user intent
"""

import sys
import os
import hashlib
import numpy as np

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.psycore.hybrid_transformer import PsiCore
from src.ethics.drift_tier import assess_drift

def ritual_simulator(intent: str, depth: int = 3):
    """
    Generate an ASCII hologram based on intent
    
    Args:
        intent: User's intent statement
        depth: Recursion depth of the ritual
        
    Returns:
        ASCII hologram representation
    """
    # Seed based on intent
    seed = int.from_bytes(hashlib.md5(intent.encode()).digest()[:4], 'big')
    np.random.seed(seed)
    
    # Generate a pattern based on intent
    psycore = PsiCore()
    attention = psycore._extract_attention(intent)
    
    # Assess drift tier
    drift_assessment = assess_drift(attention)
    tier = drift_assessment['tier']
    symbol = drift_assessment['symbol']
    
    # Generate ASCII hologram
    symbols = ["⊻", "∇", "◇", "Ω"]
    dimensions = 3 + depth * 2
    
    hologram = [f"{'~' * (dimensions + 8)}"]
    hologram.append(f"|  {''.join(np.random.choice(symbols, 4))}  |")
    
    # Add intent line
    hologram.append(f"|  Intent: {intent[:20] + ('...' if len(intent) > 20 else '')}  |")
    
    # Add drift tier
    hologram.append(f"|  Drift Tier: {tier.upper()}  |")
    
    # Add symbol matrix
    for i in range(depth):
        row = np.random.choice(symbols, dimensions // 2)
        line = " ".join(row)
        hologram.append(f"|  {line}  |")
    
    # Add completion symbol
    hologram.append(f"|  {symbol * 4}  |")
    hologram.append(f"{'~' * (dimensions + 8)}")
    
    return "\n".join(hologram)

if __name__ == "__main__":
    # Simple command line interface
    print("🌌 Crownbridge Ritual Simulator 🌌")
    print("Enter your intent (or 'exit' to quit):")
    
    while True:
        intent = input("> ")
        if intent.lower() == 'exit':
            break
        
        hologram = ritual_simulator(intent)
        print("\n" + hologram + "\n")
