from fractions import gcd
from fractions import Fraction
import sympy
import primefac
from operator import itemgetter

def resilientIndex(denom,all_subsets):
	count = 0
	for x in xrange(1,len(all_subsets)-1):
		if len(all_subsets[x]) % 2 == 1:
			count = count + ((denom-1) / product(all_subsets[x]))
		else:
			count = count - ((denom-1) / product(all_subsets[x]))
	# print count
	return Fraction(denom-count+1,denom-1)

def subsets(my_set):
    result = [[]]
    for x in my_set:
        result = result + [y + [x] for y in result]
    return result

def primesDivising(denom):
	primes = []
	startPrime = 2
	while  startPrime < denom:
		if denom % startPrime == 0:
			primes.append(startPrime)
		startPrime = primefac.nextprime(startPrime)
	return primes

def product(alist):
	prod = 1
	for x in alist:
		prod = prod * x
	return prod

def generate_prime(x):
	primes = [2]
	for x in xrange(x):
		primes.append(primefac.nextprime(primes[-1]))
	return primes

for x in xrange(2,10):
	primes = generate_prime(x)
	all_subsets = sorted(subsets(set(primes)),key=len)
	denom = product(primes)
	percentage = resilientIndex(denom,all_subsets)
	print primes
	print denom, percentage, float(percentage), float(Fraction(15499,94744))
	if percentage < Fraction(15499,94744):
		print primes
		print denom, percentage, float(percentage), float(Fraction(15499,94744))