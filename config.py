# Configuration file for the application

# Roles repartition
ROLES = {
    "villagers": 2,
    "werewolves": 3,
    "seer": 1,
    "witch": 1,
    "hunter": 1,
    "cupid": 1,
    "thief": 1,
}

# Number of players
NB_PLAYERS = sum(ROLES.values())