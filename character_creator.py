from stats_allocation import Stats


class CharacterCreator():
    def __init__(self, insert_query=None, values=None):
        self.insert_query = insert_query
        self.values = values

    def create_character(self):
        character_name = input("What is your character's name? ")

        print("What's his/her class? ")
        class_options = [
            "Barbarian",
            "Bard",
            "Cleric",
            "Druid",
            "Fighter",
            "Monk",
            "Paladin",
            "Ranger",
            "Rogue",
            "Sorcerer",
            "Warlock",
            "Wizard",
            "Artificer",
            "Blood Hunter",
        ]
        for i, char_class in enumerate(class_options):
            print(f"{i + 1}. {char_class}")
        character_class = class_options[int(input()) - 1]

        print("What's his/her race? ")
        race_options = ["Human", "Elf", "Dwarf",
                        "Halfling", "Gnome", "Half-Elf", "Half-Orc"]
        for i, race in enumerate(race_options):
            print(f"{i + 1}. {race}")
        character_race = race_options[int(input()) - 1]

        print("What's his/her alignment? ")
        alignment_options = ["Lawful Good", "Neutral Good",
                             "Chaotic Good", "Lawful Neutral",
                             "True Neutral", "Chaotic Neutral",
                             "Lawful Evil", "Neutral Evil",
                             "Chaotic Evil"]
        for i, alignment in enumerate(alignment_options):
            print(f"{i + 1}. {alignment}")
        character_alignment = alignment_options[int(input()) - 1]

        character_experience = 0
        character_stats = Stats()
        character_stats.stats_allocation()

        # Insert character data into the database
        self.insert_query = "INSERT INTO characters (name, class, race, alignment, experience_points, stats) VALUES (?, ?, ?, ?, ?, ?)"
        self.values = (
            character_name,
            character_class,
            character_race,
            character_alignment,
            character_experience,
            str(character_stats.stats_return()))
