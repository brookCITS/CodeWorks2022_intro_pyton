from abc import ABC, abstractmethod

#the abstract class
class Polygon(ABC):

	@abstractmethod
	def sides(self):
		pass


#the other classes that inherit from the abstract class
class Triangle(Polygon):

	# overriding abstract method
	def sides(self):
		print("I have 3 sides")

class Pentagon(Polygon):

	# overriding abstract method
	def sides(self):
		print("I have 5 sides")

class Hexagon(Polygon):

	# overriding abstract method
	def sides(self):
		print("I have 6 sides")

class Quadrilateral(Polygon):

	# overriding abstract method
	def sides(self):
		print("I have 4 sides")

# Driver code
R = Triangle()
R.sides()

K = Quadrilateral()
K.sides()

R = Pentagon()
R.sides()

K = Hexagon()
K.sides()
# what would happen if we try to creat an instance of the abstract class
