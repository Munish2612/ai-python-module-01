# ============================================================
# 🚀 MINI PROJECT: Rule-Based AI Chatbot
# Module: Introduction to AI & Python | Level: Beginner
# ============================================================
#
# This is your FIRST real AI project!
# It's a rule-based chatbot (the simplest form of AI).
# While it doesn't "learn", it shows how early AI worked
# and teaches you to think like an AI engineer.
#
# Concepts used: Variables, Lists, Functions, Loops,
#                Conditionals, String manipulation
# ============================================================

import random
import time

# ===========================================================
# CONFIGURATION
# ===========================================================
BOT_NAME = "PyBot"
VERSION = "1.0"
MODULE = "Module 01 — Introduction to AI & Python"

# ===========================================================
# KNOWLEDGE BASE (the "brain" of our chatbot)
# ===========================================================

# Each key is a list of trigger words/phrases
# Each value is a list of possible responses (randomized)
RESPONSES = {
    "greetings": {
        "triggers": ["hello", "hi", "hey", "good morning", "good evening",
                     "howdy", "what's up", "sup", "namaste", "hola"],
        "replies": [
            f"Hello! I'm {BOT_NAME}, your AI learning assistant! 🤖",
            f"Hey there! Great to meet you! I'm {BOT_NAME}! 👋",
            f"Hi! Ready to learn about AI together? I'm {BOT_NAME}! 🎓",
            "Namaste! Welcome to the AI learning journey! 🙏",
        ]
    },
    "ai_definition": {
        "triggers": ["what is ai", "define ai", "what is artificial intelligence",
                     "explain ai", "ai meaning", "ai definition"],
        "replies": [
            "🤖 AI (Artificial Intelligence) is the simulation of human intelligence by machines!\n"
            "   It enables computers to learn, reason, understand language, and make decisions.",
            
            "🧠 Great question! AI is about making machines 'smart'.\n"
            "   Instead of following fixed rules, AI systems can learn from data and experience.",
        ]
    },
    "ml_definition": {
        "triggers": ["what is ml", "machine learning", "what is machine learning",
                     "explain ml", "ml definition"],
        "replies": [
            "📈 Machine Learning (ML) is a type of AI where machines LEARN from data!\n"
            "   Instead of writing rules, you feed data and the machine figures out patterns.\n"
            "   Example: Show 10,000 cat photos → machine learns what a cat looks like!",
            
            "🎯 ML is teaching machines to learn without explicit programming.\n"
            "   Traditional AI: You write rules. ML: Machine discovers the rules from data!",
        ]
    },
    "dl_definition": {
        "triggers": ["what is dl", "deep learning", "what is deep learning",
                     "neural network", "explain deep learning"],
        "replies": [
            "🧠 Deep Learning uses NEURAL NETWORKS — systems inspired by the human brain!\n"
            "   These networks have many layers (that's why it's 'deep').\n"
            "   Powers: ChatGPT, image recognition, voice assistants, Tesla Autopilot!",
        ]
    },
    "ai_vs_ml": {
        "triggers": ["difference between ai and ml", "ai vs ml", "ai or ml",
                     "ml vs deep learning", "difference"],
        "replies": [
            "🪆 Think of it like Russian dolls!\n"
            "   AI is the BIG picture (all intelligent machines)\n"
            "   ML is INSIDE AI (machines that learn from data)\n"
            "   Deep Learning is INSIDE ML (using neural networks)\n"
            "   Every DL system is ML, and every ML system is AI!",
        ]
    },
    "python": {
        "triggers": ["python", "why python", "python for ai", "best language for ai",
                     "learn python"],
        "replies": [
            "🐍 Python is the #1 language for AI because:\n"
            "   • Simple, readable syntax (almost like English!)\n"
            "   • Huge ecosystem: NumPy, Pandas, TensorFlow, PyTorch\n"
            "   • Massive community and free resources\n"
            "   • Used by Google, Tesla, Netflix, and NASA for AI!",
        ]
    },
    "real_world_ai": {
        "triggers": ["real world", "ai applications", "ai examples", "ai in life",
                     "where is ai used", "ai use cases"],
        "replies": [
            "🌍 AI is EVERYWHERE in your daily life:\n"
            "   🎬 Netflix — recommends your next show\n"
            "   📱 Face ID — recognizes your face to unlock phone\n"
            "   🗺️  Google Maps — predicts traffic in real time\n"
            "   📧 Gmail — filters 100M+ spam emails daily\n"
            "   🏥 Healthcare — detects cancer from X-rays\n"
            "   🚗 Tesla — self-driving car autopilot",
        ]
    },
    "variables": {
        "triggers": ["variable", "variables", "data type", "string", "integer",
                     "float", "boolean", "int"],
        "replies": [
            "📦 Variables are named containers for storing data!\n"
            "   4 basic types in Python:\n"
            "   • str   → text        → name = 'Alice'\n"
            "   • int   → whole number → age = 20\n"
            "   • float → decimal     → gpa = 3.8\n"
            "   • bool  → True/False  → is_student = True",
        ]
    },
    "loops": {
        "triggers": ["loop", "loops", "for loop", "while loop", "iteration",
                     "repeat"],
        "replies": [
            "🔁 Loops repeat code without rewriting it!\n"
            "   FOR loop — repeat a known number of times:\n"
            "     for i in range(5): print(i)\n\n"
            "   WHILE loop — repeat while a condition is true:\n"
            "     while count < 10: count += 1",
        ]
    },
    "functions": {
        "triggers": ["function", "functions", "def", "return", "reusable"],
        "replies": [
            "🛠️  Functions are reusable blocks of code!\n"
            "   def greet(name):\n"
            "       return f'Hello, {name}!'\n\n"
            "   Call it: greet('Alice') → 'Hello, Alice!'\n"
            "   Rule: Write once, use many times! (DRY principle)",
        ]
    },
    "lists": {
        "triggers": ["list", "lists", "array", "collection", "append", "remove"],
        "replies": [
            "📋 Lists store multiple items in one variable!\n"
            "   fruits = ['apple', 'banana', 'cherry']\n"
            "   fruits[0]        → 'apple'\n"
            "   fruits.append('mango') → adds to end\n"
            "   len(fruits)      → number of items\n"
            "   for f in fruits  → loop through all items",
        ]
    },
    "help": {
        "triggers": ["help", "what can you do", "commands", "topics", "menu",
                     "options"],
        "replies": [
            f"🤖 I'm {BOT_NAME}! I can help you with these topics:\n"
            "   📚 AI Topics:\n"
            "      • what is ai / what is ml / what is deep learning\n"
            "      • difference between ai and ml\n"
            "      • real world ai applications\n\n"
            "   🐍 Python Topics:\n"
            "      • variables / loops / functions / lists / python\n\n"
            "   Type 'quiz' to test your knowledge!\n"
            "   Type 'fact' for a random AI fact!\n"
            "   Type 'bye' to exit.",
        ]
    },
    "fact": {
        "triggers": ["fact", "random fact", "ai fact", "tell me something",
                     "interesting", "did you know"],
        "replies": [
            "💡 Did you know? AI was first coined as a term in 1956 at Dartmouth!",
            "💡 Did you know? Netflix uses AI to save $1 billion per year on recommendations!",
            "💡 Did you know? ChatGPT reached 100 million users in just 2 months!",
            "💡 Did you know? Google Translate handles 100 billion word translations daily!",
            "💡 Did you know? Tesla's Autopilot processes 2,300 photos per second!",
            "💡 Did you know? AlphaFold solved a 50-year-old protein folding problem in 2020!",
            "💡 Did you know? The first AI program was written in 1951 — it played checkers!",
            "💡 Did you know? By 2030, AI could add $15.7 trillion to the global economy!",
        ]
    },
    "quiz": {
        "triggers": ["quiz", "test me", "question", "challenge me"],
        "replies": ["quiz_mode"]   # Special trigger
    },
    "goodbye": {
        "triggers": ["bye", "goodbye", "exit", "quit", "see you", "cya",
                     "farewell", "later"],
        "replies": [
            f"👋 Goodbye! Keep learning — you're doing great! Come back anytime!",
            f"🚀 See you soon! Remember: every expert was once a beginner. Keep going!",
            f"🎓 Farewell! You've taken the first step in your AI journey. Great work!",
        ]
    },
    "thanks": {
        "triggers": ["thanks", "thank you", "ty", "appreciate", "helpful",
                     "great", "awesome", "cool", "nice"],
        "replies": [
            "😊 You're very welcome! Happy to help!",
            "🤖 That's what I'm here for! Any other questions?",
            "🎓 Glad that helped! Keep asking — curiosity is the key to learning!",
        ]
    },
}

# ===========================================================
# QUIZ QUESTIONS
# ===========================================================
QUIZ_QUESTIONS = [
    {
        "question": "What does 'AI' stand for?",
        "options": ["A) Automated Intelligence", "B) Artificial Intelligence",
                    "C) Advanced Internet", "D) Algorithmic Interface"],
        "answer": "b",
        "explanation": "Artificial Intelligence — machines simulating human thinking!"
    },
    {
        "question": "Which is the most popular language for AI development?",
        "options": ["A) Java", "B) C++", "C) Python", "D) JavaScript"],
        "answer": "c",
        "explanation": "Python! Its simple syntax and rich library ecosystem make it perfect for AI."
    },
    {
        "question": "Deep Learning is a subset of which field?",
        "options": ["A) Web Development", "B) Data Entry",
                    "C) Machine Learning", "D) Game Design"],
        "answer": "c",
        "explanation": "Deep Learning ⊂ Machine Learning ⊂ Artificial Intelligence!"
    },
    {
        "question": "What is a 'variable' in Python?",
        "options": ["A) A type of loop", "B) A named container for data",
                    "C) A Python function", "D) A website feature"],
        "answer": "b",
        "explanation": "Variables are named containers — like labeled boxes storing values!"
    },
    {
        "question": "Which of these is an example of real-world AI?",
        "options": ["A) A light switch", "B) A calculator",
                    "C) Netflix recommendations", "D) A regular clock"],
        "answer": "c",
        "explanation": "Netflix uses ML to analyze your viewing history and suggest shows!"
    },
]

# ===========================================================
# CHATBOT FUNCTIONS
# ===========================================================

def find_response(user_input):
    """Find the best response for the user's input."""
    text = user_input.lower().strip()
    
    for category, data in RESPONSES.items():
        for trigger in data["triggers"]:
            if trigger in text:
                reply = random.choice(data["replies"])
                if reply == "quiz_mode":
                    return "QUIZ"
                return reply
    
    # Default response if nothing matches
    unknowns = [
        f"🤔 Hmm, I'm not sure about '{user_input}'. Try asking about:\n"
        f"   AI, Machine Learning, Deep Learning, Python, or type 'help'!",
        
        "❓ I didn't quite catch that! Type 'help' to see what I can answer.",
        
        "🤖 Interesting question! That's beyond my Module 01 knowledge.\n"
        "   Ask me about AI concepts or Python basics — I'm good at those!",
    ]
    return random.choice(unknowns)


def run_quiz():
    """Run a mini quiz with the user."""
    questions = random.sample(QUIZ_QUESTIONS, min(3, len(QUIZ_QUESTIONS)))
    score = 0
    
    print(f"\n  🎯 Starting {BOT_NAME} Quiz! ({len(questions)} questions)")
    print("  Type the letter of your answer (a/b/c/d)\n")
    
    for i, q in enumerate(questions, 1):
        print(f"  Q{i}: {q['question']}")
        for opt in q["options"]:
            print(f"       {opt}")
        
        answer = input(f"  Your answer: ").strip().lower()
        
        if answer == q["answer"]:
            print(f"  ✅ Correct! {q['explanation']}\n")
            score += 1
        else:
            correct_letter = q["answer"].upper()
            print(f"  ❌ Not quite! The answer was {correct_letter}. {q['explanation']}\n")
        
        time.sleep(0.3)
    
    pct = (score / len(questions)) * 100
    print(f"  🏆 Quiz Complete! Score: {score}/{len(questions)} ({pct:.0f}%)")
    
    if pct == 100:
        print("  🌟 Perfect score! You're crushing it!")
    elif pct >= 66:
        print("  👍 Great job! Keep studying!")
    else:
        print("  📖 Review the lessons and try again!")


def type_effect(text, delay=0.02):
    """Print text with a typing effect."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


def print_separator():
    print(f"\n  {'─' * 50}")


# ===========================================================
# MAIN CHATBOT LOOP
# ===========================================================

def main():
    # Welcome banner
    print()
    print("  ╔══════════════════════════════════════════════╗")
    print(f"  ║  🤖  {BOT_NAME} — AI Learning Chatbot v{VERSION}       ║")
    print(f"  ║  {MODULE[:44]:<44}  ║")
    print("  ╚══════════════════════════════════════════════╝")
    print()
    
    time.sleep(0.5)
    type_effect(f"  {BOT_NAME}: Hello! I'm {BOT_NAME}, your AI learning assistant!")
    type_effect(f"  {BOT_NAME}: Ask me anything about AI, ML, or Python basics.")
    type_effect(f"  {BOT_NAME}: Type 'help' to see topics, 'quiz' to test yourself,")
    type_effect(f"  {BOT_NAME}: or 'bye' to exit. Let's learn! 🚀")
    print_separator()
    
    conversation_count = 0
    
    while True:
        try:
            print()
            user_input = input("  You: ").strip()
            
            if not user_input:
                print(f"  {BOT_NAME}: Oops! Looks like you forgot to type something 😄")
                continue
            
            conversation_count += 1
            
            # Check for exit
            goodbye_words = ["bye", "goodbye", "exit", "quit", "cya", "farewell"]
            if any(word in user_input.lower() for word in goodbye_words):
                reply = random.choice(RESPONSES["goodbye"]["replies"])
                print_separator()
                type_effect(f"  {BOT_NAME}: {reply}")
                print(f"\n  Total messages exchanged: {conversation_count}")
                print("  ═" * 26)
                break
            
            # Get response
            response = find_response(user_input)
            
            print_separator()
            
            if response == "QUIZ":
                print(f"  {BOT_NAME}: Great! Let's test your knowledge! 🎓")
                run_quiz()
            else:
                # Add bot name prefix and type effect
                lines = response.split('\n')
                type_effect(f"  {BOT_NAME}: {lines[0]}")
                for line in lines[1:]:
                    time.sleep(0.05)
                    print(f"  {' ' * (len(BOT_NAME) + 4)}{line}")
            
            # Occasional encouragement
            if conversation_count % 5 == 0:
                print()
                encouragements = [
                    f"  💬 You've asked {conversation_count} questions! Curious minds learn fast! 🌟",
                    f"  🎓 {conversation_count} messages in! You're on a learning streak!",
                    f"  🔥 Wow, {conversation_count} questions! That's the spirit of a true AI student!",
                ]
                type_effect(random.choice(encouragements))
        
        except KeyboardInterrupt:
            print(f"\n\n  {BOT_NAME}: Caught an interruption! Type 'bye' to exit properly. 😊")
            continue


if __name__ == "__main__":
    main()
