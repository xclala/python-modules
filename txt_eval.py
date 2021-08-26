def txt_run(path:str):
	"""python_version:>=3.6"""
	with open(path,"r") as f:
		return eval(f.read())
