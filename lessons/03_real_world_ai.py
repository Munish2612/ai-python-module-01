# ============================================================
# LESSON 03 — Real-World AI Applications
# Module: Introduction to AI & Python | Level: Beginner
# ============================================================
# 🎯 Goal: Discover how AI is used in the real world today
# ============================================================

import random

print("=" * 60)
print("   LESSON 03: Real-World AI Applications")
print("=" * 60)
print()
print("🌍 AI is not science fiction — it's happening RIGHT NOW!")
print("   Let's explore where AI is transforming the world...\n")

input("Press ENTER to begin the tour...")

# ----------------------------------------------------------
# Real-world AI by industry
# ----------------------------------------------------------
industries = {
    "🏥 Healthcare": {
        "description": "AI is saving lives and transforming medicine",
        "applications": [
            ("Cancer Detection", "AI scans X-rays and MRIs to detect cancer earlier than doctors",
             "Google's AI detects breast cancer with 94.5% accuracy"),
            ("Drug Discovery", "AI finds new medicines by simulating molecular interactions",
             "AlphaFold solved protein folding — a 50-year unsolved problem!"),
            ("Robotic Surgery", "AI-guided robots perform surgery with superhuman precision",
             "Da Vinci surgical robot has completed 10 million+ procedures"),
            ("Mental Health Chatbots", "AI chatbots provide 24/7 mental health support",
             "Woebot has helped thousands manage anxiety and depression"),
        ]
    },
    "🚗 Transportation": {
        "description": "AI is redefining how we move from place to place",
        "applications": [
            ("Self-Driving Cars", "AI processes cameras, radar, and lidar to navigate roads",
             "Waymo has driven 20+ million miles autonomously"),
            ("Traffic Optimization", "AI predicts congestion and optimizes traffic lights",
             "Google Maps saves 1.2 billion hours of driving time annually"),
            ("Flight Autopilot", "Modern planes use AI for autopilot and turbulence avoidance",
             "AI flies commercial planes for ~95% of flight duration"),
            ("Delivery Drones", "AI-powered drones deliver packages to your doorstep",
             "Amazon Prime Air completed its first autonomous delivery in 2022"),
        ]
    },
    "💬 Communication": {
        "description": "AI is making communication smarter and borderless",
        "applications": [
            ("Language Translation", "AI translates between 100+ languages in real time",
             "Google Translate handles 100 billion translations per day"),
            ("Spam Detection", "AI filters unwanted emails with 99%+ accuracy",
             "Gmail's AI blocks 100 million spam emails per day"),
            ("Voice Assistants", "AI understands natural language and responds intelligently",
             "There are 8+ billion voice assistant devices in the world"),
            ("Real-time Subtitles", "AI generates subtitles live during video calls",
             "Teams & Zoom use AI to subtitle millions of meetings daily"),
        ]
    },
    "🎬 Entertainment": {
        "description": "AI is transforming how we create and consume content",
        "applications": [
            ("Content Recommendation", "AI learns your taste and suggests what to watch/listen",
             "Netflix saves $1 billion/year using AI recommendations"),
            ("AI-Generated Art", "AI creates paintings, music, and videos from text prompts",
             "DALL-E and Midjourney have democratized digital art"),
            ("Game AI", "AI creates realistic NPCs that learn and adapt to players",
             "Chess AI (Stockfish) is 300+ Elo points above world champions"),
            ("Deepfakes", "AI can swap faces in videos (used ethically for movies)",
             "Disney uses AI de-aging tech in Marvel films"),
        ]
    },
    "💰 Finance": {
        "description": "AI is making finance smarter, faster, and safer",
        "applications": [
            ("Fraud Detection", "AI spots suspicious transactions in milliseconds",
             "Visa's AI reviews 500 data points per transaction in <1 second"),
            ("Algorithmic Trading", "AI buys and sells stocks faster than any human",
             "60-70% of stock market trades are made by AI algorithms"),
            ("Credit Scoring", "AI analyzes alternative data to assess creditworthiness",
             "Upstart uses AI to approve 27% more loans with 16% lower losses"),
            ("Customer Service", "AI chatbots handle banking queries 24/7",
             "Bank of America's Erica has had 1.5 billion client interactions"),
        ]
    },
}

for industry, data in industries.items():
    print(f"\n{'=' * 60}")
    print(f"  {industry}")
    print(f"  {data['description']}")
    print(f"{'=' * 60}")
    
    for app_name, description, fact in data["applications"]:
        print(f"\n  📌 {app_name}")
        print(f"     How: {description}")
        print(f"     Fact: 💡 {fact}")
    
    input(f"\n  [Press ENTER for next industry...]")

# ----------------------------------------------------------
# AI in India specifically
# ----------------------------------------------------------
print("\n🇮🇳 AI in India — Close to Home!")
print("-" * 40)

india_ai = [
    ("🌾 Crop Disease Detection", "Apps like AgroStar use AI to identify plant diseases from photos"),
    ("🏦 UPI Fraud Prevention", "NPCI uses AI to detect fraudulent UPI transactions in real-time"),
    ("🚂 Indian Railways", "AI predicts delays and optimizes train schedules"),
    ("📱 Jio AI", "Jio uses AI for network optimization and customer service"),
    ("🏥 Arogya Setu", "AI-powered contact tracing during COVID-19"),
    ("🗣️ Bhashini", "Govt's AI platform translating content into 22 Indian languages"),
]

for name, description in india_ai:
    print(f"  {name}: {description}")

# ----------------------------------------------------------
# AI Impact Reflection
# ----------------------------------------------------------
print("\n\n🤔 REFLECTION EXERCISE")
print("-" * 40)
print("Think about the AI applications you just learned about...")
print()

ai_you_use = input("Q1: Name ONE AI application you use or have heard about: ")
print(f"\n  Great! '{ai_you_use}' is a perfect example!")

future_ai = input("\nQ2: If you could build any AI, what would it do? ")
print(f"\n  🚀 '{future_ai}' — That's a fantastic idea!")
print("  Keep that dream! Module 10 covers building your own AI! 😊")

print()
print("=" * 60)
print("   End of Lesson 03 | Next: Python Fundamentals")
print("=" * 60)
