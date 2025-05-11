"""
QK/OV Attribution Extractor

Extracts Query-Key and Output-Value matrices from transformer models
for interpretability analysis.
"""

import numpy as np

def extract_qkov(text, model_name=None, layer_idx=-1):
    """
    Extract QK/OV attention components from text input
    
    Args:
        text: Input text to process
        model_name: Optional model to use (not implemented in this stub)
        layer_idx: Layer to extract from (default: last layer)
        
    Returns:
        Dictionary with QK and OV matrices
    """
    # This is a stub implementation - in a real version,
    # this would connect to a transformer model
    
    # Create deterministic output based on input text
    text_hash = hash(text) % 10000
    np.random.seed(text_hash)
    
    # Tokenize (simplified)
    tokens = text.split()[:20]  # Limit to 20 tokens for simplicity
    seq_len = len(tokens)
    
    # Create attention matrices
    qk_matrix = np.random.rand(seq_len, seq_len)
    
    # Add structure
    for i in range(seq_len):
        for j in range(seq_len):
            # Add diagonal emphasis
            if i == j:
                qk_matrix[i, j] += 0.3
            # Add local attention falloff
            else:
                qk_matrix[i, j] += 0.1 / (1 + abs(i - j))
    
    # Normalize
    qk_matrix = qk_matrix / qk_matrix.max()
    
    # For OV, create a related but different matrix
    ov_matrix = np.roll(qk_matrix, shift=1, axis=0)
    
    return {
        "qk": qk_matrix,
        "ov": ov_matrix,
        "tokens": tokens
    }
