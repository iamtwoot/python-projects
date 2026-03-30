from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

start_x = 0
for _ in range(3):
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.goto(start_x, 0)
    start_x -= 20




screen.exitonclick()