class TerminalService:
    """A service that handles terminal operations.

        The responsibility of a TerminalService is to provide input and output operations for the 
        terminal.
        """

    def read_letter(self, prompt):
        """Gets text input from the terminal. Directs the user with the giver prompt.

        Args:
            self (TerminalService): An instance of TerminalService.
            prompt (string): The prompt to display on the terminal.

        Returns:
            string: The user's input as text.
        """
        return input(prompt)
