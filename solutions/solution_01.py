# ============================================================
# SOLUTION 01 — Variables & Data Types
# ============================================================

print("=" * 55)
print("  SOLUTION 01: Variables & Data Types")
print("=" * 55)
print()

# TASK 1 Solution
your_name = "Alice"
your_age = 20
your_favorite_subject = "Artificial Intelligence"
is_ai_enthusiast = True
your_gpa = 3.8

print("TASK 1: Student Profile")
print(f"Student Name    : {your_name}")
print(f"Age             : {your_age}")
print(f"Favorite Subject: {your_favorite_subject}")
print(f"AI Enthusiast   : {is_ai_enthusiast}")
print(f"GPA             : {your_gpa}")
print(f"✅ Profile created for {your_name}!")

# TASK 2 Solution
print("\nTASK 2: Type Identification")
values = [42, "AI", 3.14, True, "Machine Learning", 100, False, 2.718]
correct_types = ["int", "str", "float", "bool", "str", "int", "bool", "float"]

for value, correct in zip(values, correct_types):
    print(f"  {str(value):<20} → {correct}")

print(f"\n  Score: 8/8 ✅")

# TASK 3 Solution
print("\nTASK 3: AI Cost Calculator")
gpu_hours = 10
cost_per_hour = 2.5
discount_percent = 20

total_cost = gpu_hours * cost_per_hour
discount_amount = total_cost * (discount_percent / 100)
final_cost = total_cost - discount_amount

print(f"  GPU Hours      : {gpu_hours}")
print(f"  Cost per Hour  : ${cost_per_hour}")
print(f"  Subtotal       : ${total_cost:.2f}")
print(f"  Discount ({discount_percent}%) : -${discount_amount:.2f}")
print(f"  Final Cost     : ${final_cost:.2f}")
print("  ✅ Task 3 complete!")
