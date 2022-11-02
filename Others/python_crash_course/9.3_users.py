class User:
    """This will create a user, not a specific one."""

    def __init__(self, first_name, last_name, username, password):
        """initializes first_name, last_name, username and password attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password

    def describe_user(self):
        print(
            f"USER: {self.last_name}, {self.first_name}. \nUsername: {self.username} Password: {self.password}")

    def greet_user(self):
        print(f"Welcome to the platform {self.username}")

user_1 = User("peter", "perez", "pperez56", "d8fkg9__00o")
user_1.describe_user()
user_1.greet_user()

print()

user_2 = User("john", "johnson", "jjohn33", "r89apasf**")
user_2.describe_user()
user_2.greet_user()