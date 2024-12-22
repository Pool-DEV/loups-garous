from roles.base_role import BaseRole

class LittleGirl(BaseRole):
    def __init__(self):
        super().__init__(
            name = "Petite Fille",
            team = "vil",
            description = "Son objectif est d'éliminer tous les Loups-Garous. Chaque nuit, elle peut espionner les Loups-Garous."
        )