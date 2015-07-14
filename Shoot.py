


# modules = ['math', 'Tkinter', 'time', 'random', 'tkFont']



# for module in modules:
	

# 	if module == 'Tkinter':
# 		try:
# 			from module import *

# 		except ImportError:
# 			raise ImportError("Failed to import %s" % module)


# 	else:
# 		try:
# 			import module
# 			print "%s imported!" % module

# 		except ImportError:
# 			raise ImportError("Failed to import %s" % module)


# print "All imports successful!"




from Tkinter import *
import time
import random
import math
import tkFont


OBJ_COLOR = "#fff"
BG_COLOR = "#000"


# class definition
class TomShooter(Frame):

	def __init__(self, master=None, width=400, height=200):
		Frame.__init__(self, master=master, width=width, height = height, takefocus=1)
		self.width = width
		self.height = height
		self.grid_propagate(0)
		self.grid()

		self.setupWidgets()


	def setupWidgets(self):
		self.canvas = TomShooterCanvas(self, bg_color=BG_COLOR)
		self.canvas.grid(row=0, column=0)



# class definition
class TomShooterCanvas(Canvas):

	def __init__(self, master, bg_color, width=0, height=0, gr=0, gc=0):
		if width == 0:
			width = master.width
		
		if height == 0:
			height = master.height
		
		Canvas.__init__(self, master=master, width=width, height=height, background=bg_color)
		
		self.width = width
		self.height = height
		self.grid(row=gr, column=gc)


	def create_arrow(self, arrow):
		id = self.create_line(arrow.get_x0(), arrow.get_y0(), \
							arrow.get_x1(), arrow.get_y1(), \
							arrow=arrow.heads, fill=arrow.color, width=arrow.thickness)
		
		arrow.setId(id)
		arrow.setMaster(self)




# class definition
class Arrow(object):

	def __init__(self, x0=0, y0=0, x1=0, y1=0, id=0, tags=["arrows"], master=None, thickness=1, color='#000', heads=1):
		self.x0 = x0
		self.y0 = y0
		self.x1 = x1
		self.y1 = y1
		self.id= 0
		
		if tags != ["arrows"]:
			giventags = tags

			if type(tags) == list:
				tags.insert(0, "arrows")
			else:
				tags = ["arrows"]
				tags.append(giventags)

		self.tags = tags
		self.master = master
		self.thickness = 1
		self.color = color

		if heads == 1:
			self.heads = 'first'
		elif heads == 2:
			self.heads = 'last'
		else:
			self.heads = "both"



	def setId(self, id):
		self.id = id

	def getId(self):
		return self.id


	def setMaster(self, master):
		self.master = master

	def getMaster(self):
		return master


	def getCoords(self):
		return (self.x0, self.y0, self.x1, self.y1)


	def get_x0(self):
		return self.x0

	def get_y0(self):
		return self.y0

	def get_x1(self):
		return self.x1

	def get_y1(self):
		return self.y1

	def get_width(self):
		return abs(self.x1 - self.x0)

	def get_height(self):
		return abs(self.y1 - self.y0)


# run program
def run():
	# setup and run program
	app = TomShooter()
	canvas = app.canvas
	line_coords = [10,canvas.height/2,60,canvas.height/2]

	arrow = Arrow(x0=line_coords[0], y0=line_coords[1], x1=line_coords[2], y1=line_coords[3], color='#fff', heads=2)
	canvas.create_arrow(arrow)

	#oval_coords = [10,canvas.height/2+10,60,canvas.height/2+50]
	#canvas.create_oval(oval_coords, fill=OBJ_COLOR)


	def click(event):
		print 'clicked'
		paintball(event.x, event.y)

	def paintball(x,y, width=50, height=50):
		print 'painted'
		oval_coords = [x,y, x+width, y+height]
		canvas.create_oval(oval_coords, fill=OBJ_COLOR)

	canvas.bind("<Button-1>", click)

	app.mainloop()


# run if called as a script; not when imported as a module
if __name__=='__main__':
	run()
	
