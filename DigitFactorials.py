from operator import mul
def factorial(x):
	return reduce(mul, xrange(x,1,-1), 1)

def sum_of_factorials(x):
	string = str(x)
	result = 0
	for c in string:
		result += factorial(int(c))
	return result

for x in xrange(10,2540161):
	if x == sum_of_factorials(x):
		print x