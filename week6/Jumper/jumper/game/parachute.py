class Parachute():
    """A parachute is an object you use when you jump from
    airplanes, buildings or when you want to fly.

    Attributes:
        word(str): A random word
    """

    def parachute_1(self):
        print("\n   ____   ")
        print("  /____\  ")
        print("  \    / ")
        print("   \  / ")
        print("   .O.  ")
        print("   /|\ ")
        print("   / \ ")

        print("\n^^^^^^^^^^")

    def parachute_2(self):
        print("\n  /____\  ")
        print("  \    / ")
        print("   \  / ")
        print("   .O.  ")
        print("   /|\ ")
        print("   / \ ")

        print("\n^^^^^^^^^^")

    def parachute_3(self):
        print("\n  \    / ")
        print("   \  / ")
        print("   .O.  ")
        print("   /|\ ")
        print("   / \ ")

        print("\n^^^^^^^^^^")

    def parachute_4(self):
        print("\n   \  / ")
        print("   .O.  ")
        print("   /|\ ")
        print("   / \ ")

        print("\n^^^^^^^^^^")

    def parachute_5(self):
        print("\n   .x.  ")
        print("   /|\ ")
        print("   / \ ")

        print("\n^^^^^^^^^^")
        print("You lost! :(")
        return

    def print_parachute(self, player_points):
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
