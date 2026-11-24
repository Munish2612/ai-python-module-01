# ============================================================
# SOLUTION 04 — Lists
# ============================================================

print("=" * 55)
print("  SOLUTION 04: Lists")
print("=" * 55)
print()

# TASK 1 Solution
print("TASK 1: AI Model Manager")
ai_models = ["GPT-4", "BERT", "ResNet", "DALL-E", "Gemini"]
print(f"  Your list: {ai_models}")
print(f"  Total models: {len(ai_models)}")

first_model = ai_models[0]
last_model = ai_models[-1]
print(f"  First model: {first_model}")
print(f"  Last model: {last_model}")

ai_models.append("Claude")
print(f"  After adding Claude: {ai_models}")

ai_models.remove("BERT")
print(f"  After removing BERT: {ai_models}")

# TASK 2 Solution
print("\nTASK 2: Class Score Analysis")
scores = [78, 92, 65, 88, 71, 95, 83, 56, 90, 74]
print(f"  Scores: {scores}")

average = sum(scores) / len(scores)
highest = max(scores)
lowest = min(scores)
total = sum(scores)

print(f"\n  Total students : {len(scores)}")
print(f"  Total points   : {total}")
print(f"  Average score  : {average:.1f}")
print(f"  Highest score  : {highest}")
print(f"  Lowest score   : {lowest}")

above_80 = 0
for s in scores:
    if s > 80:
        above_80 += 1
print(f"  Students above 80: {above_80}")

passing_scores = []
for s in scores:
    if s >= 70:
        passing_scores.append(s)
print(f"  Passing scores  : {passing_scores}")

# TASK 3 Solution
print("\nTASK 3: AI Trivia Builder")
ai_facts = [
    "AI was first coined as a term at Dartmouth in 1956.",
    "There are more possible chess moves than atoms in the universe.",
    "Netflix saves $1 billion per year using AI recommendations.",
    "Google Translate handles 100 billion word translations daily.",
    "ChatGPT reached 100 million users in just 2 months.",
]

print("  🤖 AI Fun Facts:")
for i, fact in enumerate(ai_facts, 1):
    print(f"  {i}. {fact}")
print(f"\n  Total facts collected: {len(ai_facts)}")
print("  ✅ Great fact collection!")

# BONUS Solution
print("\nBONUS TASK: Sorted AI Models")
models = ["Whisper", "GPT-4", "BERT", "AlexNet", "ResNet", "Gemini"]
print(f"  Original  : {models}")
sorted_models = sorted(models)
print(f"  Sorted    : {sorted_models}")
reverse_sorted = sorted(models, reverse=True)
print(f"  Reversed  : {reverse_sorted}")
