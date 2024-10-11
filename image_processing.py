#using cv2 module
import cv2

def gray_scale(img):
    try:
        if img is None:
            print("Image couldn't be loaded")
        else:
            #grayscaling an image
            gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            cv2.imshow("Gray_img",gray_img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
    except Exception as e:
        print(f"An error occured {e}")
        
def rotate_right(img):
    try:
        if img is None:
            print("Image couldn't be loaded")
        else:
            #rotate right
            right_rot_imag=cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
            cv2.imshow("image rotated right",right_rot_imag)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
    except Exception as e:
        print(f"An error occured {e}")
        
def rotate_left(img):
    try:
        if img is None:
            print("Image couldn't be loaded")
        else:
            #rotate left
            left_rot_imag=cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE)
            cv2.imshow("image rotated left",left_rot_imag)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
    except Exception as e:
        print(f"An error occured {e}")
        
def resize(img):
    try:
        if img is None:
            print("Image couldn't be loaded")
        else:
            w=int(input("Enter the width:"))
            h=int(input("Enter the height:"))
            resize_imag=cv2.resize(img,(w,h))
            cv2.imshow("resized image",resize_imag)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
    except Exception as e:
        print(f"An error occured {e}")
            
def main():
    img=cv2.imread("dogs.jpeg")
    #to show the original image
    cv2.imshow("image:",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    while True:
        action=input("Enter the action to be performed on the image:\ngrayscale\nrotate right\nrotate left\nresize\nexit)?\n")
        if action.lower()=="grayscale":
            gray_scale(img)
        elif action.lower()=="rotate right":
            rotate_right(img)
        elif action.lower()=="rotate left":
            rotate_left(img)
        elif action.lower()=="resize":
            resize(img)
        elif action.lower()=="exit":
            break
        else:
            print("Invalid action to be performed on the image.")

main()

    
    
    
    
    
   
    
    
    
    
    
    
    
    #hsv_img =cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #resize_img=cv2.resize(img,(250,300))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
''' 
    x,y,w,h=100, 100, 30, 20
    if x>=0 and y>=0 and w>0 and h>0 and x+w<=img.shape[1] and y+h<=img.shape[0]:
        cropped_img=img[y:y+h,x:x+w]
        cv2.imshow("Cropped image",cropped_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("an error occured")
    #cv2.imwrite("Output_image.jpeg",img)
    '''
'''
#using pillow module
from PIL import Image
import os 

img="dogs.jpeg"

if not os.path.exists(img):
    print(f"The image does not exist")    
else:
    try:
        imag=Image.open(img)
        temp="temp_Dogs.jpeg"
        imag.save(temp)
        if os.name=="nt":
            os.system(f"start {temp}")
    except Exception as e:
        print(f"An exception has occured")

from PIL import Image
img = Image.open('dogs.jpeg')
img.show()


from skimage import io

img=io.imread("dogs.jpeg")
io.imshow(img)
io.show()
'''