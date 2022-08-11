#IF, else, elif sample
bill = 0
height = int(input("What is your height: "))

if height >= 120:
    print("You can play the roller coaster")
    age = int(input("What is your age? "))
 #   if age >= 45 and age <= 55:
 #       bill = 0
 #   else:
    if age < 12:
        bill = 5
        print("The price of the ticket will be $5")
    elif age <=18:
        bill = 7
        print("YThe price of the ticket will be $7")
    elif age >= 45 and age <= 55:
        print("Enjoy the ride on us")
    else:
        bill = 12
        print("The price of the ticket will be $12")
    
    photo = input("Do you want a photo taken. Enter Y or N ? ")
    if photo == "Y":
        bill += 3
    
    print(f"The total price of the ticket is ${bill}.")
        
else:
    print("You have to grow taller before you can play on the roller coaster")
             