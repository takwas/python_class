
#### Python classes

# A class is a blueprint for creating (or instantiating)
# objects (or instances)



#class [ClassName](*SuperArgs):
#
#	def __init__(self, attrib):
#		self.attrib = attrib
#
#	def __str__(self):
#		# a string representation of this object
#		pass
#
#	def __repr__(self):
#		pass
#
#	def behavior(self):
#		my_func(*args)
#		
#	def my_func(*args):
#		pass

class Engine(object):

	def __init__(self, make, country, chasis):
		self.make = make
		self.country = country		
		self.chasis = chasis

	def __str__(self):
		return '%s - %s [%s]' % (self.make, self.country, self.chasis)


class Vehicle(object):

	def __init__(self, make, num_tyres, engine):
		self.make = make
		self.num_tyres = num_tyres
		self.engine = engine

	def __str__(self):
		return "%s (%d): %s" %(self.make, self.num_tyres, self.engine)


class Car(Vehicle):

	def __init__(self, make, num_tyres, car_engine, color):
		self.color = color
		super(Car, self).__init__(make=make, num_tyres=num_tyres, engine=car_engine)

	def __str__(self):
		return super(Car, self).__str__() + "\nColor:  %s" % self.color


class Tricycle(Vehicle):

	def __init__(self, make, engine, color):
		self.color = color
		self.num_tyres = 3
		super(Tricycle, self).__init__(make=make, num_tyres=num_tyres, engine=enginee)

	def __str__(self):
		return super(Tricycle, self).__str__() + "\nColor:  %s" % self.color


def test():
	import os
	toyeng = Engine('Toyota', 'Germany', 'e35473f')
	honeng = Engine('Honda', 'Japan', str(os.urandom(8)))

	print
	print toyeng
	print honeng
	print



if __name__ == '__main__':
	test()
	
		

		





