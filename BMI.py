def BMI(M,KG):
	if M>0 or KG>0:
		return KG/M**2
	else:
		raise ValueError('Weight or height is less than or equal to zero')	
