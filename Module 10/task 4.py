import random
from car import Car
from race import Race

cars = [Car(f"ABC-{i}", random.randint(100, 200)) for i in range(1, 11)]
race = Race("Grand Demolition Derby", 8000, cars)

hours_passed = 0
while not race.race_finished():
    race.hour_passes()
    hours_passed += 1
    if hours_passed % 10 == 0:
        print(f"\nHour {hours_passed}")
        race.print_status()

print("\nFinal Status after the race is finished:")
race.print_status()