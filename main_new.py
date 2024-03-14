import sys,subprocess
import random
from game_data import data
from art import logo,vs

def get_account_name():
    """Get data from random account"""
    return random.choice(data)


def format_account_name(account):
    """Format account into printable format: name, description and country"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    # print(f'{name}: {account["follower_count"]}')
    return f"{name}, a {description}, from {country}"

def check_answers(guess , a_followers , b_followers):
    """Checks followers against user's guess
    and returns True if they got it right.
    Or False if they got it wrong."""
    if a_followers>b_followers:
        return guess=="a"
        # or can be done like this.
        # if guess == "a"
        # return True
    else:
        return guess=="b"


def game():
    print(logo)
    score = 0
    should_continue = True
    account_a = get_account_name()
    account_b = get_account_name()
    while should_continue:
        account_a = account_b
        account_b = get_account_name()
        while account_a == account_b:
            account_b = get_account_name()
            print(f"Compare A: {format_account_name(account_a)}.")
            print(vs)
            print(f"Against B: {format_account_name(account_b)}.")
            guess = input("Who has more followers? Type 'A' or 'B': ").lower()
            a_follower_count = account_a["follower_count"]
            b_follower_count = account_b["follower_count"]
            is_correct = check_answers(guess, a_follower_count, b_follower_count)
            subprocess.run('clear',shell=True)
            print(logo)
            if is_correct:
                score += 1
                print(f"You're right! Current score: {score}.")
            else:
                game_should_continue = False
                print(f"Sorry, that's wrong. Final score: {score}")

game()