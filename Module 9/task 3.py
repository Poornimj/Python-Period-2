from car import Car

car = Car ("ABC-123",142)

print("Initial Car Details:")
car.print_car_details()

car.accelerate(30)
car.accelerate(70)
car.accelerate(50)

print("Car Details After Increasing Speed:")
car.print_car_details()

car.drive(1)

print("Car Details After Driving for 1 Hour:")
car.print_car_details()

car.accelerate(-200)

print("Car Details After Emergency Braking:")
car.print_car_details()

car.drive(2)

print("Car Details After Driving for 2 More Hours:")
car.print_car_details()