class Player:
    def __init__(self, player_id, name):
        """
        Represents a player in the game.
        """

        self.player_id = player_id
        self.name = name
        self.role = None
        self.alive = True
        self.votes = 0
        self.is_sheriff = False

    def assign_role(self, role):
        """
        Assigns a role to the player.
        """

        self.role = role

    def vote(self, target_player):
        """
        Votes for a player.
        """

        if not self.alive:
            raise Exception(f"{self.name} is dead and cannot vote.")
        
        if not target_player.alive:

            raise Exception(f"{target_player.name} is dead and cannot be voted for.")
        target_player.votes += 1

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

    def __str__(self):
        """
        Returns a string representation of the player.
        """

        return f"{self.name} ({self.role}, {'alive' if self.alive else 'dead'})"
