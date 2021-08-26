def again(number:int):
	"""for example:
	input 1 output 1
	input 2 output 22
	input 3 output 333
	python_version>=3.6
	"""
	if number>0:
		int_number=number
		number=str(number)
		str_number=number*int_number
		number=int(str_number)
		del str_number,int_number
		return number
	else:
		raise ValueError("Enter numbers less than or equal to zero")
