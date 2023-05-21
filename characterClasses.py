from random import randint


class BaseCharacter:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __str__(self):
        return f"{self.name} is level {self.level}."


class KnightCharacter(BaseCharacter):
    def __init__(self, name, race, alignment, experience_points,
                 stats={
                     "Strength": 10,
                     "Dexterity": 10,
                     "Constitution": 10,
                     "Intelligence": 10,
                     "Wisdom": 10,
                     "Charisma": 10
                 }):
        self.name = name
        self.race = race
        self.alignment = alignment
        self.experience_points = experience_points
        self.stats = stats

    def __str__(self):
        return f"{self.name} with the stats {self.stats}"

    def calculate_level(self):
        level = 1
        experience_points = self.experience_points
        level_thresholds = [
            0, 300, 900, 2700, 6500, 14000, 23000, 34000, 48000, 64000,
            85000, 100000, 120000, 140000, 165000, 195000, 225000, 265000,
            305000, 355000
        ]
        for i, threshold in enumerate(level_thresholds):
            if experience_points >= threshold:
                level = i + 1
        return level

    def calculate_attack(self, weapon_proficiency=0, personal_trait=0):
        return randint(1, 20) + self.stats["Strength"]\
            + weapon_proficiency + personal_trait

    def calculate_health(self, tough_trait=False):
        if tough_trait:
            return (self.level + self.stats["Constitution"]) * 7
        else:
            return (self.level + self.stats["Constitution"]) * 4

    def calculate_defense(self, armor=None, shield=None, ability_modifiers=None):
        10 + (self.level)/2 + armor + shield + ability_modifiers
