import random

#end_of_play = False

print("Welcome to the number guessing game!!")

print("Think of a number between 1 and 100")

sel_num = random.randint(1,100)

chosen_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if chosen_difficulty == "hard":
    no_of_attempts = 5
    print("You have 5 attempts to guess the number")
else:
    no_of_attempts = 10
    print("You have 10 attempts to guess the number")
    

def play_on(sel_num=sel_num,no_of_attempts = no_of_attempts):
    
    while no_of_attempts != 0:
        
        guess = int(input("Make a guess: "))
        
        if guess == sel_num:
            print(f"You got it! The answer was {sel_num}")
            no_of_attempts = 0
            return
        
        if no_of_attempts > 0:
            if guess < sel_num:
                print(f"Too low.")
                no_of_attempts -= 1
                #print(f"You have {no_of_attempts} remaining")
            elif guess > sel_num:
                print(f"Too high")
                no_of_attempts -= 1
            
            if no_of_attempts > 0:
                print("Guess again")
                print(f"You have {no_of_attempts} remaining")
            else:
                print(f"You are out of attempts. You lose")
                return
        
    
    #return no_of_attempts
    


play_on(sel_num,no_of_attempts)
    



    