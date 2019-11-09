#Name : K Aditya
#Roll number : BS16B019
#Popquiz 2
def bubble(a):
	n = len(a)
	if n%2 != 0 : arr1 = a[:len(a)//2+1]
	else : arr1 = a[:len(a)//2]
	arr2 = []
	for i in a:
		if i not in arr1: arr2.append(i)
	swaps = 0
	swapped = True
	for i in range(len(arr1)-1):
		for j in range(len(arr1)-1-i):
			if arr1[j] > arr1[j+1]:
				arr1[j],arr1[j+1] = arr1[j+1],arr1[j]
				swaps += 1
				swapped = True	
		if not swapped : break
	swaps = 0
	swapped = True
	for i in range(len(arr2)-1):
		for j in range(len(arr2)-1-i):
			if arr2[j] < arr2[j+1]:
				arr2[j],arr2[j+1] = arr2[j+1],arr2[j]
				swaps += 1
				swapped = True	
		if not swapped : break
	return arr1,arr2

print(bubble([9,3,5,1,2]))

#Stable as it does not compare and sort two equal elements
#Time complexity is O(n^2)
