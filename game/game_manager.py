from roles import ROLES
from player import Player
import random


class GameManager:
    def __init__(self):
        """
        Initialise le gestionnaire de jeu.
        """
        self.players = []  # Liste des joueurs dans la partie
        self.alive_players = []  # Joueurs encore en vie
        self.phase = "setup"  # Phases possibles : setup, night, day, vote
        self.current_round = 0  # Numéro de la manche actuelle
        self.logs = []  # Historique des événements du jeu
    def add_player(self, player):
        """
        Ajoute un joueur à la partie.
        
        :param player: Instance de Player.
        """
        if self.phase != "setup":
            raise Exception("Les joueurs ne peuvent être ajoutés qu'avant le début de la partie.")
        self.players.append(player)
    def assign_roles(self):
        """
        Assigne des rôles aléatoires aux joueurs à partir de la liste des rôles disponibles.
        """
        if self.phase != "setup":
            raise Exception("Les rôles ne peuvent être assignés qu'avant le début de la partie.")
        if len(self.players) > len(ROLES):
            raise Exception("Pas assez de rôles disponibles pour le nombre de joueurs.")
        roles = list(ROLES.keys())
        for player in self.players:
            role = random.choice(roles)
            roles.remove(role)
            player.assign_role(role)
            self.alive_players.append(player)
            self.logs.append(f"{player.name} a reçu le rôle {role.name}.")
    def start_game(self):
        """
        Démarre la partie.
        """
        if self.phase != "setup":
            raise Exception("La partie est déjà en cours.")
        if len(self.players) < 5:
            raise Exception("Il faut au moins 5 joueurs pour démarrer la partie.")
        
        self.phase = "night"
        self.current_round = 1
        self.logs.append("La partie commence !")
        self.assign_roles()
    def night_phase(self):
        """
        Gère la phase de nuit.
        """
        self.logs.append(f"🌙 Nuit {self.current_round} commence.")
        for player in self.alive_players:
            if player.role and hasattr(player.role, "night_action"):
                player.role.night_action(self)

        self.phase = "day"
        self.logs.append(f"🌅 Nuit {self.current_round} terminée. Le jour se lève.")

    def day_phase(self):
        """
        Gère la phase de jour.
        """
        self.logs.append(f"☀️ Jour {self.current_round} commence.")
        self.phase = "vote"

    def vote_phase(self):
        """
        Gère la phase de vote pour éliminer un joueur.
        """
        self.logs.append(f"🗳️ Vote pour éliminer un joueur.")
        most_voted_player = max(self.alive_players, key=lambda p: p.votes, default=None)

        if most_voted_player:
            self.logs.append(f"{most_voted_player.name} a été éliminé.")
            most_voted_player.kill()
            self.alive_players = [p for p in self.alive_players if p.alive]
        else:
            self.logs.append("Aucun joueur n'a été éliminé.")

        for player in self.alive_players:
            player.reset_votes()

        self.check_victory()