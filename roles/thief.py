from roles.base_role import BaseRole

class Thief(BaseRole):
    def __init__(self):
        super().__init__(
            name = "Voleur",
            team = "neutral",
            description = "Son objectif n'est pas fixe : il peut choisir son rôle parmi les deux cartes qui n'ont pas encore été distribuées."
        )