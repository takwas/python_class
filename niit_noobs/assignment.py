
assignment = { 1 : "1. Create a FizzBuzz program that prints Fizz for multiples of 3; Buzz for multiples of 5 and FizzBuzz for multiples of both 3 and 5. Try to create and make use of functions isMul3() and isMul5() is_mul_3_5() in solving the problem. ", 2 : "2. Create a program to accept a number from a user and print the prime factors of the number using an isPrime() function defined by you.", 3 : "Create a function to check if a given string is a palindrome using an isPalindrome() function defined by you. [Find out what a palindrome is.]", 4 : """Consider the following operations applicable to a dictionary in Python (comments have been added to explain each line of code):
		myDict = {}				# create a new empty dictionary stored in variable 'myDict'
		myDict = { "Noun" : "A name of any person, animal, place or thing", 2 : "The number two", "waste" : "Nothing useful"}		# update dictionary with key-value pairs as given within the curly brackets, e.g key 'waste' has a value 'Nothing useful'
		myDict				# display contents of dictionary 'myDict'
		myDict{'new value'} = 'A new value'				# Update dictionary with new key 'new value' and a value 'A new value'
		myDict[2]			# display dictionary value contained in key '2'
		del myDict{'waste'}				# delete dictionary entry with key 'waste'

Using the Python's dictionary data structure, and bearing in mind that you can use an integer or string literal as a key, create a program to manage a phonebook. The user should be able to carry out these operations:
	- Look up a phone number, using the name.
	- Look up all records in phone book.
	- Add a phonenumber.
	- Delete a phone number.
Make the program easy to use for the user. Show menu options and let the user pick the appropriate option by typing the corresponding number.""" }

if __name__ == '__main__':
	import sys
	
	while True:
		print
		option = raw_input("Choose a question number from 1-4, or 'e' to exit:  ")
		if (option == 'e' or option == 'E'):
			break
		else:
			try:
				option = int(option)
			except ValueError:
				print 'You entered an incorrect value. Try again.'
				continue
		print
		print "%s %d" % ("You selected question", option)
		print
		print assignment[option]
		print
		raw_input("Press [ENTER] to continue...")
	
	sys.exit(0)
		
		
		
		
		
		
		
		
		
		
		
		
		
