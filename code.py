import fitz  # PyMuPDF
import pytesseract
from PIL import Image
from different_file_save import save_as_pdf, save_as_epub, save_as_txt, save_as_docx, save_as_file


# Set the path to the Tesseract executable file
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# Function to save the extracted text as the desired file format
def extract_text(file_path, output_path):
    if file_path.lower().endswith('.pdf') or file_path.lower().endswith('png'):
        # PDF handling
        pdf_document = fitz.open(file_path)
        extracted_text = ""

        for page_number in range(pdf_document.page_count):
            page = pdf_document.load_page(page_number)
            pixmap = page.get_pixmap()
            img = Image.frombytes("RGB", [pixmap.width, pixmap.height], pixmap.samples)
            img_gray = img.convert('L')
            text = pytesseract.image_to_string(img_gray, lang='eng')
            extracted_text += text + '\n'

        pdf_document.close()

    elif file_path.lower().endswith('.jpg') or file_path.lower().endswith('.jpeg') or file_path.lower().endswith('png'):
        # JPEG image handling
        img = Image.open(file_path)
        img = img.resize((img.width * 3, img.height * 3))  # Resize the image for better OCR
        img_gray = img.convert('L')
        config = '--psm 6 --oem 1 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
        extracted_text = pytesseract.image_to_string(img_gray, lang='eng', config=config)

    else:
        print("Unsupported file format.")
        return
    print(extracted_text)

# Input file path
file_path = r'C:\Users\BHARAT\Desktop\my files\books and notes\8 MUST-KNOW Data Science & Analytics.pdf'

# Output file path (where the extracted text will be saved)
output_path = r'C:\Users\BHARAT\Desktop\extracted_text.txt'

# Extract text from the input file and save it as a text file

extract_text(file_path, output_path)
