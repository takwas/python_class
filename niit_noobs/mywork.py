def getAvg(a,b,c):
	sum = a+b+c
	avg = sum/3
	print "Sum:", sum
	return avg

def printAvg():
	myAvg = getAvg(1,5,6)
	print "Average is", myAvg
	print

def printDblAvg():
	myAvg = getAvg(1,5,6)
	dblAvg = myAvg * 2
	print "Double average:\t", dblAvg
	print

def printTrplAvg():
	myAvg = getAvg(1,5,6)
	dblAvg = myAvg * 2
	trpAvg = dblAvg + myAvg
	print "Triple average:\t", trpAvg
	print



if __name__ == '__main__':
	printAvg()
	printDblAvg()
	printTrplAvg()


print "I'm done"