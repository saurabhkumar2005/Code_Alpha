import random

# Predefined list of 5 words
WORDS = ["python", "coding", "intern", "laptop", "guitar"]

# Hangman ASCII art stages (0 = 6 wrong guesses left, 6 = game over)
HANGMAN_PICS = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]


def play_hangman():
    word = random.choice(WORDS)
    guessed_letters = []
    wrong_guesses = 0
    max_wrong = 6

    print("=" * 40)
    print("       WELCOME TO HANGMAN")
    print("=" * 40)
    print(f"You have {max_wrong} incorrect guesses allowed.\n")

    while wrong_guesses < max_wrong:
        # Show current hangman stage
        print(HANGMAN_PICS[wrong_guesses])

        # Show word with blanks
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        print("Word: " + display_word)
        print(f"Wrong guesses: {wrong_guesses}/{max_wrong}")
        print(f"Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'None'}\n")

        # Check win
        if all(letter in guessed_letters for letter in word):
            print("🎉 Congratulations! You guessed the word:", word.upper())
            return

        # Get user input
        guess = input("Guess a letter: ").lower().strip()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️  Please enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print(f"⚠️  You already guessed '{guess}'. Try another.\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"✅ Good guess! '{guess}' is in the word.\n")
        else:
            wrong_guesses += 1
            print(f"❌ Wrong! '{guess}' is not in the word.\n")

    # Game over
    print(HANGMAN_PICS[wrong_guesses])
    print("💀 Game Over! You ran out of guesses.")
    print(f"The word was: {word.upper()}")


if __name__ == "__main__":
    play_hangman()