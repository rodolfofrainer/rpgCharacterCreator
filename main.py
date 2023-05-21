import sqlite3
import os
from pathlib import Path
from random import randint
from characterClasses import KnightCharacter
from faker import Faker
import json

# Create database if it doesn't exist
if not os.path.exists("characters.db"):
    Path("characters.db").touch(exist_ok=True)

# Establish connection and cursor
connection = sqlite3.connect("characters.db")
cursor = connection.cursor()

# Create table if it doesn't exist
create_table = "CREATE TABLE IF NOT EXISTS characters (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, race TEXT, alignment TEXT, experience_points INTEGER, stats TEXT)"
cursor.execute(create_table)

# Populate data


def populate_data(number_of_characters=100):
    faker = Faker()
    for _ in range(100):
        name = faker.name()
        race = faker.word()
        alignment = faker.word()
        experience_points = faker.random_int(min=0, max=100)
        stats = {
            "Strength": faker.random_int(min=1, max=20),
            "Dexterity": faker.random_int(min=1, max=20),
            "Constitution": faker.random_int(min=1, max=20),
            "Intelligence": faker.random_int(min=1, max=20),
            "Wisdom": faker.random_int(min=1, max=20),
            "Charisma": faker.random_int(min=1, max=20)
        }

        insert_query = "INSERT INTO characters (name, race, alignment, experience_points, stats) VALUES (?, ?, ?, ?, ?)"
        cursor.execute(insert_query, (name, race, alignment,
                       experience_points, json.dumps(stats)))


# populate_data(100)


# Commit changes and close connection
connection.commit()
connection.close()
