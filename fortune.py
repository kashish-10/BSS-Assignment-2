# fortune.py - Version v1.1

import random

def main():
    print("🔮 Welcome to Kashish's Fortune Teller (21JE0457) 🔮")
    mood = input("How are you feeling today? (happy/sad/neutral/stressed): ").strip().lower()

    fortunes = {
        "happy": [
            "✨ Great things await you, Kashish! Keep smiling. ✨",
            "🌞 Happiness is contagious — spread it today!",
            "💛 Your joy lights up the world around you."
        ],
        "sad": [
            "💫 Tough times don't last, but tough people like you do.",
            "🌧️ Every storm passes. A rainbow is coming.",
            "🕊️ Breathe. Let it out. You're going to be okay."
        ],
        "neutral": [
            "🌟 Balance is the key. Something interesting is on its way.",
            "🍃 Sometimes calm is the best superpower.",
            "🔄 Life might feel still, but change is near."
        ],
        "stressed": [
            "🧘 Deep breaths, Kashish. Peace is just a moment away.",
            "🌿 Even machines need a reboot. Take a break.",
            "🔥 Pressure builds diamonds. You're shining soon."
        ]
    }

    if mood in fortunes:
        print(random.choice(fortunes[mood]))
    else:
        print("🤔 Hmm, I couldn't recognize that mood. Try happy/sad/neutral/stressed.")

if __name__ == "__main__":
    main()
