exp = '((5+3)/2)'
operator = []
operand = []
op = '+-*/%'

for i in exp:
	if i == '(':continue
	if i.isdigit() : operand.append(i)
	elif i in op : operator.append(i)
	if i == ')':
		val1 = operand.pop()
		val2 = operand.pop()
		if val1 < val2 : val1,val2	= val2,val1	
		val3 = str(eval(val1+operator.pop()+val2))
		print(val1,val2,val3)
		operand.append(val3)

print(operator,operand)