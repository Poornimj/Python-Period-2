from car import Car


class ElectricCar(Car):
    def __init__(self, regi_num, max_speed, battery_capacity):
        super().__init__(regi_num, max_speed)
        self.battery_capacity = battery_capacity


class GasolineCar(Car):
    def __init__(self, regi_num, max_speed, tank_volume):
        super().__init__(regi_num, max_speed)
        self.tank_volume = tank_volume


def main():
    electric_car = ElectricCar("ABC-15", 180, 52.5)
    gasoline_car = GasolineCar("ACD-123", 165, 32.3)

    electric_car.accelerate(150)
    gasoline_car.accelerate(120)

    electric_car.drive(3)
    gasoline_car.drive(3)

    print("Electric Car Details:")
    electric_car.print_car_details()

    print("Gasoline Car Details:")
    gasoline_car.print_car_details()


if __name__ == "__main__":
    main()
