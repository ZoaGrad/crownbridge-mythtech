"""
Input Sanitizer - Privacy-preserving processing for AI inputs
"""

import re
import hashlib
from typing import Dict, List, Tuple, Optional

class Sanitizer:
    """
    Sanitizes input text to remove sensitive information
    before processing with AI systems
    """
    
    def __init__(self):
        """Initialize the sanitizer with pattern recognition"""
        # PII detection patterns
        self.pii_patterns = {
            "email": r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
            "phone": r'\b(\+\d{1,2}\s?)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}\b',
            "ssn": r'\b\d{3}-\d{2}-\d{4}\b',
            "credit_card": r'\b\d{4}[ -]?\d{4}[ -]?\d{4}[ -]?\d{4}\b',
            "address": r'\b\d+\s+[A-Za-z0-9\s,]+\b(?:street|st|avenue|ave|road|rd|highway|hwy|square|sq|trail|trl|drive|dr|court|ct|parkway|pkwy|circle|cir|boulevard|blvd)\b',
        }
        
        # Replacement token format
        self.replacement_format = "[REDACTED:{0}:{1}]"
        
        # Storage for redacted items
        self.redacted_items = {}
    
    def clean(self, text: str) -> str:
        """
        Sanitize the input text by removing/replacing sensitive information
        
        Args:
            text: Text to sanitize
            
        Returns:
            Sanitized text with sensitive information replaced
        """
        if not text:
            return ""
        
        # Reset redacted items for new cleaning operation
        self.redacted_items = {}
        
        # Process text for each pattern
        sanitized_text = text
        for pii_type, pattern in self.pii_patterns.items():
            # Find all matches
            matches = re.finditer(pattern, sanitized_text, re.IGNORECASE)
            
            # Replace each match with a token
            offset = 0
            for i, match in enumerate(matches):
                # Create a unique identifier for this redacted item
                item_id = self.hash_content(match.group() + str(i))
                
                # Store the original value mapped to this ID
                self.redacted_items[item_id] = match.group()
                
                # Create the replacement token
                replacement = self.replacement_format.format(pii_type, item_id)
                
                # Calculate positions with offset
                start = match.start() + offset
                end = match.end() + offset
                
                # Replace in the text
                sanitized_text = sanitized_text[:start] + replacement + sanitized_text[end:]
                
                # Update offset for future replacements
                offset += len(replacement) - (end - start)
        
        return sanitized_text
    
    def restore(self, sanitized_text: str) -> str:
        """
        Restore redacted items in sanitized text
        
        Args:
            sanitized_text: Text with [REDACTED] placeholders
            
        Returns:
            Text with original values restored
        """
        restored_text = sanitized_text
        
        # Find all redaction tokens
        pattern = r'\[REDACTED:([^:]+):([^\]]+)\]'
        matches = re.finditer(pattern, restored_text)
        
        # Replace each token with the original value
        offset = 0
        for match in matches:
            # Extract token parts
            pii_type = match.group(1)
            item_id = match.group(2)
            
            # Get the original value
            if item_id in self.redacted_items:
                original = self.redacted_items[item_id]
                
                # Replace the token
                start = match.start() + offset
                end = match.end() + offset
                restored_text = restored_text[:start] + original + restored_text[end:]
                
                # Update offset
                offset += len(original) - (end - start)
        
        return restored_text
    
    def hash_content(self, content: str) -> str:
        """Create a short hash for content identification"""
        return hashlib.md5(content.encode()).hexdigest()[:8]

# Helper function for easy import
def sanitize_text(text: str) -> tuple:
    """
    Sanitize text and return both sanitized text and sanitizer for restoration
    
    Args:
        text: Input text to sanitize
        
    Returns:
        Tuple of (sanitized_text, sanitizer)
    """
    sanitizer = Sanitizer()
    sanitized = sanitizer.clean(text)
    return sanitized, sanitizer
