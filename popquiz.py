#PopQuiz1
#Name : K Aditya
#Roll number : BS16B019

class BinaryNumber():

	def __init__(self,arr):
		self._array = arr

	def __str__(self):
		check = ''
		false = [2,3,4,5,6,7,8,9]
		for i in range(len(self._array)):
			if self._array[i] in false : raise ValueError('Check your number')
			else :
				check += str(self._array[i])
		return '['+check[::-1]+']_2'
		
	def value(self):
		total = 0
		j = 0 
		for i in range(len(self._array)):
			total += self._array[i] * 2**j
			j += 1
		return total


b1 = BinaryNumber([0,1,1,1])
b2 = BinaryNumber([0,0,0,1])
print(b1.value()+b2.value())
