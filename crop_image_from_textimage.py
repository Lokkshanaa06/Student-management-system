import cv2
import pytesseract
from pytesseract import Output
import os
import matplotlib.pyplot as plt

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\sh\Desktop\Patterns cognitive\Tesseract python\tesseract.exe'


def show_text_from_image(image_path):
    # Read the image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Could not open or find the image {image_path}")
        return None, None
    
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Use pytesseract to get data from the image
    data = pytesseract.image_to_data(gray_image, output_type=Output.DICT)
    
    # Print all detected text
    print("Detected text from the image:")
    for i in range(len(data['text'])):
        if int(data['conf'][i]) > 0:  # Confidence level filter to ignore low-confidence words
            print(data['text'][i], end=' ')
    print()  # Newline for better readability

    return image, data

def crop_word_from_image(image, data, word):
    # Iterate through all detected text
    for i in range(len(data['text'])):
        if word.lower() in data['text'][i].lower():
            x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
            cropped_image = image[y:y+h, x:x+w]
            
            # Display the cropped image
            plt.imshow(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB))
            plt.title(f'Cropped image containing: {word}')
            plt.axis('off')
            plt.show()

            # Save the cropped image
            cropped_image_path = f"cropped_{word}.png"
            cv2.imwrite(cropped_image_path, cropped_image)
            
            print(f"Cropped image saved as {cropped_image_path}")
            return
    
    print(f"Word '{word}' not found in the image.")

if __name__ == "__main__":
    image_path = input("Enter the path to the image: ")
    image, data = show_text_from_image(image_path)
    
    if image is not None and data is not None:
        word = input("Enter the word to search for: ")
        crop_word_from_image(image, data, word)