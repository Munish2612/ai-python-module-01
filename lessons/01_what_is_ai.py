# ============================================================
# LESSON 01 — What is Artificial Intelligence?
# Module: Introduction to AI & Python | Level: Beginner
# ============================================================
# 🎯 Goal: Understand what AI is, its history, and types
# ============================================================

print("=" * 60)
print("   LESSON 01: What is Artificial Intelligence?")
print("=" * 60)
print()

# ----------------------------------------------------------
# PART 1: Defining AI
# ----------------------------------------------------------
print("📖 PART 1: What is AI?")
print("-" * 40)

definition = """
Artificial Intelligence (AI) is the ability of a machine 
to perform tasks that normally require HUMAN intelligence.

These tasks include:
  → Learning from experience
  → Understanding language
  → Recognizing images
  → Making decisions
  → Solving problems
"""
print(definition)

input("Press ENTER to continue...")

# ----------------------------------------------------------
# PART 2: Is it AI or not?
# ----------------------------------------------------------
print("\n🤔 PART 2: Is it AI?")
print("-" * 40)

examples = {
    "A calculator that adds 2 + 2": False,
    "A spam filter that learns from emails": True,
    "A light switch": False,
    "Netflix recommending your next show": True,
    "A clock showing the time": False,
    "Google Translate converting English to Hindi": True,
    "A thermostat set to 25°C": False,
    "Siri understanding your voice": True,
}

for item, is_ai in examples.items():
    label = "✅ YES — AI" if is_ai else "❌ NO  — Not AI"
    print(f"  {label}  |  {item}")

input("\nPress ENTER to continue...")

# ----------------------------------------------------------
# PART 3: Types of AI
# ----------------------------------------------------------
print("\n🤖 PART 3: Types of AI")
print("-" * 40)

ai_types = [
    ("Narrow AI (Weak AI)", "Does ONE specific task really well",
     "Chess engine, face recognition, Alexa", "EXISTS TODAY ✅"),
    ("General AI (Strong AI)", "Human-level intelligence across ALL tasks",
     "An AI that can cook, code, and dance", "THEORETICAL 🔬"),
    ("Super AI", "Surpasses human intelligence in EVERY way",
     "The AI from sci-fi movies", "FUTURE CONCEPT 🚀"),
]

for name, description, example, status in ai_types:
    print(f"\n  🔷 {name}")
    print(f"     What: {description}")
    print(f"     Example: {example}")
    print(f"     Status: {status}")

print()

# ----------------------------------------------------------
# PART 4: AI Quiz
# ----------------------------------------------------------
print("\n🧠 QUICK QUIZ — Test Your Understanding!")
print("-" * 40)

score = 0
questions = [
    ("What year was the term 'AI' first coined?",
     ["A) 1940", "B) 1956", "C) 1972", "D) 2001"],
     "B", "1956 at the Dartmouth Conference!"),
    
    ("Which of these is an example of Narrow AI?",
     ["A) A robot that does everything", "B) A spam filter",
      "C) A super-intelligent being", "D) A calculator"],
     "B", "Spam filters are trained on data to detect spam — that's Narrow AI!"),
    
    ("What does AI stand for?",
     ["A) Automated Interface", "B) Artificial Intelligence",
      "C) Advanced Internet", "D) Algorithmic Integration"],
     "B", "Artificial Intelligence — machines simulating human thinking!"),
]

for i, (question, options, answer, explanation) in enumerate(questions, 1):
    print(f"\nQ{i}: {question}")
    for option in options:
        print(f"   {option}")
    
    user_answer = input("Your answer (A/B/C/D): ").strip().upper()
    
    if user_answer == answer:
        print(f"  ✅ Correct! {explanation}")
        score += 1
    else:
        print(f"  ❌ Not quite! The answer is {answer}. {explanation}")

print(f"\n🏆 Quiz Score: {score}/{len(questions)}")
if score == len(questions):
    print("   Perfect score! You're ready for the next lesson! 🎉")
elif score >= 2:
    print("   Great job! Review any missed questions. 👍")
else:
    print("   Keep studying! Re-read the lesson and try again. 💪")

print()
print("=" * 60)
print("   End of Lesson 01 | Next: AI vs ML vs Deep Learning")
print("=" * 60)
