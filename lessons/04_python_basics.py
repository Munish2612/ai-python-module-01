# ============================================================
# LESSON 04 — Python Basics: Variables, Loops, Functions, Lists
# Module: Introduction to AI & Python | Level: Beginner
# ============================================================
# 🎯 Goal: Master Python fundamentals used in every AI project
# ============================================================

print("=" * 60)
print("   LESSON 04: Python Fundamentals")
print("=" * 60)
print()
print("🐍 Python is the LANGUAGE of AI.")
print("   Master these 4 concepts and you'll go far:\n")
print("   1. Variables  2. Loops  3. Functions  4. Lists\n")

input("Press ENTER to start with Variables...")

# ===========================================================
# SECTION 1: VARIABLES
# ===========================================================
print("\n" + "=" * 60)
print("  📦 SECTION 1: Variables")
print("=" * 60)
print("""
  A variable is a NAMED CONTAINER for storing data.
  Think of it like a labeled box 📦
  
  Syntax:   variable_name = value
""")

# --- Data Types ---
print("  🔢 The 4 Basic Data Types in Python:")
print("-" * 40)

# String
student_name = "Munish"
print(f'\n  str  (text)    → student_name = "Munish"')
print(f'                   Value: {student_name}')
print(f'                   Type:  {type(student_name)}')

# Integer
age = 20
print(f'\n  int  (whole #) → age = 20')
print(f'                   Value: {age}')
print(f'                   Type:  {type(age)}')

# Float
gpa = 3.75
print(f'\n  float(decimal) → gpa = 3.75')
print(f'                   Value: {gpa}')
print(f'                   Type:  {type(gpa)}')

# Boolean
is_enrolled = True
print(f'\n  bool (yes/no)  → is_enrolled = True')
print(f'                   Value: {is_enrolled}')
print(f'                   Type:  {type(is_enrolled)}')

print("\n  💡 Python figures out the type automatically — no need to declare it!")

print("\n  🔧 Variable Operations:")
x = 10
y = 3
print(f"     x = {x}, y = {y}")
print(f"     x + y = {x + y}   (Addition)")
print(f"     x - y = {x - y}   (Subtraction)")
print(f"     x * y = {x * y}   (Multiplication)")
print(f"     x / y = {x / y:.2f}  (Division)")
print(f"     x ** y = {x ** y}  (Power: 10³)")
print(f"     x % y = {x % y}   (Remainder/Modulo)")

# f-strings
print("\n  ✨ f-strings — Smart Text Formatting:")
name = "Alice"
score = 95
print(f'     f"Hello {{name}}, your score is {{score}}%"')
print(f'     → Hello {name}, your score is {score}%')

input("\n[Press ENTER for Loops...]")

# ===========================================================
# SECTION 2: LOOPS
# ===========================================================
print("\n" + "=" * 60)
print("  🔁 SECTION 2: Loops")
print("=" * 60)
print("""
  Loops let you REPEAT code without writing it over and over.
  
  Two types:
    for   loop — repeat a KNOWN number of times
    while loop — repeat while a CONDITION is true
""")

# --- For Loop ---
print("  FOR LOOP:")
print("  " + "-" * 36)
print("  Code:")
print('    for i in range(5):')
print('        print(f"Step {i}")')
print()
print("  Output:")
for i in range(5):
    print(f"    Step {i}")

print()
print("  Looping through items:")
print('    subjects = ["Math", "AI", "Python"]')
print('    for subject in subjects:')
print('        print(subject)')
print()
subjects = ["Math", "AI", "Python"]
print("  Output:")
for subject in subjects:
    print(f"    {subject}")

# --- While Loop ---
print("\n  WHILE LOOP:")
print("  " + "-" * 36)
print("""  Code:
    count = 1
    while count <= 3:
        print(f"Countdown: {{count}}")
        count = count + 1
        
  Output:""")
count = 1
while count <= 3:
    print(f"    Countdown: {count}")
    count = count + 1

# --- Loop with condition ---
print("\n  LOOP + CONDITION (Finding even numbers):")
print("  Code:")
print("    for num in range(1, 11):")
print('        if num % 2 == 0:')
print('            print(f"{num} is even")')
print()
print("  Output:")
for num in range(1, 11):
    if num % 2 == 0:
        print(f"    {num} is even")

input("\n[Press ENTER for Functions...]")

# ===========================================================
# SECTION 3: FUNCTIONS
# ===========================================================
print("\n" + "=" * 60)
print("  🛠️  SECTION 3: Functions")
print("=" * 60)
print("""
  A function is a REUSABLE BLOCK OF CODE that does one thing well.
  
  Rule: Write once, use many times!  (DRY = Don't Repeat Yourself)
  
  Syntax:
    def function_name(parameters):
        # code here
        return result
""")

# Basic function
print("  Example 1 — Simple Greeting:")
print('    def greet(name):')
print('        return f"Hello, {name}! Welcome to AI class!"')
print()

def greet(name):
    return f"Hello, {name}! Welcome to AI class!"

print(f"    greet('Alice')  → {greet('Alice')}")
print(f"    greet('Munish') → {greet('Munish')}")

# Function with math
print("\n  Example 2 — Calculate Area:")
print('    def rectangle_area(length, width):')
print('        area = length * width')
print('        return area')
print()

def rectangle_area(length, width):
    area = length * width
    return area

print(f"    rectangle_area(5, 3)  → {rectangle_area(5, 3)}")
print(f"    rectangle_area(10, 4) → {rectangle_area(10, 4)}")

# AI-themed function
print("\n  Example 3 — AI Classification Function:")
print('    def classify_temperature(temp_celsius):')
print('        if temp_celsius < 0:')
print('            return "❄️  Freezing"')
print('        elif temp_celsius < 15:')
print('            return "🧥 Cold"')
print('        elif temp_celsius < 25:')
print('            return "😊 Comfortable"')
print('        else:')
print('            return "🔥 Hot"')
print()

def classify_temperature(temp_celsius):
    if temp_celsius < 0:
        return "❄️  Freezing"
    elif temp_celsius < 15:
        return "🧥 Cold"
    elif temp_celsius < 25:
        return "😊 Comfortable"
    else:
        return "🔥 Hot"

test_temps = [-5, 10, 22, 38]
print("  Testing our classifier:")
for temp in test_temps:
    print(f"    {temp}°C → {classify_temperature(temp)}")

input("\n[Press ENTER for Lists...]")

# ===========================================================
# SECTION 4: LISTS
# ===========================================================
print("\n" + "=" * 60)
print("  📋 SECTION 4: Lists")
print("=" * 60)
print("""
  A list stores MULTIPLE items in one variable.
  
  Creating a list:  my_list = [item1, item2, item3]
  Items are ORDERED and can be CHANGED
  Index starts at 0 (not 1!)
""")

ai_tools = ["ChatGPT", "DALL-E", "Midjourney", "Copilot", "Gemini"]
print(f"  ai_tools = {ai_tools}")

print("\n  🔍 Accessing Items (Indexing):")
print(f"    ai_tools[0]   → {ai_tools[0]}    (first item)")
print(f"    ai_tools[2]   → {ai_tools[2]} (third item)")
print(f"    ai_tools[-1]  → {ai_tools[-1]}    (last item)")
print(f"    ai_tools[1:3] → {ai_tools[1:3]} (slice)")

print("\n  🔧 Common List Operations:")
ai_tools.append("Claude")
print(f"    .append('Claude')  → {ai_tools}")

ai_tools.remove("DALL-E")
print(f"    .remove('DALL-E') → {ai_tools}")

print(f"    len(ai_tools)      → {len(ai_tools)} items")
print(f"    sorted(ai_tools)   → {sorted(ai_tools)}")

print("\n  🔁 Looping through a List (very common in AI!):")
scores = [85, 92, 78, 95, 88]
print(f"    scores = {scores}")
print(f"    Average score: {sum(scores)/len(scores):.1f}")
print(f"    Highest score: {max(scores)}")
print(f"    Lowest score:  {min(scores)}")

print()
print("=" * 60)
print("   End of Lesson 04 | Next: Writing Python Programs")
print("=" * 60)
