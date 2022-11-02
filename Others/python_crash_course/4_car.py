from logging import makeLogRecord


class Car:
    """Simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """Initializes attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


# make an instance from the Car class
my_new_car = Car("audi", "a4", 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

print(" ")
# first way to modify an attribute's value (modify it directly)
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

print(" ")
# second way to modify an attribute's value (modify it through a method)
my_new_car.update_odometer(24)
my_new_car.read_odometer()

print(" ")
# third way to modify an attribute's value (increment attribute's value through a method)
my_new_car.increment_odometer(100)
my_new_car.read_odometer()