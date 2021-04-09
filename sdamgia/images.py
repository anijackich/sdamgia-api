try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

def img_to_str(src):
    return pytesseract.image_to_string(Image.open(src), lang='rus')

