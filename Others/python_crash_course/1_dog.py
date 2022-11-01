# class that represents a dog, not one dog in particular, but any dog
# add something that is common to most dogs
# -- dog have name and age (information)
# -- sit and roll over (behaviors)

# Think of a class as a set of instructions for how to make an instance.

# define a class
class Dog:
    # docstring describing what this class does
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """simulate rolling over in response to a command"""
        print(f"{self.name} rolled over!")


# create an instance of a specific dog
# the __init__() method creates and instance representing the particular dog
# and sets the name and age attributes using the values we provided
# Python then returns and instance representing the dog
# this line will call the __init__() method, with the arguments
my_dog = Dog('Poni', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"She is {my_dog.age} years old.")

# After we create an instance from the class Dog, we can use dot notation to
# call any method defined in Dog.
my_dog.sit()
my_dog.roll_over()

print("")
# You can create as many instances from a class as you need
dog_2 = Dog('Negro', 8)
print(f"Your dog's name is {dog_2.name}.")
print(f"He is {dog_2.age} years old.")
dog_2.sit()
dog_2.roll_over()
