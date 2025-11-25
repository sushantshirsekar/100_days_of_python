import art
import game_data
import random

def print_comparison(first_data, second_data):
    print(
        f"Compare A: {first_data["name"]}, a {first_data["description"]}, from {first_data["country"]} with {first_data["follower_count"]} followers")
    print(art.vs)
    print(
        f"Compare B: {second_data["name"]}, a {second_data["description"]}, from {second_data["country"]} with {second_data["follower_count"]} followers")

def get_random_data():
    return random.choice(game_data.data)

# 1. Print project logo
print(art.logo)

# 3. Choose random data for A and B comparison
a_data = get_random_data()
b_data = get_random_data()



# 8. While loop to run until user gives correct answers
is_game_over = False
score = 0
while not is_game_over:
    # 4. Print Compare A and B statements and also print 'vs' logo in between
    print_comparison(a_data, b_data)

    # 5. Get User Input
    user_input = input("Who has more followers? Type 'A' or 'B':  ").lower()

    # 6. Decide score for user according to answer
    if user_input == 'a' and a_data["follower_count"] > b_data["follower_count"] or user_input == 'b' and a_data["follower_count"] < b_data["follower_count"]:
        score += 1
    else:
        print("\n" * 20)
        print(art.logo)
        print(f"Sorry that's wrong. Final Score: {score}")
        is_game_over = True
        break
    # 7. Convert B to A and get new B
    a_data = b_data
    b_data = get_random_data()
    if a_data == b_data:
        b_data = get_random_data()







