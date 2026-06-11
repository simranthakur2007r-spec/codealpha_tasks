#Hangman Game

import random

# List of predefined words
words = ["alpha", "notes", "phone", "texts", "drink"]

# Select a random word
word = random.choice(words)

# Create blanks for the word
guessed_word = ["_"] * len(word)

# Variables
incorrect_guesses = 0
max_guesses = 6
guessed_letters = []

print("Welcome to Hangman Game!")

while incorrect_guesses < max_guesses and "_" in guessed_word:
    print("\nWord:", " ".join(guessed_word))
    print("Incorrect guesses left:", max_guesses - incorrect_guesses)

    guess = input("Enter a letter: ").lower()

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    # Check if letter is in the word
    if guess in word:
        print("Correct guess!")

        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        print("Wrong guess!")
        incorrect_guesses += 1

# Final Result
if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over! The word was:", word)