def prime_factorization(num):
	temp=[]
	while num!=1:
		for i in range(2,num+1):
			if num%i==0:
				temp.append(i)
				num/=i
				break
		del i
		return temp
	else:
		if num==1:
			return 1
		else:
			raise ValueError("input error")
