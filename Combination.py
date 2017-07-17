def combinations(i,j):
	num1 = 1
	for x in xrange(i-j+1,i+1):
		num1 *= x;
	num2 = 1
	for x in xrange(1,j+1):
		num2 *= x
	return num1 / num2

# print combinations(40,20)

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

def sum_of_digits(n):
	Sum = 0
	number = str(n)
	for c in number:
		Sum += int(c)
	return Sum

# print sum_of_digits(power(2,1000))

print sum_of_digits(93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864)