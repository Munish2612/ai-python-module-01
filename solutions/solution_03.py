# ============================================================
# SOLUTION 03 — Functions
# ============================================================

print("=" * 55)
print("  SOLUTION 03: Functions")
print("=" * 55)
print()

# TASK 1 Solution
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print("TASK 1: Temperature Converter")
print(f"  0°C   → {celsius_to_fahrenheit(0)}°F  (Expected: 32.0)")
print(f"  100°C → {celsius_to_fahrenheit(100)}°F (Expected: 212.0)")
print(f"  37°C  → {celsius_to_fahrenheit(37):.1f}°F  (Expected: 98.6)")
print(f"  32°F  → {fahrenheit_to_celsius(32)}°C  (Expected: 0.0)")
print(f"  212°F → {fahrenheit_to_celsius(212)}°C (Expected: 100.0)")

# TASK 2 Solution
def check_eligibility(age, gpa, knows_python):
    if age < 16:
        return f"Not Eligible ❌ (Age {age} is below minimum of 16)"
    if gpa < 2.5:
        return f"Not Eligible ❌ (GPA {gpa} is below minimum of 2.5)"
    if not knows_python:
        return "Not Eligible ❌ (Python knowledge is required)"
    return "Eligible ✅ (All requirements met!)"

print("\nTASK 2: Eligibility Checker")
print(f"  Age=18, GPA=3.2, Python=True  → {check_eligibility(18, 3.2, True)}")
print(f"  Age=15, GPA=3.8, Python=True  → {check_eligibility(15, 3.8, True)}")
print(f"  Age=20, GPA=2.0, Python=True  → {check_eligibility(20, 2.0, True)}")
print(f"  Age=22, GPA=3.5, Python=False → {check_eligibility(22, 3.5, False)}")

# TASK 3 Solution
def calculate_grade(score):
    if score >= 90:
        return ("A", "Excellent! You're AI-ready! 🌟")
    elif score >= 80:
        return ("B", "Great work! Keep pushing! 💪")
    elif score >= 70:
        return ("C", "Good effort! Review and retry. 📖")
    elif score >= 60:
        return ("D", "Needs improvement. See tutor. 🆘")
    else:
        return ("F", "Please redo this assignment. 🔄")

print("\nTASK 3: Grade Calculator")
test_scores = [95, 83, 72, 65, 45]
for s in test_scores:
    grade, feedback = calculate_grade(s)
    print(f"  Score {s}: Grade {grade} — {feedback}")
