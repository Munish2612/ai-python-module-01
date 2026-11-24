# ============================================================
# SOLUTION 02 — Loops
# ============================================================

print("=" * 55)
print("  SOLUTION 02: Loops")
print("=" * 55)
print()

# TASK 1 Solution
print("TASK 1: AI Training Countdown")
for i in range(10, 0, -1):
    print(f"  {i}...")
print("  Training Complete! 🤖")

# TASK 2 Solution
print("\nTASK 2: Accuracy Tracker")
accuracy_scores = [45.2, 61.8, 75.3, 82.1, 79.6, 88.4, 91.2, 85.7, 93.1]
print("  Scores above 80% (ready for deployment):")
for score in accuracy_scores:
    if score > 80:
        print(f"    ✅ {score}% — Deployable!")

# TASK 3 Solution
print("\nTASK 3: Neural Network Layer Sizes")
input_size = 64
for i in range(1, 11):
    result = input_size * i
    print(f"  Layer {i:2}: {input_size} × {i:2} = {result}")

# TASK 4 Solution
print("\nTASK 4: AI Model Search")
ai_models = ["BERT", "ResNet", "LSTM", "GPT-2", "GPT-4", "DALL-E", "Gemini"]
search_target = "GPT-4"
index = 0
found = False

while index < len(ai_models):
    print(f"  Checking: {ai_models[index]}...")
    if ai_models[index] == search_target:
        print(f"  ✅ Found '{search_target}' at position {index}!")
        found = True
        break
    index += 1

if not found:
    print(f"  ❌ Model '{search_target}' not found")
