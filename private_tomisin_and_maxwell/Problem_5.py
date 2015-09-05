

# finds the smallest integer that is divisible
# by all numbers in range: (1 - 'rng')
def f_sm_super(rng):

	ind, num = 0, rng

	l = range(1, rng+1)
	l.reverse()	# reverse list

	# reduce range of numbers to check
	while True:
		print 'before filter: %s\t\t' %l,	#DEBUG
		l = filter_list(l, get_fact(num))
		print 'after filter: %s' %l	#DEBUG
		ind = l.index(num)+1

		if ind < len(l):
			num = l[ind]
		else:
			import time
			print 'Checking with numbers %s' % l	#DEBUG
			rng = l
			#time.sleep(4)
			break

	x=rng[0]
	diff = x

	while True:
		if is_super(x, rng):
			print 'checking %d in range %s' % (x, rng)	#DEBUG
			return x
		x += diff


# returns True is 'x' is divisible by all the natural
# numbers in the range: (1 - 'rng')
def is_super(x, rng):
	for i in rng:
		if not is_div(x, i):
			return False
	return True


# returns True is 'y' is a factor of 'x'
def is_fact(x,y):
	return is_div(x,y)


# returns True is 'x' is divisible by 'y'
def is_div(x,y):
	return x%y == 0





# Get a 'list' of all the factors of n
# l: if 'l' is given, get the factors of n from the list 'l'
def get_fact(n, l=None):
	factors = []		# create a new empty  list

	if l is None:
		l = range(1, n/2+1)
	
	for i in l:
		if is_fact(n, i):
			factors.append(i)

	return factors


# return l1-l2
# filters list 'l1' and returns a new list of elements
# of list l1 that are not in list l2
def filter_list(l1, l2):
	l3 = []		# create a new empty  list
	for i in l1:
		if not i in l2:
			l3.append(i)

	return l3



if __name__ == '__main__':
	x = f_sm_super(19)
	print 'found # \b', x