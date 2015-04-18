



def run():
	import sys
	print 'Hello,\nThe name of this file is', sys.argv[0]
	
	if(len(sys.argv)>1):
		print 'Second argument is', sys.argv[1]
	
	if(len(sys.argv)>2):
		print 'Third argument is', sys.argv[2]
		
		print 'All arguments are:', sys.argv
		print '\nWhen separated:\n\n'
		print '\t', sys.argv[0]
		print '\t', sys.argv[1]
		print '\t', sys.argv[2]




if __name__ == '__main__':
	run()
