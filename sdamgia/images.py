try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract



def img_to_str(src, path_to_tesseract):
    pytesseract.pytesseract.tesseract_cmd = path_to_tesseract
    return pytesseract.image_to_string(Image.open(src), lang='rus+eng')

