from random import randint
from faker import Faker

faker = Faker()


class BaseCharacter:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __str__(self):
        return f"{self.name} is level {self.level}."


class KnightCharacter(BaseCharacter):
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.attack = 7 * self.level
        self.health = 30 * self.level

    def __str__(self):
        return f"{self.name} is level {self.level} with {self.attack} attack and {self.health} health."


for index, obj in enumerate(range(10)):
    char = KnightCharacter(faker.name(), randint(1, 10))
    print(f'{index+1}: {char}')
