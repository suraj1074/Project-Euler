triangle = []
lines = open("triangle.txt","r").readlines()
for line in lines:
	triangle.append([int(x) for x in line.split()])

for i in xrange(98,-1,-1):
	for x in xrange(0,len(triangle[i])):
		print i,x
		triangle[i][x] += max(triangle[i+1][x],triangle[i+1][x+1])

print triangle[0][0]