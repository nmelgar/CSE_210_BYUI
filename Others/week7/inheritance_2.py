# a parent class called Person
class Person:                    

    def __init__(self, number):
        self._number = number

    def get_number(self):
        return self._number

# a child class called Student
class Student(Person):
    
    # invoking the parent constructor using "super"!
    def __init__(self, number):
        super().__init__(number)

student = Student("0123456789")
number = student.get_number()
print(number)

# Opinions vary but a good rule of thumb is to limit inheritance 
# levels to the average number of items a person can remember at once. 
# For most people, that means three or four. If you find yourself 
# creating more, stop and ask the question, "do I actually need a 
# different abstraction?" 