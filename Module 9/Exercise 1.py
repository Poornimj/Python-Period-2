class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def display_info(self):
        print(f"Registration Number: {self.registration_number}")
        print(f"Maximum Speed: {self.max_speed} Km/h")
        print(f"Current Speed: {self.current_speed} Km/h")
        print(f"Travelled Distance: {self.travelled_distance} Km")

car = Car("ABC-123",142)
car.display_info()
