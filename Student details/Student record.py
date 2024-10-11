from datetime import datetime
import re
def details():
    
    #student name
    def name():
        stud_name=input("Enter the name again:")
        return stud_name
    s_name=input("Enter the student name:")
    while not re.match(r'^[a-zA-Z\s]+$', s_name):
            if not s_name.isalnum():
                print("You have entered some special characters. please provide name in alphabets")
                s_name=name()
            else:
                if not s_name.replace(' ', '').isalpha():
                    print("You have entered numbers.please provide name in alphabet")
                s_name=name()
    #print("The student name is",s_name) 
    
    #student register no
    def regno():
        stud_regno=input("Enter the register no(only 6 digits):")
        return stud_regno
    s_regno=input("Enter the student register no:")
    while not s_regno.isdigit():
        if s_regno.isalpha():
            print("You have entered alphabets.Enter digits" )
            s_regno=regno()
        elif s_regno.isalnum():
            print("You have entered combination of alphabets and numbers.Enter digits")
            s_regno=regno()
        else:
            print("You have entered special characters.Enter digits")
            s_regno=regno()
    while (len(s_regno)!=6):
            print("The register number should contains 6 digits")
            s_regno=regno()
    #print("The student register number:",s_regno)
    
    #student date of birth
    while True:
        stud_dob=input("Enter the date of birth:")
        format_of_dob=r'^\d{2}-\d{2}-\d{4}$'
        if re.match(format_of_dob,stud_dob):
            #print("Date of birth:",stud_dob)
            break
        else:
            print("Invalid format of date of birth")
    
    #language 1 marks
    def l1_mark():
        l1=int(input("Enter the language 1 mark (0-100):"))
        return l1
    lang1_mark=int(input("Enter the language 1 mark:"))
    while lang1_mark<0 or lang1_mark>100:
        print("Invalid input of marks")
        lang1_mark=l1_mark()
    #print("Language 1:",lang1_mark)       
    
    #language 2 marks
    def l2_mark():
        l2=int(input("Enter the language 2 mark (0-100):"))
        return l2
    lang2_mark=int(input("Enter the language 2 mark:"))
    while lang2_mark<0 or lang2_mark>100:
        print("Invalid input of marks")
        lang2_mark=l2_mark()
    #print("Language 2:",lang2_mark)
    
    #maths mark
    def m_mark():
        m=int(input("Enter the maths mark (0-100):"))
        return m
    maths_mark=int(input("Enter the maths mark:"))
    while maths_mark<0 or maths_mark>100:
        print("Invalid input of marks")
        maths_mark=m_mark()
    #print("Maths:",maths_mark)
    
    #science mark
    def s_mark():
        s=int(input("Enter the science mark (0-100):"))
        return s
    sci_mark=int(input("Enter the science mark:"))
    while sci_mark<0 or sci_mark>100:
        print("Invalid input of marks")
        sci_mark=s_mark()
    #print("Science:",sci_mark)
    
    #social science mark
    def ss_mark():
        ss=int(input("Enter the social science mark (0-100):"))
        return ss
    socsci_mark=int(input("Enter the social science mark:"))
    while socsci_mark<0 or socsci_mark>100:
        print("Invalid input of marks")
        socsci_mark=ss_mark()
    #print("Social Science:",socsci_mark)
    """
    #student phone number
    def phno():
        s_phno=input("Enter student phone number:")
        return s_phno
    stud_phno=input("Enter student phone number:")
    while not stud_phno.isdigit():
        if stud_phno.isalnum():
            print("Phone number should contain only digits.")
            stud_phno=phno()
        else:
            print("You have entered special characters.")
            stud_phno=phno()
    if len(stud_phno)!=10:
        print("Phone number should contain 10 digits")
        stud_phno=phno()
    #print("The student phone number is",stud_phno)
    
    #student mail id
    def mail():
        s_mail=input("Enter student mail id:")
        return s_mail
    stud_mail=input("Enter student mail id:")
    while stud_mail.isalnum():
        print("Since it is an email it should have an special symbol @")
        stud_mail=mail()
    while not stud_mail.isalnum():
        x=stud_mail.find("@gmail.com")
        if x==-1:
            print("You have entered other special characters than @")
            stud_mail=mail()
        else:
            break
    #print("Student mail id:",stud_mail)
    """
    #student gender
    gender=input("Enter the gender (Male/Female):")
    #print("The gender of the student is:",gender)

    stud_total=0
    stud_total=lang1_mark+lang2_mark+maths_mark+sci_mark+socsci_mark
    
    
    stud_percent=(stud_total/500)*100
    #pass or fail
    final_result=" "
    
    if lang1_mark<35 or lang2_mark<35 or maths_mark<35 or sci_mark<35 or socsci_mark<35:
        final_result="Fail"
    else:
        final_result="Pass"
    
    print("SSLC EXAMINATION RESULTS")
    print("STUDENT DETAILS:")
    print("Student Name:   ",s_name)
    print("Register Number:",s_regno)  
    print("Date of birth:  ",stud_dob)  
    print("Language 1:   ",lang1_mark)
    print("Language 2:     ",lang2_mark)
    print("Maths:          ",maths_mark)
    print("Science:        ",sci_mark)
    print("Social Science: ",socsci_mark)
    print("Total:          ",stud_total)
    print("Percentage:     ",stud_percent)
    print("Final result:   ",final_result)
    
    
    
#starting of the program
def start():
    while True:
        y = input("Do you want to enter student details? (yes/no): ")
        if y == "yes":
            details()
        else:
            break

print("STUDENT DETAILS:")
start()