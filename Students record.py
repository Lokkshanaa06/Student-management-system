import re
from tabulate import tabulate
def details():
    
    #student name
    try:
        s_name=input("Enter the student name:")
        while not re.match(r'^[a-zA-Z\s]+$', s_name):
                if not s_name.isalnum():
                    print("You have entered some special characters. please provide name in alphabets")
                    s_name=input("Enter the student name:")
                else:
                    if not s_name.replace(' ', '').isalpha():
                        print("You have entered numbers.please provide name in alphabet")
                    s_name=input("Enter the student name:")
    except Exception as e:
        print(f"An error occured {e}")
    
    #student register no
    try:
        s_regno=input("\nEnter your register number:")   
        while not s_regno.isdigit():
            if s_regno.isalpha():
                print("You have entered alphabets.Please enter only digits")
                s_regno=input("\nEnter your register number:")  
            elif s_regno.isalnum():
                print("You have entered the combination of letters and digits.Please enter only digits")
                s_regno=input("\nEnter your register number:") 
            else:
                print("You have entered special characters.Please enter only digits")
                s_regno=input("\nEnter your register number:") 
        while len(s_regno)!=6:
            print("Reguster number should contain 6 digits only.")
            s_regno=input("\nEnter your register number:") 
    except Exception as e:
        print(f"An error occured {e}")
    
    #student date of birth
    try:
        while True:
            stud_dob=input("Enter the date of birth:")
            format_of_dob=r'^\d{2}-\d{2}-\d{4}$'
            if re.match(format_of_dob,stud_dob):
                #print("Date of birth:",stud_dob)
                break
            else:
                print("Invalid format of date of birth") 
    except Exception as e:
        print(f"An error occured {e}")
    
    #gender=input("Enter the gender (Male/Female):")
    #print("The gender of the student is:",gender)
 
    stud_marks=[]
    for i in range(5):
        if i==0:
            #language 1 mark
            while True: 
                try:
                    lang1_mark=int(input("Enter the language 1 mark:"))
                    if lang1_mark<0 or lang1_mark>100:
                        raise ValueError("Marks should be within 0-100")
                    else:
                        stud_marks.append(lang1_mark)
                        break
                except ValueError as ve:
                    print(ve)
        elif i==1:
            #language 2 mark
            while True: 
                try:
                    lang2_mark=int(input("Enter the language 2 mark:"))
                    if lang2_mark<0 or lang2_mark>100:
                        raise ValueError("Marks should be within 0-100")
                    else:
                        stud_marks.append(lang2_mark)
                        break
                except ValueError as ve:
                    print(ve) 
        elif i==2:
            #maths mark        
            while True: 
                try:
                    maths_mark=int(input("Enter the maths mark:"))
                    if maths_mark<0 or maths_mark>100:
                        raise ValueError("Marks should be within 0-100")
                    else:
                        stud_marks.append(maths_mark)
                        break
                except ValueError as ve:
                    print(ve)
        elif i==3:
            #science mark
            while True: 
                try:
                    sci_mark=int(input("Enter the science mark:"))
                    if sci_mark<0 or sci_mark>100:
                        raise ValueError("Marks should be within 0-100")
                    else:
                        stud_marks.append(sci_mark)
                        break
                except ValueError as ve:
                    print(ve) 
        elif i==4:
            #social science mark
            while True: 
                try:
                    socsci_mark=int(input("Enter the social science mark:"))
                    if socsci_mark<0 or socsci_mark>100:
                        raise ValueError("Marks should be within 0-100")
                    else:
                        stud_marks.append(socsci_mark)
                        break
                except ValueError as ve:
                    print(ve)         
    print(stud_marks)  
    
    grades=[]
    for i in stud_marks:
        if 90<i<=100:
            grades.append("O")
        elif 80<i<=90:
            grades.append("A+")
        elif 70<i<=80:
            grades.append("A")
        elif 60<i<=70:
            grades.append("B+")
        elif 50<i<=60:
            grades.append("C")
        elif 35<i<=50:
            grades.append("D")
        else:
            grades.append("E")         
            
    print(grades)       
    
    stud_total=0
    stud_total=lang1_mark+lang2_mark+maths_mark+sci_mark+socsci_mark
    
    stud_percent=(stud_total/500)*100
    #pass or fail
    
    try:
        if lang1_mark<35 or lang2_mark<35 or maths_mark<35 or sci_mark<35 or socsci_mark<35:
            final_result="Fail"
        else:
            final_result="Pass"
    except ValueError as ve:
        print(ve)   
    
    table_data=[
        ["Language 1",stud_marks[0],grades[0]],
        ["Language 2",stud_marks[1],grades[1]],
        ["Maths",stud_marks[2],grades[2]],
        ["Science",stud_marks[3],grades[3]],
        ["Social science",stud_marks[4],grades[4]],
        ["Total",stud_total," "],
        ["Percentage",stud_percent," "],
    ]
    
    print("SSLC EXAMINATION RESULTS")
    print("STUDENT DETAILS:")
    print("------------------------------------------------")
    print(f"Student Name:   {s_name}")
    print(f"Register Number:{s_regno}")  
    print(f"Date of birth:  {stud_dob}")  
    print("\n Marks and grades obtained")
    print(tabulate(table_data,headers=["Subjects","Marks","Grades"],tablefmt="grid"))
    print("Final result:   ",final_result)
    
    
def start():
    while True:
        y = input("Do you want to enter student details? (yes/no): ")
        if y.lower() == "yes":
            details()
        else:
            break

print("STUDENT DETAILS:")
start()