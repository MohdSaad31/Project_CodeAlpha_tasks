import random

# Words that the game can choose from
words = [
    "python",
    "computer",
    "programming",
    "keyboard",
    "developer",
    "internet",
    "software",
    "github",
    "variable",
    "function"
]

# Choose a random word
word = random.choice(words)

# Store the letters guessed by the player
guessed_letters = []

# Number of incorrect guesses allowed
attempts = 6

# Display the hidden word
display_word = ["_"] * len(word)

print("================================")
print("        HANGMAN GAME")
print("================================")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses.")
print()


# Main game loop
while attempts > 0 and "_" in display_word:

    # Show the current progress
    print("Word:", " ".join(display_word))
    print("Guessed letters:", " ".join(guessed_letters))
    print("Attempts remaining:", attempts)
    print()

    # Ask the player for a letter
    guess = input("Enter a letter: ").lower()

    # Check if the input is valid
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        print()
        continue

    # Check if the letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        print()
        continue

    # Add the guess to the list
    guessed_letters.append(guess)

    # Check whether the guessed letter is in the word
    if guess in word:

        print("Correct guess!")

        # Reveal the guessed letter
        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess

    else:
        attempts -= 1
        print("Wrong guess!")

    print()


# Game result
if "_" not in display_word:
    print("================================")
    print("Congratulations! You won!")
    print("The word was:", word)
    print("================================")

else:
    print("================================")
    print("Game over!")
    print("The word was:", word)
    print("================================")