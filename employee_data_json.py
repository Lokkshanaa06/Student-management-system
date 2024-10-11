import json

#reading the details in the json file
def get_details():
    try:
        filename="employee.json"
        with open(filename,"r") as f:
            data=json.load(f)
            print(data)
            
            emp=data["employee"]
            for i in range(len(emp)):
                name=emp[i]["name"]
                print(f"Name of the employee: {name}")
                age=emp[i]["age"]
                print(f"Age of the employee: {age}")
                city=emp[i]["city"]
                print(f"City where employee located: {city}")
    except Exception as e:
        print(f"An error occured {e}")
#appending new values in the json file       
def append_details():
    try:
        filename="employee.json"
        new_employee={"name":"Naina","age":24,"city":"Salem"}
        with open(filename,"r") as f:
            data=json.load(f)
            
        data["employee"].append(new_employee)
        
        with open(filename,"w") as f:
            json.dump(data,f,indent=4)
            
        print("The new employee is added")
        get_details()
    except Exception as e:
        print(f"An error occured {e}")
            
#starting of the program      
def main():
    while True:
        action=input("Do you want to get the details or append the details?(read/append/exit)")
        if action.lower()=="read":
            get_details()
        elif action.lower()=="append":
            append_details()
        elif action.lower()=="exit":
            break
        else:
            print(f"Invalid input")
    
main()