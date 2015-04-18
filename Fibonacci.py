


# This is what the Fibonacci series looks like:
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...
#
# General formuar to generate nth Fibonacci number:
#		fib(n) = fib(n-1) + fib(n-2)		(where the first and second terms in the series are 1)




# This function prints the 'nth' Fibonacci series number
# 
# The 'nth' index is supplied as a parameter.
#
# Usage example:
#		fib(10)
#		This will print the 10th fibonacci number
#		fib(100)
#		This will print the 100th fibonacci number
def n_fib(nth):
	if(nth==1):						# Do this if 1st term is required
		print 'fib (', nth, ') =', c
		return						# end the function
	
	if(nth==2):						# Do this if 2nd term is required
		print 'fib (', nth, ') =', c
		return						# end the function
	
	if(nth>2):						# Do this for terms beyond the 2nd term
		a, b = 1, 1					# initialise variables 'a' and 'b';		first and second terms in the series
		count = 2					# initialise variable 'count';		for counting the number of terms that have been computed

		while True:					# Begin loop and keep track with variable 'count'
			c = a+b					# calculate 'c' as sum of its two preceding terms in the series; i.e 'a' and 'b'
			count +=1				# increment count
			
			if(count==nth)			# if nth fibonacci has been found
				print 'fib (', count, ') =', c
				return				# end the function
			a, b = b, c				# first term becomes the previous second term, and second term becomes the previous third term
									# i.e if first term 'a' was 1 and second term 'b' was 2, then third term 'c' would be computed as: 1 + 2 = 3
									# to get the next term (i.e the new 'c'), 'a' would become the previous 'b' (2) and 'b' becomes the previous 'c' (3)
									# the new 'c' would now be equal to new 'a' + new 'b': (2 + 3); which would be equal to 5
									# so the loop continues like that...
		
			
		


# This function prints the first 'n' Fibonacci series numbers
# 'n' is supplied as a parameter.
# In the code 'n' is named 'upToN'
#
# Usage example:
#		fib(10)
#		This will print the first 10 fibonacci numbers
#		fib(100)
#		This will print the first 100 fibonacci numbers
def fib(upToN):
	if(upToN>=1):					# Do this if upToN is 1 or higher
		print 'fib ( 1 ) = 1'
		
	if(upToN>=2):					# Do this if upToN is 2 or higher
		print 'fib ( 2 ) = 1'
	
	if(upToN>2):					# Do this if upToN is higher than 2
		a, b = 1, 1					# initialise variables 'a' and 'b'
		count = 2					# initialise variable 'count'

		while True:					# Begin loop and track with variable 'count'
			c = a+b					# calculate 'c' as sum of two preceding terms in the series; i.e 'a' and 'b'
			count +=1				# increment count
			if count>=upToN:		# have you gotten to nth member
				break
	
			print 'fib (', count, ') =', c
			a, b = b, c				# first term becomes the previous second term, and second term becomes the previous third term
									# i.e if first term 'a' was 1 and second term 'b' was 2, then third term 'c' would be computed as: 1 + 2 = 3
									# to get the next term (i.e the new 'c'), 'a' would become the previous 'b' (2) and 'b' becomes the previous 'c' (3)
									# the new 'c' would now be equal to new 'a' + new 'b': (2 + 3); which would be equal to 5
									# so the loop continues like that...

		



def run():
	from sys import argv
	# 'argv' is a variable belonging to the the 'sys' module,
	# it stores  a 'list' of 'strings' of command-line arguments
	# supplied when you run your program (i.e python script)
	#
	# For example to run a script saved as Fibonacci.py, type:
	# 		python Fibonacci
	# Doing the above will automatically populate the argv list with
	# its first and only member: 	['Fibonacci'],
	# which is the name of your script
	# Any subsequent strings typed after 'Fibonacci' above will be added
	# to the argv list in order. So if you typed:
	#		python Fibonacci 1000
	# argv would look like this:	['Fibonacci', '1000']
	#
	# NB: argv[0] will always be the name of your program
	
	if len(argv)>1:					# if user supplies number:	use user's number as 'num'
		num = int(argv[1])			# get user-supplied number from the argv variable
	else:
		num = 10					# else:	use our number as 'num'

	print 'What do you wish to do? (1/2)'
	print '\t1.\tPrint nth Fibonacci number'
	print '\t2.\tPrint Fibonacci numbers up to nth member'
	
	opt = int(raw_input('>_'))
	if (opt==1):
		n_fib(num)
	else:
		fib(num)
		


# Starting point of program
if __name__ == '__main__':
	run()
