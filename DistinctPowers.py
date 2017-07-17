def power(x,i):
	if i == 1:
		return x
	elif i == 0:
		return 1
	elif (i % 2 == 0):
		half = power(x,i/2)
		return half * half
	else:
		half = power(x,i/2)
		return half * half * x

numbers = set()
for i in xrange(2,101):
	for j in xrange(2,101):
		numbers.add(power(i,j))

print len(list(numbers))