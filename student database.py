import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="December06!",
  database="localdb"
)
def insert_student_record(stud_regno,stud_name,stud_phno,lang1_mark,lang2_mark,maths_mark,sci_mark,socsci_mark,gender,mail,school):
    mycursor = mydb.cursor()
    sql="""INSERT INTO stud (stud_regno,stud_name,lang1_mark,lang2_mark,maths_mark,sci_mark,socsci_mark,gender,mail,school) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    values=(stud_regno,stud_name,stud_phno,lang1_mark,lang2_mark,maths_mark,sci_mark,socsci_mark,gender,mail,school)
    mycursor.execute(sql,values)
    mydb.commit()
    print("Row inserted successfully")
    mycursor.close()
    

def details():
    stud_name=input("Enter the student name:")
    for i in stud_name:
        if not i.isalpha():
            print("The name contains other characters than the alphabets")
            stud_name=input("Enter the student name:")
            break
    print("The student name:",stud_name)
    
    stud_regno=int(input("Enter the student register no:"))
    if (len(str(stud_regno)))!=6:
        print("The register number should contains 6 digits")
        stud_regno=int(input("Enter the student register no:"))
    print("The student register number:",stud_regno)
   
    lang1_mark=int(input("Enter the language 1 mark:"))
    if lang1_mark<0 or lang1_mark>100:
        print("Invalid input of marks")
        lang1_mark=int(input("Enter the language 1 mark:"))
    print("The language 1 mark:",lang1_mark)       
    
    lang2_mark=int(input("Enter the language 2 mark:"))
    if lang2_mark<0 or lang2_mark>100:
        print("Invalid input of marks")
        lang2_mark=int(input("Enter the language 2 mark:"))
    print("The language 2 mark:",lang2_mark)
    
    maths_mark=int(input("Enter the maths mark:"))
    if maths_mark<0 or maths_mark>100:
        print("Invalid input of marks")
        maths_mark=int(input("Enter the maths mark:"))
    print("The maths mark:",maths_mark)
    
    sci_mark=int(input("Enter the science mark:"))
    if sci_mark<0 or sci_mark>100:
        print("Invalid input of marks")
        sci_mark=int(input("Enter the maths mark:"))
    print("The science mark:",sci_mark)
    
    socsci_mark=int(input("Enter the social science mark:"))
    if socsci_mark<0 or socsci_mark>100:
        print("Invalid input of marks")
        socsci_mark=int(input("Enter the maths mark:"))
    print("The science mark:",socsci_mark)
    
    stud_mail=input("Enter student mail id:")
    print("Enter student mail id:",stud_mail)
    
    gender=input("Enter the gender (M/F):")
    print("The gender of the student is:",gender)
    
    school=input("Enter the school name:")
    print("The school name is",school)
    
    if lang1_mark<35 or lang2_mark<35 or maths_mark<35 or sci_mark<35 or socsci_mark<35:
        print("Fail")
    
    insert_student_record(stud_regno,stud_name,lang1_mark,lang2_mark,maths_mark,sci_mark,socsci_mark,gender,stud_mail,school)
print("STUDENT DETAILS :")
details()