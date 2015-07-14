

class Animal(object):

	def __init__(self, name, weight, gender):
		self.name = name
		self.weight = weight
		self.gender = gender

	
	def __str__(self):
		#print "Animal:\nName - %d\nWeight - %skg" %(self.name, self.weight)
		return "Animal:\nName - %s\nWeight - %dkg" %(self.name, self.weight)
		


class Man(Animal):
	
	def __init__(self, name, weight, gender, color):
		super(Man, self).__init__(name, weight, gender)
		self.color = color

	def __str__(self):
		#print "Man:\nName - %d\nWeight - %skg" %(self.name, self.weight, self.color)
		return "Man:\nName - %s\nWeight - %dkg\nColor - %s" %(self.name, self.weight, self.color)





if __name__ == '__main__':
	anime1 = Animal('Dog', 45, 'Male')
	anime2 = Animal('Cat', 25, 'Female')
	man = Man('Teddy', 90, 'Male', 'Black')
	print
	print
	print anime1
	print
	print anime2
	print
	print man, '\nGender: %s' %man.gender
	print
	print


#animal1 = Animal()
#animal2 = Animal()

#animal1.__init__()
#print animal1

#%s %r
