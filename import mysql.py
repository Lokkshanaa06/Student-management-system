import mysql.connector


def get_details():
  stud_id=int(input("Enter the student id:"))
  stud_name=input("Enter the student name:")
  stud_phno=int(input("Enter the phone no:"))
  m1=int(input("Enter subject 1 mark:"))
  m2=int(input("Enter subject 2 mark:"))
  m3=int(input("Enter subject 3 mark:"))
  student_record_insert(stud_id,stud_name,stud_phno,m1,m2,m3)

def student_record_insert():
  #sql="INSERT INTO stud(studno,studname,contactNo,M1,M2,M3) VALUES (102,"baal",371213535,45,56,89)"
  #val=(s_id,s_name,s_phno,s_m1,s_m2,s_m3)
  #mycursor.execute(sql,val)
  
  #mycursor.execute(f'INSERT INTO stud(studno,studname,contactNo,M1,M2,M3) VALUES (102,"baal",371213535,45,56,89)')
  mydb.commit
  print("Row inserted successfully")
 # mycursor.execute("SELECT * FROM stud")

  #myresult = mycursor.fetchall()

  #for x in myresult:
    #print(x)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="December06!",
  database="localdb"

)
mycursor = mydb.cursor()
print(mydb)
#mycursor.execute("SELECT * FROM stud")

#myresult = mycursor.fetchall()

#for x in myresult:
    #print(x)
#get_details()
#student_record_insert()
#sql="INSERT INTO stud VALUES (102,,,371213535,45,56,89)"
#mycursor.execute(sql)
#(studno,studname,contactNo,M1,M2,M3)
insert_query = """INSERT INTO stud (studno,studname,contactNo,M1,M2,M3)
                              VALUES (%s, %s, %s, %s, %s.)"""
record = (102,"baal",371213535,45,56,89)


mycursor.execute(insert_query, record)
mydb.commit()
print("Row inserted successfully")