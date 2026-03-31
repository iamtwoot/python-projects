import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player_object = Player()
cars = [CarManager(x=random.randint(-250, 280), y=random.randint(-230, 240)) for _ in range(25)]

scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player_object.up, "Up")

car_speed = 0.1
game_is_on = True
while game_is_on:
    time.sleep(car_speed)
    screen.update()

    for car in cars:
        car.move()
        if car.off_screen():
            cars.remove(car)
            cars.append(CarManager(y=random.randint(-250, 280)))

    if player_object.finished():
        player_object.reset_position()
        scoreboard.level += 1
        car_speed *= 0.6
