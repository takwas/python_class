def cat(filename=None):
	if filename is None:
		filename = raw_input('Enter a file name:\n\t>_')
	
	try:
		file = open(filename, 'r')
	
	except IOError:
		print 'That file does not exist!'
		print '\n Exiting the system!\n'
		return


	lines = file.readlines()
	
	for line in lines:
		print line
	
	file.close()



if __name__=='__main__':

	filename = 'README.md'


	import sys
	if len(sys.argv) > 1:
		filename = sys.argv[1]
	
	cat(filename)