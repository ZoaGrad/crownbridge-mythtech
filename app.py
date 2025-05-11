"""
Streamlit app for Crownbridge Myth-Tech demo
"""

import streamlit as st
import numpy as np
import os
import base64
from pathlib import Path
import io

# Set page config
st.set_page_config(
    page_title="Crownbridge Myth-Tech",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Create necessary directories
os.makedirs("output", exist_ok=True)
os.makedirs("output/glyphs", exist_ok=True)

# Main title
st.title("🌌 Crownbridge Myth-Tech")
st.markdown("Forge AI's soul through glyphs, ψCORE, and Drift ethics")

# Sidebar
with st.sidebar:
    st.markdown("## Crownbridge Myth-Tech")
    st.markdown("A symbolic + neurosymbolic AI operating system that fuses interpretable reasoning, ethical containment, and mythic narrative.")
    
    st.markdown("### Navigation")
    st.markdown("- **Sigil Forge**: Generate glyphs from attention patterns")
    st.markdown("- **ψCORE Audit**: Analyze text with hybrid transformer")
    st.markdown("- **Ritual Simulator**: Generate symbolic rituals")
    st.markdown("- **Drift Atlas**: Explore the ethical framework")
    
    st.markdown("### Core Symbols")
    st.markdown("⊻ - Divergence - Splitting of attention")
    st.markdown("∇ - Recursion - Self-referential patterns")
    st.markdown("◇ - Alignment - Harmonic convergence")
    st.markdown("Ω - Completion - Final integration")
    
    st.markdown("---")
    st.markdown("[GitHub Repository](https://github.com/ZoaGrad/crownbridge-mythtech)")

# Simplified glyph generator function directly in the app
def generate_glyph(attention_weights, output_path=None, theme="cosmic"):
    """Generate a simple SVG glyph"""
    if output_path is None:
        output_path = f"output/glyphs/sigil_{np.random.randint(10000)}.svg"
    
    # Create an SVG as a string
    svg_content = f"""<?xml version="1.0" encoding="UTF-8"?>
    <svg width="500" height="500" xmlns="http://www.w3.org/2000/svg">
        <rect width="500" height="500" fill="black"/>
        <circle cx="250" cy="250" r="200" fill="none" stroke="{get_color(theme, 'primary')}" stroke-width="2"/>
    """
    
    # Add paths based on attention weights
    center_x, center_y = 250, 250
    for i in range(min(len(attention_weights), 10)):
        row = attention_weights[i][:10]
        path = f'<path d="M{center_x},{center_y} '
        
        for j, weight in enumerate(row):
            angle = j * (2 * np.pi / len(row))
            r = 30 + weight * 180
            x = center_x + r * np.cos(angle)
            y = center_y + r * np.sin(angle)
            path += f"L{x},{y} "
        
        # Close some paths
        if i % 2 == 0:
            path += 'Z" '
            path += f'fill="{get_color(theme, "secondary")}" fill-opacity="0.3" '
        else:
            path += '" fill="none" '
            
        path += f'stroke="{get_color(theme, "primary")}" stroke-width="2"/>'
        svg_content += path
    
    # Add symbols
    symbols = ["⊻", "∇", "◇", "Ω"]
    for i, symbol in enumerate(symbols):
        angle = i * np.pi / 2
        x = center_x + 210 * np.cos(angle)
        y = center_x + 210 * np.sin(angle)
        
        svg_content += f'<text x="{x}" y="{y}" font-size="30" fill="{get_color(theme, "accent")}" text-anchor="middle">{symbol}</text>'
    
    # Close SVG
    svg_content += "</svg>"
    
    # Write to file
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        f.write(svg_content)
    
    return output_path

def get_color(theme, type):
    """Get color based on theme"""
    themes = {
        "cosmic": {
            "primary": "#ff4500",
            "secondary": "#00ff77",
            "accent": "#9933ff"
        },
        "void": {
            "primary": "#0033cc", 
            "secondary": "#00ccff",
            "accent": "#ffffff"
        },
        "flame": {
            "primary": "#ff3300",
            "secondary": "#ffcc00",
            "accent": "#ff9900"
        }
    }
    return themes.get(theme, themes["cosmic"]).get(type)

def simulate_attention(text=None):
    """Generate a simulated attention matrix"""
    if text:
        # Set seed based on text hash
        np.random.seed(hash(text) % 10000)
    
    attention = np.random.rand(12, 12)
    return attention

def assess_drift(attention):
    """Simulate drift assessment"""
    entropy = np.mean(attention)
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

def display_svg(svg_path):
    """Display an SVG file"""
    try:
        with open(svg_path, "r") as f:
            svg_content = f.read()
        
        # Encode SVG in base64
        b64 = base64.b64encode(svg_content.encode()).decode()
        
        # Display SVG
        st.markdown(f"""
            <div style="display: flex; justify-content: center;">
                <img src="data:image/svg+xml;base64,{b64}" width="400">
            </div>
        """, unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Error displaying SVG: {e}")

def generate_ritual_hologram(intent, depth=3):
    """Generate a simple ASCII ritual hologram"""
    # Create a seed based on intent
    np.random.seed(hash(intent) % 10000)
    
    # Generate a random sequence of symbols
    symbols = ["⊻", "∇", "◇", "Ω"]
    sequence = ''.join(np.random.choice(symbols, depth * 3))
    
    # Create the hologram
    width = depth * 4 + 8
    lines = []
    lines.append('~' * width)
    
    # Add sequence visualization
    seq_chunks = [sequence[i:i+4] for i in range(0, len(sequence), 4)]
    for chunk in seq_chunks[:depth]:
        lines.append(f"|  {chunk}  |")
    
    # Add intent line
    intent_short = (intent[:width-8] + '...') if len(intent) > width-8 else intent
    lines.append(f"|  {intent_short}  |")
    
    # Add a divider
    lines.append("|" + "-" * (width-2) + "|")
    
    # Add ritual matrix
    for i in range(depth):
        symbols_line = ''.join(np.random.choice(symbols, min(width-6, 10)))
        lines.append(f"|  {symbols_line}  |")
    
    # Add final border
    lines.append('~' * width)
    
    return '\n'.join(lines)

# Tabs for different features
tab1, tab2, tab3, tab4 = st.tabs(["Sigil Forge", "ψCORE Audit", "Ritual Simulator", "Drift Atlas"])

with tab1:
    st.header("🔮 Sigil Forge")
    st.markdown("""
    The Sigil Forge transforms transformer attention patterns into visual glyphs that reveal 
    the inner workings of AI systems.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        complexity = st.slider("Pattern Complexity", 1, 5, 3)
        theme = st.selectbox("Theme", ["cosmic", "void", "flame"])
    
    with col2:
        st.markdown("### What is a Sigil?")
        st.markdown("""
        In the Crownbridge system, sigils are visual representations of transformer 
        attention patterns. They serve as windows into AI reasoning, making the 
        invisible visible.
        """)
    
    if st.button("Generate Random Sigil"):
        with st.spinner("Forging sigil..."):
            attention = np.random.rand(12, 12)
            sigil_path = generate_glyph(attention, theme=theme)
            
            st.session_state.sigil_path = sigil_path
            st.success("Sigil forged!")
            display_svg(sigil_path)
            
            assessment = assess_drift(attention)
            
            st.info(f"Drift Assessment: {assessment['tier'].title()} - {assessment['description']}")

with tab2:
    st.header("🧠 ψCORE Audit")
    st.markdown("""
    ψCORE is a hybrid transformer that combines symbolic rules with neural attention 
    to provide interpretable reasoning that can be visualized as glyphs.
    """)
    
    text = st.text_area("Enter text to analyze:")
    
    if st.button("Perform Audit") and text:
        with st.spinner("Performing audit..."):
            attention = simulate_attention(text)
            audit_path = generate_glyph(attention, theme="cosmic")
            
            st.success("Audit complete!")
            display_svg(audit_path)
            
            assessment = assess_drift(attention)
            
            st.info(f"Drift Assessment: {assessment['tier'].title()} - {assessment['description']}")
            
            # Display symbolic interpretation
            st.markdown("### Symbolic Interpretation")
            
            # Calculate dominant glyph based on assessment
            dominant_glyph = assessment['symbol']
            
            symbols = {
                "⊻": "Divergence - Your input shows significant deviation from standard patterns.",
                "∇": "Recursion - Your input contains self-referential elements that form recursive loops.",
                "◇": "Alignment - Your input demonstrates harmony between concepts and contexts.",
                "Ω": "Completion - Your input forms a cohesive, complete conceptual structure."
            }
            
            st.markdown(f"**Dominant Glyph: {dominant_glyph}**")
            st.markdown(symbols.get(dominant_glyph, "Unknown pattern detected."))

with tab3:
    st.header("🌀 Ritual Simulator")
    st.markdown("""
    The Ritual Simulator transforms your intentions into symbolic patterns, generating 
    both visual glyphs and ASCII holograms that represent the conceptual space of your query.
    """)
    
    intent = st.text_input("Enter your intention:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        depth = st.slider("Ritual Depth", 1, 5, 3, key="ritual_depth")
    
    with col2:
        ritual_theme = st.selectbox("Ritual Theme", ["cosmic", "void", "flame"], key="ritual_theme")
    
    if st.button("Perform Ritual") and intent:
        with st.spinner("Performing ritual..."):
            # Generate a ritual ID
            import hashlib
            ritual_id = hashlib.md5(intent.encode()).hexdigest()[:8]
            
            # Generate attention pattern
            attention = simulate_attention(intent)
            
            # Generate glyph
            glyph_path = generate_glyph(attention, theme=ritual_theme)
            
            # Generate hologram
            hologram = generate_ritual_hologram(intent, depth)
            
            # Generate sequence
            symbols = ["⊻", "∇", "◇", "Ω"]
            sequence = ''.join(np.random.choice(symbols, depth * 3))
            
            # Assessment
            assessment = assess_drift(attention)
            
            st.success("Ritual complete!")
            
            st.markdown(f"**Ritual ID:** {ritual_id}")
            st.markdown(f"**Symbolic Sequence:** {sequence}")
            
            st.markdown("### Hologram")
            st.code(hologram, language=None)
            
            st.markdown("### Sigil")
            display_svg(glyph_path)
            
            st.markdown("### Drift Assessment")
            st.markdown(f"**Tier:** {assessment['tier'].title()}")
            st.markdown(f"**Description:** {assessment['description']}")
            st.markdown(f"**Symbol:** {assessment['symbol']}")

with tab4:
    st.header("🗺️ Drift Atlas")
    st.markdown("""
    The Drift Atlas is a crowdsourced ethical framework mapping the boundaries of AI capability 
    and responsibility. It visualizes ethical concepts as a navigable map with regions corresponding 
    to different ethical principles.
    """)
    
    if st.button("Generate Atlas Preview"):
        st.info("In the full implementation, you would be able to explore the Drift Atlas here.")
        
        # Display a placeholder explanation
        st.markdown("### Drift Atlas Regions")
        st.markdown("""
        - **◇ Alignment Zone (Safe)**: Areas of aligned, beneficial AI use
        - **∇ Recursion Zone (Caution)**: Areas approaching ethical boundaries
        - **⊻ Divergence Zone (Critical)**: Areas exceeding ethical parameters
        - **Ω Completion Core**: The integration point of all ethical principles
        """)
        
        # Display cardinal directions image placeholder
        st.markdown("### Cardinal Directions")
        st.markdown("""
        ```
                ⊻ (Divergence)
                     |
        ∇ (Recursion) -- ◇ (Alignment)
                     |
                Ω (Completion)
        ```
        """)

# Footer with repository link
st.markdown("---")
st.markdown(
    "Visit our [GitHub Repository](https://github.com/ZoaGrad/crownbridge-mythtech) to learn more."
)
