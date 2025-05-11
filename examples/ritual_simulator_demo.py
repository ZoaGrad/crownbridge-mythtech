"""
Ritual Simulator Demo - Interactive ritual simulation
"""

import sys
import os

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.ritual.simulator import perform_ritual

def main():
    """Run an interactive ritual simulation"""
    print("🌌 Crownbridge Ritual Simulator 🌌")
    print("Enter your intent to forge a sigil and generate a ritual hologram.")
    
    while True:
        # Get user intent
        intent = input("\nEnter your intent (or 'exit' to quit):\n> ")
        
        if intent.lower() == 'exit':
            break
        
        if not intent.strip():
            print("Please enter a meaningful intent.")
            continue
        
        # Get ritual depth
        depth = 3  # Default
        try:
            depth_input = input("Enter ritual depth (1-5) [default: 3]: ")
            if depth_input.strip():
                depth = int(depth_input)
                if depth < 1 or depth > 5:
                    raise ValueError("Depth must be between 1 and 5.")
        except ValueError as e:
            print(f"Invalid depth: {e}")
            print("Using default depth of 3.")
            depth = 3
        
        # Get theme
        theme = "cosmic"  # Default
        theme_input = input("Choose theme (cosmic, void, flame) [default: cosmic]: ")
        if theme_input.strip().lower() in ["cosmic", "void", "flame"]:
            theme = theme_input.strip().lower()
        
        print("\n🔮 Performing ritual...")
        
        try:
            # Perform the ritual
            ritual = perform_ritual(intent, depth, theme)
            
            # Display results
            print("\n✨ Ritual complete! ✨")
            print(f"Ritual ID: {ritual['id']}")
            print(f"Symbolic Sequence: {ritual['sequence']}")
            print("\nHologram:")
            print(ritual['hologram'])
            
            print(f"\nGlyph generated: {ritual['glyph_path']}")
            print(f"To view the glyph, open the file: {os.path.abspath(ritual['glyph_path'])}")
            
            print("\nDrift Assessment:")
            print(f"  Tier: {ritual['drift_assessment']['tier']}")
            print(f"  Description: {ritual['drift_assessment']['description']}")
            print(f"  Symbol: {ritual['drift_assessment']['symbol']}")
            
            print(f"\nRitual record saved: output/rituals/ritual_{ritual['id']}.txt")
            
        except Exception as e:
            print(f"Error performing ritual: {e}")
    
    print("\nThank you for using the Crownbridge Ritual Simulator.")

if __name__ == "__main__":
    main()
