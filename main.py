import turtle
#
# timmy = turtle.Turtle()
# timmy.shape("turtle")
# timmy.color("cyan")
#
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)
#
# my_screen = turtle.Screen()
#
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ["Pokemon name", "Type"]
table.add_row(["Pikachu", "Electric"])
table.add_row(["Squirtle", "Water"])
table.add_row(["Charmander", "Fire"])

print(table)

table1 = PrettyTable()

table1.add_column("Pokemon name", ["Pikachu", "Squirtle", "Charmander"], align="l")
table1.add_column("Type", ["Electric", "Water", "Fire"], align="l")

print(table1)

