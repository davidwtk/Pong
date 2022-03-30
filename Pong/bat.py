# This module makes the CPU bat and the player-controlled bat
from turtle import Turtle
BAT_COLOUR = "White"


class Bat(Turtle):
    def __init__(self, x_position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.x_position = x_position
        self.hideturtle()
        self.color(BAT_COLOUR)
        self.setpos(x_position, 0)
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.showturtle()

    def left_up(self):
        new_y = self.ycor() + 20
        self.setpos(self.x_position, new_y)

    def left_down(self):
        new_y = self.ycor() - 20
        self.setpos(self.x_position, new_y)

    def right_up(self):
        new_y = self.ycor() + 20
        self.setpos(self.x_position, new_y)

    def right_down(self):
        new_y = self.ycor() - 20
        self.setpos(self.x_position, new_y)
