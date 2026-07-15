# DecodeLabs AI Assistant

[![Python Version](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)]()
[![Code Quality](https://img.shields.io/badge/code%20quality-PEP8%20compliant-orange.svg)]()

An industrial-quality, rule-based AI Assistant designed for the **DecodeLabs AI Internship**. This project is a production-level console application that showcases clean architecture, structured dictionary-based intent matching, session memory context, file transactions logging, and automated test-driven verification.

---

## ╔════════════════════════════════════════════════════════════╗
## ║ 🤖 Project Features & Overview                          ║
## ╚════════════════════════════════════════════════════════════╝

The system acts as an interactive command-line assistant supporting 28 intent categories (including tech support, pricing, weather info, jokes, quotes, programming concepts, and date/time commands). It avoids inefficient and hard-to-maintain `if-elif` logic ladders, using a structured tiered search engine instead.

### 📋 Feature Matrix

| Feature | Description | Implementation Status |
| :--- | :--- | :---: |
| **Synonym Matcher** | Smart synonym resolution supporting multiple keyword phrases. | **✓ Ready** |
| **Rich Terminal UI** | Clean Unicode box enclosing borders, status panels, and console art. | **✓ Ready** |
| **AI Typing Animation** | Simulates human response generation character-by-character. | **✓ Ready** |
| **Dynamic Command Resolvers** | Programs runtime system time, date, and terminal clear actions. | **✓ Ready** |
| **In-Memory Session Store** | Tracks user name, last query intent, and conversation count. | **✓ Ready** |
| **Diagnostic Diagnostics** | Debug mode showing intent, tiers, keyword matches, and speeds. | **✓ Ready** |
| **Event Logging** | Standard logging writing transaction trails to `logs/chatbot.log`. | **✓ Ready** |
| **Robust Error Handlers** | Suppresses stack traces on interrupt signals (Ctrl+C / Ctrl+D). | **✓ Ready** |
| **Coverage Suites** | Automated suite with 15 test checkpoints verifying features. | **✓ Ready** |

---

## ╔════════════════════════════════════════════════════════════╗
## ║ 📂 Project Directory Structure                         ║
## ╚════════════════════════════════════════════════════════════╝

```text
decodelabs-ai-assistant/
│
├── main.py                     # Entry point to launch the CLI
├── config.py                   # Central settings, ASCII art, and colors
├── LICENSE                     # MIT Open Source License
├── CHANGELOG.md                # Milepost logs tracking system changes
├── CONTRIBUTING.md             # Guidelines for making contributions
├── CODE_OF_CONDUCT.md          # Contributor Covenant Code of Conduct
├── README.md                   # Comprehensive repository documentation
│
├── core/                       # Package housing orchestrator mechanics
│   ├── __init__.py
│   ├── engine.py               # Main conversation loop, welcome screen, statistics
│   ├── preprocessor.py         # Strips whitespace, tokenizes input, regex names
│   └── response_generator.py   # Intent confidence scores, dynamic responses
│
├── data/                       # Config schemas and dictionaries
│   ├── __init__.py
│   └── intents.py              # Dictionaries containing patterns, keys, responses
│
├── logs/                       # Automated transaction logger directory
│   └── chatbot.log             # Output trails mapping inputs to answers
│
├── assets/                     # Media attachments directory
│   └── screenshots/            # Contains screenshots of application runs
│       ├── startup.png         # [Placeholder] Startup header banner
│       ├── conversation.png    # [Placeholder] Conversation interactions
│       ├── debug.png           # [Placeholder] Debug mode runs
│       └── stats.png           # [Placeholder] Terminal exit statistics
│
└── tests/                      # Testing package
    ├── __init__.py
    └── test_chatbot.py         # Automation unit test suite
```

---

## ╔════════════════════════════════════════════════════════════╗
## ║ 🛠️ Architectural Diagram (ASCII)                         ║
## ╚════════════════════════════════════════════════════════════╝

The diagram below traces the data flow from user keystroke input to console rendering and file logging:

```text
     +-------------------+
     | User Prompt Input |
     +-------------------+
               |
               v
     +-------------------+
     |  preprocessor.py  |  <--- Strips whitespace/punctuation
     +-------------------+
               |
               v
   +-----------------------+
   | response_generator.py | <--- Searches dictionary intents
   +-----------------------+
               |
               +---> Tier 1: Exact Matching (High Confidence)
               +---> Tier 2: Substring Matching (Medium Confidence)
               +---> Tier 3: Keyword Intersection (Low Confidence)
               +---> Tier 4: Fallback Default (Low Confidence)
               |
               v
     +-------------------+
     |     engine.py     |  <--- Formats Unicode borders & text animation
     +-------------------+
               |
        +------+------+
        |             |
        v             v
+--------------+ +------------+
| Console View | | logs/      | <--- Event tracking
+--------------+ | chatbot.log|
                 +------------+
```

### Why Dictionary Matching is Better than If-Elif Chains
- **$O(1)$ Time Complexity**: Flat lookups resolve matching immediately.
- **Separation of Concerns**: Configurations remain independent of execution flow.
- **Scalability**: Adding new commands is as simple as adding an entry to `intents.py`, without touching code.

---

## ╔════════════════════════════════════════════════════════════╗
## ║ ⚙️ Technologies Used                                      ║
## ╚════════════════════════════════════════════════════════════╝

- **Language**: Python 3.9+ (utilizing type hints, collections, regex libraries)
- **Standard Library Modules**:
  - `sys` & `os`: Terminal interaction and platform-agnostic commands (screen clearing)
  - `time` & `datetime`: Query latency tracking and dynamic date-time formatting
  - `random`: Dynamic, varied responses selection
  - `re`: Introduction name-extraction parsing
  - `logging`: File audit trail updates under `logs/chatbot.log`
  - `unittest`: Component-level unit testing verification

---

## ╔════════════════════════════════════════════════════════════╗
## ║ 🎓 Learning Outcomes                                      ║
## ╚════════════════════════════════════════════════════════════╝

Building this project provided several critical software engineering takeaways:
1. **Clean Code Isolation**: Discovered how to separate configs (`config.py`), metadata assets (`intents.py`), text sanitization (`preprocessor.py`), matching algorithms (`response_generator.py`), and console orchestrators (`engine.py`).
2. **Computational Efficiency**: Implemented dictionary lookups to avoid $O(N)$ branch matching time penalties.
3. **State Management**: Built memory-tracking containers within session loops without database overhead.
4. **Resiliency**: Handled platform limits (clearing Windows vs POSIX terminals) and gracefully handled termination signals (`KeyboardInterrupt`, `EOFError`).
5. **Robust Test Coverage**: Wrote unit tests checking all matching heuristics (Exact, Substring, Keywords, Fallback) to confirm production readiness.

---

## ╔════════════════════════════════════════════════════════════╗
## ║ 🚀 How to Install and Run                                 ║
## ╚════════════════════════════════════════════════════════════╝

### Prerequisites
- **Python 3.9+** (No external libraries required)

### Run the Application
Start the interactive session:
```bash
python main.py
```

### Run the Test Suite
Execute the automated unit tests:
```bash
python -m unittest tests/test_chatbot.py
```

---

## ╔════════════════════════════════════════════════════════════╗
## ║ 💬 Sample Terminal Interaction                            ║
## ╚════════════════════════════════════════════════════════════╝

```text
  _____                     _      _          _          
 |  __ \                   | |    | |        | |         
 | |  | | ___  ___ ___   __| | ___| |     __ _| |__  ___ 
 | |  | |/ _ \/ __/ _ \ / _` |/ _ \ |    / _` | '_ \/ __|
 | |__| |  __/ (_| (_) | (_| |  __/ |___| (_| | |_) \__ \
 |_____/ \___|\___\___/ \__,_|\___|______\__,_|_.__/|___/
                      AI ASSISTANT v1.0

╔══════════════════════════════════════════════════════════════════════╗
║ ℹ DecodeLabs AI Assistant                                            ║
╠══════════════════════════════════════════════════════════════════════╣
║  • Version:      1.0                                                 ║
║  • Author:       DecodeLabs Team                                     ║
║  • Startup Time: 2026-07-15 20:53:11                                 ║
║                                                                      ║
║  Instructions: Ask tech questions or type 'help' for options.        ║
║  Type 'debug on' to display diagnostic parameters.                   ║
╚══════════════════════════════════════════════════════════════════════╝
╔══════════════════════════════════════════════════════════════════════╗
║ ℹ DecodeLabs AI Assistant                                            ║
╠══════════════════════════════════════════════════════════════════════╣
║ ✓ Welcome to your first AI Assistant session. How can I serve you?   ║
╚══════════════════════════════════════════════════════════════════════╝

👤 You > My name is Adithyan
╔══════════════════════════════════════════════════════════════════════╗
║ 🤖 DecodeLabs AI Assistant                                            ║
╠══════════════════════════════════════════════════════════════════════╣
║ Nice to meet you, Adithyan!                                          ║
╚══════════════════════════════════════════════════════════════════════╝

👤 You > Who am I?
╔══════════════════════════════════════════════════════════════════════╗
║ 🤖 DecodeLabs AI Assistant                                            ║
╠══════════════════════════════════════════════════════════════════════╣
║ Your name is Adithyan.                                               ║
╚══════════════════════════════════════════════════════════════════════╝
```

---

## ╔════════════════════════════════════════════════════════════╗
## ║ 🛣️ Future Roadmap                                         ║
## ╚════════════════════════════════════════════════════════════╝

- **Interactive GUI Dashboard**: Support wrapping the core package inside a Flask/Tkinter web or desktop control dashboard.
- **Database Storage**: Integrate SQLite to preserve history across server restarts.
- **Natural Language Parsing**: Leverage regex-based named entity recognition (NER) to pull numbers or contact details from strings.

---

## ╔════════════════════════════════════════════════════════════╗
## ║ 📄 License                                                ║
## ╚════════════════════════════════════════════════════════════╝

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.
