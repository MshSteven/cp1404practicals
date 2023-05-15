from prac_09.car import Car
import random


class UnreliableCar(Car):
    """Child class UnreliableCar extend from parent class Car."""

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        random_num = random.randint(0, 100)
        if random_num < self.reliability:
            if distance > self.fuel:
                distance = self.fuel
                self.fuel = 0
            else:
                self.fuel -= distance
            self.odometer += distance
        return distance
