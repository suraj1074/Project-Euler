import itertools
import enchant
line = open("p059_cipher.txt","r").readlines()[0]
codes = line.split(",")
d = enchant.Dict("en_US")

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
keywords = itertools.product(alphabets, repeat = 3)
for keyword in keywords:
	key = keyword[0] + keyword[1] + keyword[2]
	for x in xrange(len(codes)/3):
		a = int(codes[x*3])
		b = int(codes[x*3+1])
		c = int(codes[x*3+2])

		a = a ^ ord(key[0])
		b = b ^ ord(key[1])
		c = c ^ ord(key[2])

		if not d.check(chr(a)+chr(b)+chr(c)):
			print key, chr(a)+chr(b)+chr(c) 
			break

		if x == len(codes)/3 - 1:
			print "Found key : ", key
			break