import numpy as np 

def sieve(n):
	"""
	returns a list of all positive primes up to n
	"""
	p = 2
	integers = list(range(p, n))
	for i in integers: 
		if i != 0: 
			multiples = list(range(i, n, i))[1:]
			for m in multiples: 
				integers[m-p] = 0

	primes = [i for i in integers if i != 0]
	return primes

def estimate_primes(n):
	"""
	returns the estimate size of the nth prime for n > 5
	"""
	return int(n * np.log(n) + n * np.log(np.log(n)))

def n_primes(n): 
	"""
	returns a list of the n first primes 
	"""
	primes = sieve(estimate_primes(n))
	return primes[:n]

print(n_primes(8))