import mysql.connector
import re
import os
import json

#connection to mysql
try:
    with open ("mysql_details.json","r") as json_file:
        data=json.load(json_file)
        mydb=mysql.connector.connect(
            host=data["host"],
            username=data["username"],
            password=data["password"],
            database=data["database"]
    )
except mysql.connector.Error as e:
    print(f"An error occured {e}")


cursor=mydb.cursor()

#method to search the record in mysql
def search_record(cursor,table_name):
    try:
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
        
        select_query = f"SELECT * FROM {table_name} WHERE Reg_no = %s AND Date_of_birth = %s"
        cursor.execute(select_query, (s_regno, stud_dob))
        record = cursor.fetchone()
        
        if record:
            print("Record found:")
            print(f"\n Student details")
            print(f"\nStudent Name:        {record[0]}")
            print(f"\nStudent Register no: {record[1]}")
            print(f"\nDate of birth:       {record[2]}")
            print("\nMarks Obtained")
            print(f"\nLanguage 1      :  {record[3]}")
            print(f"\nLanguage 2      :  {record[4]}")
            print(f"\nMaths           :  {record[5]}")
            print(f"\nScience         :  {record[6]}")
            print(f"\nSocial Science  :  {record[7]}")
            print(f"\nTotal           :  {record[8]}")  
            print(f"\nPercentage      :  {record[9]}") 
            print(f"\nFinal Result    :  {record[10]}")
            
            detail=input("\nDo you want to print?(yes/no)")
            if detail.lower()=="yes":
                file_path="Students Information"
                if not os.path.exists(file_path):
                    os.mkdir(file_path)
                file=os.path.join(file_path,f"{record[1]}.txt")
                with open (file,"w") as f:
                    f.write(f"\nStudent details")
                    f.write(f"\nStudent Name:        {record[0]}")
                    f.write(f"\nStudent Register no: {record[1]}")
                    f.write(f"\nDate of birth:       {record[2]}")
                    f.write(f"\nMarks Obtained")
                    f.write(f"\nLanguage 1      :  {record[3]}")
                    f.write(f"\nLanguage 2      :  {record[4]}")
                    f.write(f"\nMaths           :  {record[5]}")
                    f.write(f"\nScience         :  {record[6]}")
                    f.write(f"\nSocial Science  :  {record[7]}")
                    f.write(f"\nTotal           :  {record[8]}")  
                    f.write(f"\nPercentage      :  {record[9]}") 
                    f.write(f"\nFinal Result    :  {record[10]}")
                os.system(f"notepad.exe {file}")            
                
        else:
            print("No matching record found.")
      
    except Exception as e:
        print(f"An error occurred: {e}")

#starting of the program
while True:
    action=input("Do you want to search(yes/no)?")
    if action.lower()=="yes":
            table_name=input("Enter the table name:")
            cursor.execute(f"SHOW TABLES LIKE '{table_name}';")
            record=cursor.fetchone()
            if record:
                search_record(cursor,table_name)
            else:
                print(f"The {table_name} table does not exist")
    elif action.lower()=="no":
            break
    else:
            print("Invalid input")

#closing the established connection
cursor.close()
mydb.commit()
mydb.close()
