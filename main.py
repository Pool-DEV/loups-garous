#!/usr/bin/python3
from game import *

names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hank", "Ivy", "John"]

players = [Player(i, names[i]) for i in range(len(names))]

game = GameManager()

for player in players:
    game.add_player(player)

game.assign_roles()
for player in game.players:
    print(f"{player.name} est {player.role.name}")

