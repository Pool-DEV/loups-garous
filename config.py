from roles import *

# Configuration file for the application

# Roles repartition
ROLES = {
    SimpleVillager(): 2,
    Werewolf(): 3,
    Seer(): 1,
    Witch(): 1,
    Hunter(): 1,
    Cupid(): 1,
    Thief(): 1,
}

# Number of players
NB_PLAYERS = sum(ROLES.values())