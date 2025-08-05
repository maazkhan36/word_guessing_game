import random

# Word lists by difficulty
easy_words = ["apple", "train", "tiger", "money", "japan"]
medium_words = ["python", "battle", "monkey", "planet", "laptop"]
hard_words = ["elephant", "diamond", "umbrella", "computer", "mountain"]

print("🔑 Welcome to the Word Guessing Game!")
print("Choose a difficulty level: easy, medium, or hard.")

while True:
    level = input("Enter difficulty level: ").lower()

    # Select word based on difficulty
    if level == "easy":
        secret = random.choice(easy_words)
    elif level == "medium":
        secret = random.choice(medium_words)
    elif level == "hard":
        secret = random.choice(hard_words)
    else:
        print("Invalid choice! Defaulting to easy level.")
        secret = random.choice(easy_words)

    attempts = 0
    print("\nGuess the secret word!")

    while True:
        guess = input("Enter your guess: ").lower()
        attempts += 1

        if guess == secret:
            print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
            break

        # Generate hint
        hint = ""
        for i in range(len(secret)):
            if i < len(guess) and guess[i] == secret[i]:
                hint += guess[i]
            else:
                hint += "_"
        print("Hint:", hint)

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! 👋 Game over.")
        break
