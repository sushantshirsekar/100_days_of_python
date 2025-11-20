import random
import art

def define_attempts(game_level):
    if game_level == "easy":
        nr = 10
    else:
        nr = 5
    return nr

def reduce_attempts(x):
    x = x-1
    return x

def think_a_nr():
    return random.randint(1,100)

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a Number between 1 to 100")
user_defined_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
attempts = define_attempts(user_defined_level)
o_nr = think_a_nr()
print(f"Guessed number is {o_nr}")
is_game_over = False

while attempts > 0 :
    print(f"You have {attempts} attempts to guess the number")
    user_guess = int(input("Make a guess: "))
    if user_guess > o_nr:
        print("Too High.")
        print("Guess Again!")
        attempts = reduce_attempts(attempts)
    elif user_guess < o_nr:
        print("Too Low.")
        print("Guess Again!")
        attempts = reduce_attempts(attempts)
    else:
        print( f"You got it! the guessed number was {o_nr}")
        is_game_over = True
        break

if not is_game_over:
    print(f"You lose! the Number was {o_nr}")


