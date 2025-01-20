import fitz  # PyMuPDF
from flask import Flask, Response
from fpdf import FPDF
import json
import os
import io
from helpers.pdfHandling import create_pdf, count_images_in_pdf, process_pdf_to_text

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    data = {
        'process': 0,
        'is_done': False
    }

    return Response(json.dumps(data), status=200, mimetype='application/json')


def process_document(pdf_path, output_folder, max_images=5, lang='tur'):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    pdf_document = fitz.open(pdf_path)

    total_image_count = count_images_in_pdf(pdf_document)
    process_pdf_to_text(pdf_document, total_image_count, lang, output_folder)

pdf_path = './test-files/test-1.pdf'
output_folder = 'PDF_OUTPUT'
max_images = 15  # Maximum image count to scan

#process_document(pdf_path, output_folder)

if __name__ == "__main__":
    app.run(debug=True)