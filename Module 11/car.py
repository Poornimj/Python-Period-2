class Car:
    def __init__(self, regi_num, max_speed):
        self.registration_number = regi_num
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0


    def accelerate(self, speed_change):
        new_speed = self.current_speed + speed_change

        if new_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif new_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed

    def drive(self, hours):
        # Increase the distance travelled based on the current speed and number of hours
        if hours > 0:
            self.travelled_distance += self.current_speed * hours

    def print_car_details(self):
        print(f"Registration Number: {self.registration_number}")
        print(f"Maximum Speed: {self.max_speed} Km/h")
        print(f"Current Speed: {self.current_speed} Km/h")
        print(f"Travelled Distance: {self.travelled_distance} Km")
        print()

    def print_car_details_task4(self):
        # Print the details of the car
        print(
            f"{self.registration_number:<10} | {self.max_speed:<10} | {self.current_speed:<12} | {self.travelled_distance:<15}")



