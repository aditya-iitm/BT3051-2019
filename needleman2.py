import numpy as np


def score(a,b):
	if a == b : return 0
	else : return 1


source = "ATTATCAT"
target = "TTATCATT"

matrix = np.zeros((len(source)+1,len(target)+1))
gap = 1

for i in range(len(source)+1) :
	matrix[i][0] = i

for i in range(len(target)+1) :
	matrix[0][i] = i


for i in range(1,len(source)+1):
	for j in range(1,len(target)+1):
		match = matrix[i-1][j-1] + score(target[j-1],source[i-1])
		deletion = matrix[i-1][j] + gap
		insertion = matrix[i][j-1] + gap

		matrix[i][j] = min(match,deletion,insertion)

print(matrix)

