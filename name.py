def name(first_name:str,middle_name=None,last_name:str) -> str:
	"""python_version>=3.6"""
	if middle_name==None:
		return first_name+' '+last_name
	else:
		return first_name+' '+middle_name+' '+last_name
