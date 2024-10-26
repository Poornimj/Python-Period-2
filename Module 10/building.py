from elevator import Elevator
class Building:
    def __init__(self, bottom, top, num):
        self.bottom_floor = bottom
        self.top_floor = top
        self.num_of_elevators = num
        self.elevators = [Elevator(bottom, top) for _ in range(num)]

    def operate_elevator(self, elevator_number, target_floor):
        if 0 <= elevator_number < len(self.elevators):
            print(f"\nOperating Elevator {elevator_number + 1}")
            self.elevators[elevator_number].go_to_floor(target_floor)
        else:
            print("Invalid elevator number. Please select a valid elevator.")

    def reset_all_elevators(self):
        print("\nReturning all elevators to the bottom floor.")
        for i, elevator in enumerate(self.elevators):
            print(f"\nResetting Elevator {i + 1}")
            elevator.reset_to_bottom()

    def fire_alarm(self):
        print("\nFire alarm activated! Sending all elevators to the ground floor.")
        for i, elevator in enumerate(self.elevators):
            print(f"Elevator {i + 1} is heading to the ground floor.")
            elevator.reset_to_bottom()