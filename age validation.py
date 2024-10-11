global n1
def age():
  n1=int(input("Enter the age:\n"))  
  return n1


list1=[18]
#n=int(input("Enter the age:\n"))
n=age()
while n not in list1:
    stud_age=age()
    n=stud_age
print("age is",n)