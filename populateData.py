import sqlite3
from faker import Faker
import json


def populate_data(number_of_characters=100):
    connection = sqlite3.connect("characters.db")
    cursor = connection.cursor()
    faker = Faker()
    for _ in range(number_of_characters):
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
    connection.commit()
    connection.close()
