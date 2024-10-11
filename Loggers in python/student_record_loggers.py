import re
import logging


logging.basicConfig(level=logging.INFO ,filename="student_details",filemode="a",
                        format=("%(asctime)s - %(levelname)s - %(message)s"))
    
def details():
    
    def name():
        while True:
            try:
                s_name = input("Enter the student name: ")
                if not re.match(r'^[a-zA-Z\s]+$', s_name):
                    if not s_name.isalnum():
                        raise ValueError("You have entered some special characters. Please provide the name in alphabets.")
                    elif not s_name.replace(' ', '').isalpha():
                        raise ValueError("You have entered numbers. Please provide the name in alphabets.")
                return s_name
            except ValueError as ve:
                print(ve)
                logging.error("Invalid input")
                #s_name = name()

    stud_name =name()
    #print(student_name)
    
    def regno():
        while True:
            try:
                s_regno=input("Enter the student register no:")
                while not s_regno.isdigit():
                    if s_regno.isalpha():
                        raise ValueError("You have entered alphabets.Enter digits" )
                    elif s_regno.isalnum():
                        raise ValueError("You have entered combination of alphabets and numbers.Enter digits")
                    else:
                        raise ValueError("You have entered special characters.Enter digits")
                if (len(s_regno)!=6):
                    print("The register number should contains 6 digits")
                    s_regno=regno()
                return s_regno
            except ValueError as ve:
                print(ve)
                logging.error("Invalid input")
    stud_regno=regno()
    #print(stud_regno)
    
    
    while True:
        try:
            stud_dob=input("Enter the date of birth:")
            format_of_dob=r'^\d{2}-\d{2}-\d{4}$'
            if re.match(format_of_dob,stud_dob):
                #print("Date of birth:",stud_dob)
                break
            else:
                raise ValueError("Invalid format of date of birth")
        except ValueError as ve:
            print(ve)
            logging.error("Invalid input")
    #print(stud_dob)
        
    while True: 
        try:
            lang1_mark=int(input("Enter the language 1 mark:"))
            if lang1_mark<0 or lang1_mark>100:
                raise ValueError("Marks should be within 0-100")
            else:
                break
        except ValueError as ve:
            print(ve)
    
    #print(lang1_mark)
    while True: 
        try:
            lang2_mark=int(input("Enter the language 2 mark:"))
            if lang2_mark<0 or lang2_mark>100:
                raise ValueError("Marks should be within 0-100")
            else:
                break
        except ValueError as ve:
            print(ve) 
            logging.error("Invalid input") 
            
    while True: 
        try:
            maths_mark=int(input("Enter the maths mark:"))
            if maths_mark<0 or maths_mark>100:
                raise ValueError("Marks should be within 0-100")
            else:
                break
        except ValueError as ve:
            print(ve)
            logging.error("Invalid input")
    
    while True: 
        try:
            sci_mark=int(input("Enter the science mark:"))
            if sci_mark<0 or sci_mark>100:
                raise ValueError("Marks should be within 0-100")
            else:
                break
        except ValueError as ve:
            print(ve)
            logging.error("Invalid input")        
    
    while True: 
        try:
            socsci_mark=int(input("Enter the social science mark:"))
            if socsci_mark<0 or socsci_mark>100:
                raise ValueError("Marks should be within 0-100")
            else:
                break
        except ValueError as ve:
            print(ve)
            logging.error("Invalid input")  

    gender=input("Enter the gender (Male/Female):")
    #print("The gender of the student is:",gender)

    stud_total=0
    stud_total=lang1_mark+lang2_mark+maths_mark+sci_mark+socsci_mark
    
    
    stud_percent=(stud_total/500)*100
    #pass or fail
    final_result=" "
    
    try:
        if lang1_mark<35 or lang2_mark<35 or maths_mark<35 or sci_mark<35 or socsci_mark<35:
            final_result="Fail"
        else:
            final_result="Pass"
    except ValueError as ve:
        print(ve)
        logging.warning("Something went wrong")
    '''  
    print("SSLC EXAMINATION RESULTS")
    print("STUDENT DETAILS:")
    print("Student Name:   ",stud_name)
    print("Register Number:",stud_regno)  
    print("Date of birth:  ",stud_dob)  
    print("\nLanguage 1:   ",lang1_mark)
    print("Language 2:     ",lang2_mark)
    print("Maths:          ",maths_mark)
    print("Science:        ",sci_mark)
    print("Social Science: ",socsci_mark)
    print("Total:          ",stud_total)
    print("Percentage:     ",stud_percent)
    print("Final result:   ",final_result)
    ''' 
    print("\n")
    logging.info("SSLC EXAMINATION RESULTS")
    logging.info("STUDENT DETAILS:")
    logging.info("Student Name:%s   ",stud_name)
    logging.info("Register Number:%s",stud_regno)  
    logging.info("Date of birth:  %s",stud_dob)  
    logging.info("Language 1:  %s ",lang1_mark)
    logging.info("Language 2:    %s ",lang2_mark)
    logging.info("Maths:         %s ",maths_mark)
    logging.info("Science:       %s ",sci_mark)
    logging.info("Social Science:%s ",socsci_mark)
    logging.info("Total:         %s ",stud_total)
    logging.info("Percentage:    %s ",stud_percent)
    logging.info("Final result:  %s ",final_result)
    

while True:
    y=input("Do you want to enter the student details (yes/no)?")
    if y.lower()=="yes":
        details()
    elif y.lower()=="no":
        break
    else:
        logging.error("Invalid input")