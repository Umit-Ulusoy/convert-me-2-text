from fpdf import FPDF

def create_pdf(pdf_output_path, ocr_text):
    pdf = FPDF()

    pdf.add_page()

    font_path = './fonts/ttf/DejaVuSans.ttf'
    pdf.add_font('DejaVu', '', font_path, uni=True)
    pdf.set_font("DejaVu", size=12)

    for line in ocr_text.splitlines():
        pdf.cell(200, 10, txt=line, ln=True, align='L')

    pdf.output(pdf_output_path)