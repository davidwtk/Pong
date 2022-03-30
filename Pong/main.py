from turtle import Screen
import ball
import bat
import score
import time
# Ln 7-10 makes the screen
s = Screen()
s.screensize(canvwidth=800, canvheight=600, bg="black")
s.title("Pong")
s.tracer(0)
# Ln 12-14 makes the net and scores
sN = score.Net()
s_Left = score.Scoreboard("left")
s_Right = score.Scoreboard("right")
# Ln 16 makes the ball
b1 = ball.Ball()
# Ln 18-19 makes the player bats
player1_bat = bat.Bat(-350)
player2_bat = bat.Bat(350)
# Ln 21-25 makes the game detect keypress for movement of bats
s.listen()
s.onkeypress(player1_bat.left_up, "w")
s.onkeypress(player1_bat.left_down, "s")
s.onkeypress(player2_bat.right_up, "Up")
s.onkeypress(player2_bat.right_down, "Down")
# Ln 27-53 is game logic. 32-38 allows ball to bounce off walls. 40-56 checks if ball hits paddle/scores also end game
game_on = True
while game_on:
    time.sleep(b1.velocity)
    s.update()
    b1.move()
    if b1.ycor() > 300 or b1.ycor() < -300:
        b1.wall_bounce()

    elif b1.distance(player1_bat) < 50 and b1.xcor() <= -335:
        b1.paddle_bounce()
    elif b1.distance(player2_bat) < 50 and b1.xcor() >= 335:
        b1.paddle_bounce()

    elif b1.xcor() > 360:
        s_Left.score(-50)

        if s_Left.check_win():
            sN.game_over(1)
            game_on = False
        else:
            b1.new_point()

    elif b1.xcor() < -360:
        s_Right.score(70)

        if s_Right.check_win():
            sN.game_over(2)
            game_on = False
        else:
            b1.new_point()
s.exitonclick()
