import pytesseract
from PIL import Image
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\sh\Desktop\Patterns cognitive\Tesseract python\tesseract.exe'

img_file="computer.jpg"

#method to count the number of words in the text file
def count_words(file):
    try:
        with open(file,"r") as f:
            content=f.read()
            word_count=len(content.split())
            print(f"No of words: {word_count}")
    except Exception as e:
        print(f"An error occured : {e}")

#method to count the number of lines in the text file
def count_lines(file):
    try:
        with open(file,"r") as f:
            content=f.read()
            line_count=content.count('\n')+1
            print(f"No of lines: {line_count}")  
    except Exception as e:
        print(f"An error occured : {e}")    
        
#method to count the occurence of each character in the text file
def count_each_character(file):
    try:
        with open (file,"r") as f:
            content=f.read()
            char={}
            for i in content:
                if i.isalnum():
                    if i in char:
                        char[i]+=1
                    else:
                        char[i]=1
        print("Count of the each character in the text file")
        for i,count in char.items():
            print(f"{i}:{count}")
    except Exception as e:
        print(f"An error occured : {e}")  

#method to count the special characters in the text file
def count_special_character(file):
    try:
        with open(file,"r") as f:
            content=f.read()
            sc=0
            for i in content:
                if not i.isalnum() and not i.isspace():
                        sc+=1
            print(f"No of special characters: {sc}")
    except Exception as e:
        print(f"An error occured : {e}") 

#method to count the specific words in the textfile
def count_specific_word(file):
    try:
        with open(file,"r") as f:
            content=f.read()
            count={}
            specific_word=["for","the","of","it"]
            for word in specific_word:
                count[word]=content.count(word)
        for i,count in count.items():
            print(f"{i}:{count}")
    except Exception as e:
        print(f"An error occured : {e}")           
                    
#method to transfer the text from the image to the text file
def transfer(imag):
    try:
        img=Image.open(imag)
        ocr_result=pytesseract.image_to_string(img)
        file="computer.txt"
        with open (file,"w") as f:
            f.write(ocr_result)
    except Exception as e:
        print(f"An error occured: {e}")
    os.startfile(file)
    
    
    while True:
        op=input("Enter to perform the following operations \n1.count words \n2.count lines \n3.count each character  \n4.count special character \n5.count specific word \n6.exit \n")
        if op.lower()=="count words":
            count_words(file)  
        elif op.lower()=="count lines":
            count_lines(file)  
        elif op.lower()=="count each character":
            count_each_character(file)      
        elif op.lower()=="count special character":
            count_special_character(file)  
        elif op.lower()=="count specific word":
            count_specific_word(file)
        elif op.lower()=="exit":
            break
        else:
            print("Invalid input")
    
#starting of the program
def start():
    while True:
        s=input("Enter \n1.transfer \n2.exit \n")
        if s.lower()=="transfer":
            transfer(img_file)
        elif s.lower()=="exit":
            break
        else:
            print("Invalid input")
    
start()
