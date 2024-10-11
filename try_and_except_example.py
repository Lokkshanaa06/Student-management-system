'''
try:
    a=10/0
except ZeroDivisionError:
    print("Denominator cannot be zero")
try:
    b=int("abc")
except ValueError:
    print("The string cannot be turned into an integer")
    
try:
    even=[2,4,6,8]
    print(even[2])  
    print(even[6])
except IndexError:
    print("Out of index")
finally:
    print("This is always executed even if the try block is executed or except block is executed")
    
#array=[1,2,3,4,5,6]
array=[]
try:
    assert len(array)>0 , "data array should not be empty"
    print(len(array))
except Exception as e:
    print(e)
    print("Data should be present in the array")
 '''   
def performoperation(a,b):
    try:
        res=a/b
        print("Result:",res)
        arr=[1,2,4,5]
        print(arr[5])
    except ZeroDivisionError:
        print("Denominator cannot be zero")
    except IndexError:
        print("Out of index")
performoperation(10,2)
performoperation(10,0)
        