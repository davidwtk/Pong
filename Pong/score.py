# This module makes the scoreboard for the game.
from turtle import Turtle

SCOREBOARD_COLOUR = "White"
POINTS_TO_WIN = 5


class Net(Turtle):
    def __init__(self):
        super().__init__()
        self.net()
        self.speed(0)

    def net(self):
        self.hideturtle()
        self.pencolor(SCOREBOARD_COLOUR)
        self.penup()
        self.pensize(5)
        self.setpos(0, -280)
        self.setheading(90)
        for line in range(12):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(30)

    def game_over(self, player):
        self.clear()
        self.penup()
        self.setpos(0, 0)
        self.color("green")
        self.write(arg=f"GAME OVER. \nPlayer {player} wins!", align="center", font=("Algerian", 20, "bold"))


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.speed(0)
        self.hideturtle()
        self.pencolor(SCOREBOARD_COLOUR)
        self.penup()
        self.pensize(5)
        self.current_score = 0
        if position == "left":
            self.score(-50)
        elif position == "right":
            self.score(70)

    def score(self, x_position):
        self.clear()
        self.penup()
        self.setpos(x_position, 250)
        self.pendown()
        self.write(arg=f"{self.current_score}", align="right", font=("Algerian", 20, "bold"))
        self.current_score += 1
        return self.current_score

    def check_win(self):
        if self.current_score == POINTS_TO_WIN + 1:
            return True




