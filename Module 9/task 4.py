import random
from car import Car

cars = []

for i in range(1, 11):
    registration_number = f"ABC-{i}"
    top_speed = random.randint(100, 200)  # Random top speed between 100 and 200 km/h
    car = Car(registration_number, top_speed)
    cars.append(car)

race_finished = False

while not race_finished:

    for car in cars:
        speed_change = random.randint(-10, 15)
        car.accelerate(speed_change)

    for car in cars:
        car.drive(1)

    for car in cars:
        if car.travelled_distance >= 10000:
            race_finished = True
            break

print("\nRace Results:")
print("Registration | Top Speed | Current Speed | Travelled Distance")
print("-" * 60)
for car in cars:
    car.print_car_details_task4()