def name():
    stud_name=input("Enter the name again:")
    return stud_name

s_name=input("Enter the student name:")
while not s_name.isalpha() or not s_name.isspace():
    if not s_name.isalnum() and not s_name.isspace():
            print("You have entered some special characters. please provide name in alphabets")
            s_name=name()
    else:
        if not s_name.isalpha() and s_name.isspace():
            print("You have entered numbers.please provide name in alphabets")
            s_name=name()
print(s_name)
    