lines = open("largeSum.txt","r").readlines()
sum = 0
for line in lines:
	sum += long(line)

print sum