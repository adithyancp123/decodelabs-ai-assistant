"""
Intents mapping module for the DecodeLabs AI Assistant.
Contains dictionaries of patterns, keywords, and response choices.
"""

INTENT_DATA = {
    "greeting": {
        "patterns": [
            "hello", "hi", "hey", "hola", "greetings", "good morning", 
            "good afternoon", "good evening", "howdy", "yo", "hi there", "hello there"
        ],
        "keywords": [
            "hello", "hi", "hey", "hola", "greetings", "morning", 
            "afternoon", "evening", "howdy", "yo"
        ],
        "responses": [
            "Hello! I am DecodeLabs AI Assistant. How can I help you today?",
            "Hi there! How may I assist you today?",
            "Greetings! What can I do for you today?",
            "Nice to meet you. I'm here to help with your tech and support queries.",
            "Welcome back! How can I support you in this session?",
            "Happy to assist you. What is on your mind?",
            "Hello! Ready to assist you with any questions or diagnostics."
        ]
    },
    "exit": {
        "patterns": [
            "exit", "quit", "bye", "goodbye", "close", "stop", "terminate", 
            "end", "see ya", "farewell", "leave", "exit session"
        ],
        "keywords": [
            "exit", "quit", "bye", "goodbye", "stop", "terminate", 
            "end", "farewell", "leave", "logout"
        ],
        "responses": [
            "Goodbye! Hope to assist you again soon.",
            "Farewell! Have a wonderful day ahead.",
            "Bye! Keep learning and growing!",
            "Thank you for chatting with me. Have a great day!",
            "Wishing you a productive day! Goodbye.",
            "It was a pleasure assisting you. Take care!",
            "Goodbye! Don't hesitate to reach out if you need anything else.",
            "Farewell! Stay curious and keep coding.",
            "Signing off. Have an excellent day ahead!",
            "Have a great day! Looking forward to our next conversation.",
            "Goodbye! Best of luck with your current projects!"
        ]
    },
    "help": {
        "patterns": [
            "help", "info", "what can you do", "commands", "menu", 
            "features", "options", "instructions", "guide"
        ],
        "keywords": [
            "help", "info", "commands", "menu", "features", "options", 
            "instructions", "guide", "capabilities", "do"
        ],
        "responses": [
            "=====================================================\n"
            "                 AVAILABLE COMMANDS                  \n"
            "=====================================================\n"
            " • Greeting      : Say hello ('hi', 'hello', 'hey')\n"
            " • Help          : Display this command menu ('help')\n"
            " • About         : Show system details ('about')\n"
            " • Creator       : Find out who built me ('creator')\n"
            " • Version       : Get current software version ('version')\n"
            " • Date / Time   : Get current system date/time ('date', 'time')\n"
            " • Weather       : Get weather forecast placeholder ('weather')\n"
            " • Jokes         : Ask for a joke ('tell me a joke')\n"
            " • Motivation    : Get inspired ('motivate me')\n"
            " • Topics        : Ask about 'programming', 'python', 'ai',\n"
            "                   'machine learning', or 'data science'\n"
            " • Internship    : Details about DecodeLabs internship ('internship')\n"
            " • Project       : Details about this project ('project')\n"
            " • DecodeLabs    : Details about DecodeLabs ('decodelabs')\n"
            " • Support       : Ask for support portal details ('support')\n"
            " • Contact       : Get email and helpdesk contact details ('contact')\n"
            " • Status        : Check servers and databases ('status')\n"
            " • Pricing       : Show current pricing models ('pricing')\n"
            " • Clear         : Clear screen ('clear')\n"
            " • Debug         : Toggle diagnostics mode ('debug on' / 'debug off')\n"
            " • Bye / Exit    : Close the session ('bye', 'exit', 'quit')\n"
            "====================================================="
        ]
    },
    "about": {
        "patterns": [
            "about", "about the project", "about you", "info about bot",
            "project details", "who are you"
        ],
        "keywords": [
            "about", "details", "project", "technology", "architecture", "who"
        ],
        "responses": [
            "--------------------------------------------------\n"
            "Project Name:         DecodeLabs AI Assistant\n"
            "Purpose:              Rule-Based Intelligent Support Agent\n"
            "Technology:           Standard Library Only (Zero Dependency)\n"
            "Programming Language: Python 3\n"
            "Architecture:         Modular Package Architecture with Tiered Dictionary Matching\n"
            "Version:              1.0\n"
            "--------------------------------------------------"
        ]
    },
    "thanks": {
        "patterns": [
            "thanks", "thank you", "ty", "appreciate it", "grateful",
            "thank you very much"
        ],
        "keywords": [
            "thanks", "thank", "grateful", "appreciate", "ty"
        ],
        "responses": [
            "You're very welcome! Let me know if you need anything else.",
            "Anytime! Happy to help.",
            "My pleasure! Let me know if you have more questions.",
            "Glad I could be of assistance!"
        ]
    },
    "creator": {
        "patterns": [
            "creator", "who created you", "who is your creator", "who made you",
            "developer", "who developed you", "built by"
        ],
        "keywords": [
            "creator", "made", "developed", "developer", "built", "author"
        ],
        "responses": [
            "I was developed by the engineering team at DecodeLabs.",
            "DecodeLabs designed and built me to serve as an intelligent, rule-based virtual assistant.",
            "My creator is DecodeLabs! I am configured to operate as a high-quality coding assistant."
        ]
    },
    "version": {
        "patterns": [
            "version", "what is your version", "version number", "current version",
            "release"
        ],
        "keywords": [
            "version", "release", "number"
        ],
        "responses": [
            "I am currently running DecodeLabs AI Assistant version 1.0.",
            "My current software version is 1.0 (Stable Release).",
            "DecodeLabs AI Assistant: Version 1.0."
        ]
    },
    "date": {
        "patterns": [
            "date", "what is the date", "today's date", "current date", "what day is it", "calendar"
        ],
        "keywords": [
            "date", "day", "today", "calendar"
        ],
        "responses": [
            # Handled programmatically
            "Today's system date is checkable on command."
        ]
    },
    "time": {
        "patterns": [
            "time", "what time is it", "current time", "tell me the time", "clock"
        ],
        "keywords": [
            "time", "clock"
        ],
        "responses": [
            # Handled programmatically
            "The current system time is checkable on command."
        ]
    },
    "weather": {
        "patterns": [
            "weather", "how is the weather", "what is the weather", "weather forecast",
            "is it raining", "temperature outside"
        ],
        "keywords": [
            "weather", "temperature", "raining", "forecast", "sunny", "cloudy", "rain"
        ],
        "responses": [
            "Weather Report [Placeholder]: The weather is currently clear and sunny at 24°C, with a light breeze. A perfect day for coding!",
            "Weather Report [Placeholder]: Partly cloudy, 21°C. No rain expected today.",
            "Weather Report [Placeholder]: Clear blue skies, temperature at 26°C. Enjoy the pleasant weather!"
        ]
    },
    "jokes": {
        "patterns": [
            "joke", "tell me a joke", "make me laugh", "another joke",
            "funny", "do you know any jokes"
        ],
        "keywords": [
            "joke", "jokes", "laugh", "funny", "humor"
        ],
        "responses": [
            "Why do programmers wear glasses? Because they can't C#!",
            "How many programmers does it take to change a light bulb? None, that's a hardware problem.",
            "What is a programmer's favorite hangout place? Foo Bar!",
            "Why did the programmer quit his job? Because he didn't get arrays (a raise)!",
            "There are 10 types of people in the world: those who understand binary, and those who don't."
        ]
    },
    "motivation": {
        "patterns": [
            "motivation", "motivate me", "give me a quote", "inspiration",
            "inspirational quote", "inspire me", "motivational"
        ],
        "keywords": [
            "motivation", "motivate", "inspiration", "inspire", "quote", "quotes"
        ],
        "responses": [
            "The best way to predict the future is to invent it. - Alan Kay",
            "First, solve the problem. Then, write the code. - John Johnson",
            "Talk is cheap. Show me the code. - Linus Torvalds",
            "Clean code always looks like it was written by someone who cares. - Michael Feathers",
            "Strive not to be a success, but rather to be of value. - Albert Einstein"
        ]
    },
    "programming": {
        "patterns": [
            "programming", "what is programming", "coding", "what is coding",
            "write code"
        ],
        "keywords": [
            "programming", "coding", "code", "coder", "software"
        ],
        "responses": [
            "Programming is the process of creating a set of instructions that tell a computer how to perform a task.",
            "Coding/Programming allows us to solve complex problems, build automated systems, and bring digital products to life using languages like Python, C++, or Java.",
            "Programming is the craft of writing instructions for computers to execute, combining logic, design, and problem solving."
        ]
    },
    "python": {
        "patterns": [
            "python", "what is python", "tell me about python", "why python",
            "python language"
        ],
        "keywords": [
            "python", "py"
        ],
        "responses": [
            "Python is a high-level, interpreted programming language known for its readability, simplicity, and versatility.",
            "Python is widely used in web development, data science, artificial intelligence, scientific computing, and automation.",
            "Python was created by Guido van Rossum and released in 1991. It emphasizes code readability and clean syntax."
        ]
    },
    "ai": {
        "patterns": [
            "ai", "what is ai", "artificial intelligence", "what is artificial intelligence",
            "define ai"
        ],
        "keywords": [
            "ai", "artificial", "intelligence"
        ],
        "responses": [
            "Artificial Intelligence (AI) refers to the simulation of human intelligence processes by machines, especially computer systems.",
            "AI includes subfields like Machine Learning, Natural Language Processing, Robotics, and Computer Vision.",
            "AI is the technology enabling computers and machines to simulate human learning, reasoning, problem-solving, and decision-making."
        ]
    },
    "machine_learning": {
        "patterns": [
            "machine learning", "what is machine learning", "what is ml", "define machine learning",
            "ml concept"
        ],
        "keywords": [
            "ml", "machine", "learning", "algorithms"
        ],
        "responses": [
            "Machine Learning (ML) is a subset of AI that allows systems to learn from data, identify patterns, and make decisions with minimal human intervention.",
            "Unlike rule-based systems, Machine Learning algorithms build mathematical models based on sample training data to make predictions or decisions.",
            "ML enables computers to improve their performance on tasks dynamically by analyzing datasets rather than relying on explicit programming."
        ]
    },
    "data_science": {
        "patterns": [
            "data science", "what is data science", "define data science", "ds"
        ],
        "keywords": [
            "data", "science", "analytics", "statistics", "ds"
        ],
        "responses": [
            "Data Science is an interdisciplinary field that uses scientific methods, processes, algorithms, and systems to extract knowledge and insights from structured and unstructured data.",
            "Data Science combines programming, mathematics, statistics, and domain expertise to analyze data and inform business decisions.",
            "Data scientists collect, clean, analyze, and visualize data to solve complex problems and uncover actionable trends."
        ]
    },
    "internship": {
        "patterns": [
            "internship", "tell me about the internship", "internship details", "program",
            "intern role", "about internship"
        ],
        "keywords": [
            "internship", "intern", "internships", "role", "duration", "program"
        ],
        "responses": [
            "The DecodeLabs AI Internship program provides hands-on experience in building clean, industrial-grade software products and AI systems.",
            "Our internship focuses on standard software engineering practices, clean code, modular architecture, and developer-level unit testing.",
            "The internship is designed to bridge the gap between classroom theory and real-world software engineering processes."
        ]
    },
    "project": {
        "patterns": [
            "project", "what project is this", "tell me about this project", "chatbot project",
            "explain this application"
        ],
        "keywords": [
            "project", "app", "application", "chatbot", "system"
        ],
        "responses": [
            "This project is a high-quality, production-ready rule-based AI Assistant. It avoids long if-elif ladders by implementing a clean, modular lookup dictionary match system.",
            "This application showcases robust Python engineering, incorporating strict input preprocessing, custom diagnostic debug modes, in-memory state tracking, and automated unit testing.",
            "This project implements a tiered rule-based matching engine designed as an internship review showcase."
        ]
    },
    "decodelabs": {
        "patterns": [
            "decodelabs", "what is decodelabs", "tell me about decodelabs", "about decodelabs"
        ],
        "keywords": [
            "decodelabs"
        ],
        "responses": [
            "DecodeLabs is an innovative software solutions and technology research organization specializing in clean architectures and modern engineering patterns.",
            "DecodeLabs delivers state-of-the-art tech consultancy and runs specialized training pipelines for aspiring developers.",
            "At DecodeLabs, we prioritize engineering craftsmanship, unit-tested components, and beautiful user experience designs."
        ]
    },
    "support": {
        "patterns": [
            "support", "ticket", "issue", "problem", "bug", "helpdesk", 
            "open ticket", "report issue", "create ticket", "contact customer support"
        ],
        "keywords": [
            "support", "ticket", "issue", "problem", "bug", "helpdesk", "contact", "human", "representative"
        ],
        "responses": [
            "To report an issue or create a support ticket, please visit our portal at support.example.com or email support@example.com.",
            "I'm sorry to hear you're experiencing issues. Please describe the problem at support.example.com so our engineering team can address it immediately.",
            "You can open a support ticket by typing your issue in our customer portal or sending an email to support@example.com."
        ]
    },
    "contact": {
        "patterns": [
            "contact", "how to contact", "contact details", "email address",
            "phone number", "get in touch"
        ],
        "keywords": [
            "contact", "email", "phone", "touch", "details", "reach"
        ],
        "responses": [
            "You can contact us via email at contact@decodelabs.com or call our helpline at +1-800-DECODE.",
            "Reach out to DecodeLabs support by emailing support@decodelabs.com or calling +1-800-555-0199.",
            "For general queries, drop an email to hello@decodelabs.com. We respond within 24 business hours."
        ]
    },
    "status_check": {
        "patterns": [
            "status", "server status", "is the server down", "check system status", 
            "system check", "is everything working", "uptime", "server check"
        ],
        "keywords": [
            "status", "server", "down", "working", "uptime", "online", "operational"
        ],
        "responses": [
            "All systems are operational! Main Server uptime: 99.98%. No active incidents reported.",
            "System Status: ONLINE. Database and API servers are responding normally (latencies < 50ms).",
            "Everything is running smoothly. Our devops team reported no issues today."
        ]
    },
    "pricing": {
        "patterns": [
            "pricing", "price", "cost", "plans", "subscription", 
            "how much does it cost", "rates", "fees", "billing"
        ],
        "keywords": [
            "pricing", "price", "cost", "plans", "subscription", "rates", "fees", "billing", "charges"
        ],
        "responses": [
            "We offer three tiers:\n"
            " 1. Free Developer Tier ($0/mo - 1,000 API calls)\n"
            " 2. Professional Tier ($29/mo - 100,000 API calls)\n"
            " 3. Enterprise Tier (Custom - Unlimited calls, 24/7 Support).\n"
            "Would you like details on a specific tier?",
            "Our plans start at $0 for developers, going up to $29 for Professional teams.\n"
            "Check out our pricing page at https://example.com/pricing for a full feature comparison."
        ]
    },
    "name_declaration": {
        "patterns": [
            "my name is", "i am", "call me", "name is"
        ],
        "keywords": [
            "name", "call", "am"
        ],
        "responses": [
            "Nice to meet you, {name}!",
            "Great to meet you, {name}! How can I help you today?",
            "Hello {name}! How can I assist you?",
            "Welcome, {name}! Let me know what you need."
        ]
    },
    "name_query": {
        "patterns": [
            "what is my name", "do you know my name", "who am i", "my name", "tell me my name"
        ],
        "keywords": [
            "what", "my", "name", "who", "i", "am"
        ],
        "responses": [
            "I don't know your name yet! You can tell me by saying 'My name is Adithyan'."
        ]
    },
    "smalltalk_how_are_you": {
        "patterns": [
            "how are you", "how are you doing", "how is it going", "are you okay"
        ],
        "keywords": [
            "how", "are", "you", "doing", "going", "okay"
        ],
        "responses": [
            "I'm functioning at peak efficiency, thank you! How are you doing today?",
            "I am doing great, ready to help you write some code or check system status!",
            "Doing fantastic! How are things on your side?"
        ]
    },
    "fallback": {
        "responses": [
            "I'm sorry, I didn't quite catch that. Could you rephrase your question?",
            "I am still learning and don't understand that request. Try typing 'help' to see what I can do.",
            "Hmm, that seems outside my current scope. How else can I support you?",
            "I'm not sure how to respond to that. Feel free to ask about pricing, server status, or support!",
            "I didn't quite grasp that. Could you try asking in a different way?",
            "That's an interesting question, but it's not in my database. Can I help you with our services, pricing, or status instead?",
            "Apologies, I couldn't resolve that query. Try using simpler keywords or type 'help' for guidance.",
            "I'm a rule-based assistant, so I work best with specific topics like billing, status, or help. Could you ask about those?",
            "I'm not sure I follow. Could you specify if this is about pricing, status, or technical support?",
            "I might have missed your point. Could you try rephrasing with different keywords?",
            "I'm sorry, I don't have an answer for that yet. What else can I assist you with today?",
            "That query didn't match my rule system. Is there something else I can help you find?",
            "My training is currently limited to tech support, pricing, and system checks. Could we try one of those?",
            "I didn't recognize that command. Type 'help' to see a list of things you can ask me!",
            "Oops! I couldn't map that to an intent. Could you try phrasing it differently so I can assist you?",
            "I'm here to help, but I didn't understand that. Could you re-word your query?"
        ]
    }
}
