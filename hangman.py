import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)
no_of_lives = 0
chosen_len = len(chosen_word)

#ch = 'a'
correct = 0
while no_of_lives <= 8 and correct < chosen_len:
  ch = input("Input a letter: ")
  for char in chosen_word:
    if char == ch:
      print("Right")
      correct += 1
    else:
      print("Wrong")
    
  no_of_lives += 1
    
    