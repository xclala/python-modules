class Perimeter():
	def square(side):
		return side*4
	def rectangle(length,width):
		return (length+width)*2
	def circle(radius):
		from math import pi
		return pi*radius*2
	def parallelogram(base,height):
		return (base+height)*2
	def sector(fan_angle,radius):
		from math import pi
		return (radius*2+pi*fan_angle*radius)/180
class Area():
	def rectangle(length,width):
		return length*width/2
	def square(side):
		return side**2
	def parallelogram(base,height):
		return base*height
	def triangle(base,height):
		return base*height/2
	def trapezoid(upper_base,bottom_base,height):
		return (upper_base+bottom_base)*height/2
	def circle(radius):
		from math import pi
		return pi*radius**2
	def annulus(Outer_radius,inner_radius):
		from math import pi
		return (Outer_radius**2-inner_radius**2)*pi
	def sector(fan_angle,radius):
		from math import pi
		return (pi*radius**2*fan_angle)/360
	def ellipse(major_semi_axis,semiminor_axis):
		from math import pi
		return pi*major_semi_axis*semiminor_axis
	def semicircle(radius):
		from math import pi
		return (pi*radius**2)/2
	class SuperficialArea():
		def square(side):
			return 6*side**2
		def rectangle(length,width,height):
			return 2*(length*width+length*height+width*height)
		def circle(radius):
			from math import pi
			return 4*pi*radius**2
class Bulk():
	def rectangle(length,width,height):
		return length*width*height
	def square(side):
		return side**3
	def cylinder(bottom_radius,height):
		from math import pi
		return pi*bottom_radius**2*height
	def circular_cone(bottom_radius,height):
		from math import pi
		return pi*bottom_radius**2*(height/3)
	def pyramid(bottom_radius,height):
		return bottom_radius*height/3
	def circle(radius):
		from math import pi
		return 4/3*pi*radius**3
	def general(basal_area,height):
		return basal_area*height