import time
from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    # Detect collision with wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with right paddle
    if ball.distance(r_paddle) < 63 and ball.xcor() > 320:
        ball.bounce_x_r_paddle()

    # Detect collision with left paddle
    if ball.distance(l_paddle) < 63 and ball.xcor() < -320:
        ball.bounce_x_l_paddle()

    # Detect R paddle misses
    if ball.xcor() > 370:
        ball.reset_position()
        scoreboard.l_point()

    # Detect L paddle misses
    if ball.xcor() < -370:
        ball.reset_position()
        scoreboard.r_point()





screen.exitonclick()