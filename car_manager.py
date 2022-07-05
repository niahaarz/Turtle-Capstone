from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager():
    def __init__(self):
        self.car_list = []
        self.car_speed = STARTING_MOVE_DISTANCE

    
    def create_car(self):
        
        chance = random.randint(1, 6)
        if chance == 1:
            new_car = Turtle('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.setheading(180)
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randrange(-250, 250))
            self.car_list.append(new_car)


    def car_move(self):
        for car in self.car_list:
            car.forward(self.car_speed)


    def level_up(self):
        self.car_speed += MOVE_INCREMENT
