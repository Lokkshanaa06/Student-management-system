import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\sh\Desktop\Patterns cognitive\Tesseract python\tesseract.exe'

img_file="poem.jpeg"
img=cv2.imread(img_file)



resize_img=cv2.resize(img,(450,450))
'''
cv2.imshow("resized image",resize_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
gray_img=cv2.cvtColor(resize_img,cv2.COLOR_BGR2GRAY)
'''
cv2.imshow("gray",gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''


ret,thresh_imag=cv2.threshold(resize_img,127,255,cv2.THRESH_BINARY)
cv2.imshow("threshed image",thresh_imag)
cv2.waitKey(0)
cv2.destroyAllWindows()

#result=pytesseract.image_to_string(gray_img)
#print(result)