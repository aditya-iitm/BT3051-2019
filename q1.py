a = 123
rev = 0

while (a > 0) :
	b = a%10
	rev = rev*10 + b
	a = a//10
print(rev)