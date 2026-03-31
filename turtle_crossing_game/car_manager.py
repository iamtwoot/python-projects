import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self, y, x=350):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.setheading(180)
        self.color(random.choice(COLORS))
        self.goto(x, y)

    def move(self):
        self.forward(STARTING_MOVE_DISTANCE)

    def off_screen(self):
        return self.xcor() < -340
