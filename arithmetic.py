print("ARITHMATICAL OPERATIONS \N")
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
print("MENU OF OPERATIONS\n 1. ADDITION\n 2.SUBSTRACTION\n 3.MULTIPLICATION\n 4.DIVISION\n 5.EXPONENTION\n 6.FLOOR DIVISION\n 7.MODULOS\n")
n=int(input("\n enter the desired operation you want to perform:"));
if n==1:
print("ADDITION\n sum=",a+b)
elif n==2:
print("SUBSTRACTION\n diff=",a-b)
elif n==3:
print("MULTIPLICATION\n pro=",a*b)
elif n==4:
print("DIVISION\n quo=",a/b)
elif n==5:
print("EXPONENTIATION\n expo=",a**b)
elif n==6:
print("FLOOR DIVISION\n fldiv=",a//b)
elif n==7:
print("MODULOS\n rem=",a%b)
else:
print("error,no such operation") 
