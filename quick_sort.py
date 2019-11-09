def split(a,low,high):
	i = low -1
	pivot = a[high]
	print(i,pivot,a[-1])
	for j in range(low,high):
		if a[j] <= pivot:
			i += 1
			a[i],a[j] = a[j],a[i]

	a[i+1],a[high] = a[high],a[i+1]

	return i+1

def quick(a,low,high):
	if low < high:
		index = split(a,low,high)
		quick(a,low, index - 1)
		quick(a,index +1,high)

a = [10,7,8,9,1,5]
n = len(a)
quick(a,0,n-1)
print(a)