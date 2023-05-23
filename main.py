import sqlite3
import os
from pathlib import Path
from random import randint
from characterClasses import KnightCharacter
from stats_allocation import Stats


def createCharacter():
    character_name = input("What is your character's name? ")
    race_options = ["Human", "Elf", "Dwarf",
                    "Halfling", "Gnome", "Half-Elf", "Half-Orc"]
    for i, race in enumerate(race_options):
        print(f"{i + 1}. {race}")
    character_race = race_options[int(input()) - 1]

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
    insert_query = "INSERT INTO characters (name, race, alignment, experience_points, stats) VALUES (?, ?, ?, ?, ?)"
    values = (character_name, character_race, character_alignment,
              character_experience, str(character_stats.stats_return()))
    cursor.execute(insert_query, values)
    print("Character created and saved.")


# Create database if it doesn't exist
if not os.path.exists("characters.db"):
    Path("characters.db").touch(exist_ok=True)

# Establish connection and cursor
connection = sqlite3.connect("characters.db")
cursor = connection.cursor()

# Create table if it doesn't exist
create_table = "CREATE TABLE IF NOT EXISTS characters (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, race TEXT, alignment TEXT, experience_points INTEGER, stats TEXT)"
cursor.execute(create_table)

# Create character
createCharacter()

# Commit changes and close connection
connection.commit()
connection.close()

# populate database with 100 entries
# populate_data(100)
