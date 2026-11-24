# ============================================================
# EXERCISE 04 — Lists
# Module: Introduction to AI & Python | Level: Beginner
# ============================================================

print("=" * 55)
print("  EXERCISE 04: Lists")
print("=" * 55)
print()

# ----------------------------------------------------------
# TASK 1: Build an AI Model List
# ----------------------------------------------------------
print("TASK 1: AI Model Manager")
print("-" * 40)

# TODO: Create a list called 'ai_models' with these 5 items:
# "GPT-4", "BERT", "ResNet", "DALL-E", "Gemini"

ai_models = []  # TODO: Fill this list!

print(f"  Your list: {ai_models}")
print(f"  Total models: {len(ai_models)}")

# TODO: Access and print the FIRST model
first_model = None  # TODO: Access ai_models[?]
print(f"  First model: {first_model}")

# TODO: Access and print the LAST model (use negative indexing!)
last_model = None   # TODO: Access ai_models[?]
print(f"  Last model: {last_model}")

# TODO: Add "Claude" to the end of the list
# HINT: Use .append()

print(f"  After adding Claude: {ai_models}")

# TODO: Remove "BERT" from the list
# HINT: Use .remove()

print(f"  After removing BERT: {ai_models}")

# ----------------------------------------------------------
# TASK 2: Student Scores Analysis
# ----------------------------------------------------------
print("\nTASK 2: Class Score Analysis")
print("-" * 40)

scores = [78, 92, 65, 88, 71, 95, 83, 56, 90, 74]
print(f"  Scores: {scores}\n")

# TODO: Calculate and print the following:

average = 0    # TODO: sum(scores) / len(scores)
highest = 0    # TODO: Use max()
lowest = 0     # TODO: Use min()
total = 0      # TODO: Use sum()

print(f"  Total students : {len(scores)}")
print(f"  Total points   : {total}")
print(f"  Average score  : {average:.1f}")
print(f"  Highest score  : {highest}")
print(f"  Lowest score   : {lowest}")

# TODO: Count how many students scored above 80
above_80 = 0  # TODO: Use a loop or list comprehension to count
print(f"  Students above 80: {above_80}")

# TODO: Create a new list with only scores >= 70 (passing scores)
passing_scores = []  # TODO: Filter scores using a loop
print(f"  Passing scores  : {passing_scores}")

# ----------------------------------------------------------
# TASK 3: AI Trivia List
# ----------------------------------------------------------
print("\nTASK 3: AI Trivia Builder")
print("-" * 40)
print("  Build a list of AI facts, then display them nicely.\n")

# TODO: Create a list called 'ai_facts' with at least 4 facts
# (Write your own or use the ones from your learning notes)
ai_facts = [
    # "AI was coined in 1956",
    # "Add more facts here...",
]

if len(ai_facts) >= 4:
    print("  🤖 AI Fun Facts:")
    for i, fact in enumerate(ai_facts, 1):
        print(f"  {i}. {fact}")
    
    # TODO: Print the total number of facts
    print(f"\n  Total facts collected: {len(ai_facts)}")
    print("  ✅ Great fact collection!")
else:
    print("  ⚠️  Add at least 4 AI facts to ai_facts list!")

# ----------------------------------------------------------
# BONUS TASK: Sorting
# ----------------------------------------------------------
print("\nBONUS TASK: Sorted AI Models")
print("-" * 40)

models = ["Whisper", "GPT-4", "BERT", "AlexNet", "ResNet", "Gemini"]

# TODO: Print the models in alphabetical order using sorted()
print(f"  Original  : {models}")
sorted_models = []  # TODO: Use sorted()
print(f"  Sorted    : {sorted_models}")

# TODO: Print in REVERSE alphabetical order
reverse_sorted = []  # TODO: Use sorted() with reverse=True
print(f"  Reversed  : {reverse_sorted}")

print()
print("=" * 55)
print("  When done, check solutions/solution_04.py")
print("=" * 55)
