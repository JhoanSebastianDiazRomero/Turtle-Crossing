import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "Up")


game_is_on = True
counter = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.generate_car()
    car_manager.move_cars()

    if player.at_finish_line():
        player.reset_position()
        car_manager.level_up()
        scoreboard.level_up()

    for car in car_manager.cars:
        if car.distance(player) <= 20:
            game_is_on = False
            scoreboard.game_over()

    counter += 1

screen.exitonclick()