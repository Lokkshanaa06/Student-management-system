##list1=[]
##n=int(input("\nEnter the no of students:"))
#for i in range(n):
    #name=input("\nEnter the student name:")
    #list1.append(name)
    #if len(list1)==5:
        #break
#print(list1)
#n=int(input("Enter the no of students:"))
#common_list=[]
#for i in range(n):
#    name=input("Enter the student name:")
#    common_list.append(name)
stud_list=[]
current=[]
while True:
    stud_name=input("\nEnter the student name or if it is over give finish:")
    if stud_name=="finish":
        break
    current.append(stud_name)
    if len(current)==5:
        stud_list.append(current)
        current=[]
if current:
    stud_list.append(current)
for i,stud_list in enumerate(stud_list):
    print(f"Class{i+1}:{stud_list}")
        
        
