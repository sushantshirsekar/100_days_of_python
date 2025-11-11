"""
Purpose:
    A simple command-line Hangman game implemented step-by-step following
    Angela Yu's "100 Days of Code" Python tutorial. This script demonstrates
    basic Python concepts such as modules, lists, loops, conditionals,
    random selection, and user input handling.

Features:
    - Selects a random word from `hangman_words.word_list`
    - Displays a logo and hangman stages from `hangman_art`
    - Tracks guessed letters and remaining lives (6 by default)
    - Notifies the player on repeated guesses, incorrect guesses,
      and game outcomes (win/lose)
    - Designed as an educational project to practice Python fundamentals

File to run:
    day_7_goal.py

Notes / Credits:
    - This project was implemented by following Angela Yu's step-by-step
      tutorial from the "100 Days of Code" course (educational use).
    - Intended for learning and practise — not production software.
"""

import random
import hangman_words
import hangman_art
# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
word_list = hangman_words
lives = 6

# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
stages = hangman_art
chosen_word = random.choice(word_list.word_list)
print(hangman_art.logo)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    # TODO-6: - Update the code below to tell the user how many lives they have left.
    print(f"****************************<${lives}>/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
            print(f'''You've already guessed letter: ${guess} ''')
        else:
            display += "_"

    print("Word to guess: " + display)

    # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    #  e.g. You guessed d, that's not in the word. You lose a life.

    if guess not in chosen_word:
        print(f'''You guessed ${guess}, that's not in the word. You lose a life ''')
        lives -= 1

        if lives == 0:
            game_over = True

            # TODO 7: - Update the print statement below to give the user the correct word they were trying to guess.
            print(f'''It was ${chosen_word}!''')
            print(f"***********************YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    # TODO-2: - Update the code below to use the stages List from the file hangman_art.py
    print(stages.logo[lives])
