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

def count_images_in_pdf(pdf_document):
    total_images = 0
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        image_list = page.get_images(full=True)
        total_images += len(image_list)

    return total_images