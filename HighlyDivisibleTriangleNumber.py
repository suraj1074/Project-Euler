
primes = []
primes.append(2)

def sievePrime(upto):
		last = primes[-1]
		for i in xrange(last,upto+1):
			if not is_divisible(i):
				primes.append(i)


def is_divisible(number):
	for prime in primes:
		if number % prime == 0:
			return True
		if number < prime * prime:
			break
	return False

def primeFactorize(number):
	primeFactors = {}
	sievePrime(number)
	last_divisor = 2
	count = 0
	x = 0
	while True:
		if(number % primes[x] == 0):
			if last_divisor == primes[x]:
				count = count + 1
			else:
				primeFactors[last_divisor] = count
				count = 1
			last_divisor = primes[x]
			number = number / primes[x]
			# print last_divisor, count, factors, primes[x], number
		else:
			x = x+1

		if number == 1:
			primeFactors[last_divisor] = count
			break

		if x == len(primes):
			break

	return primeFactors

def num_of_divisors(number):
	primeFactorize(number)

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

def sum_of_divisors(number):
	result = 1
	primeFactors = primeFactorize(number)
	for key in primeFactors:
		# print key,primeFactors[key]
		value = (power(key,primeFactors[key]+1) - 1) / (key - 1)
		result = result * value
	return result

# print sum_of_divisors(28)

def sum_of_proper_divisors(number):
	return sum_of_divisors(number) - number

# The idea is that n and n+1 won't have anything in common except 1
# so take the factors of n/2 or (n+1)/2 accordingly and multiply factors
# very good solution

def question1():
	n = 1
	while True:
		print n
		if(n % 2 == 0):
			divisors_count = divisors(n / 2) * divisors(n+1)
		else:
			divisors_count = divisors(n) * divisors((n+1)/2)
		number = (n * (n+1)) / 2
		print number, divisors_count
		if divisors_count > 500:
			break
		n = n + 1

def AmicableNumbers(upto):
	amicableNums = set()
	for i in xrange(2,upto+1):
		x = sum_of_proper_divisors(i)
		y = sum_of_proper_divisors(x)
		if(y == i):
			print y,x
			if x != y:
				amicableNums.add(x)
				amicableNums.add(y)

	amicableNums = list(amicableNums)
	print amicableNums
	return amicableNums

def AbundantNumbers(upto):
	abundantNums = []
	for i in xrange(2,upto):
		print i
		if sum_of_proper_divisors(i) > i:
			abundantNums.append(i)
	return abundantNums

def binarySearch(alist,item):
	first = 0
	last = len(alist) - 1
	found = False

	while first <= last and not found:
		midpoint = (first + last) // 2
		if alist[midpoint] == item:
			found = True
		else:
			if item < alist[midpoint]:
				last = midpoint-1
			else:
				first = midpoint+1
	return found

def is_it_summable(alist,number):
	x = 0
	while True:
		if(alist[x] > number):
			break
		if(binarySearch(alist,number-alist[x])):
			print number,alist[x],number-alist[x]
			return True
		x = x + 1
	return False

def nums_not_as_sum_of_abundant_nums(alist,upto):
	nums = []
	for x in xrange(2,upto):
		if not is_it_summable(alist,x):
			nums.append(x)
	return nums

abundantNums = AbundantNumbers(28123)
print abundantNums
nums = nums_not_as_sum_of_abundant_nums(abundantNums,28123)
print nums
print sum(nums)