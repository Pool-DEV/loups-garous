class Player:
    def __init__(self, socket, name):
        """
        Represents a player in the game.
        """

        self.socket = socket
        self.name = name
        self.role = None
        self.alive = True
        self.votes = 0
        self.is_sheriff = False
        self.is_in_love = False

    def assign_role(self, role):
        """
        Assigns a role to the player.
        """

        self.role = role

    def vote(self):
        """
        Votes for the player.
        """

        if not self.alive:
            raise Exception(f"{self.name} est mort, vous ne pouvez pas voter pour lui.")
        
        self.votes += 1

    def reset_votes(self):
        """
        Resets the number of votes for the player.
        """

        self.votes = 0

    def kill(self):
        """
        Kills the player.
        """

        self.alive = False

    def elect_sheriff(self):
        """
        Elects the player as sheriff.
        """

        self.is_sheriff = True

    def unelect_sheriff(self):
        """
        Dismisses the player as sheriff.
        """

        self.is_sheriff = False
    
    def fall_in_love(self):
        """
        Makes the player fall in love.
        """

        self.is_in_love = True

    def __str__(self):
        """
        Returns a string representation of the player.
        """

        return f"{self.name} ({self.role}, {'alive' if self.alive else 'dead'})"