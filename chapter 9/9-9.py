class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles = 20):
        self.odometer_reading += miles


class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + " -kwh battery.")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        else:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def update_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


elctric_car = ElectricCar('tesla', 'model x', 2018)
print(elctric_car.get_descriptive_name())
elctric_car.update_odometer(100)
elctric_car.read_odometer()
elctric_car.update_odometer(110)
elctric_car.read_odometer()
elctric_car.increment_odometer()
elctric_car.read_odometer()
elctric_car.battery.describe_battery()
elctric_car.battery.get_range()
elctric_car.battery.update_battery()
elctric_car.battery.describe_battery()
elctric_car.battery.get_range()
