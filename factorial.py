def factorial(n):
	if n == 1:
		return 1
	return n*factorial(n-1)
print(factorial(5))

def fib(n):
	if n <= 2:
		return [0,1][:n]
	seq = fib(n-1)
	x = len(seq)
	seq.append(seq[x-1]+seq[x-2])
	return seq

print(fib(50))