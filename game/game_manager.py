import random

class GameManager:
    def __init__(self, roles):
        """
        Create a new game.
        """

        self.players = []
        self.roles = roles
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

    def start_game(self):
        """
        Start the game.
        """

        if self.phase != "setup":
            raise Exception("La partie a déjà commencé.")
        
        self.assign_roles()
        self.phase = "night"
        self.current_round = 1

    def check_game_is_over(self):
        """
        Check if the game is over.
        """

        wolves = 0
        villagers = 0

        for player in self.players:
            if villagers > 0 and wolves > 0:
                return False
            elif player.role.team == "wolf" and player.alive:
                wolves += 1
            elif player.role.team == "vil" and player.alive:
                villagers += 1
        
        if wolves == 0 or villagers == 0:
            return True
        else:
            return False