#calculator
n1=int(input("\nEnter the first number:"))
n2=int(input("\nEnter the second number:"))
op=int(input("\nEnter the operation to be done: \n1.Add \n2.Subtract \n3.Multiply \n4.Division \n"))
if(op==1):
    print("Addition operation is done")
    result=n1+n2
elif(op==2):
    print("Subtraction operation is done")
    result=n1-n2
elif(op==3):
    print("Multiplication operation is done")
    result=n1*n2
elif(op==4):
    print("Division operation is done")
    result=n1/n2
else:
    print("Invalid input given ")
print("Result is",result)