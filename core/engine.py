"""
Engine module for the DecodeLabs AI Assistant.
Orchestrates the main conversation loop, input flow, logging, diagnostics, and session state.
"""

import sys
import time
import datetime
import os
import re
import string
import logging
import config
from typing import Dict, Any
from config import (
    BOT_NAME, 
    AUTHOR,
    VERSION, 
    COLOR_BOT, 
    COLOR_USER, 
    COLOR_SYSTEM, 
    COLOR_INFO,
    COLOR_HIGHLIGHT, 
    COLOR_WARNING,
    COLOR_ERROR,
    COLOR_SUCCESS,
    COLOR_RESET, 
    EXIT_INTENT,
    FALLBACK_INTENT,
    ICON_BOT,
    ICON_USER,
    ICON_SUCCESS,
    ICON_WARNING,
    ICON_ERROR,
    ICON_INFO
)
from core.preprocessor import sanitize_input, tokenize_input
from core.response_generator import find_intent, get_response

# Global logger handle
logger: logging.Logger = logging.getLogger("DecodeLabsChatbot")

def setup_logger() -> logging.Logger:
    """
    Initializes a logging file handler targeting logs/chatbot.log.

    Returns:
        logging.Logger: The configured application logger.
    """
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, "chatbot.log")
    
    logger.setLevel(logging.INFO)
    
    # Avoid attaching handlers repeatedly
    if not logger.handlers:
        handler = logging.FileHandler(log_file, encoding="utf-8")
        formatter = logging.Formatter("[%(asctime)s] %(levelname)s: %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger


class SessionStats:
    """
    Tracks statistics and lightweight session memory for the current interaction.
    """
    def __init__(self) -> None:
        """
        Initializes session start time, diagnostic flag, and memory properties.
        """
        self.start_time: float = time.time()
        self.total_questions: int = 0
        self.recognized_questions: int = 0
        self.unknown_questions: int = 0
        self.user_name: str = ""
        self.first_greeting: str = ""
        self.last_intent: str = ""
        self.message_count: int = 0
        self.debug_mode: bool = False
        self.intent_counts: Dict[str, int] = {}

    def record_query(self, is_fallback: bool) -> None:
        """
        Records a single query event, incrementing relevant counters.

        Args:
            is_fallback (bool): True if intent matched the fallback category.
        """
        self.total_questions += 1
        if is_fallback:
            self.unknown_questions += 1
        else:
            self.recognized_questions += 1

    def get_duration(self) -> float:
        """
        Returns the duration of the session in seconds.

        Returns:
            float: Elapsed time since session start.
        """
        return time.time() - self.start_time

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts session memory parameters to a dictionary context.

        Returns:
            Dict[str, Any]: Representation of the session variables.
        """
        return {
            "user_name": self.user_name,
            "first_greeting": self.first_greeting,
            "last_intent": self.last_intent,
            "message_count": self.message_count,
            "session_duration": self.get_duration()
        }


def extract_name(cleaned_input: str) -> str:
    """
    Extracts title-cased name from common introduction patterns.

    Args:
        cleaned_input (str): Sanitized user query.

    Returns:
        str: Extracted name, title-cased. Empty if not found.
    """
    patterns = [
        r"\bmy name is\s+([a-zA-Z\s]+)",
        r"\bi am\s+([a-zA-Z\s]+)",
        r"\bcall me\s+([a-zA-Z\s]+)",
        r"\bname is\s+([a-zA-Z\s]+)"
    ]
    for pattern in patterns:
        match = re.search(pattern, cleaned_input, re.IGNORECASE)
        if match:
            raw_name = match.group(1).strip()
            # Clean punctuation from the name
            clean_name = raw_name.translate(str.maketrans("", "", string.punctuation))
            return clean_name.strip().title()
    return ""


def print_welcome_banner(startup_time_str: str) -> None:
    """
    Prints the startup welcome screen including DecodeLabs ASCII Art.

    Args:
        startup_time_str (str): The date/time when the chatbot was initialized.
    """
    # 1. Print primary ASCII Banner Logo
    print(f"{COLOR_SYSTEM}{config.ASCII_LOGO}{COLOR_RESET}")
    
    # 2. Render structured system panel information
    sys_info = (
        f" • Version:      {VERSION}\n"
        f" • Author:       {AUTHOR}\n"
        f" • Startup Time: {startup_time_str}\n\n"
        f" Instructions: Ask tech questions or type 'help' for options.\n"
        f" Type 'debug on' to display diagnostic parameters."
    )
    print_bot_response(sys_info, is_info=True)


def print_bot_response(message: str, is_info: bool = False) -> None:
    """
    Renders bot responses inside a beautiful, structured Unicode box.
    Borders and labels print instantly; content types out using character delay.

    Args:
        message (str): The message string to type.
        is_info (bool): True if message is system notification/summary.
    """
    delay: float = getattr(config, "TYPING_DELAY", 0.01)
    
    # Determine styles based on info vs conversational response
    border_color = COLOR_SYSTEM if is_info else COLOR_BOT
    title_color = COLOR_HIGHLIGHT if is_info else COLOR_BOT
    icon = ICON_INFO if is_info else ICON_BOT
    title_text = f"{icon} {BOT_NAME}"
    
    lines = message.split('\n')
    max_line_len = max(len(line) for line in lines) if lines else 0
    box_width = max(max_line_len, len(title_text), 50) + 4
    if box_width > 78:
        box_width = 78
        
    limit = box_width - 4

    # Top border
    print(f"{border_color}╔" + "═" * (box_width - 2) + "╗")
    # Title line
    padded_title = title_text.ljust(limit)
    print(f"║ {title_color}{padded_title}{border_color} ║")
    # Divider line
    print(f"╠" + "═" * (box_width - 2) + "╣")
    
    # Content character-by-character print
    for line in lines:
        while len(line) > limit:
            part = line[:limit]
            sys.stdout.write(f"║ {COLOR_RESET}")
            sys.stdout.flush()
            for char in part:
                sys.stdout.write(char)
                sys.stdout.flush()
                if delay > 0.0:
                    time.sleep(delay)
            print(f"{border_color} ║")
            line = line[limit:]
            
        sys.stdout.write(f"║ {COLOR_RESET}")
        sys.stdout.flush()
        
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            if delay > 0.0:
                time.sleep(delay)
        
        # Pad line end spaces
        rem_spaces = limit - len(line)
        sys.stdout.write(" " * rem_spaces)
        print(f"{border_color} ║")
        
    # Bottom border
    print(f"╚" + "═" * (box_width - 2) + "╝" + COLOR_RESET)


def print_debug_diagnostics(intent: str, meta: Dict[str, Any]) -> None:
    """
    Prints matching details and runtime execution statistics in debug mode.

    Args:
        intent (str): The identified intent key.
        meta (Dict[str, Any]): Diagnostic information metadata dictionary.
    """
    proc_time = meta.get("processing_time", 0.0)
    keywords = meta.get("matched_keywords", [])
    keywords_str = ", ".join(keywords) if keywords else "None"
    
    debug_msg = (
        f" {ICON_INFO} [DEBUG DIAGNOSTICS]\n"
        f"  • Detected Intent:  {intent}\n"
        f"  • Matching Tier:    {meta.get('tier')}\n"
        f"  • Confidence:       {meta.get('confidence')}\n"
        f"  • Matched Keywords: [{keywords_str}]\n"
        f"  • Processing Time:  {proc_time:.6f} seconds"
    )
    print_bot_response(debug_msg, is_info=True)


def print_session_statistics(stats: SessionStats) -> None:
    """
    Displays the formatted session statistics inside a beautiful Unicode box upon exit.

    Args:
        stats (SessionStats): The tracker object containing session details.
    """
    duration: float = stats.get_duration()
    minutes: int = int(duration // 60)
    seconds: int = int(duration % 60)
    duration_str: str = f"{minutes}m {seconds}s" if minutes > 0 else f"{seconds}s"
    
    # Determine Favorite Intent
    fav_intent = "None"
    if stats.intent_counts:
        fav_intent = max(stats.intent_counts, key=stats.intent_counts.get)
        fav_intent = fav_intent.replace("_", " ").title()
        
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    summary_text = (
        f" {ICON_SUCCESS} Session Summary statistics:\n"
        f"  • Total Queries Processed:     {stats.total_questions}\n"
        f"  • Recognized Commands/Intents: {stats.recognized_questions}\n"
        f"  • Unknown Queries (Fallbacks): {stats.unknown_questions}\n"
        f"  • Favorite Intent Category:    {fav_intent}\n"
        f"  • Session Active Duration:     {duration_str}\n"
        f"  • Current System Date/Time:    {current_date}\n\n"
        f" Thank you for using DecodeLabs AI Assistant!\n"
        f" We look forward to assisting you in your next session."
    )
    print_bot_response(summary_text, is_info=True)


def run_chatbot_loop() -> None:
    """
    Coordinates the primary interaction loop. Runs continuously until 
    an exit signal/command is detected or Ctrl+C / EOF is received.
    """
    # Force UTF-8 encoding for standard streams to prevent UnicodeEncodeError on Windows CP1252 consoles
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass
    if hasattr(sys.stderr, "reconfigure"):
        try:
            sys.stderr.reconfigure(encoding="utf-8")
        except Exception:
            pass

    # Configure logs
    setup_logger()
    logger.info("Session started.")

    stats = SessionStats()
    startup_time_str: str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Render welcome art and system banners
    print_welcome_banner(startup_time_str)
    
    # Display smart startup welcome prompt
    print_bot_response(f"{ICON_SUCCESS} Welcome to your first AI Assistant session. How can I serve you?", is_info=True)
    print()
    
    while True:
        try:
            # Prompt user input
            raw_input = input(f"{COLOR_USER}{ICON_USER} You > {COLOR_RESET}")
            
            # Sanitize and tokenize
            cleaned_input = sanitize_input(raw_input)
            tokens = tokenize_input(cleaned_input)
            
            # If the user typed only whitespace, ignore
            if not cleaned_input:
                continue
            
            # Intercept Debug Commands
            if cleaned_input == "debug on":
                stats.debug_mode = True
                print_bot_response(f"{ICON_SUCCESS} Debug mode has been ENABLED. Diagnostic stats will be displayed.", is_info=True)
                logger.info("Debug mode enabled by user.")
                continue
            
            if cleaned_input == "debug off":
                stats.debug_mode = False
                print_bot_response(f"{ICON_SUCCESS} Debug mode has been DISABLED.", is_info=True)
                logger.info("Debug mode disabled by user.")
                continue

            # Clear Screen command handling
            if cleaned_input in ("clear", "cls"):
                os.system('cls' if os.name == 'nt' else 'clear')
                print_welcome_banner(startup_time_str)
                logger.info("Terminal screen cleared.")
                continue
            
            # Match intent and gather diagnostic metrics
            intent, meta = find_intent(cleaned_input, tokens)
            
            # Track memory parameters
            stats.message_count += 1
            stats.last_intent = intent
            
            # Extract name and save to memory
            if intent == "name_declaration":
                extracted_name = extract_name(cleaned_input)
                if extracted_name:
                    stats.user_name = extracted_name
                    
            # Capture first greeting string
            if intent == "greeting" and not stats.first_greeting:
                stats.first_greeting = raw_input

            # Record query metrics (ignoring utility commands: clear, exit, debug)
            if intent != EXIT_INTENT:
                stats.record_query(is_fallback=(intent == FALLBACK_INTENT))
                stats.intent_counts[intent] = stats.intent_counts.get(intent, 0) + 1
            
            # Print diagnostic metadata if debug is enabled
            if stats.debug_mode:
                print_debug_diagnostics(intent, meta)

            # Retrieve response with memory context
            response = get_response(intent, stats.to_dict())
            
            # Append smart suggestions if intent was unrecognized
            if intent == FALLBACK_INTENT:
                suggestions = (
                    f"\n\n{COLOR_WARNING}{ICON_WARNING} Command Suggestions:{COLOR_RESET}\n"
                    "  Try asking about:\n"
                    "   • help       • about      • python\n"
                    "   • ai         • internship • project"
                )
                response += suggestions
            
            # Display response via typing simulation
            print_bot_response(response)
            print()  # Spacer line
            
            # Log turn details
            logger.info("Input: '%s' | Intent: '%s' | Response: '%s'", raw_input, intent, response.replace('\n', ' '))

            # Exit loop if exit command triggered
            if intent == EXIT_INTENT:
                print_session_statistics(stats)
                logger.info("Session ended normally. Active duration: %.2f seconds.", stats.get_duration())
                break
                
        except (KeyboardInterrupt, EOFError):
            # Gracefully catch interrupt signals
            print(f"\n\n{COLOR_WARNING}{ICON_WARNING} [System Info] Session interrupted by user.{COLOR_RESET}")
            exit_response = get_response(EXIT_INTENT)
            print_bot_response(exit_response)
            print_session_statistics(stats)
            logger.info("Session interrupted by user. Active duration: %.2f seconds.", stats.get_duration())
            break
            
        except Exception as err:
            # Robust catch-all to prevent app crashing
            print(f"\n{COLOR_ERROR}{ICON_ERROR} [Error] An unexpected error occurred: {err}{COLOR_RESET}")
            print(f"{COLOR_INFO}Resuming conversation loop...{COLOR_RESET}\n")
            logger.error("Error encountered: '%s'", str(err))
            continue
