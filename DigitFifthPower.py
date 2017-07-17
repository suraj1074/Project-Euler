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

def check(number):
	number_str = str(number)
	value = 0
	for c in number_str:
		value = value + power(int(c),5)
	if(value == number):
		return True
	else:
		return False

# A number of x digits will be atleast 10^x and a number of x digits could have digits sum atmost 
# 9^5 * x that gives 10^x >= 9^5*x. Take log and solve atmost 6 digits numbers only

for i in xrange(2,1000000):
	if check(i):
		print "This is the one : ", i
