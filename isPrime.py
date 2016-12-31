def isPrime(int):
	for i in range(2,int//2,1):
		if int % i == 0:
			return False
	return True