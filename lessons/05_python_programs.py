# ============================================================
# LESSON 05 — Writing Beginner-Friendly Python Programs
# Module: Introduction to AI & Python | Level: Beginner
# ============================================================
# 🎯 Goal: Put it all together by writing complete programs
# ============================================================

import random

print("=" * 60)
print("   LESSON 05: Writing Python Programs")
print("=" * 60)
print()
print("   We've learned the tools. Now let's BUILD something!")
print("   Four complete programs — each more exciting than the last.\n")

input("Press ENTER to start building...")

# ===========================================================
# PROGRAM 1: Personal Introduction Generator
# ===========================================================
print("\n" + "🔷 " + "=" * 56)
print("  PROGRAM 1: Personal Introduction Generator")
print("🔷 " + "=" * 56)
print("""
  Concepts used: Variables, f-strings, input()
  
  Code:
    name = input("What is your name? ")
    age = int(input("How old are you? "))
    interest = input("What's your AI interest? ")
    
    print(f"Hello! I'm {{name}}, {{age}} years old.")
    print(f"I'm excited to learn about {{interest}} using AI!")
""")
print("  Let's run it! Fill in your details:\n")

name = input("  What is your name? ")
age = int(input("  How old are you? "))
interest = input("  What's your AI interest? ")

print()
print("  📄 Generated Introduction:")
print(f"  Hello! I'm {name}, {age} years old.")
print(f"  I'm on a mission to master {interest} using the power of AI!")
print(f"  By 2027, I will have built {age - 10} AI projects. Watch out world! 🚀")

input("\n[Press ENTER for Program 2...]")

# ===========================================================
# PROGRAM 2: AI Vocabulary Flashcard Game
# ===========================================================
print("\n" + "🔷 " + "=" * 56)
print("  PROGRAM 2: AI Vocabulary Flashcard Game")
print("🔷 " + "=" * 56)
print("""
  Concepts used: Lists, Loops, Conditionals, Functions
  
  How to play: You'll be shown a flashcard.
               Press ENTER to reveal the answer.
               Then tell us if you got it right!
""")

flashcards = [
    ("Artificial Intelligence",
     "The field of making machines simulate human intelligence"),
    ("Machine Learning",
     "AI that learns from data without being explicitly programmed"),
    ("Deep Learning",
     "Machine learning using layers of artificial neurons (neural networks)"),
    ("Neural Network",
     "A system of interconnected nodes inspired by the human brain"),
    ("Training Data",
     "The dataset used to teach a machine learning model"),
    ("Algorithm",
     "A step-by-step set of instructions to solve a problem"),
    ("Model",
     "The result of training — a program that can make predictions"),
    ("Python",
     "The most popular programming language for AI and data science"),
]

random.shuffle(flashcards)
score = 0
total = len(flashcards)

print(f"  📚 Starting Flashcard Game ({total} cards)...\n")

for i, (term, definition) in enumerate(flashcards, 1):
    print(f"  Card {i}/{total}")
    print(f"  ┌─────────────────────────────────────────────┐")
    print(f"  │  Term: {term:<42}│")
    print(f"  └─────────────────────────────────────────────┘")
    
    input("  Press ENTER to reveal the definition...")
    print(f"  Definition: {definition}")
    
    answer = input("  Did you know it? (y/n): ").strip().lower()
    if answer == "y":
        score += 1
        print("  ✅ Great! Keep it up!")
    else:
        print("  📝 No worries! Note it down and review later.")
    print()

print(f"  🏆 Final Score: {score}/{total}")
percentage = (score / total) * 100
print(f"  Accuracy: {percentage:.0f}%")
if percentage >= 80:
    print("  Outstanding! You're ready for the next module! 🎉")
elif percentage >= 60:
    print("  Good effort! Review the missed terms once more. 👍")
else:
    print("  Keep practicing! Revisit LEARNING_NOTES.md 💪")

input("\n[Press ENTER for Program 3...]")

# ===========================================================
# PROGRAM 3: AI Application Finder
# ===========================================================
print("\n" + "🔷 " + "=" * 56)
print("  PROGRAM 3: AI Application Finder")
print("🔷 " + "=" * 56)
print("""
  Concepts used: Dictionaries, Functions, User Input
  
  Describe your problem → AI finds the right application!
""")

def find_ai_application(industry):
    """Find AI applications for a given industry."""
    applications = {
        "healthcare": [
            "🔬 AI-powered disease diagnosis from medical images",
            "💊 Drug discovery using molecular simulation",
            "🤖 Surgical robots guided by AI",
        ],
        "finance": [
            "🔒 Real-time fraud detection on transactions",
            "📈 Algorithmic trading systems",
            "💳 AI-powered credit scoring",
        ],
        "education": [
            "👩‍🏫 Personalized learning paths for each student",
            "✏️  Automated essay grading",
            "🌐 Real-time language tutoring",
        ],
        "agriculture": [
            "🌾 Crop disease detection from drone photos",
            "💧 Smart irrigation using weather prediction",
            "🚜 Autonomous farming equipment",
        ],
        "entertainment": [
            "🎬 Content recommendations (Netflix/Spotify)",
            "🎮 Intelligent game NPCs that learn from players",
            "🎨 AI-generated art and music",
        ],
    }
    
    industry_lower = industry.lower().strip()
    
    for key, apps in applications.items():
        if key in industry_lower or industry_lower in key:
            return key, apps
    
    return None, None

print("  Industries available: healthcare, finance, education, agriculture, entertainment\n")
user_industry = input("  Enter an industry to explore: ")
industry_name, apps = find_ai_application(user_industry)

if apps:
    print(f"\n  🤖 AI Applications in {industry_name.title()}:")
    for app in apps:
        print(f"    → {app}")
else:
    print(f"\n  🔍 No specific results for '{user_industry}', but AI is used EVERYWHERE!")
    print("     Try: healthcare, finance, education, agriculture, or entertainment")

input("\n[Press ENTER for Program 4...]")

# ===========================================================
# PROGRAM 4: Simple Number Pattern AI
# ===========================================================
print("\n" + "🔷 " + "=" * 56)
print("  PROGRAM 4: Pattern Recognizer (Mini AI!)")
print("🔷 " + "=" * 56)
print("""
  Concepts used: Functions, Loops, Lists, Conditionals
  
  This program detects patterns in a list of numbers —
  just like a real AI would analyze data!
""")

def analyze_pattern(numbers):
    """Analyze a list of numbers and detect patterns."""
    if len(numbers) < 2:
        return "Need at least 2 numbers to find a pattern."
    
    results = []
    
    # Check if increasing
    is_increasing = all(numbers[i] < numbers[i+1] for i in range(len(numbers)-1))
    is_decreasing = all(numbers[i] > numbers[i+1] for i in range(len(numbers)-1))
    
    # Check if arithmetic sequence (constant difference)
    differences = [numbers[i+1] - numbers[i] for i in range(len(numbers)-1)]
    is_arithmetic = len(set(differences)) == 1
    
    # Check if geometric (constant ratio)
    if all(n != 0 for n in numbers[:-1]):
        ratios = [numbers[i+1] / numbers[i] for i in range(len(numbers)-1)]
        is_geometric = all(abs(r - ratios[0]) < 0.001 for r in ratios)
    else:
        is_geometric = False
    
    if is_arithmetic:
        d = differences[0]
        next_val = numbers[-1] + d
        results.append(f"✅ Arithmetic sequence! Each number {'increases' if d>0 else 'decreases'} by {abs(d)}")
        results.append(f"🔮 Next number prediction: {next_val}")
    elif is_geometric and is_geometric:
        r = ratios[0]
        next_val = numbers[-1] * r
        results.append(f"✅ Geometric sequence! Each number is multiplied by {r:.2f}")
        results.append(f"🔮 Next number prediction: {next_val:.1f}")
    elif is_increasing:
        results.append("📈 Numbers are increasing, but no simple pattern detected.")
    elif is_decreasing:
        results.append("📉 Numbers are decreasing, but no simple pattern detected.")
    else:
        results.append("🔀 No obvious sequential pattern found.")
    
    results.append(f"📊 Statistics:")
    results.append(f"   Sum: {sum(numbers)}")
    results.append(f"   Average: {sum(numbers)/len(numbers):.2f}")
    results.append(f"   Min: {min(numbers)}, Max: {max(numbers)}")
    
    return "\n  ".join(results)

print("  Try the following test cases or enter your own!\n")

test_cases = [
    [2, 4, 6, 8, 10],
    [3, 6, 12, 24, 48],
    [100, 75, 50, 25],
    [1, 1, 2, 3, 5, 8],  # Fibonacci!
]

for i, case in enumerate(test_cases, 1):
    print(f"  Test {i}: {case}")
    print(f"  {analyze_pattern(case)}")
    print()

user_input = input("  Enter your own numbers (comma-separated, e.g. 5,10,15): ")
try:
    user_numbers = [float(x.strip()) for x in user_input.split(",")]
    print(f"\n  Your sequence: {user_numbers}")
    print(f"  {analyze_pattern(user_numbers)}")
except ValueError:
    print("  ⚠️  Invalid input. Please use numbers separated by commas.")

print()
print("=" * 60)
print("   🎓 Congratulations! You've completed all 5 Lessons!")
print("   Next Step: Try the exercises in the /exercises folder")
print("=" * 60)
