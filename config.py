# Configuration settings for DecodeLabs AI Assistant

# ANSI escape codes for professional console styling
COLOR_BOT = "\033[92m"         # Bright Green
COLOR_USER = "\033[94m"        # Bright Blue
COLOR_SYSTEM = "\033[96m"      # Cyan (Information)
COLOR_INFO = "\033[96m"        # Cyan (Information)
COLOR_HIGHLIGHT = "\033[95m"    # Magenta
COLOR_WARNING = "\033[93m"      # Yellow
COLOR_ERROR = "\033[91m"        # Red
COLOR_SUCCESS = "\033[92m"      # Bright Green (Success matches BOT)
COLOR_RESET = "\033[0m"        # Reset formatting

# UI Unicode Icons
ICON_BOT = "🤖"
ICON_USER = "👤"
ICON_SUCCESS = "✓"
ICON_WARNING = "⚠"
ICON_ERROR = "✗"
ICON_INFO = "ℹ"

# Bot profile
BOT_NAME = "DecodeLabs AI Assistant"
AUTHOR = "DecodeLabs Team"
VERSION = "1.0"

# Typing animation delay (seconds per character)
# Can be set to 0.0 in tests for instant output
TYPING_DELAY = 0.01

# Central ASCII Logo Banner
ASCII_LOGO = """
  _____                     _      _          _          
 |  __ \\                   | |    | |        | |         
 | |  | | ___  ___ ___   __| | ___| |     __ _| |__  ___ 
 | |  | |/ _ \\/ __/ _ \\ / _` |/ _ \\ |    / _` | '_ \\/ __|
 | |__| |  __/ (_| (_) | (_| |  __/ |___| (_| | |_) \\__ \\
 |_____/ \\___|\\___\\___/ \\__,_|\\___|______\\__,_|_.__/|___/
                      AI ASSISTANT v1.0
"""

# Matching limits
MATCH_THRESHOLD = 0.5  # Keyword overlap threshold ratio if matching tokens

# Fallback configuration
FALLBACK_INTENT = "fallback"
EXIT_INTENT = "exit"
