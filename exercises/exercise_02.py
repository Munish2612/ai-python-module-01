# ============================================================
# EXERCISE 02 — Loops
# Module: Introduction to AI & Python | Level: Beginner
# ============================================================

print("=" * 55)
print("  EXERCISE 02: Loops")
print("=" * 55)
print()

# ----------------------------------------------------------
# TASK 1: Countdown Timer
# ----------------------------------------------------------
print("TASK 1: AI Training Countdown")
print("-" * 40)
print("  Simulate an AI model training countdown from 10 to 1")
print("  Then print 'Training Complete! 🤖'\n")

# TODO: Write a loop that counts DOWN from 10 to 1
# Then print "Training Complete! 🤖"
# HINT: Use range(start, stop, step) — step can be negative!

# Your code here:


# ----------------------------------------------------------
# TASK 2: AI Accuracy Tracker
# ----------------------------------------------------------
print("\nTASK 2: AI Model Accuracy Tracker")
print("-" * 40)
print("  During training, an AI model's accuracy improves.")
print("  Loop through these accuracy scores and print only")
print("  the ones that are ABOVE 80% (good enough to deploy!)\n")

accuracy_scores = [45.2, 61.8, 75.3, 82.1, 79.6, 88.4, 91.2, 85.7, 93.1]

print("  Accuracy Scores:", accuracy_scores)
print()
print("  Scores above 80% (ready for deployment):")

# TODO: Write a for loop that prints only scores above 80
# HINT: Use an if statement inside your loop

# Your code here:


# ----------------------------------------------------------
# TASK 3: Multiplication Table for AI
# ----------------------------------------------------------
print("\nTASK 3: Neural Network Layer Sizes")
print("-" * 40)
print("  Neural networks multiply layer sizes.")
print("  Print a 'multiplication table' for input size 64:")
print("  64 x 1, 64 x 2, 64 x 3 ... up to 64 x 10\n")

input_size = 64

# TODO: Write a for loop from 1 to 10 (inclusive)
# Print: f"Layer {i}: {input_size} × {i} = {result}"

# Your code here:


# ----------------------------------------------------------
# TASK 4: Find First Item in List
# ----------------------------------------------------------
print("\nTASK 4: AI Model Search")
print("-" * 40)
print("  You have a list of AI models. Write a while loop that")
print("  searches for 'GPT-4' and stops when found!\n")

ai_models = ["BERT", "ResNet", "LSTM", "GPT-2", "GPT-4", "DALL-E", "Gemini"]
search_target = "GPT-4"

print(f"  Searching for '{search_target}' in: {ai_models}")
print()

# TODO: Use a while loop to search through ai_models
# - Use an index variable starting at 0
# - Print "Checking: model_name" for each model
# - When found, print "✅ Found 'GPT-4' at position X!" and stop
# - If not found by end, print "❌ Model not found"

index = 0
# Your code here:


print()
print("=" * 55)
print("  When done, check solutions/solution_02.py")
print("=" * 55)
