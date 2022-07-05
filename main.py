import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.move,'Up')


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car.create_car()
    car.car_move()

    for item in car.car_list:
        if item.distance(player) < 20:
            score.game_over()
            game_is_on = False

    if player.ycor() == 290:
        player.reset_player()
        car.level_up()
        score.update_score()

    screen.update()


screen.exitonclick()