import random

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)

    def print_status(self):
        print(f"\n{'Registration':10} {'Max Speed (km/h)':15} {'Current Speed (km/h)':15} {'Travelled Distance (km)':20}")
        print("="*70)
        for car in self.cars:
            car.print_car_details_task4()

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False