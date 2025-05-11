"""
Streamlit app for Crownbridge Myth-Tech demo
"""

import streamlit as st
import numpy as np
from PIL import Image
import os
import io
import base64

# Add path for local imports
import sys
sys.path.append(".")

# Try to import our modules
try:
    from src.glyphs.generator import generate_glyph
    from src.psycore.hybrid_transformer import PsiCore
    from src.ethics.drift_tier import assess_drift
    from src.ritual.simulator import perform_ritual
    from src.atlas.visualizer import generate_atlas_visualization
    MODULES_LOADED = True
except ImportError:
    MODULES_LOADED = False

# Create output directories
os.makedirs("output/glyphs", exist_ok=True)
os.makedirs("output/rituals", exist_ok=True)
os.makedirs("output/atlas", exist_ok=True)

# Set page config
st.set_page_config(
    page_title="Crownbridge Myth-Tech",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded",
)

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

# Function to display SVG
def display_svg(svg_path):
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

# Tabs for different features
tab1, tab2, tab3, tab4 = st.tabs(["Sigil Forge", "ψCORE Audit", "Ritual Simulator", "Drift Atlas"])

with tab1:
    st.header("🔮 Sigil Forge")
    
    if not MODULES_LOADED:
        st.warning("Modules not loaded. This is a placeholder for the actual app.")
        st.info("In the full implementation, you would be able to generate glyphs here.")
    else:
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
                st.session_state.attention = np.random.rand(12, 12)
                st.session_state.sigil_path = generate_glyph(
                    st.session_state.attention,
                    theme=theme
                )
                
                st.success("Sigil forged!")
                display_svg(st.session_state.sigil_path)
                
                assessment = assess_drift(st.session_state.attention)
                
                st.info(f"Drift Assessment: {assessment['tier'].title()} - {assessment['description']}")

with tab2:
    st.header("🧠 ψCORE Audit")
    
    if not MODULES_LOADED:
        st.warning("Modules not loaded. This is a placeholder for the actual app.")
        st.info("In the full implementation, you would be able to analyze text here.")
    else:
        st.markdown("""
        ψCORE is a hybrid transformer that combines symbolic rules with neural attention 
        to provide interpretable reasoning that can be visualized as glyphs.
        """)
        
        text = st.text_area("Enter text to analyze:")
        
        if st.button("Perform Audit") and text:
            with st.spinner("Performing audit..."):
                psycore = PsiCore()
                audit_path = psycore.audit(text)
                
                st.success("Audit complete!")
                display_svg(audit_path)
                
                # Get the attention pattern and assess drift
                attention = psycore._extract_attention(text)
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
    
    if not MODULES_LOADED:
        st.warning("Modules not loaded. This is a placeholder for the actual app.")
        st.info("In the full implementation, you would be able to perform symbolic rituals here.")
    else:
        st.markdown("""
        The Ritual Simulator transforms your intentions into symbolic patterns, generating 
        both visual glyphs and ASCII holograms that represent the conceptual space of your query.
        """)
        
        intent = st.text_input("Enter your intention:")
        
        col1, col2 = st.columns(2)
        
        with col1:
