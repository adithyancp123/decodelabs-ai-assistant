"""
Input preprocessing module for the DecodeLabs AI Assistant.
Handles raw string sanitization (lowercase, strip) and tokenization.
"""

import string
from typing import List

def sanitize_input(raw_input: str) -> str:
    """
    Sanitizes raw user input.
    Trims whitespace and converts to lowercase.

    Args:
        raw_input (str): The raw string from the user.

    Returns:
        str: The sanitized lowercase string.
    """
    if not raw_input:
        return ""
    return raw_input.strip().lower()

def tokenize_input(cleaned_input: str) -> List[str]:
    """
    Splits the cleaned input into a list of word tokens.
    Removes standard punctuation characters.

    Args:
        cleaned_input (str): The sanitized, lowercase string.

    Returns:
        List[str]: Tokenized words.
    """
    if not cleaned_input:
        return []
    
    # Remove punctuation
    translator = str.maketrans("", "", string.punctuation)
    no_punctuation = cleaned_input.translate(translator)
    
    # Split by whitespace
    return no_punctuation.split()
