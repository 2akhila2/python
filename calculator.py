def add(num1,num2):
	return num1+num2
def subtract(num1,num2):
	return num1-num2
def multiply(num1,num2):
	return num1*num2
def divide(num1,num2):
	return num1/num2
def power(num1,num2):
	return num1**num2
def calculator(num1,operator,num2):
	if operator=="+":
		return add(num1,num2)
	elif operator=="-":
		return subtract(num1,num2)
	elif operator=="*":
		return multiply(num1,num2)
	elif operator=="/":
		return divide(num1,num2)
	elif operator=="^":
		return power(num1,num2)
	else:
		return"invalid operator"
num1=float(input("enter the first number:"))
operator=input("enter a operator(+,-,*,/,^):")
num2=float(input("enter the second number:"))
result=calculator(num1,operator,num2)
print("result:",result)
