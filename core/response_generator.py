"""
Response generation module for the DecodeLabs AI Assistant.
Performs tiered matching using intent dictionaries, records metrics, 
and dynamically resolves session-dependent queries.
"""

import time
import datetime
import random
from typing import List, Dict, Any, Tuple
from data.intents import INTENT_DATA
from config import FALLBACK_INTENT

def find_intent(cleaned_input: str, tokens: List[str]) -> Tuple[str, Dict[str, Any]]:
    """
    Finds the matched intent key for the given user input using tiered lookup rules
    and records diagnostics metadata.

    Args:
        cleaned_input (str): The sanitized, lowercase user input string.
        tokens (List[str]): The tokenized word list.

    Returns:
        Tuple[str, Dict[str, Any]]: The matched intent key and a diagnostic metadata dictionary.
    """
    start_time: float = time.perf_counter()
    
    # Initialize diagnostics metadata
    meta: Dict[str, Any] = {
        "tier": "Tier 4: Fallback",
        "confidence": "Low",
        "matched_keywords": [],
        "processing_time": 0.0
    }

    # 1. Tier 1: Exact Match Check (Highest Priority)
    for intent, data in INTENT_DATA.items():
        if "patterns" in data and cleaned_input in data["patterns"]:
            meta["tier"] = "Tier 1: Exact Match"
            meta["confidence"] = "High"
            meta["processing_time"] = time.perf_counter() - start_time
            return intent, meta

    # 2. Tier 2: Substring Pattern Match Check
    best_substring_intent = None
    longest_match_len = 0
    
    for intent, data in INTENT_DATA.items():
        if "patterns" in data:
            for pattern in data["patterns"]:
                if pattern in cleaned_input:
                    # Select the intent matching the longest pattern for higher accuracy
                    if len(pattern) > longest_match_len:
                        longest_match_len = len(pattern)
                        best_substring_intent = intent
                        
    if best_substring_intent:
        meta["tier"] = "Tier 2: Substring Match"
        meta["confidence"] = "Medium"
        meta["processing_time"] = time.perf_counter() - start_time
        return best_substring_intent, meta

    # 3. Tier 3: Keyword Overlap Check (Token set intersection)
    best_keyword_intent = None
    max_overlap = 0
    matched_kws: List[str] = []
    
    for intent, data in INTENT_DATA.items():
        if "keywords" in data:
            overlap = set(tokens).intersection(set(data["keywords"]))
            if len(overlap) > max_overlap:
                max_overlap = len(overlap)
                best_keyword_intent = intent
                matched_kws = list(overlap)

    if best_keyword_intent and max_overlap > 0:
        meta["tier"] = "Tier 3: Keyword Match"
        meta["confidence"] = "Low"
        meta["matched_keywords"] = sorted(matched_kws)
        meta["processing_time"] = time.perf_counter() - start_time
        return best_keyword_intent, meta

    # 4. Tier 4: Fallback
    meta["processing_time"] = time.perf_counter() - start_time
    return FALLBACK_INTENT, meta


def get_response(intent_key: str, memory: Dict[str, Any] = None) -> str:
    """
    Selects a random response string matching the given intent key, 
    injecting session memory parameters where applicable.

    Args:
        intent_key (str): The key representing the matched intent.
        memory (Dict[str, Any]): Lightweight session memory structure.

    Returns:
        str: The selected response message.
    """
    # Programmatic Dynamic Intents
    if intent_key == "time":
        current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
        return f"The current system time is {current_time}."
    
    if intent_key == "date":
        current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        return f"Today's system date is {current_date}."

    if intent_key == "name_declaration" and memory:
        user_name = memory.get("user_name", "friend")
        responses = INTENT_DATA.get("name_declaration", {}).get("responses", ["Hello {name}!"])
        return random.choice(responses).format(name=user_name)

    if intent_key == "name_query" and memory:
        user_name = memory.get("user_name")
        if user_name:
            return f"Your name is {user_name}."
        return "I don't know your name yet! You can tell me by saying 'My name is Adithyan'."

    intent_info = INTENT_DATA.get(intent_key)
    if not intent_info or "responses" not in intent_info:
        # Fallback response retrieval
        fallback_info = INTENT_DATA.get(FALLBACK_INTENT, {})
        responses = fallback_info.get("responses", ["I didn't quite catch that. Can you rephrase?"])
        return random.choice(responses)

    return random.choice(intent_info["responses"])
