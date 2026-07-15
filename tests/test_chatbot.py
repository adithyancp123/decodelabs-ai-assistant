"""
Unit tests for the upgraded DecodeLabs AI Assistant.
Verifies preprocessing, tokenization, tiered routing, confidence,
memory state extraction, log creation, and dynamic responses.
"""

import unittest
import sys
import os
import datetime

# Adjust path to import from workspace root
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import config
# Bypass typing animation delays in unit tests for speed
config.TYPING_DELAY = 0.0

from core.preprocessor import sanitize_input, tokenize_input
from core.response_generator import find_intent, get_response
from core.engine import SessionStats, extract_name, setup_logger
from data.intents import INTENT_DATA

class TestChatbotCore(unittest.TestCase):
    def setUp(self):
        """Sets up any necessary parameters before running tests."""
        # Ensure log setup runs
        setup_logger()

    def test_sanitize_input(self):
        """Tests input cleanup (strip and lowercase)."""
        self.assertEqual(sanitize_input("   HELLO WORLD   "), "hello world")
        self.assertEqual(sanitize_input(""), "")
        self.assertEqual(sanitize_input(None), "")

    def test_tokenize_input(self):
        """Tests word splitting and punctuation removal."""
        self.assertEqual(tokenize_input("hello, world!"), ["hello", "world"])
        self.assertEqual(tokenize_input("status check?"), ["status", "check"])
        self.assertEqual(tokenize_input(""), [])
        self.assertEqual(tokenize_input(None), [])

    def test_name_extraction(self):
        """Tests regular-expression introduction parsing."""
        self.assertEqual(extract_name("my name is adithyan"), "Adithyan")
        self.assertEqual(extract_name("i am adithyan"), "Adithyan")
        self.assertEqual(extract_name("call me adithyan"), "Adithyan")
        self.assertEqual(extract_name("name is adithyan!"), "Adithyan")
        self.assertEqual(extract_name("hello general query"), "")

    def test_find_intent_exact(self):
        """Tests tier 1 exact pattern matching and confidence levels."""
        intent, meta = find_intent("hello", ["hello"])
        self.assertEqual(intent, "greeting")
        self.assertEqual(meta["tier"], "Tier 1: Exact Match")
        self.assertEqual(meta["confidence"], "High")

        intent, meta = find_intent("exit", ["exit"])
        self.assertEqual(intent, "exit")
        self.assertEqual(meta["tier"], "Tier 1: Exact Match")
        self.assertEqual(meta["confidence"], "High")

    def test_find_intent_substring(self):
        """Tests tier 2 substring matching and confidence levels."""
        intent, meta = find_intent("can i get some help please", ["can", "i", "get", "some", "help", "please"])
        self.assertEqual(intent, "help")
        self.assertEqual(meta["tier"], "Tier 2: Substring Match")
        self.assertEqual(meta["confidence"], "Medium")

    def test_find_intent_keyword(self):
        """Tests tier 3 keyword overlap checking and confidence levels."""
        intent, meta = find_intent(
            "representative human query", 
            ["representative", "human", "query"]
        )
        self.assertEqual(intent, "support")
        self.assertEqual(meta["tier"], "Tier 3: Keyword Match")
        self.assertEqual(meta["confidence"], "Low")
        self.assertIn("human", meta["matched_keywords"])

    def test_find_intent_fallback(self):
        """Tests tier 4 fallback matching when no intents match."""
        intent, meta = find_intent("randomgibberish12345", ["randomgibberish12345"])
        self.assertEqual(intent, "fallback")
        self.assertEqual(meta["tier"], "Tier 4: Fallback")
        self.assertEqual(meta["confidence"], "Low")

    def test_get_response_static(self):
        """Verifies retrieving standard responses from pool."""
        resp = get_response("greeting")
        self.assertIn(resp, INTENT_DATA["greeting"]["responses"])

    def test_get_response_dynamic_time(self):
        """Verifies dynamic system time response generation."""
        resp = get_response("time")
        self.assertTrue(resp.startswith("The current system time is"))
        
        # Parse time structure from response to check validity
        time_part = resp.split("is ")[1][:-1] # strip period
        try:
            datetime.datetime.strptime(time_part, "%I:%M:%S %p")
        except ValueError:
            self.fail(f"Dynamic time '{time_part}' has invalid format.")

    def test_get_response_dynamic_date(self):
        """Verifies dynamic system date response generation."""
        resp = get_response("date")
        self.assertTrue(resp.startswith("Today's system date is"))
        
        # Parse date structure from response
        date_part = resp.split("is ")[1][:-1]
        now = datetime.datetime.now()
        expected_date_str = now.strftime("%A, %B %d, %Y")
        self.assertEqual(date_part, expected_date_str)

    def test_get_response_memory_name(self):
        """Verifies name declarations and name query memory mapping."""
        memory = {"user_name": "Adithyan"}
        
        # Test name declaration greeting injection
        resp = get_response("name_declaration", memory)
        self.assertTrue(any(resp.format(name="Adithyan") == r or "Adithyan" in resp for r in INTENT_DATA["name_declaration"]["responses"]))
        
        # Test name query lookup
        resp_query = get_response("name_query", memory)
        self.assertEqual(resp_query, "Your name is Adithyan.")
        
        # Test name query when no name exists
        resp_empty = get_response("name_query", {})
        self.assertEqual(resp_empty, "I don't know your name yet! You can tell me by saying 'My name is Adithyan'.")

    def test_farewell_pool_size(self):
        """Asserts at least 10 farewell exit responses exist."""
        self.assertGreaterEqual(len(INTENT_DATA["exit"]["responses"]), 10)

    def test_fallback_pool_size(self):
        """Asserts at least 15 fallback responses exist."""
        self.assertGreaterEqual(len(INTENT_DATA["fallback"]["responses"]), 15)

    def test_session_statistics_tracking(self):
        """Tests accuracy of session statistic events."""
        stats = SessionStats()
        
        # Record recognized questions
        stats.record_query(is_fallback=False)
        stats.record_query(is_fallback=False)
        
        # Record unknown questions
        stats.record_query(is_fallback=True)
        
        self.assertEqual(stats.total_questions, 3)
        self.assertEqual(stats.recognized_questions, 2)
        self.assertEqual(stats.unknown_questions, 1)
        self.assertGreaterEqual(stats.get_duration(), 0.0)

    def test_log_creation(self):
        """Verifies that the log file is created and writable."""
        self.assertTrue(os.path.exists("logs/chatbot.log"))

if __name__ == "__main__":
    unittest.main()
