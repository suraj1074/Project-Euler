import math
import sympy

def is_prime(number):
	# print "to check :" , number, 
	if number <= 1:
		# print "False"
		return False
	if number == 2:
		# print "True"
		return True
	i = 2
	while True:
		if number % i == 0:
			# print "False"
			return False
		i = i + 1
		if i * i > number:
			break
	# print "True"
	return True

def primesInDiagonal(spiral):
	i = 0
	j = 0
	count = 0
	while i < len(spiral) and j < len(spiral[0]):
		if is_prime(spiral[i][j]):
			count = count + 1
		i = i + 1
		j = j + 1

	i = 0
	j = len(spiral[0])-1
	while i < len(spiral) and j >= 0:
		if is_prime(spiral[i][j]):
			count = count + 1
		i = i + 1
		j = j - 1

	return count

def createSpiral(size):
	spiral = [[0 for x in xrange(size)] for j in xrange(size)]
	startX = size / 2
	startY = size / 2

	start = 1

	spiral[startX][startY] = start 
	startY += 1

	stepsize = 2
	while True:
		for x in xrange(stepsize-1):
			start = start + 1
			spiral[startX][startY] = start
			startX = startX - 1

		for x in xrange(stepsize):
			start = start + 1
			spiral[startX][startY] = start
			startY = startY - 1

		for x in xrange(stepsize):
			start = start + 1
			spiral[startX][startY] = start
			startX = startX + 1

		for x in xrange(stepsize+1):
			start = start + 1
			spiral[startX][startY] = start
			startY = startY + 1

		stepsize += 2

		if stepsize >= size:
			break

	return spiral

def primesOfSpiral(size):
	diagonals = []
	start = 1
	diagonals.append(start)
	step = 2
	for x in xrange(1,size/2+1):
		start = 4 * x * x - 2 * x + 1
		diagonals.append(start)
		diagonals.append(start + step)
		diagonals.append(start + 2 * step)
		diagonals.append(start + 3 * step)
		step = step + 2


	primeCount = 0
	for x in diagonals:
		if sympy.isprime(x):
			primeCount = primeCount + 1

	percentage = float((primeCount * 100 )) / (2 * size - 1)
	print size , primeCount, percentage

for x in xrange(26001,27505,2):
	primesOfSpiral(x)

def binaryApproach():
	start = 9005
	end = 15005
	while True:
		mid = ( start + end ) / 2
		if mid % 2 == 0:
			mid = mid + 1
		print "Trying for ", mid
		spiral = createSpiral(mid)
		print "spiral created"
		primeCount = primesInDiagonal(spiral)
		percentage = float((primeCount * 100 )) / (2 * len(spiral) - 1)
		print len(spiral) , primeCount, percentage
		if percentage > 10:
			start = mid + 2

def old_waste_approach():
	spiral = [[1]]
	size = 1
	while True:
		size = size + 2
		spiral = [[]] + spiral
		spiral.append([])
		i = len(spiral)-1
		j = len(spiral)-1

		startNum = size * size
		for k in xrange(size):
			spiral[i] = [startNum] + spiral[i] 
			startNum = startNum - 1

		for k in xrange(size-1):
			i = i - 1
			spiral[i] = [startNum] + spiral[i]
			startNum = startNum - 1
			

		for k in xrange(size-1):
			spiral[i].append(startNum)
			startNum = startNum - 1

		for k in xrange(size-2):
			i = i + 1
			spiral[i].append(startNum)
			startNum = startNum - 1

		primeCount = primesInDiagonal(spiral)
		print len(spiral) , (primeCount * 100 ) / (2 * size - 1)

		if (primeCount * 100 ) / (2 * size - 1) < 10:
			print len(spiral) , (primeCount * 100 ) / (2 * size - 1)
			break

		# if size >= 7:
		# 	print primesInDiagonal(spiral)
		# 	break

	print spiral
