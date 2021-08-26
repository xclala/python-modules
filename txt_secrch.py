def txt_secrch(path,message):
	from re import compile,search
	p=compile(message)
	with open(path) as file_object:
		file_object=codecs.open(path,'r+',encoding='utf-8')
	a=p.search(file_object.read())
	del p,file_object
	if a:
		del a
		return True
	else:
		del a
		return False
