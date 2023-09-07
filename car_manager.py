from car import Car
import random
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        super().__init__()
        self.level = 1
        self.cars = []
        self.current_speed = STARTING_MOVE_DISTANCE

    def level_up(self):
        self.current_speed = STARTING_MOVE_DISTANCE + (MOVE_INCREMENT * self.level)
        for car in self.cars:
            car.increase_speed(self.current_speed)
        self.level += 1

    def generate_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Car(self.current_speed)
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.move()

            if car.xcor() > 300:
                self.cars.remove(car)
                car.delete_self()

