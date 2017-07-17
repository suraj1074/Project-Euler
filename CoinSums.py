count = 0
for i1 in xrange(2):
	if i1 * 200 > 200:
		continue 
	for i2 in xrange(3):
		if i1 * 200 + i2 * 100 > 200:
			continue
		for i3 in xrange(5):
			if i1 * 200 + i2 * 100 + i3 * 50 > 200:
				continue
			for i4 in xrange(11):
				if i1 * 200 + i2 * 100 + i3 * 50 + i4 * 20 > 200:
					continue
				for i5 in xrange(21):
					if i1 * 200 + i2 * 100 + i3 * 50 + i4 * 20 + i5 * 10 > 200:
						continue
					for i6 in xrange(41):
						if i1 * 200 + i2 * 100 + i3 * 50 + i4 * 20 + i5 * 10 + i6 * 5 > 200:
							continue
						for i7 in xrange(101):
							if i1 * 200 + i2 * 100 + i3 * 50 + i4 * 20 + i5 * 10 + i6 * 5 + i7 * 2 > 200:
								continue
							for i8 in xrange(201):
								if i1 * 200 + i2 * 100 + i3 * 50 + i4 * 20 + i5 * 10 + i6 * 5 + i7 * 2 + i8 * 1 > 200:
									continue
								elif i1 * 200 + i2 * 100 + i3 * 50 + i4 * 20 + i5 * 10 + i6 * 5 + i7 * 2 + i8 * 1 == 200:
									count = count + 1
									# print i1,i2,i3,i4,i5,i6,i7,i8
print count