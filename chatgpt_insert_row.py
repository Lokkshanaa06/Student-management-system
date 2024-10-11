import mysql.connector

# Establish the database connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="December06!",
    database="localdb"
)

def insert_student_record(stud_id, stud_name, stud_phno, stud_mark1, stud_mark2, stud_mark3):
    mycursor = mydb.cursor()
    sql = """INSERT INTO stud (studno, studname, contactNo, M1, M2, M3) VALUES (%s, %s, %s, %s, %s, %s)"""
    values = (stud_id, stud_name, stud_phno, stud_mark1, stud_mark2, stud_mark3)
    mycursor.execute(sql, values)
    mydb.commit()
    print("Row inserted successfully")
    mycursor.close()

# Collect student details and insert the record
stud_name = input("Enter the student name: ")
stud_id = int(input("Enter the student id: "))
stud_phno = input("Enter the phone number: ")  # Keep it as a string to avoid leading zero issues
stud_mark1 = int(input("Enter the student mark 1: "))
stud_mark2 = int(input("Enter the student mark 2: "))
stud_mark3 = int(input("Enter the student mark 3: "))
insert_student_record(stud_id, stud_name, stud_phno, stud_mark1, stud_mark2, stud_mark3)
