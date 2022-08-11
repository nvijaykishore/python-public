# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

from turtle import Turtle
from turtle import listen

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)
screen.delay(3000)

#create paddle

l_pos = (-350.0, 0.0)
r_pos = (350, 0.0)
l_paddle = Paddle(l_pos,"white")
r_paddle = Paddle(r_pos,"red")

ball1 = Ball()
ball1.penup()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up" )
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w" )
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
ball_direction = "up"

ball1.ball_move()

while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball1.ball_move()



    #Detect collision with wall

    if ball1.ycor() > 280 or ball1.ycor() < -280:
        ball1.bounce_y()
        ball1_direction = "down"

    #To detect collission with wall and 1 player game
    #if ball1.xcor() < -380:
    #    ball1.bounce_x()
    #    ball1_direction = "down"

         # Detect collision with paddles

    if ball1.distance(r_paddle) < 50 and ball1.xcor() > 330 or ball1.distance(l_paddle) < 50 and ball1.xcor() < -330:
        ball1.bounce_x()


    #if ball1.distance(r_paddle) < 50 and ball1.xcor() > 320:
    #   ball1.bounce_x()

    # detect rt paddle miss
    if ball1.xcor() > 380:
        ball1.reset_position()
        l_paddle.goto(l_pos)
        r_paddle.goto(r_pos)
        scoreboard.l_point()

    # detect left paddle miss
    if ball1.xcor() < -380:
        ball1.reset_position()
        l_paddle.goto(l_pos)
        r_paddle.goto(r_pos)
        scoreboard.r_point()

    if scoreboard.r_score >= 7 or scoreboard.l_score >= 7:
        scoreboard.goto(-50,0)
        scoreboard.write("GAME Over", font=("Courier", 50, "normal"))
        game_is_on = False

screen.exitonclick()
