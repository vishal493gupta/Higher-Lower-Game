from art import logo, versis
from game_data import data
import random

def format_data(account):
    """Takes the account data and return printable format"""
    account_name = account['name']
    account_profession = account['Profession']
    return f"{account_name},a {account_profession}"

def check_answer(user_guess, A_followers, B_followers):
    """Take the user's guess and the follower counts aand return if they got it right"""
    if A_followers > B_followers:
        return user_guess == "A"
    else:
        return user_guess == "B"

score = 0
print("Let's start to play the Higher-Lower Game...")
print(logo)
account_B = random.choice(data)
game_should_repeated = True

while game_should_repeated:
    account_A = account_B
    account_B = random.choice(data)
   
    if account_A == account_B:
        account_B = random.choice(data)

    print(f"Compare A: {format_data(account_A)}")
    print(versis)
    print(f"Against B: {format_data(account_B)}")

    guess = input("Who has more Followers? Type 'A' or 'B': ")

    print("\n"*10)
    print(logo)

    A_follower_count = account_A["follower-count"]
    B_follower_count = account_B["follower-count"]

    is_correct = check_answer(guess, A_follower_count, B_follower_count)

    if is_correct:
        score += 1
        print(f"Yes, Yor're Right! Current Score is {score}.")
        print("--------------------------------------------")
    else:
        print(f"Sorry, that's wrong. Final Score is {score}.") 
        print("--------------------------------------------")
        game_should_repeated = False