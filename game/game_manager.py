import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import *
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
        """

        if self.phase != "setup":
            raise Exception("Les joueurs ne peuvent être ajoutés qu'avant le début de la partie.")
        
        self.players.append(player)
        self.logs.append(f"{player.name} a rejoint la partie.")

    def remove_player(self, player):
        """
        Retire un joueur de la partie.
        """
        if self.phase != "setup":
            raise Exception("Les joueurs ne peuvent être retirés qu'avant le début de la partie.")
        
        self.players.remove(player)
        self.logs.append(f"{player.name} a quitté la partie.")

    def assign_roles(self):
        """
        Assigner des rôles aux joueurs.
        """
        if self.phase != "setup":
            raise Exception("Les rôles ne peuvent être assignés qu'avant le début de la partie.")
        
        if len(self.players) != NB_PLAYERS:
            raise Exception(f"Le nombre de joueurs doit être de {NB_PLAYERS} pour commencer la partie.")
        
        roles = list(ROLES.keys())
        random.shuffle(roles)

        print(roles)