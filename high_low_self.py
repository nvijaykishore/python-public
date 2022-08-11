import random
from art import logo,vs
#Import game_data from data
from game_data import data
#Get random account

def random_account():
  return random.choice(data)

def format_data(account):
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return f"{name}, a {description}, from {country}"

def check_answer(guess,a_foll,b_foll):
    if a_foll > b_foll:
        return guess == "a"
    else :
        return guess == "b"
    
    

account_a = random_account()
account_b = random_account()

game_continue = True
score = 0
while game_continue:
    
    while account_b == account_a:
        account_b = random_account()
    
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B:{format_data(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_foll_count = account_a["follower_count"]
    b_foll_count = account_b["follower_count"]

    is_correct = check_answer(guess,a_foll_count,b_foll_count)
    
    if is_correct:
        score += 1
        print(f"You are right!. Current score is {score}")
        print(f"A: {a_foll_count} and B: {b_foll_count}")
        account_a = account_b
        account_b = random_account()
        
    else:
        game_continue = False
        print(f"Sorry!!. That's wrong. Final score is {score}")
        print(f"A: {a_foll_count} and B: {b_foll_count}")
    
    


