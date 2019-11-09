#BT3051 Assignment 0b
#Roll number : BS16B019
#Collaborators : -
#Time : 0:2

number = input("Enter a number : ")
#Convert string to input
for i in range(1,int(number)+1):
	for j in range(1,i+1):
		print(j**i,end=' ')
	print()
