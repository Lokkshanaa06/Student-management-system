import cv2
import numpy as np
from matplotlib import pyplot as pt

image_file="dogs.jpeg"
#imag=cv2.imread(image_file)


def show_image(image_file):
    img=cv2.imread(image_file)
    cv2.imshow("image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    blurred_img = cv2.GaussianBlur(img, (5, 5), 0)
    cv2.imshow("Blurred Image", blurred_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def threshing_image(image_file):
    
    img=cv2.imread(image_file,cv2.IMREAD_GRAYSCALE)
    ret,thresh_image=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    cv2.imshow("Threshed image",thresh_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    ret,thresh_image_inv=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
    cv2.imshow("Threshed image",thresh_image_inv)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    ret,thresh_image_trunc=cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
    cv2.imshow("Threshed image",thresh_image_trunc)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    ret,thresh_image_tozero=cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
    cv2.imshow("Threshed image",thresh_image_tozero)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    ret,thresh_image_tozeroinv=cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
    cv2.imshow("Threshed image",thresh_image_tozeroinv)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def intensity_calculation(image_file):
    
    img=cv2.imread(image_file,cv2.IMREAD_GRAYSCALE)
    #calculaing the average using numpy module
    average_intensity=np.mean(img)
    
    #limiting decimals to 2 points using round function
    print(f"Average intensity: {round(average_intensity,2)}")
    #limiting decimals to 2 points using .2f 
    print(f"Average intensity: {average_intensity:.2f}")

    #maximum intensity of the image
    max_intensity=np.max(img)
    print(f"Maximum intensity:{round(max_intensity,2)}")
    
    #minimum intensity of the image
    min_intensity=np.min(img)
    print(f"Minimum intensity:{round(min_intensity,2)}")
    
    #standard deviation of the image 
    std=np.std(img)
    print(f"Standard deviation: {std}")
    
def histogram_calculation(image_file):
    
    imag=cv2.imread(image_file)
    resize_image=cv2.resize(imag,(450,450))
    img=cv2.cvtColor(resize_image,cv2.COLOR_BGR2GRAY)
    hist,bins=np.histogram(img.flatten(),bins=256,range=[0,256])
    pt.plot(bins[:-1], hist)
    pt.title('Grayscale Histogram')
    pt.xlabel('Pixel Intensity')
    pt.ylabel('Frequency')
    pt.show()
    
def add_images():
    image_file1="dogs.jpeg"
    image_file2="person.jpeg"
    image1=cv2.imread(image_file1)
    image2=cv2.imread(image_file2)
    res1=cv2.resize(image1,(300,300))
    res2=cv2.resize(image2,(300,300))
    
    added_image=cv2.add(res1,res2)
    cv2.imshow("Added",added_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def crop_image():
    image_file="dogs.jpeg"
    img=cv2.imread(image_file)
    print("shape of the image",img.shape)
    crop=img[50:100,80:130]
    cv2.imshow("cropped",crop)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

show_image(image_file)
threshing_image(image_file)
intensity_calculation(image_file)
histogram_calculation(image_file)
add_images()
crop_image()


