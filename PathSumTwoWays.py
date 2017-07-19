lines = open("p081_matrix.txt","r").readlines()

matrix = []

for line in lines:
	matrix_row = [int(x) for x in line.split(",")]
	matrix.append(matrix_row)

rows = 80

pathSumMatrix = [[0 for x in xrange(rows)] for i in xrange(rows)]

pathSumMatrix[0][0] = matrix[0][0]

for i in xrange(1,rows):
	pathSumMatrix[0][i] = pathSumMatrix[0][i-1] + matrix[0][i]

for i in xrange(1,rows):
	pathSumMatrix[i][0] = pathSumMatrix[i-1][0] + matrix[i][0]

for i in xrange(1,rows):
	for j in xrange(1,rows):
		pathSumMatrix[i][j] = matrix[i][j] + min(pathSumMatrix[i-1][j], pathSumMatrix[i][j-1])

# print matrix
print pathSumMatrix[-1][-1]