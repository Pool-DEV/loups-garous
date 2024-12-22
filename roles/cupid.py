from roles.base_role import BaseRole

class Cupid(BaseRole):
    def __init__(self):
        super().__init__(
            name = "Cupidon",
            team = "vil",
            description = "Son objectif est d'éliminer tous les Loups-Garous. Dès le début de la partie, il doit former un couple de deux joueurs. Leur objectif sera de survivre ensemble, car si l'un d'eux meurt, l'autre se suicidera."
        )