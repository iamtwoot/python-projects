from turtle import Turtle

class Snake:

    def __init__(self):
        self.segments = []

        start_x = 0
        for _ in range(3):
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(start_x, 0)
            start_x -= 20
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)
        self.segments[0].left(90)