from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.goto(-200, 250)
        self.color("black")
        self.hideturtle()
        self.write(f"Level: {self.level}", align="center", font=FONT)

