# Hangman Game in Python

## About the Project

This is a simple command-line Hangman game developed using Python.

The player has to guess the hidden word one letter at a time. The player gets 6 incorrect guesses before the game ends.

## Features

* Randomly selects a word
* Accepts letter guesses from the player
* Shows correctly guessed letters
* Keeps track of guessed letters
* Gives 6 incorrect attempts
* Checks invalid input
* Prevents repeated guesses
* Displays the final result

## Technologies Used

* Python
* Random module

## How to Run

1. Make sure Python is installed on your computer.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run:

```bash
python hangman.py
```

On some Windows systems, use:

```bash
py hangman.py
```

## How the Game Works

1. The program randomly selects a word from a list.
2. The letters of the word are hidden.
3. The player enters one letter at a time.
4. If the letter is present in the word, it is revealed.
5. If the letter is incorrect, one attempt is removed.
6. The player wins by guessing all the letters before running out of attempts.
7. The game ends when the word is guessed or all attempts are used.

## Learning Outcomes

Through this project, I practiced:

* Variables
* Lists
* Conditional statements
* While loops
* For loops
* User input
* String methods
* The random module
* Basic input validation

## Project Type

Beginner Python Project / Internship Task
