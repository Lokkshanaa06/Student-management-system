import pytesseract
from PIL import Image
import cv2
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\sh\Desktop\Pattens cognitive\Tesseract python\tesseract.exe'

img_file="letter.jpg"
img=Image.open(img_file)

temp="temp.png"
img.save(temp)

os.system(temp)


#print(img)
#print(img.size)
#img.show()
 
try:
    img=Image.open(img_file)
    
    #image preprocessing
    img_cv=cv2.imread(img_file,cv2.IMREAD_GRAYSCALE)
    _, img_cv=cv2.threshold(img_cv,150,255,cv2.THRESH_BINARY)
    img=Image.fromarray(img_cv)

    ocr_result=pytesseract.image_to_string(img)
    print(ocr_result)
except Exception as e:
    print(f"An error occurred: {e}")

