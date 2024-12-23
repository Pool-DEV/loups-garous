import random

class GameManager:
    def __init__(self, roles):
        """
        Create a new game.
        """

        self.players = []
        self.roles = roles
        self.alive_players = []
        self.phase = "setup"  
        self.current_round = 0

    def add_player(self, player):
        """
        Add a player to the game.
        """

        if self.phase != "setup":
            raise Exception("Les joueurs ne peuvent être ajoutés qu'avant le début de la partie.")
        
        self.players.append(player)

    def remove_player(self, player):
        """
        Remove a player from the game.
        """

        if self.phase != "setup":
            raise Exception("Les joueurs ne peuvent être retirés qu'avant le début de la partie.")
        
        self.players.remove(player)

    def assign_roles(self):
        """
        Assign roles randomly to players.
        """

        if self.phase != "setup":
            raise Exception("Les rôles ne peuvent être assignés qu'avant le début de la partie.")
        
        if len(self.players) != len(self.roles):
            raise Exception("Le nombre de joueurs et le nombre de rôles ne correspondent pas.")
        
        random.shuffle(self.roles)

        for player in self.players:
            player.assign_role(self.roles.pop())