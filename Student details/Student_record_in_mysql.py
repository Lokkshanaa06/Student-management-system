import mysql.connector
#from mysql.connector import Error
import re

mydb=mysql.connector.connect(
        host="localhost",
        username="root",
        password="Sairam2003!123",
        database="school"
        )
        
#checking the connection
def check_mysql_connection():
    
    try:
        if mydb.is_connected():
            db_info=mydb.get_server_info()
            print(f"Connected to the mysql server version {db_info}")
            cursor=mydb.cursor()
            cursor.execute("SELECT DATABASE();")
            record=cursor.fetchone()
            print(f"You are connected to database : {record}")
            
        #to check the existence of the table 
        cursor.execute("""SELECT COUNT(*) FROM information_schema.tables WHERE table_name='Student_details' AND table_schema=DATABASE();""")    
        
        #if the table does not exist
        if cursor.fetchone()[0]==0:
            cursor.execute("""CREATE TABLE Student_details(
                                Student_Name VARCHAR(20),
                                Student_Regno VARCHAR(10),
                                Student_dob VARCHAR(10),
                                Lang1_mark int,
                                Lang2_mark int,
                                Maths_mark int,
                                Science_mark int,
                                SocialScience_mark int,
                                Total float,
                                Percentage float,
                                result varchar(10));""")
            print(f"Student details table is created")
        else:
            print(f"The table already exists")
    
    except Exception as e:
        print(f"An error occured : {e}")

def details_validation():
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
        
    #language 1 mark
    while True: 
        try:
            lang1_mark=int(input("Enter the language 1 mark:"))
            if lang1_mark<0 or lang1_mark>100:
                raise ValueError("Marks should be within 0-100")
            else:
                break
        except ValueError as ve:
            print(ve)
    #language2 mark            
    while True: 
        try:
            lang2_mark=int(input("Enter the language 2 mark:"))
            if lang2_mark<0 or lang2_mark>100:
                raise ValueError("Marks should be within 0-100")
            else:
                break
        except ValueError as ve:
            print(ve) 
    #maths mark       
    while True: 
        try:
            maths_mark=int(input("Enter the maths mark:"))
            if maths_mark<0 or maths_mark>100:
                        raise ValueError("Marks should be within 0-100")
            else:
                break
        except ValueError as ve:
                    print(ve)
    #science mark
    while True: 
        try:
            sci_mark=int(input("Enter the science mark:"))
            if sci_mark<0 or sci_mark>100:
                raise ValueError("Marks should be within 0-100")
            else:
                break
        except ValueError as ve:
                    print(ve) 
    #social science mark
    while True: 
        try:
            socsci_mark=int(input("Enter the social science mark:"))
            if socsci_mark<0 or socsci_mark>100:
                raise ValueError("Marks should be within 0-100")
            else:
                break
        except ValueError as ve:
            print(ve)
            
    stud_total=lang1_mark+lang2_mark+maths_mark+sci_mark+socsci_mark
    stud_percent=(stud_total/500)*100
    
    if lang1_mark<35 or lang2_mark<35 or maths_mark<35 or sci_mark<35 or socsci_mark<35:
        result="Fail"
    else:
        result="Pass"

    insert_record(s_name,s_regno,stud_dob,lang1_mark,lang2_mark,maths_mark,sci_mark,socsci_mark,stud_total,stud_percent,result)

#inserting the record       
def insert_record(name,regno,dob,l1_mark,l2_mark,m_mark,s_mark,ss_mark,tot,percent,res) :  
    try:
        cursor=mydb.cursor()
        insert_query = """
                INSERT INTO Student_details (
                    Student_Name, Student_Regno, Student_dob, Lang1_mark, Lang2_mark, 
                    Maths_mark, Science_mark, SocialScience_mark, Total, Percentage, Result
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
            """
        cursor.execute(insert_query, (name, regno, dob, l1_mark, l2_mark, m_mark, s_mark, ss_mark, tot, percent, res))
        mydb.commit()
        print(f"Record inserted successfully")
            
    except Exception as e:
        print(f"An error occured : {e}")
       
def display_record():
    try:
        cursor=mydb.cursor()
        query="""SELECT * FROM Student_details;"""
        cursor.execute(query)
        records=cursor.fetchall()
        print("Total number of records:",cursor.rowcount)
        for row in records:
            print(f"\nStudent Name:      {row[0]}")
            print(f"Student Register no: {row[1]}")
            print(f"Date of birth:       {row[2]}")
            print("\nMarks Obtained")
            print(f"Language 1      :  {row[3]}")
            print(f"Language 2      :  {row[4]}")
            print(f"Maths           :  {row[5]}")
            print(f"Science         :  {row[6]}")
            print(f"Social Science  :  {row[7]}")
            print(f"Total           :  {row[8]}")  
            print(f"Percentage      :  {row[9]}") 
            print(f"Final Result    :  {row[10]}") 
 
        cursor.close()
        print(f"The records are displayed")
    
    except Exception as e:
        print(f"An error occured : {e}")
       
def search_record():
    try:
        cursor=mydb.cursor()
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
            
        query="""Select * from Student_details where Student_Regno=%s and Student_dob=%s; """
        cursor.execute(query,(s_regno,stud_dob))
        record=cursor.fetchone()
        if not record:
            print("Student details are not found")
            
        else:
            print(f"\n Student details")
            print(f"Student Name:        {record[0]}")
            print(f"Student Register no: {record[1]}")
            print(f"Date of birth:       {record[2]}")
            print("\nMarks Obtained")
            print(f"Language 1      :  {record[3]}")
            print(f"Language 2      :  {record[4]}")
            print(f"Maths           :  {record[5]}")
            print(f"Science         :  {record[6]}")
            print(f"Social Science  :  {record[7]}")
            print(f"Total           :  {record[8]}")  
            print(f"Percentage      :  {record[9]}") 
            print(f"Final Result    :  {record[10]}") 
            
        cursor.close()
        
    except Exception as e:
        print(f"An error occured {e}")

while True:
    action=input("Do u want to check the connection or insert a record or display the records or search a record ?(check/insert/display/search/exit)")
    if action.lower()=="check":
        check_mysql_connection()
    elif action.lower()=="insert":
        details_validation()
    elif action.lower()=="display":
        display_record()
    elif action.lower()=="search":
        search_record()
    elif action.lower()=="exit":
        break
    else:
        print("Invalid input")
