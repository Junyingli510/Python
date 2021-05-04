from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

im = Image.open('images/P_5.png')
text = pytesseract.image_to_string(im, lang='eng')
print(text)