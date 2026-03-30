import random
import turtle as t
# Uses ones only for extracting the colors
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("image.jpg", 30)
# for color in colors[1:]:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

t.colormode(255)

rgb_colors = [(24, 116, 160), (211, 180, 21), (158, 20, 25), (254, 250, 253), (229, 239, 242), (5, 65, 30),
              (220, 63, 24), (225, 204, 103), (233, 69, 46), (16, 141, 47), (9, 42, 84), (8, 101, 17),
              (117, 176, 152), (159, 25, 22), (126, 171, 184), (145, 84, 101), (50, 173, 58), (47, 162, 178),
              (234, 53, 56), (69, 25, 30), (24, 12, 10), (11, 63, 134), (180, 133, 151), (238, 169, 160),
              (235, 200, 17), (163, 208, 184), (235, 165, 170),]
brush = t.Turtle()
brush.hideturtle()
brush.penup()

# These parameters can be adjusted as desired
dot_size = 20
step = 50
num_of_rows = 10

x_start = -330
y_start = -300
x_end = x_start + step * num_of_rows
y_end = y_start + step * num_of_rows

for y in range(y_start, y_end, step):
    for x in range(x_start, x_end, step):
        brush.goto(x, y)
        brush.dot(dot_size, random.choice(rgb_colors))

screen = t.Screen()
screen.exitonclick()
