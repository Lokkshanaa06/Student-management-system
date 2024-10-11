import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'Pattens cognitive\tesseract python\tesseract.exe'
img_file="assignment.jpg"

img=Image.open(img_file)

ocr_result=pytesseract.image_to_string(img)

print(ocr_result)