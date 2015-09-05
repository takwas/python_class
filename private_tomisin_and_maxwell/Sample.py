

from sys import argv


# skeleton of the structure of a function
# def [name]([param]):

# 	[body of code]
# 	[return]



# 	[]




def say_hello():
	print 'Hello!'


def say_hello_to(name):
	print 'Hello', name


def get_name():
	return raw_input("\n\nEnter your name: ")






if __name__ == '__main__':
	mr_who = get_name()
	say_hello_to(mr_who)
