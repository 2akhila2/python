
n=int(input("enter the number of names:"))
names=[]
for i in range(n):
	name=input("enter name:")
	names.append(name)
	names.sort()
print("name in Alphabetical order:")
for name in names:
	print(name)
