from art import logo, vs
from game_data import data
import random

def print_profile(dummy_data):
    return (
        f"{dummy_data["name"]}, a {dummy_data["description"]}, from {dummy_data["country"]} with {dummy_data["follower_count"]} followers")


def check_user_guess(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"


# 3. Choose random data for B.
b_data = random.choice(data)


# 8. While loop to run until user gives correct answers.
is_game_over = False
score = 0
while True:
    # 1. Print project logo
    print(logo)

    # 7. Convert B to A and get new B.
    a_data = b_data
    if a_data == b_data:
        b_data = random.choice(data)

    # 9. Show user his/her score if he/she is right.
    if score > 0:
        print(f"You're right! Current Score : {score}")

    # 4. Print game comparison statements.
    print(f"Compare A : {print_profile(a_data)}")
    print(vs)
    print(f"Against B : {print_profile(b_data)}")

    # 5. Get User Guess.
    user_input = input("Who has more followers? Type 'A' or 'B':  ").lower()

    # 6. Decide score for user according to answer.
    is_user_correct = check_user_guess(user_input,a_data['follower_count'], b_data['follower_count'])
    if is_user_correct:
        score += 1
    else:
        print("\n" * 20)
        print(logo)
        print(f"Sorry that's wrong. Final Score: {score}")
        is_game_over = True
        break









