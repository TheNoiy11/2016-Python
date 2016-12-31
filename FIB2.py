def fib(n):
	list = [1,1]
	if n <= 0:
		return []
	elif n <= 2:
		return list[:n]
	seq = fib(n-1)
	x = len(seq)
	
	seq.append(seq[x-1] + seq[x-2])
	return seq
	
print(fib(90))