import itertools

def prime_factors(n):
	i = 2
	factors = []
	while i * i <= n:
		if n % i:
			i += 1
		else:
			n //= i
			factors.append(i)
	if n > 1:
		factors.append(n)
	return factors

def factorization_str(num, primes):
	return " x ".join([(str(f[0]) if f[1] == 1 else "^".join([str(i) for i in f])) for f in primes])
	

def print_questions(): 
	for i in range(2,101):
		primes = prime_factors(i)
		g_primes = list(set([(p, primes.count(p)) for p in primes]))
		g_primes.sort(key=(lambda x: x[0]))
		fstrs = [factorization_str(i, pr) for pr in list(itertools.permutations(g_primes))]
		print(i,'|',", ".join(fstrs))
		
def union(arr1, arr2):
	arr = []
	while len(arr1) + len(arr2) > 0:
		try:
			x1 = arr1.pop()
		except:
			arr.extend(arr2)
			return arr
		try:
			x2 = arr2.pop()
		except:
			arr.extend(arr1)
			return arr
		if x1 == x2:
			arr.append(x1)
		# todo - finish

for x in range(2,50):
	print(x, prime_factors(x))

