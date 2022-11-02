class Restaurant:
    """A place where you can eat amazing food.
    Not a specific one."""

    def __init__(self, restaurant_name, cuisine_type):
        """initialize restaurant_name and cuisine_type attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Provides description about the restaurant."""
        print(f"The restaurant {self.restaurant_name} is amazing.")
        print(f"If serves a great {self.cuisine_type} food.")

    def open_restaurant(self):
        """Provides the info about the restaurant opened or closed."""
        print(f"The restaurant is open.")

    def set_number_served(self, new_customers):
        self.number_served += new_customers

    def increment_number_served(self, customers_served):
        self.number_served += customers_served

restaurant_1 = Restaurant("DOGOS", "Mexican")
print(
    f"The restaurant {restaurant_1.restaurant_name} has {restaurant_1.cuisine_type} food.")

restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()

print()

restaurant_2 = Restaurant("PAOLOS", "Italian")
restaurant_2.describe_restaurant()

print()

restaurant_3 = Restaurant("ADBUL", "Iraqis")
restaurant_3.describe_restaurant()

restaurant_4 = Restaurant("George's", "US")
print(f"Has served {restaurant_4.number_served} foods.")
print(" ")
restaurant_4.set_number_served(20)
print(f"Has served {restaurant_4.number_served} foods.")

print(" ")
restaurant_4.increment_number_served(25)
print(f"Has served {restaurant_4.number_served} foods today.")
