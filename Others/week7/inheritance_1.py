# a regular class called Person
class Person:                    

    def get_name(self):
        return "Joseph"

# a class that inherits from Person
class Student(Person):

    def get_number(self):
        return "0123456789"

# the student instance automatically has the get_name() method!
student = Student()
name = student.get_name()
print(name)

#  In this case, the Person class is known as a parent class. 
#  The Student class is known as a child class. They are also called base 
#  and derived or super and sub classes. It doesn't matter what pair 
#  of terms you use as long as you understand the distinction. 