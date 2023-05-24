import sqlite3
import os
from pathlib import Path
from random import randint
from characterClasses import KnightCharacter
from character_creator import CharacterCreator
from pdfSheet import characterSheet


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
createCharacter = CharacterCreator()
createCharacter.createCharacter()
cursor.execute(createCharacter.insert_query, createCharacter.values)
print("Character created and saved.")

# Instantiation of inherited class
pdf = characterSheet()
pdf.add_page()
pdf_path = f"character_sheets/{createCharacter.values[0]}_Sheet.pdf"
pdf.output(pdf_path)

# Commit changes and close connection
connection.commit()
connection.close()


# populate database with 100 entries
# populate_data(100)
