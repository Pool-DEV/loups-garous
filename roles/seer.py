from roles.base_role import BaseRole

class Seer(BaseRole):
    def __init__(self):
        super().__init__(
            name = "Voyante",
            team = "vil",
            description = "Son objectif est d'éliminer tous les Loups-Garous. Chaque nuit, elle peut espionner un joueur et découvrir sa véritable identité."
        )