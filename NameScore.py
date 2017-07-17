def score(name,rank):
	r = 0
	for c in name:
		if c != "\"":
			r += (ord(c) - ord('A') + 1)
	print name,r,rank
	return r * rank

l = open("p022_names.txt","r").readline()
# print l
result = 0
names = l.split(",")
names.sort()
for x in xrange(len(names)):
	result += score(names[x],x+1)
print result

print score("AHMED",1)
print score("COLIN",1)