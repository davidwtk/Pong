# This module makes the pong ball
from turtle import Turtle
BALL_COLOUR = "White"
BALL_SHAPE = "circle"
BALL_SPEED = 0.05


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(BALL_SHAPE)
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color(BALL_COLOUR)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.velocity = BALL_SPEED

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.setpos(new_x, new_y)

    def wall_bounce(self):
        self.y_move *= -1
        self.move()

    def paddle_bounce(self):
        self.x_move *= -1
        self.velocity *= 0.9
        self.move()

    def new_point(self):
        self.setpos(0, 0)
        self.velocity = BALL_SPEED
        self.paddle_bounce()
