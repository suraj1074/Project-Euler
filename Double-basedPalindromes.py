def is_palindrome(s):
	i = 0
	j = len(s)-1
	while i < j and s[i] == s[j]:
		i = i + 1
		j = j -1
	if i >= j:
		return True
	else:
		return False

nums = []
for x in xrange(1,1000000):
	if is_palindrome(str(x)) and is_palindrome(bin(x)[2:]):
		print x
		nums.append(x)

print sum(nums)
