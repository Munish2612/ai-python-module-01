# ============================================================
# SOLUTION 05 — Mini AI Simulator Challenge (Complete)
# ============================================================

print("=" * 60)
print("  🏆 SOLUTION 05: Mini AI Simulator")
print("=" * 60)
print()

# STEP 1: Data
students = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

student_scores = [
    [85, 88, 90, 87, 92],   # Alice — consistently high
    [70, 72, 68, 75, 73],   # Bob   — stable mid-range
    [60, 65, 70, 68, 72],   # Charlie — improving!
    [95, 97, 93, 98, 96],   # Diana — excellent
    [45, 50, 55, 60, 65],   # Eve   — needs help but improving
]

print(f"STEP 1: Loaded {len(students)} students")

# STEP 2: Functions
def calculate_average(scores):
    return sum(scores) / len(scores)

def detect_trend(scores):
    mid = len(scores) // 2
    first_half_avg = calculate_average(scores[:mid])
    second_half_avg = calculate_average(scores[mid:])
    diff = second_half_avg - first_half_avg
    if diff > 3:
        return "📈 Improving"
    elif diff < -3:
        return "📉 Declining"
    else:
        return "➡️  Stable"

def predict_next_score(scores):
    return calculate_average(scores[-3:])

def give_recommendation(average, trend):
    if average >= 90 and "Improving" in trend:
        return "🌟 Excellent! Consider advanced modules"
    elif average >= 80:
        return "✅ On track! Keep it up"
    elif average >= 70 and "Improving" in trend:
        return "📈 Making good progress!"
    elif average < 70 and "Declining" in trend:
        return "🆘 Needs immediate support"
    else:
        return "📖 Review materials and practice more"

print("STEP 2: Functions defined ✅")

# STEP 3: Analysis
print("\nSTEP 3: Running AI Analysis...")
print("-" * 60)

for student, scores in zip(students, student_scores):
    avg = calculate_average(scores)
    trend = detect_trend(scores)
    prediction = predict_next_score(scores)
    recommendation = give_recommendation(avg, trend)
    
    print(f"\n  👤 Student: {student}")
    print(f"     Scores  : {scores}")
    print(f"     Average : {avg:.1f}")
    print(f"     Trend   : {trend}")
    print(f"     Next est: ~{prediction:.1f}")
    print(f"     AI says : {recommendation}")

# STEP 4: Summary
print("\nSTEP 4: Class Summary Report")
print("-" * 60)

all_averages = [calculate_average(s) for s in student_scores]
class_avg = calculate_average(all_averages)
print(f"  Class Average     : {class_avg:.1f}")

# Find top student
top_index = all_averages.index(max(all_averages))
print(f"  Top Student       : {students[top_index]} ({all_averages[top_index]:.1f} avg)")

above_80_count = sum(1 for avg in all_averages if avg > 80)
print(f"  Students above 80 : {above_80_count}/{len(students)}")

print()
print("=" * 60)
print("  🏁 Module 01 Final Exercise — Complete Solution!")
print("  → Ready for Module 02! 🚀")
print("=" * 60)
