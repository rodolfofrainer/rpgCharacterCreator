from fpdf import FPDF


class characterSheet(FPDF):
    def character_information(self, character):
        self.name = character.values[0]
        self.ch_class = character.values[1]
        self.race = character.values[2]
        self.alignment = character.values[3]
        self.experience_points = character.values[4]
        self.stats = character.values[5]
        print(self.stats.split())

    def header(self):
        # Rendering logo:
        self.image("DNDDICE.COM_Character_Sheet.webp", 0, 0, 210, 297)
        self.set_font("helvetica", "B", 15)
        # Moving cursor down and to the right:
        self.cell(20, 7, ln=1)
        self.cell(38)
        # Printing Character Name and class:
        self.cell(87, 10, f"{self.name.title()}")
        self.cell(43, 14, f"{self.ch_class.title()}", ln=1)
        # Race, Alignment:
        self.ln(1.5)
        self.cell(87, 10)
        self.cell(43, 10, f"{self.race.title()}")
        self.set_font("helvetica", "B", 7)
        self.cell(43, 12, f"{self.alignment.title()}", ln=1)
        # strength stat:
        self.set_font("helvetica", "B", 24)
        self.ln(12)
        self.cell(2, 5)
        self.cell(5, 5, f"{self.stats.split()[1][:-1]}")
        # dexterity stat:
        self.ln(30)
        self.cell(3, 5)
        self.cell(5, 5, f"{self.stats.split()[3][:-1]}")
