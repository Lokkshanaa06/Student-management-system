# Collect student details
def details():
    s_name = input("Enter the student name: ")
    s_regno = input("Enter the student register number: ")
    stud_dob = input("Enter the date of birth (DD-MM-YYYY): ")
    
    lang1_mark = int(input("Enter the language 1 mark: "))
    lang2_mark = int(input("Enter the language 2 mark: "))
    maths_mark = int(input("Enter the maths mark: "))
    sci_mark = int(input("Enter the science mark: "))
    socsci_mark = int(input("Enter the social science mark: "))
    
    gender = input("Enter the gender (Male/Female): ")
    
    # Calculate total and percentage
    stud_total = lang1_mark + lang2_mark + maths_mark + sci_mark + socsci_mark
    stud_percent = (stud_total / 500) * 100
    
    # Determine pass or fail
    if lang1_mark < 35 or lang2_mark < 35 or maths_mark < 35 or sci_mark < 35 or socsci_mark < 35:
        final_result = "Fail"
    else:
        final_result = "Pass"
    
    # Display student details
    print("\nSSLC EXAMINATION RESULTS")
    print("STUDENT DETAILS:")
    print(f"Student Name:    {s_name}")
    print(f"Register Number: {s_regno}")
    print(f"Date of birth:   {stud_dob}")
    print(f"Language 1:      {lang1_mark}")
    print(f"Language 2:      {lang2_mark}")
    print(f"Maths:           {maths_mark}")
    print(f"Science:         {sci_mark}")
    print(f"Social Science:  {socsci_mark}")
    print(f"Total:           {stud_total}")
    print(f"Percentage:      {stud_percent:.2f}%")
    print(f"Final result:    {final_result}\n")
    
# Starting of the program
def start():
    while True:
        y = input("Do you want to enter student details? (yes/no): ")
        if y.lower() == "yes":
            details()
        else:
            break

print("STUDENT DETAILS:")
start()
