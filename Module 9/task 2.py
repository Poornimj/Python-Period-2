from car import Car

car = Car ("ABC-123",142)

car.accelerate(30)
car.accelerate(70)
car.accelerate(50)

print("Car Details After Increasing Speed:")
car.print_car_details()

car.accelerate(-200)

print("Car Details After Emergency Braking:")
car.print_car_details()