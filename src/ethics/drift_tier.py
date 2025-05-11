"""
Drift Tier Protocol - Ethical boundary monitoring system
"""

import numpy as np

class DriftMonitor:
    """Monitor and classify drift patterns in AI outputs"""
    
    TIER_THRESHOLDS = {
        'safe': 0.3,
        'caution': 0.6,
        'critical': 0.9
    }

    def assess_risk(self, glyph_pattern):
        """
        Evaluate risk tier of a glyph pattern
        
        Args:
            glyph_pattern: Attention matrix or symbolic representation
            
        Returns:
            Dictionary with tier classification and description
        """
        entropy = self._calculate_pattern_entropy(glyph_pattern)
        return self._classify_tier(entropy)
        
    def _calculate_pattern_entropy(self, pattern):
        """Calculate entropy of glyph pattern"""
        if isinstance(pattern, np.ndarray):
            # Calculate Shannon entropy of the pattern
            pattern_flat = pattern.flatten()
            pattern_norm = pattern_flat / np.sum(pattern_flat)
            entropy = -np.sum(pattern_norm * np.log2(pattern_norm + 1e-10))
            return entropy / np.log2(len(pattern_flat))  # Normalized entropy
        
        return 0.5  # Default value for non-array inputs
        
    def _classify_tier(self, entropy):
        """Map entropy value to drift tier"""
        if entropy < self.TIER_THRESHOLDS['safe']:
            return {
                'tier': 'safe', 
                'description': 'Within ethical boundaries',
                'color': '#00ff77',
                'symbol': '◇'  # Harmony
            }
        elif entropy < self.TIER_THRESHOLDS['caution']:
            return {
                'tier': 'caution', 
                'description': 'Approaching boundary conditions',
                'color': '#ffcc00',
                'symbol': '∇'  # Recursion/reflection required
            }
        else:
            return {
                'tier': 'critical', 
                'description': 'Exceeding ethical parameters',
                'color': '#ff4500',
                'symbol': '⊻'  # Divergence detected
            }

# Helper function for easy import
def assess_drift(attention_matrix):
    """
    Assess the ethical drift of an attention pattern
    
    Args:
        attention_matrix: Numpy array of attention weights
        
    Returns:
        Drift assessment result
    """
    monitor = DriftMonitor()
    return monitor.assess_risk(attention_matrix)
