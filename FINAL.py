def James(x):
	if x == 0:
		return 1
	else:
		return x*James(x-1)