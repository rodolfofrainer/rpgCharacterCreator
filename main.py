import sqlite3
import os
from pathlib import Path
from random import randint
from characterClasses import KnightCharacter
from faker import Faker

# create table if it doesn't exist


def does_table_exist():
    if not os.path.exists("characters.db"):
        Path("characters.db").touch(exist_ok=True)
    connection = sqlite3.connect("characters.db")
    cursor = connection.cursor()
    create_table = "CREATE TABLE IF NOT EXISTS characters (id INTEGER PRIMARY KEY AUTOINCREMENT, name text, level integer, attack integer, health integer)"
    cursor.execute(create_table)
    connection.commit()
    connection.close()


def populate_data(number_of_records):
    faker = Faker()
    for i in range(number_of_records):
        char = KnightCharacter(faker.name(), randint(1, 10))
        char_tuple = (char.name, char.level, char.attack, char.health)
        insert_query = "INSERT INTO characters (name, level, attack, health) VALUES (?, ?, ?, ?)"
        cursor.execute(insert_query, char_tuple)


does_table_exist()

connection = sqlite3.connect("characters.db")
cursor = connection.cursor()

populate_data(100)

connection.commit()
connection.close()
