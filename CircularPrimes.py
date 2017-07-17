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

def rotate(l, n):
    return l[-n:] + l[:-n]

def all_combinations(number):
	number_str = str(number)
	rotations = []
	for i in xrange(1,len(number_str)):
		rotations.append(rotate(number_str,i))
	return rotations

def check_all_combinations(number):
	for x in all_combinations(number):
		if is_divisible(int(x)):
			return False
	return True

def question():
	sievePrime(1000000)
	print "Primes done"
	for prime in primes:
		if check_all_combinations(prime):
			print prime

def check_truncatable_prime(number):
	for i in xrange(len(str(number))):
		x = int(str(number)[i:])
		if is_divisible(x):
			return False

	for i in xrange(len(str(number)),0,-1):
		x = int(str(number)[:i])
		if is_divisible(x):
			return False

	return True

def x_digit_nums(alist,n):
	nums = []
	alists
	


def another_question():
	count = 0
	i = 1
	start = [3,7]
	end = [3,7]
	middle = [1,3,7,9]
	while True:
		number = ""
		
# check_truncatable_prime(3797)
another_question()