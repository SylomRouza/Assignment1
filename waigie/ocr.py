from pdf2image import convert_from_path
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

pdf_path = r'heat_stroke.pdf'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

pages = convert_from_path(pdf_path, 350, poppler_path=r'poppler-\bin')
with open('heat_stroke.txt', 'w') as my_file:
    for page in pages:
        out = pytesseract.image_to_string(page)
        my_file.write(out)