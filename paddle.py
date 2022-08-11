from turtle import Turtle

#pos = (0, 0)


class Paddle(Turtle):

    def __init__(self, pos1,colr):
        super().__init__()
        self.color(colr)
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.setposition(pos1)
        self.speed(15)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)