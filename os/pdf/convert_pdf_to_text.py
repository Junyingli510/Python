import os
os.environ["MAGICK_HOME"] = r"C:\Program Files (x86)\ImageMagick-6.7.5-Q8"
magick_home = os.environ.get('MAGICK_HOME')
import PyPDF2
# from wand.image import Image
from PythonMagick import Image
# from PIL import Image
import io


def pdf_page_to_png(src_pdf, pagenum = 0, resolution = 72,):
    """
    Returns specified PDF page as wand.image.Image png.
    :param PyPDF2.PdfFileReader src_pdf: PDF from which to take pages.
    :param int pagenum: Page number to take.
    :param int resolution: Resolution for resulting png in DPI.
    """
    dst_pdf = PyPDF2.PdfFileWriter()
    dst_pdf.addPage(src_pdf.getPage(pagenum))

    pdf_bytes = io.BytesIO()
    dst_pdf.write(pdf_bytes)
    pdf_bytes.seek(0)


    img = Image(pdf_bytes, resolution = resolution)
    img.convert("png")

    return img


src_pdf = PyPDF2.PdfFileReader('Building Bots with Node.js.pdf')
img = pdf_page_to_png(src_pdf, pagenum = 1, resolution = 300)
img.save(filename = '1.png')