# the mystery function below can be called with an integer argument and will return some value
# 1. What useful function does it perform?
# 2. Explain in detail how it works!

def is_prime(a):
	return not (a < 2 or any(a % x == 0 for x in range(2, int(a**0.5) + 1)))
	
	
# below is a line of code using the mystery function
# 3. Describe what it does and how it works!

print([z for z in range(100) if is_prime(z) or z % 3 == 0])


		

