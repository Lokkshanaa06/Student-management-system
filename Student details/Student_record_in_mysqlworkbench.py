import mysql.connector
import re

#connection to mysql
def connect_to_mysql():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sairam2003!123"
    )

#creating the database 
def create_database(cursor):
    try:
        db_name = input("Enter the database name to be created: ")
        cursor.execute(f"SHOW DATABASES LIKE '{db_name}'")
        result = cursor.fetchone()
        if result:
            print(f"Database '{db_name}' already exists.")
        else:
            cursor.execute(f"CREATE DATABASE `{db_name}`")
            print(f"Database '{db_name}' created successfully.")
        return db_name
    except Exception as e:
        print(f"An error occurred: {e}")

#creating the tabele and passing the cursor as the parameter 
def create_table(cursor):
    try:
        while True:
            table_name = input("Enter the table name to be created (or type 'exit' to stop): ")
            if table_name.lower() == 'exit':
                break
            
            cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
            result = cursor.fetchone()
            if result:
                print(f"Table '{table_name}' already exists.")
                continue
            
            columns = []
            print("Enter column details (type 'done' to finish):")
            while True:
                column = input("Column name (or type 'done'): ")
                if column.lower() == 'done':
                    break
                col_type = input(f"Data type for column '{column}': ")
                columns.append(f"`{column}` {col_type}")
            
            columns_str = ", ".join(columns)
            create_table_query = f"CREATE TABLE `{table_name}` ({columns_str});"
            cursor.execute(create_table_query)
            print(f"Table '{table_name}' created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

#inserting record in the specified table in the database
def insert_student_record(cursor, table_name):
    try:
        # Student name
        while True:
            s_name = input("Enter the student name: ")
            if re.match(r'^[a-zA-Z\s]+$', s_name):
                break
            elif not s_name.isalnum():
                print("You have entered some special characters. Please provide name in alphabets")
            else:
                print("You have entered numbers. Please provide name in alphabet")
        
        # Student register number
        while True:
            s_regno = input("Enter the student register number: ")
            if s_regno.isdigit() and len(s_regno) == 6:
                break
            elif s_regno.isalpha():
                print("You have entered alphabets. Please enter only digits")
            elif s_regno.isalnum():
                print("You have entered a combination of letters and digits. Please enter only digits")
            else:
                print("You have entered special characters. Please enter only digits")
            if len(s_regno) != 6:
                print("Register number should contain 6 digits only.")
        
        # Student date of birth
        while True:
            stud_dob = input("Enter the date of birth (DD-MM-YYYY): ")
            if re.match(r'^\d{2}-\d{2}-\d{4}$', stud_dob):
                break
            else:
                print("Invalid format of date of birth")
     
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
        
        
        stud_total = lang1_mark + lang2_mark + maths_mark + sci_mark + socsci_mark
        stud_percent = (stud_total / 500) * 100
        
        if lang1_mark<35 or lang2_mark<35 or maths_mark<35 or sci_mark<35 or socsci_mark<35:
            result="Fail"
        else:
            result="Pass"
        
        insert_query = f"INSERT INTO {table_name}  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(insert_query, (s_name, s_regno, stud_dob, lang1_mark, lang2_mark, maths_mark, sci_mark, socsci_mark, stud_total, stud_percent, result))
        print(f"Record inserted successfully into table '{table_name}'")
        
    except Exception as e:
        print(f"An error occurred: {e}")

def alter_table(cursor,table_name):
    action=input("Do you want to add a column or delete a column?(add/delete):")
    if action.lower() == "add":
        new_col_name = input("Enter the column name to be added:")
        #data_type = input(f"Enter the data type of the {new_col_name}: ")
        
        # Adding backticks around table and column names to handle special characters
        add_column_query = f"ALTER TABLE {table_name} ADD COLUMN {new_col_name} VARCHAR(10) ;"
        #add_column_query=f"alter table Student_record add column gender VARCHAR(10);"
        try:
            cursor.execute(add_column_query)
            #print("added")
            print(f"The column '{new_col_name}' has been added to the table '{table_name}'.")
        except mysql.connector.Error as e:
            print(f"Error: {e}")
    elif action.lower()=="delete":
        cursor.execute(f"SHOW COLUMNS FROM {table_name};")
        records=cursor.fetchall()
        for col in records:
            print(col)
        col_name=input("Enter the column name to be deleted:")
        cursor.execute(f"ALTER TABLE {table_name} DROP COLUMN {col_name};")
        print(f"The {col_name} column is deleted successfully from {table_name}")
    else:
        print("Invalid action to perform in the table")
               
#updating the existing record in the specified table in the database
def update_student_record(cursor,table_name):
    try:
        while True:
            s_regno = input("Enter the student register number that has to be modified: ")
            if s_regno.isdigit() and len(s_regno) == 6:
                break
            elif s_regno.isalpha():
                print("You have entered alphabets. Please enter only digits")
            elif s_regno.isalnum():
                print("You have entered a combination of letters and digits. Please enter only digits")
            else:
                print("You have entered special characters. Please enter only digits")
            if len(s_regno) != 6:
                print("Register number should contain 6 digits only.")
        cursor.execute(f"SELECT * FROM {table_name} WHERE Reg_no=%s ",(s_regno,))
        result=cursor.fetchone()
        if result:
            print(f"Record exists with the register number {s_regno}")
            cursor.execute(f"SHOW COLUMNS FROM {table_name};")
            records=cursor.fetchall()
            for col in records:
                print(col)
            col_name=input("Enter the column name that has to be modified:")
            new_value=input("Enter the new value of that column:")
            cursor.execute(f"UPDATE {table_name} SET {col_name} =%s WHERE Reg_no=%s",(new_value,s_regno))
            print("Updated the record successfully")
            
            if col_name in ["Lang1_mark","Lang2_mark","Maths_mark","Science_mark","Social_mark"]:
                cursor.execute(f"SELECT Lang1_mark,Lang2_mark,Maths_mark,Science_mark,Social_mark FROM {table_name} WHERE Reg_no=%s",(s_regno,))
                marks=cursor.fetchone()
                lang1_mark , lang2_mark , maths_mark , sci_mark , socsci_mark=marks
                s_total = lang1_mark + lang2_mark + maths_mark + sci_mark + socsci_mark
                s_percent = (s_total / 500) * 100
                if lang1_mark<35 or lang2_mark<35 or maths_mark<35 or sci_mark<35 or socsci_mark<35:
                    res="Fail"
                else:
                    res="Pass"
                    
                cursor.execute(f"UPDATE {table_name} SET Total=%s,Percentage=%s,Result=%s WHERE Reg_no=%s",(s_total,s_percent,res,s_regno))
                print("Records are updated successfully")
                
            
        else:
            print(f"Record with register number {s_regno} does not exist.")
    
    except Exception as e:
        print(f"An error occured {e}")
    
#searching for the specific record in the table
def search_student_record(cursor, table_name):
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
        else:
            print("No matching record found.")
    except Exception as e:
        print(f"An error occurred: {e}")

#deleting the existing record in the table 
def delete_student_record(cursor,table_name):
    try:
        while True:
            s_regno = input("Enter the student register number that has to be deleted: ")
            if s_regno.isdigit() and len(s_regno) == 6:
                break
            elif s_regno.isalpha():
                print("You have entered alphabets. Please enter only digits")
            elif s_regno.isalnum():
                print("You have entered a combination of letters and digits. Please enter only digits")
            else:
                print("You have entered special characters. Please enter only digits")
            if len(s_regno) != 6:
                print("Register number should contain 6 digits only.")
        cursor.execute(f"DELETE FROM {table_name} WHERE Reg_no=%s",(s_regno,))
        print(f"The record with register number {s_regno} is deleted successfully")
        
    except Exception as e:
        print(f"An error occured {e}")
 
 
def display_student_record(cursor,table_name):
    try:
        query=f"SELECT * FROM {table_name} ORDER BY Reg_no;"
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
            
    except Exception as e:
        print(f"An error occured {e}")       
#main function
def main():
    mydb = connect_to_mysql()
    cursor = mydb.cursor()

    db_name = create_database(cursor)
    mydb.database = db_name
    
    create_table(cursor)

    while True:
        add_record = input("Do you want to add a record to a table? (yes/no): ")
        if add_record.lower() == 'no':
            break
        elif add_record.lower() == 'yes':
            table_name = input("Enter the table name to add records: ")
            cursor.execute(f"SHOW TABLES LIKE '{table_name}';")
            result=cursor.fetchone()
            if result:
                insert_student_record(cursor, table_name)
            else:
                print(f"The {table_name} table does not exist.Create the table to insert the details.")
                #create_table(cursor)
        else:        
            print(f"Invalid input")
    
    
    while True:
        alter_table_input=input("Do you want alter the table?(yes/no):")
        if alter_table_input.lower()=="no":
            break
        elif alter_table_input.lower()=="yes":
            table_name=input("Enter the table name to be altered:")
            cursor.execute(f"SHOW TABLES LIKE '{table_name}';")
            result=cursor.fetchone()
            if result:
                alter_table(cursor,table_name)
            else:
                print(f"The {table_name} table does not exist.")        
        else:        
            print(f"Invalid input")
          
    while True:
        update_record=input("Do you want to update the record?(yes/no):")
        if update_record.lower()=="no":
            break
        elif update_record.lower()=="yes":
            table_name = input("Enter the table name to update records: ")
            cursor.execute(f"SHOW TABLES LIKE '{table_name}';")
            result=cursor.fetchone()
            if result:
                update_student_record(cursor, table_name)
            else:
                print(f"The {table_name} table does not exist.")
                #create_table(cursor)
        else:        
            print(f"Invalid input")
    
    while True:
        display_record=input("Do you want to display the record?(yes/no):")
        if display_record.lower()=="no":
            break
        elif display_record.lower()=="yes":
            table_name = input("Enter the table name to update records: ")
            cursor.execute(f"SHOW TABLES LIKE '{table_name}';")
            result=cursor.fetchone()
            if result:
                display_student_record(cursor,table_name)
            else:
                print(f"The {table_name} table does not exist.")
                #create_table(cursor)
        else:        
            print(f"Invalid input")
            
            
        
    while True:
        search_record = input("Do you want to search for a record? (yes/no): ")
        if search_record.lower() == 'no':
            break
        elif search_record.lower() == 'yes':
            table_name = input("Enter the table name to search records: ")
            cursor.execute(f"SHOW TABLES LIKE '{table_name}';")
            result=cursor.fetchone()
            if result:
                search_student_record(cursor, table_name)
            else:
                print(f"The {table_name} table does not exist.")
                #create_table(cursor)
        else:
            print(f"Invalid input")
            
    while True:
        delete_record=input("Do you want a delete the student_record?(yes/no):")
        if delete_record.lower()=="no":
            break
        elif delete_record.lower()=="yes":
            table_name=input("Enter the table name:")
            cursor.execute(f"SHOW TABLES LIKE '{table_name}';")
            result=cursor.fetchone()
            if result:
                delete_student_record(cursor, table_name)
            else:
                print(f"The {table_name} table does not exist.")
                #create_table(cursor)
        else:
            print(f"Invalid input")
    
    cursor.close()
    mydb.commit()
    mydb.close()

main()
