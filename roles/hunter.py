from roles.base_role import BaseRole

class Hunter(BaseRole):
    def __init__(self):
        super().__init__(
            name = "Chasseur",
            team = "vil",
            description = "Son objectif est d'éliminer tous les Loups-Garous. A sa mort, il doit éliminer un joueur en utilisant sa dernière balle."
        )