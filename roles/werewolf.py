from roles.base_role import BaseRole

class Werewolf(BaseRole):
    def __init__(self):
        super().__init__(
            name = "Loup-Garou",
            team = "wolf",
            description = "Son objectif est d'éliminer tous les innocents (ceux qui ne sont pas Loups-Garous). Chaque nuit, il se réunit avec ses compères Loups pour décider d'une victime à éliminer."
        )