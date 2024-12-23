from game import *
from roles import *
from config import *

names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hank", "Ivy", "John"]

players = [Player(i, names[i]) for i in range(len(names))]

roles = [role for role, count in ROLES.items() for _ in range(count)]

game = GameManager(roles)

for player in players:
    game.add_player(player)

game.assign_roles()

for player in game.players:
    if isinstance(player.role, Werewolf):
        print(f"\033[91m{player.name} est {player.role.name}\033[0m")
    else:
        print(f"{player.name} est {player.role.name}")