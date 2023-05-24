from fpdf import FPDF


class characterSheet(FPDF):
    def header(self):
        # Rendering logo:
        self.image("DNDDICE.COM_Character_Sheet.webp", 0, 0, 210, 297)
