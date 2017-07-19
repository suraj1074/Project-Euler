from fractions import Fraction
start = Fraction(3, 2)

full_list = []
for x in xrange(1,1001):
	f1 = start + Fraction(2,1)
	f2 = start + Fraction(1,1)
	start = f1 / f2
	if len(str(start.numerator)) > len(str(start.denominator)):
		print x
		full_list.append(x)

print len(full_list)