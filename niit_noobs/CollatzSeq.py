# author: ac3Takwas
# File: CollatzSeq.py
#
# This program takes a number from a user
# and carries out some operation on it.
# If the number is an even number, it is divided
# in half. Otherwise, as an odd number it is
# multiplied by three and one is added to it.

#Initialization
usernum = 1
final_number = 1


# function to check if number is even
def isEven(num):
	if num % 2 == 0:
		return True
	else:
		return False

# function to check if number is odd
def isOdd(num):
	return not isEven(num)
# Other implementations of this function below:
#	return num % 2 != 0
#	if num % 2 != 0:
#		return True

def collatz(num):
	if isEven(num):
		num = num/2

	elif isOdd(num):
		num = (num * 3) + 1
	
	return num

# function to run program
def run():
	# accept a number from the user
	usernumstr = raw_input("Please enter a number: ")
	# convert  number from string to integer
	usernum = int(usernumstr)
	
	# keep track of number of collatz steps
	count = 0

	# run collatz
	while True:
		# break when user number is collatzed to number one (1)
		if (usernum <= final_number):
			break

		else:
			usernum = collatz(usernum)
		
		count  += 1
		#print "usernum:", usernum		#DEBUG
	
	print "Number of steps:\t", count



# program entry point
if __name__ == "__main__" :
	run()
	


print "I'm done!"
