import numpy as np


def score(a,b):
	if a == b : return 1
	else : return -1


seq1 = "ATTACA"
seq2 = "ATGCT"

matrix = np.zeros((len(seq2)+1,len(seq1)+1))
gap = -1

for i in range(len(seq2)+1) :
	matrix[i][0] = gap * i

for i in range(len(seq1)+1) :
	matrix[0][i] = gap * i


for i in range(1,len(seq2)+1):
	for j in range(1,len(seq1)+1):
		match = matrix[i-1][j-1] + score(seq1[j-1],seq2[i-1])
		deletion = matrix[i-1][j] + gap
		insertion = matrix[i][j-1] + gap

		matrix[i][j] = max(match,deletion,insertion)

print(matrix)