from roles.base_role import BaseRole

class SimpleVillager(BaseRole):
    def __init__(self):
        super().__init__(
            name = "Simple Villageois",
            team = "vil",
            description = "Son objectif est d'éliminer tous les Loups-Garous. Il ne dispose d'aucun pouvoir particulier : uniquement sa perspicacité et sa force de persuasion."
        )