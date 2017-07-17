from fractions import gcd

def equal_fraction(a,b,x,y):
	p = gcd(a,b)
	q = gcd(x,y)
	if(a / p, b / p) == (x / q, y /q):
		return True

	return False
	

def wrong_simplify(a,b):
	a = str(a)
	b = str(b)
	if a[0] == b[0]:
		x,y = int(a[1]), int(b[1])
		if equal_fraction(int(a),int(b),x,y):
			print a,b

	if a[0] == b[1]:
		x,y = int(a[1]), int(b[0])
		if equal_fraction(int(a),int(b),x,y):
			print a,b

	if a[1] == b[0]:
		x,y = int(a[0]), int(b[1])
		if equal_fraction(int(a),int(b),x,y):
			print a,b

	if a[1] == b[1]:
		x,y = int(a[0]), int(b[0])
		if equal_fraction(int(a),int(b),x,y):
			print a,b

for i in xrange(10,100):
	for j in xrange(10,100):
		if i < j and gcd(i,j) != 1:
			wrong_simplify(i,j)