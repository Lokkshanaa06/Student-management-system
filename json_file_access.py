import json
import os

#to know the current directory that is working
print(f"Current working directory: {os.getcwd()}")

def read_data():
    try:
        file_name=input("Enter the file name:")
        with open (file_name,"r") as file:
            
            #loading the contents of the file into data
            data=json.load(file)
            
            #to read the json file and print the contents of the file
            print(data)
            
            #accessing each elements of the json file 
            print(f"Name : {data["name"]}")
            print(f"Age: {data["age"]}")
            print(f"Is student: {data["isstudent"]}")
            print(f"Courses: {data["courses"]}")
            print(f"City: {data["city"]}")
    
    except FileNotFoundError:
        print(f"An error occured ")



def main():
    while True:
        action=input("Do you want to read or write in the json file?(read/exit)")
        if action.lower()=="read":
            read_data()
        elif action.lower()=="exit":
            break   
main()