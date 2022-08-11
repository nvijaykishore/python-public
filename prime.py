import math

def prime_checker(number):
    num_of_loops = round(math.sqrt(number))
    Prime = True
    EOL = False
    for num in range(2,num_of_loops+1):
        if not EOL:
            if number % num == 0:
                Prime = False
                EOL = True
            else:
                Prime = True
    
    if Prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)