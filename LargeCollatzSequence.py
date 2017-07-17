import threading

def chain_length(number):
	count = 0
	while number != 1:
		if number % 2 == 0:
			number = number / 2
		else:
			number = number * 3 + 1
		count = count + 1
		# print number, count
	return count

def update_chain_length(start ,end):
	for i in xrange(start,end):
		print "Processing number " ,i
		chain_length_numbers[i] = chain_length(i)

chain_length_numbers = [0 for x in xrange(1,1000000)]

# threads = []
# for i in xrange(1,5):
# 	t = threading.Thread(target=update_chain_length, args=((i-1)*100000 + 1,(i+1)*100000))
# 	threads.append(t)
# 	t.start()

# for t in threads:
#     t.join()

# print max(chain_length_numbers)

result = 0
count = 0
for i in xrange(1,1000000):
	length = chain_length(i)
	if length > count:
		count = length
		result = i
	print i,length

print result,count
# chain_length(4)