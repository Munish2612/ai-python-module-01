# ============================================================
# EXERCISE 03 — Functions
# Module: Introduction to AI & Python | Level: Beginner
# ============================================================

print("=" * 55)
print("  EXERCISE 03: Functions")
print("=" * 55)
print()

# ----------------------------------------------------------
# TASK 1: Celsius to Fahrenheit Converter
# ----------------------------------------------------------
print("TASK 1: Temperature Converter")
print("-" * 40)
print("  AI weather models work with both Celsius and Fahrenheit.")
print("  Write a function to convert between them.\n")

# TODO: Complete the function below
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit.
    Formula: F = (C × 9/5) + 32
    """
    # Your code here:
    pass   # Remove 'pass' and write your formula


# TODO: Complete this function too
def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius.
    Formula: C = (F - 32) × 5/9
    """
    # Your code here:
    pass  # Remove 'pass' and write your formula


# Tests — these should print correct values when you're done
print("  Testing celsius_to_fahrenheit:")
print(f"    0°C  → {celsius_to_fahrenheit(0)}°F  (Expected: 32.0)")
print(f"    100°C → {celsius_to_fahrenheit(100)}°F (Expected: 212.0)")
print(f"    37°C  → {celsius_to_fahrenheit(37)}°F  (Expected: 98.6)")

print("\n  Testing fahrenheit_to_celsius:")
print(f"    32°F  → {fahrenheit_to_celsius(32)}°C  (Expected: 0.0)")
print(f"    212°F → {fahrenheit_to_celsius(212)}°C (Expected: 100.0)")

# ----------------------------------------------------------
# TASK 2: AI Eligibility Checker
# ----------------------------------------------------------
print("\nTASK 2: AI Course Eligibility Checker")
print("-" * 40)
print("  Write a function that checks if a student is eligible")
print("  for an advanced AI course.\n")
print("  Eligibility rules:")
print("    1. Age must be 16 or older")
print("    2. GPA must be 2.5 or higher")
print("    3. Must have basic Python knowledge (True/False)\n")

# TODO: Write the function
def check_eligibility(age, gpa, knows_python):
    """
    Check if a student is eligible for an advanced AI course.
    
    Parameters:
        age (int): Student's age
        gpa (float): Student's GPA (0.0 to 4.0)
        knows_python (bool): Does the student know Python?
    
    Returns:
        str: "Eligible ✅" or "Not Eligible ❌" with a reason
    """
    # Your code here:
    pass  # Remove and write your logic


# Tests
print("  Test Cases:")
print(f"    Age=18, GPA=3.2, Python=True  → {check_eligibility(18, 3.2, True)}")
print(f"    Age=15, GPA=3.8, Python=True  → {check_eligibility(15, 3.8, True)}")
print(f"    Age=20, GPA=2.0, Python=True  → {check_eligibility(20, 2.0, True)}")
print(f"    Age=22, GPA=3.5, Python=False → {check_eligibility(22, 3.5, False)}")

# ----------------------------------------------------------
# TASK 3: Grade Calculator
# ----------------------------------------------------------
print("\nTASK 3: AI Assignment Grade Calculator")
print("-" * 40)
print("  Write a function that takes a score (0-100) and")
print("  returns the letter grade and feedback.\n")
print("  Grading scale:")
print("    90-100 → A → 'Excellent! You're AI-ready! 🌟'")
print("    80-89  → B → 'Great work! Keep pushing! 💪'")
print("    70-79  → C → 'Good effort! Review and retry. 📖'")
print("    60-69  → D → 'Needs improvement. See tutor. 🆘'")
print("    0-59   → F → 'Please redo this assignment. 🔄'\n")

# TODO: Write this function
def calculate_grade(score):
    """Return (letter_grade, feedback) for a given score."""
    # Your code here:
    pass  # Remove and write your logic


# Tests
test_scores = [95, 83, 72, 65, 45]
print("  Results:")
for s in test_scores:
    result = calculate_grade(s)
    print(f"    Score {s}: {result}")

print()
print("=" * 55)
print("  When done, check solutions/solution_03.py")
print("=" * 55)
