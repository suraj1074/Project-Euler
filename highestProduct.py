def down(i,j):
	if(i > 16):
		return 0
	else:
		return gridNumber[i][j] * gridNumber[i+1][j] * gridNumber[i+2][j] * gridNumber[i+3][j]

def right(i,j):
	if(j > 16):
		return 0
	else:
		return gridNumber[i][j] * gridNumber[i][j+1] * gridNumber[i][j+2] * gridNumber[i][j+3]

def diagonalDown(i,j):
	if i > 16 or j > 16:
		return 0
	else:
		return gridNumber[i][j] * gridNumber[i+1][j+1] * gridNumber[i+2][j+2] * gridNumber[i+3][j+3]

def diagonalUp(i,j):
	if i < 3 or j > 16:
		return 0
	else:
		return gridNumber[i][j] * gridNumber[i-1][j+1] * gridNumber[i-2][j+2] * gridNumber[i-3][j+3]


gridNumber = []
lines = open("gridNumber.txt","r").readlines()

for line in lines:
	nums = [int(x) for x in line.split()]
	gridNumber.append(nums)

result = 0
for i in xrange(0,20):
	for j in xrange(0,20):
		result = max(result,down(i,j),right(i,j),diagonalDown(i,j),diagonalUp(i,j))	

print result

