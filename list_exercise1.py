#o create a class of 5 students where the students'names are given as input and new class is created if maximum 5 
#is reaached and group the same names and unique names from the student record 
stud_list=[]
current=[]
same_name=[]
unique_name=set()
while True:
    stud_name=input("\nEnter the student name or if it is over give finish:")
    if stud_name=="finish":
        break
    if stud_name in same_name:
        continue
    else:
        if stud_name in unique_name:
            unique_name.remove(stud_name)
            same_name.append(stud_name)
        else:
            unique_name.add(stud_name)
    current.append(stud_name)
    if len(current)==5:
        stud_list.append(current)
        current=[]
if current:
    stud_list.append(current)
for i,stud_list in enumerate(stud_list):
    print(f"Class{i+1}:{stud_list}")
print("\nUnique names:", unique_name)
print("\nSame names:", same_name)