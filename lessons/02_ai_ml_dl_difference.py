# ============================================================
# LESSON 02 — AI vs ML vs Deep Learning
# Module: Introduction to AI & Python | Level: Beginner
# ============================================================
# 🎯 Goal: Clearly understand the difference between AI, ML, DL
# ============================================================

print("=" * 60)
print("   LESSON 02: AI vs ML vs Deep Learning")
print("=" * 60)
print()

# ----------------------------------------------------------
# PART 1: The Russian Doll Explanation
# ----------------------------------------------------------
print("🪆 PART 1: The Big Picture")
print("-" * 40)

diagram = """
  ┌───────────────────────────────────────────────────┐
  │             ARTIFICIAL INTELLIGENCE               │
  │   ┌───────────────────────────────────────────┐   │
  │   │           MACHINE LEARNING                │   │
  │   │   ┌───────────────────────────────────┐   │   │
  │   │   │         DEEP LEARNING             │   │   │
  │   │   └───────────────────────────────────┘   │   │
  │   └───────────────────────────────────────────┘   │
  └───────────────────────────────────────────────────┘
  
  Every Deep Learning system is ML.
  Every ML system is AI.
  But NOT every AI system is ML!
"""
print(diagram)
input("Press ENTER to continue...")

# ----------------------------------------------------------
# PART 2: Artificial Intelligence
# ----------------------------------------------------------
print("\n🤖 PART 2: Artificial Intelligence (AI)")
print("-" * 40)

print("""
  Definition : Making machines simulate human intelligence
  Approach   : Can use rules, data, logic, search, etc.
  Example    : A chess program using rules + search
  
  Analogy 🧠 : Think of AI as the entire field of "teaching
               machines to be smart" — it's the BIG umbrella.
""")

input("Press ENTER to continue...")

# ----------------------------------------------------------
# PART 3: Machine Learning
# ----------------------------------------------------------
print("\n📈 PART 3: Machine Learning (ML)")
print("-" * 40)

print("""
  Definition : AI that learns from DATA — no explicit rules!
  Approach   : Feed data → algorithm finds patterns → makes predictions
  Example    : Email spam filter learns from 10,000 emails
  
  🔑 KEY INSIGHT — Old vs New Way:
  
  OLD (Traditional Programming):
    You write rules → computer follows them
    
    IF email contains "FREE MONEY" → mark as SPAM
    IF email contains "Dear Friend" → mark as SPAM
    ... (you write hundreds of rules manually)
    
  NEW (Machine Learning):
    You show examples → computer learns the rules itself!
    
    Show 10,000 spam emails → AI figures out the pattern!
    
  Analogy 🎓 : Like a student who learns from examples
               instead of memorizing a rulebook.
""")

# Live ML demonstration (simplified)
print("  📊 Simple ML Concept Demo:")
print("  Training Data (emails labeled spam or not spam):")

training_data = [
    ("FREE MONEY! Click now!", "SPAM"),
    ("You won a prize!", "SPAM"),
    ("Claim your reward today!", "SPAM"),
    ("Hi, are you free for lunch?", "NOT SPAM"),
    ("Meeting at 3pm tomorrow", "NOT SPAM"),
    ("Can you review this document?", "NOT SPAM"),
]

spam_words = []
for email, label in training_data:
    print(f"    [{label}] {email}")
    if label == "SPAM":
        for word in email.lower().split():
            word = word.strip("!?,.")
            if len(word) > 3:
                spam_words.append(word)

print(f"\n  🧠 Words the 'model' learned are spammy: {list(set(spam_words))}")

test_email = "Free prize! Claim your money now!"
spam_score = sum(1 for word in test_email.lower().split() if word.strip("!?,. ") in spam_words)
prediction = "SPAM" if spam_score > 1 else "NOT SPAM"
print(f"\n  🧪 New email: '{test_email}'")
print(f"  🤖 Prediction: {prediction} (spam words found: {spam_score})")

input("\nPress ENTER to continue...")

# ----------------------------------------------------------
# PART 4: Deep Learning
# ----------------------------------------------------------
print("\n🧠 PART 4: Deep Learning (DL)")
print("-" * 40)

print("""
  Definition : ML using layers of "neurons" (like a brain)
  Approach   : Data flows through layers, each layer learns features
  Example    : ChatGPT, image recognition, voice assistants
  
  Why "DEEP"? Because neural networks have many (deep) hidden layers!
  
  Simplified Neural Network for recognizing a cat photo:
  
  Input Layer       Hidden Layer 1      Hidden Layer 2    Output
  [Pixel 1]  ──┐                                        
  [Pixel 2]  ──┼──→ [Edges & Lines] ──→ [Eyes, Ears] ──→ 🐱 Cat: 97%
  [Pixel 3]  ──┘                                             🐶 Dog: 2%
  ...                                                        🐭 Mouse: 1%
  
  Real-world DL applications:
    🗣️  ChatGPT   — Understands and generates human language
    👁️  DALL-E    — Creates images from text descriptions  
    🎵  Suno      — Generates full songs from text prompts
    🚗  Tesla FSD — Drives a car autonomously
""")

input("Press ENTER to continue...")

# ----------------------------------------------------------
# PART 5: Side-by-Side Comparison
# ----------------------------------------------------------
print("\n📊 PART 5: Side-by-Side Comparison")
print("-" * 40)

print(f"{'Feature':<22} {'AI':<15} {'ML':<20} {'Deep Learning':<20}")
print("-" * 80)
comparison = [
    ("Data needed?", "Sometimes", "Yes", "LOTS of data"),
    ("Learns automatically?", "Sometimes", "Yes", "Yes"),
    ("Human rules needed?", "Often", "Rarely", "Almost never"),
    ("Compute power?", "Low-Medium", "Medium", "Very High"),
    ("Interpretable?", "Yes", "Sometimes", "Very hard"),
    ("Example", "Chess bot", "Spam filter", "ChatGPT"),
]

for row in comparison:
    print(f"  {row[0]:<20} {row[1]:<15} {row[2]:<20} {row[3]:<20}")

print()
print("=" * 60)
print("   End of Lesson 02 | Next: Real-World AI Applications")
print("=" * 60)
