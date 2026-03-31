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
cars = [CarManager(x=random.randint(-250, 280), y=random.randint(-230, 280)) for _ in range(25)]


screen.listen()
screen.onkeypress(player_object.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    for car in cars:
        car.move()
        if car.off_screen():
            cars.remove(car)
            cars.append(CarManager(y=random.randint(-250, 280)))
