from fpdf import FPDF

class Shirtificate(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 24)
        self.cell(0, 10, 'CS50 Shirtificate', ln=True, align='C')
        self.ln(10)

    def add_shirtificate(self, name):
        self.image('shirtificate.png', x=0, y=60, w=self.w, h=150)
        self.set_font('Arial', 'B', 24)
        self.set_text_color(255, 255, 255)
        self.cell(0, 210, f'{name} took CS50', align='C', ln=True)

def main():
    name = input("What's your name? ")

    pdf = Shirtificate()
    pdf.add_page()
    pdf.add_shirtificate(name)

    pdf.output('shirtificate.pdf')

if __name__ == "__main__":
    main()
