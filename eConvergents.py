from fractions import Fraction

expansionList = [Fraction(2)]

e = 0

for i in xrange(1,34):
	expansionList.append(Fraction(1))
	expansionList.append(Fraction(2*i))
	expansionList.append(Fraction(1))

# print expansionList
result = expansionList[-1]
for i in xrange(len(expansionList)-2,-1,-1):
	result = expansionList[i] + (Fraction(1) / result)
	# print i, result

print result.numerator
r = 0
for c in str(result.numerator):
	r = r + int(c)

print r