from fpdf import FPDF


class characterSheet(FPDF):
    def character_information(self, character):
        self.name = character.values[0]
        self.race = character.values[1]
        self.alignment = character.values[2]
        self.experience_points = character.values[3]
        self.stats = character.values[4]

    def header(self):
        # Rendering logo:
        self.image("DNDDICE.COM_Character_Sheet.webp", 0, 0, 210, 297)
        self.set_font("helvetica", "B", 15)
        # Moving cursor down and to the right:
        self.cell(20, 7.5, ln=1)
        self.cell(38)
        # Printing Character Name:
        self.cell(60, 10, f"{self.name.title()}")
        # Performing a line break:
        self.ln(20)
