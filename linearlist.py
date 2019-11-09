def Insert(arr,num):
	print(arr)
	for i in range(len(arr)):
		if num > arr[i] and num < arr[i+1] : 
			return arr[:i+1] + [num] + arr[i+1:]

def find(arr1,num):
	flag = -1
	for i in range(len(arr1)):
		#print(arr1[i])
		if arr1[i] == num : 
			flag = i
			break
	if flag > 1: return flag
	else : return "no"

print(Insert([1,2,3,5],4))
print(find([1,2,3],4))