"""
Streamlit app for Crownbridge Myth-Tech demo
"""

import streamlit as st
import numpy as np
from PIL import Image
import os
import base64

# Add path for local imports
import sys
sys.path.append(".")

# Try to import our modules
try:
    from src.glyphs.generator import generate_glyph
    from src.psycore.hybrid_transformer import PsiCore
    from src.ethics.drift_tier import assess_drift
    MODULES_LOADED = True
except ImportError:
    MODULES_LOADED = False

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

# Tabs for different features
tab1, tab2, tab3 = st.tabs(["Sigil Forge", "ψCORE Audit", "Drift Atlas"])

# Function to display SVG
def display_svg(svg_path):
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

with tab1:
    st.header("🔮 Sigil Forge")
    
    if not MODULES_LOADED:
        st.warning("Modules not loaded. This is a placeholder for the actual app.")
        st.info("In the full implementation, you would be able to generate glyphs here.")
    else:
        complexity = st.slider("Recursion Depth", 1, 5, 3)
        theme = st.selectbox("Theme", ["cosmic", "void", "flame"])
        
        if st.button("Generate Random Sigil"):
            st.session_state.attention = np.random.rand(12, 12)
            st.session_state.sigil_path = generate_glyph(
                st.session_state.attention,
                theme=theme
            )
            
            display_svg(st.session_state.sigil_path)
            
            assessment = assess_drift(st.session_state.attention)
            
            st.info(f"Drift Assessment: {assessment['tier'].title()} - {assessment['description']}")

with tab2:
    st.header("🧠 ψCORE Audit")
    
    if not MODULES_LOADED:
        st.warning("Modules not loaded. This is a placeholder for the actual app.")
        st.info("In the full implementation, you would be able to analyze text here.")
    else:
        text = st.text_area("Enter text to analyze:")
        
        if st.button("Perform Audit") and text:
            psycore = PsiCore()
            audit_path = psycore.audit(text)
            
            display_svg(audit_path)
            
            # Get the attention pattern and assess drift
            attention = psycore._extract_attention(text)
            assessment = assess_drift(attention)
            
            st.info(f"Drift Assessment: {assessment['tier'].title()} - {assessment['description']}")

with tab3:
    st.header("🗺️ Drift Atlas")
    
    st.markdown("""
    The Drift Atlas is a crowdsourced ethical framework mapping the boundaries of AI capability and responsibility.
    
    In the complete implementation, this tab would display:
    
    1. A visual map of the ethical landscape
    2. Community-contributed ethical principles
    3. Tools to navigate and contribute to the Atlas
    
    For now, we present the core principles of the Drift Atlas:
    """)
    
    st.markdown("""
    | Symbol | Principle | Description |
    |--------|-----------|-------------|
    | ⊻ | Divergence | Ethical boundaries must be clearly defined |
    | ∇ | Recursion | Systems must be self-examining and transparent |
    | ◇ | Alignment | AI goals must align with human values |
    | Ω | Completion | The full impact of AI systems must be considered |
    """)

# Footer with repository link
st.markdown("---")
st.markdown(
    "Visit our [GitHub Repository](https://github.com/YOUR_USERNAME/crownbridge-mythtech) to learn more."
)
