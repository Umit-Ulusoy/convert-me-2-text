import os
import io
from PIL import Image
import fitz  # PyMuPDF
import pytesseract
from fpdf import FPDF

pytesseract.pytesseract.tesseract_cmd = r'C:\OCR\tesseract.exe'

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

def process_pdf_to_text(pdf_document, total_image_count, lang='tur', output_folder='PDF_OUTPUT'):
    ocr_text = ""

    processed_image_count = 0
    for page_number in range(len(pdf_document)):
        page = pdf_document.load_page(page_number)
        images_on_page = page.get_images(full=True)

        for image_index, image in enumerate(images_on_page):
            processed_image_count += 1
            progress_percentage = (processed_image_count / total_image_count) * 100
            print(f"Processing: {progress_percentage:.2f}%")

            xref = image[0]
            extracted_image = pdf_document.extract_image(xref)
            image_bytes = extracted_image["image"]

            image_pil = Image.open(io.BytesIO(image_bytes))
            extracted_text = pytesseract.image_to_string(image_pil, lang=lang)

            ocr_text += extracted_text.strip() + "\n\n"

            if processed_image_count >= total_image_count:
                break

        if processed_image_count >= total_image_count:
            break

    pdf_output_path = os.path.join(output_folder, "OCR_Output.pdf")
    create_pdf(pdf_output_path, ocr_text)

    print(f"PDF created: {pdf_output_path}")

