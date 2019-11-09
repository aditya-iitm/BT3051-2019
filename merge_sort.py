def merge_sort(a):
	n = len(a)
	if n == 1 : return a
	else : return merge(merge_sort(a[:n//2]),merge_sort(a[n//2:]))

def merge(left,right):
	print(left,right)
	p,q = 0,0
	sort = []
	while p <len(left) and q <len(right):
		if left[p] < right[q]:
			sort.append(left[p])
			p += 1
		else :
			sort.append(right[q])
			q += 1
	while p == len(left):
		sort += right[q:]
		print(sort)
		return sort
	while q == len(right):
		sort += left[p:]
		print(sort)
		return sort


data = [10,1,4,2,7]
print("Final",merge_sort(data))
		 