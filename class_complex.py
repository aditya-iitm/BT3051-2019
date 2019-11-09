class Complex():

	def __init__(self,real,imag = 0.0):
		self._r = real
		self._i = imag

	def __str__(self):
		if self._i > 0:
			return	str(self._r) + '+' + str(self._i) + 'i'
		else:
			return str(float(self._r)) + ' + ' + str(float(self._i)) + 'i'

	def __add__ (self,other):
		return Complex(self._r + other._r, self._i + other._i)

	def __sub__ (self,other):
		return Complex(self._r - other._r, self._i - other._i)

	def __mul__ (self,other):
		return Complex(self._r * other._r - self._i * other._i, self._i * other._r + self._r * other._i)

	def __div__(self,other):
		val = float(other._r ** 2 + other._i ** 2)
		return Complex((self._r * other._r + self._i * other._i)/val , (self._i * other._r - self._r * other._i)/val)

if __name__ == '__main__':
	comp = Complex(0,1)
	comp2 = Complex(0,1)

	comp3 = comp2 * comp
	print(comp3)
