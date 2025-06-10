import sys
from PIL import Image
import pytesseract

def extract_text(image_path: str) -> str:
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text

if __name__ == "__main__":
    image_path = sys.argv[1]
    print(extract_text(image_path))