class FileRun():
	"""python_version>=3.6"""
	def txt_run(path:str):
		with open(path,"r") as f:
			return exec(f.read())
	def py_run(path:str):
		from os import system
		system("python %s"%(path))