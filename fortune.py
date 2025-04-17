# fortune.py - Version v1.0

def main():
    print("🔮 Welcome to Kashish's Fortune Teller (21JE0457) 🔮")
    mood = input("How are you feeling today? (happy/sad/neutral): ").strip().lower()

    if mood == "happy":
        print("✨ Your fortune: Great things await you, Kashish! Keep smiling. ✨")
    elif mood == "sad":
        print("💫 Your fortune: Tough times don't last, but tough people like you do. 💫")
    elif mood == "neutral":
        print("🌟 Your fortune: Balance is the key. Something interesting is on its way. 🌟")
    else:
        print("🤔 Hmm, I couldn't recognize that mood. Try again with happy/sad/neutral.")

if __name__ == "__main__":
    main()
