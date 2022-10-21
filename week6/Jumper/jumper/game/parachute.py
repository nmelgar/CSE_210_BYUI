class Parachute():
    """A parachute is an object you use when you jump from
    airplanes, buildings or when you want to fly.

    Attributes:
        
    """

    def parachute_1(self):
        """This method will print the parachute when the user starts the game.
        Args:
            self (Parachute): an instance of Parachute.
        """
        print("\n   ____   ")
        print("  /____\  ")
        print("  \    / ")
        print("   \  / ")
        print("   .O.  ")
        print("   /|\ ")
        print("   / \ ")

        print("\n^^^^^^^^^^")

    def parachute_2(self):
        """This method will print the parachute when the user fails one time guessing.
        Args:
            self (Parachute): an instance of Parachute.
        """
        print("\n  /____\  ")
        print("  \    / ")
        print("   \  / ")
        print("   .O.  ")
        print("   /|\ ")
        print("   / \ ")

        print("\n^^^^^^^^^^")

    def parachute_3(self):
        """This method will print the parachute when the user fails 2 times guessing.
        Args:
            self (Parachute): an instance of Parachute.
        """
        print("\n  \    / ")
        print("   \  / ")
        print("   .O.  ")
        print("   /|\ ")
        print("   / \ ")

        print("\n^^^^^^^^^^")

    def parachute_4(self):
        """This method will print the parachute when the user fails 3 times guessing.
        Args:
            self (Parachute): an instance of Parachute.
        """
        print("\n   \  / ")
        print("   .O.  ")
        print("   /|\ ")
        print("   / \ ")

        print("\n^^^^^^^^^^")

    def parachute_5(self):
        """This method will print the parachute when the user fails 4 times guessing.
        When the user comes to this point he/she has lost.
        Args:
            self (Parachute): an instance of Parachute.
        """
        print("\n   .x.  ")
        print("   /|\ ")
        print("   / \ ")

        print("\n^^^^^^^^^^")
        print("You lost! :(")

    def print_parachute(self, player_points):
        """This method will decide about what parachute to print based on user's points.
        Args:
            self (Parachute): an instance of Parachute.
            player_points(int): the user will begin with 4 points
        """
        if player_points == 4:
            self.parachute_1()
        elif player_points == 3:
            self.parachute_2()
        elif player_points == 2:
            self.parachute_3()
        elif player_points == 1:
            self.parachute_4()
        elif player_points == 0:
            self.parachute_5()
