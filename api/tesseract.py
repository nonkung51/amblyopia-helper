from PIL import Image
import pytesseract

def text_from_image_file(image_name,lang):
    read = pytesseract.image_to_string(Image.open(image_name), lang=lang)
    return read

if __name__ == '__main__':
    print(text_from_image_file("text.jpg", "tha"))
