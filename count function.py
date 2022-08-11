name1 = "Angela Yu"
name2 = "Jack Bauer"

name = name1.lower() + name2.lower()

true_ctr = name.count("t") + name.count("r") + name.count("u") + name.count("e")
love_ctr = name.count("l") + name.count("o") + name.count("v") + name.count("e")

print(int((str(true_ctr) + str(love_ctr))))