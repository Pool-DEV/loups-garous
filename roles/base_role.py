class BaseRole:
    def __init__(self, name, team, description, night_action):
        self.name = name
        self.team = team # "vil", "wolf", "neutral"
        self.description = description