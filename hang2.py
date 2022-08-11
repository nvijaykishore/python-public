import random
# word_list = ["aardvark", "baboon", "camel"]

from hangman_words import word_list

chosen_word = random.choice(word_list)
# print(chosen_word)
no_of_lives = 6
chosen_len = len(chosen_word)
solution = []

from hangman_art import stages

from hangman_art import logo
print(logo)

for num in range(chosen_len):
    solution.insert(num,'_')
#ch = 'a'
correct = 0
while no_of_lives >= 0 and correct < chosen_len:
    ch = input("Input a letter: ").lower()
    if ch not in solution: 
      for num in range(chosen_len):
        if ch == chosen_word[num]:
          #print("Right")
          correct += 1
          solution[num] = ch
        #else:
        
    else:
        print("You already selected that letter. Try again")
        print(stages[no_of_lives])
        no_of_lives -= 1
        
    
    if ch not in chosen_word:
          print(stages[no_of_lives])
          no_of_lives -= 1
    
    
    print(solution)

if "_" not in solution:
    print("You win")
else:
    print("You lose")

print(f"Your answer is : {' '.join(solution)}")

print(f"chosen word is: {' '.join(chosen_word)}")
      