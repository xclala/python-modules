#The distance between two points in 1-4 dimensions
#dtpfd
class DBTP():
	def four_ddbtp(x1,x2,y1,y2,z1,z2,w1,w2):
		from math import sqrt
		return abs(sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2+(w1-w2)**2))
	def three_ddbtp(x1,x2,y1,y2,z1,z2):
		from math import sqrt
		return abs(sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2))
	def two_ddbtp(x1,x2,y1,y2):
		from math import sqrt
		return abs(sqrt((x1-x2)**2+(y1-y2)**2))
	def one_ddbtp(x1,x2):
		from math import sqrt
		return abs(x1-x2)