from roles.base_role import BaseRole

class Witch(BaseRole):
    def __init__(self):
        super().__init__(
            name = "Sorcière",
            team = "vil",
            description = "Son objectif est d'éliminer tous les Loups-Garous. Elle dispose de deux potions : une potion de vie pour sauver la victime des Loups, et une potion de mort pour assassiner quelqu'un."
        )