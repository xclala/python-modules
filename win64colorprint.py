def color_print(text:str,color:str):
	"""python_version:>=3.6"""
	from os import system
	if color=='blue':
		system("color 01")
		print(text)
	elif color=='green':
		system("color 02")
		print(text)
	elif color=='red':
		system("color 04")
		print(text)
	elif color=='purple':
		system("color 05")
		print(text)
	elif color=='yellow':
		system("color 06")
		print(text)
	elif color=='gray':
		system("color 08")
		print(text)
def random_color_print(text):
	from random import choice
	from os import system
	system("color 0"+choice(['1','2','4','5','6','8']))
	print(text)
