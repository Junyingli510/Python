from pdf2image import convert_from_path
import os

folder_name = os.getcwd() + r'\temp'
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

pages = convert_from_path('0003.pdf')
print(len(pages))
for i, page in enumerate(pages):
    print(i)
    page.save(folder_name + r'\{:04d}.jpg'.format(i+1), 'JPEG')

'''
pyinstaller --onefile --clean convert_pdf_to_jpg.py
'''