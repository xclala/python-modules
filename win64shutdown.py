class shutdown():
	def slidetoshutdown(t=0):
		from os import system
		from time import sleep
		sleep(t)
		system("slidetoshutdown")
	def shutdown(t=0,m=None):
		if m==None:
			from os import system
			from time import sleep
			sleep(t)
			system('shutdown -c "%s"-s -t 0'%(m))
		else:
			from os import system
			from time import sleep
			sleep(t)
			system('shutdown -s -t 0')
	def remoteshutdown():
		from os import system
		system("shutdown /i")
	def poweroff():
		from os import system
		system("shutdown -s -t 0")