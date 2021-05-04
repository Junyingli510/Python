from openpyxl import Workbook
from openpyxl.drawing.image import Image

book = Workbook()
sheet = book.active

img = Image("pic1.png")
sheet['A1'] = 'This is a picture'

sheet.add_image(img, 'A1')

