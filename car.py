from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5


class Car(Turtle):
    def __init__(self, speed):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.penup()
        self.main_y = random.randint(-250, 250)
        self.goto(300, self.main_y)
        self.movement_speed = speed

    def move(self):
        self.backward(self.movement_speed)

    def increase_speed(self, speed):
        self.movement_speed = speed

