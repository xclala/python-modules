class RandomCoordinates():
	"""python_version:>=3.6"""
	def two_dimension(xsecope:int,ysecope:int) -> str:
		from random import randint
		x=randint(0,xsecope)
		y=randint(0,ysecope)
		x=str(x)
		y=str(y)
		return "("+x+","+y+")"

	def three_dimension(xsecope: int, ysecope: int, zsecope: int) -> str:
		from random import randint
		x=randint(0,xsecope)
		y=randint(0,ysecope)
		z=randint(0,zsecope)
		x=str(x)
		y=str(y)
		z=str(z)
		return "("+x+","+y+","+z+")"
