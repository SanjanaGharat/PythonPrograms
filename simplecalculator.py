#code to make simple calculator
#actions that will be performed are:
#1. ADD
#2. SUBTRACT
#3. MULTIPLY
#4. DIVIDE

print("Enter the operation to perform:")
print("1.ADD")
print("2.SUBTRACT")
print("3.MULTIPLY")
print("4.DIVIDE")

operation=int(input())
if operation==1:
 #code for addtion
 num1=int(input("Enter 1st number: "))
 num2=int(input("Enter 2nd number: "))
 print("The addtion is: "+str(int(num1+num2)))
elif operation==2:
      #code for subtraction
      num1=int(input("Enter 1st number: "))
      num2=int(input("Enter 2nd number: "))
      print("The difference is: "+str(int(num1-num2)))
elif operation==3:
     #code for multiplication
     num1=int(input("Enter 1st number: "))
     num2=int(input("Enter 2nd number: "))
     print("The multiplication is: "+str(int(num1*num2)))
elif operation==4:
     #code for division
     num1=int(input("Enter 1st number: "))
     num2=int(input("Enter 2nd number: "))
     print("The result is: "+str(int(num1/num2)))
else:
     print("INVALID OPERATION")
print("THANK YOU...!")     