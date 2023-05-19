class BaseCharacter:
    def __init__(self, name, level, stats):
        self.name = name
        self.level = level
        self.stats = stats

    def __str__(self):
        return f"{self.name} is level {self.level} with {self.stats} stats."


character1 = BaseCharacter("Bob", 1, {"str": 10, "dex": 10, "int": 10})
print(character1)
