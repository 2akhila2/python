student={ }
Is=[]
n=int(input("enter number of students:"))
for i in range(0,n):
	name=input("enter name:")
	age=input("enter age:")
	grade=input("enter grade:")
	student[name]=age,grade
print(student)
