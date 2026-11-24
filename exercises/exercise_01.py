# ============================================================
# EXERCISE 01 — Variables & Data Types
# Module: Introduction to AI & Python | Level: Beginner
# ============================================================
# 🎯 Complete all TODO sections to pass the exercise
# ============================================================

print("=" * 55)
print("  EXERCISE 01: Variables & Data Types")
print("=" * 55)
print()

# ----------------------------------------------------------
# TASK 1: Create variables about yourself
# ----------------------------------------------------------
print("TASK 1: Create your student profile")
print("-" * 40)

# TODO: Fill in your details below

your_name = "YOUR_NAME_HERE"          # e.g., "Alice"
your_age = 0                           # e.g., 20
your_favorite_subject = "SUBJECT_HERE" # e.g., "Mathematics"
is_ai_enthusiast = False               # Change to True if you are!
your_gpa = 0.0                         # e.g., 3.8

# Don't modify below — this checks your work
print(f"Student Name    : {your_name}")
print(f"Age             : {your_age}")
print(f"Favorite Subject: {your_favorite_subject}")
print(f"AI Enthusiast   : {is_ai_enthusiast}")
print(f"GPA             : {your_gpa}")

# Validation
if your_name == "YOUR_NAME_HERE":
    print("\n⚠️  Reminder: Replace 'YOUR_NAME_HERE' with your actual name!")
else:
    print(f"\n✅ Profile created for {your_name}!")

# ----------------------------------------------------------
# TASK 2: Type checking
# ----------------------------------------------------------
print("\nTASK 2: Identify the data type of each value")
print("-" * 40)

values = [42, "AI", 3.14, True, "Machine Learning", 100, False, 2.718]

print("Value               → Your Answer   → Correct Answer")
print("-" * 60)

# TODO: For each value, what is its type?
# Options: str, int, float, bool
your_answers = [
    "int",  # 42         → Change if wrong
    "str",  # "AI"       → Change if wrong
    "int",  # 3.14       → HINT: This has a decimal!
    "bool", # True       → Change if wrong
    "str",  # "Machine Learning" → Change if wrong
    "int",  # 100        → Change if wrong
    "bool", # False      → Change if wrong
    "int",  # 2.718      → HINT: e (Euler's number), has a decimal!
]

correct_types = [type(v).__name__ for v in values]
score = 0

for value, your_ans, correct in zip(values, your_answers, correct_types):
    status = "✅" if your_ans == correct else "❌"
    if your_ans == correct:
        score += 1
    print(f"  {str(value):<20} → {your_ans:<13} → {correct:<10} {status}")

print(f"\n  Score: {score}/{len(values)}")

# ----------------------------------------------------------
# TASK 3: Arithmetic with Variables
# ----------------------------------------------------------
print("\nTASK 3: AI Cost Calculator")
print("-" * 40)
print("  You're running an AI training job on the cloud.")
print("  Calculate the total cost!\n")

# TODO: Fill in the values
gpu_hours = 0          # Number of GPU hours used (e.g., 10)
cost_per_hour = 0.0    # Cost per GPU hour in USD (e.g., 2.5)
discount_percent = 0   # Discount percentage (e.g., 20)

# TODO: Calculate these values using the variables above
total_cost = 0.0           # = gpu_hours * cost_per_hour
discount_amount = 0.0      # = total_cost * (discount_percent / 100)
final_cost = 0.0           # = total_cost - discount_amount

print(f"  GPU Hours      : {gpu_hours}")
print(f"  Cost per Hour  : ${cost_per_hour}")
print(f"  Subtotal       : ${total_cost:.2f}")
print(f"  Discount ({discount_percent}%) : -${discount_amount:.2f}")
print(f"  Final Cost     : ${final_cost:.2f}")

if gpu_hours > 0 and cost_per_hour > 0:
    print("\n  ✅ Task 3 complete!")
else:
    print("\n  ⚠️  Fill in gpu_hours and cost_per_hour to complete Task 3")

print()
print("=" * 55)
print("  When done, check solutions/solution_01.py")
print("=" * 55)
