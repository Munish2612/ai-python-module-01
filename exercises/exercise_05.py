# ============================================================
# EXERCISE 05 — Mini AI Simulator Challenge
# Module: Introduction to AI & Python | Level: Beginner
# ============================================================
# 🎯 FINAL CHALLENGE: Put EVERYTHING together!
# This exercise combines: Variables, Loops, Functions, Lists
# ============================================================

print("=" * 60)
print("  🏆 FINAL CHALLENGE: Mini AI Simulator")
print("=" * 60)
print("""
  You will simulate how a simple AI "learns" from data.
  
  Scenario: You have student test scores from multiple tests.
  Your AI must:
    1. Load the data (list of scores)
    2. Calculate statistics (functions)
    3. Predict future performance (simple algorithm)
    4. Give personalized recommendations (conditionals)
  
  Complete all TODO sections below!
""")

# ----------------------------------------------------------
# STEP 1: Data Loading
# ----------------------------------------------------------
print("STEP 1: Loading Student Data")
print("-" * 40)

# TODO: Create a list of student names
students = []  # Add: "Alice", "Bob", "Charlie", "Diana", "Eve"

# TODO: Create a corresponding list of their recent 5 test scores
# Each student has 5 scores — make them realistic (50-100 range)
student_scores = [
    # [85, 88, 90, 87, 92],   # Alice's scores
    # [70, 72, 68, 75, 73],   # Bob's scores
    # [60, 65, 70, 68, 72],   # Charlie's (improving!)
    # [95, 97, 93, 98, 96],   # Diana's scores
    # [45, 50, 55, 60, 65],   # Eve's scores (needs help)
]

print(f"  Loaded {len(students)} students with {len(student_scores)} datasets")

if len(students) == 0:
    print("  ⚠️  Fill in 'students' and 'student_scores' lists first!")

# ----------------------------------------------------------
# STEP 2: Analysis Functions
# ----------------------------------------------------------
print("\nSTEP 2: Define Analysis Functions")
print("-" * 40)

# TODO: Write a function to calculate average
def calculate_average(scores):
    """Calculate and return the average of a list of scores."""
    # Your code here:
    pass

# TODO: Write a function to detect trend (improving or declining)
def detect_trend(scores):
    """
    Detect if scores are improving, declining, or stable.
    Compare first half average vs second half average.
    Return: "📈 Improving", "📉 Declining", or "➡️  Stable"
    """
    # HINT: Split scores into two halves and compare averages
    # first_half = scores[:len(scores)//2]
    # second_half = scores[len(scores)//2:]
    # Your code here:
    pass

# TODO: Write a function to predict next score
def predict_next_score(scores):
    """
    Simple prediction: return the average of the last 3 scores.
    This is a basic "moving average" — a real ML technique!
    """
    # HINT: Use the last 3 scores: scores[-3:]
    # Your code here:
    pass

# TODO: Write a function to give recommendations
def give_recommendation(average, trend):
    """
    Give a recommendation based on average and trend.
    Rules:
    - average >= 90 AND improving → "🌟 Excellent! Consider advanced modules"
    - average >= 80               → "✅ On track! Keep it up"  
    - average >= 70 AND improving → "📈 Making good progress!"
    - average < 70  AND declining → "🆘 Needs immediate support"
    - otherwise                   → "📖 Review materials and practice more"
    """
    # Your code here:
    pass

print("  ✓ Functions defined (complete the TODO code inside each)")

# ----------------------------------------------------------
# STEP 3: Run the AI Analysis
# ----------------------------------------------------------
print("\nSTEP 3: Running AI Analysis...")
print("-" * 40)

if len(students) > 0 and len(student_scores) > 0:
    for i, (student, scores) in enumerate(zip(students, student_scores)):
        print(f"\n  👤 Student: {student}")
        print(f"     Scores  : {scores}")
        
        avg = calculate_average(scores)
        trend = detect_trend(scores)
        prediction = predict_next_score(scores)
        recommendation = give_recommendation(avg, trend)
        
        print(f"     Average : {avg:.1f}" if avg else "     Average : (complete calculate_average)")
        print(f"     Trend   : {trend}" if trend else "     Trend   : (complete detect_trend)")
        print(f"     Next est: ~{prediction:.1f}" if prediction else "     Next est: (complete predict_next_score)")
        print(f"     AI says : {recommendation}" if recommendation else "     AI says : (complete give_recommendation)")
else:
    print("  ⚠️  Add student data in Step 1 to run analysis!")

# ----------------------------------------------------------
# STEP 4: Summary Report
# ----------------------------------------------------------
print("\nSTEP 4: Class Summary Report")
print("-" * 40)

if len(students) > 0 and len(student_scores) > 0:
    all_averages = [calculate_average(s) for s in student_scores if calculate_average(s)]
    
    if all_averages:
        # TODO: Print the class average
        class_avg = 0  # TODO: average of all_averages
        print(f"  Class Average     : {class_avg:.1f}" if class_avg else "  Class Average: (TODO)")
        
        # TODO: Find the top student
        # HINT: Use max() with zip(students, all_averages)
        print("  Top Student       : (TODO — find using max())")
        
        # TODO: Count students above 80
        above_80_count = 0  # TODO: count using a loop
        print(f"  Students above 80 : {above_80_count}")

print()
print("=" * 60)
print("  🏁 Module 01 Final Exercise Complete!")
print("  → Check solutions/solution_05.py for the full solution")
print("  → You're ready for Module 02! 🚀")
print("=" * 60)
