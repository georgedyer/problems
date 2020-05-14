# Sherlock: solve the mystery!!!
# What does this mystery function return and how does it work?
# What kind of data structure does it return? Why?
# If you don't know what a particular command does, look it up and try it out in the console with examples. Tinker!
# Work out what EACH STEP of what the function does when you pass it several example values, like 6, 7, 10, 25, 32, etc. What does it return in these cases?
# Be able to explain how this function works in detail! 

def mystery(n):
	i = 2
	f = []
	while i * i <= n:
		if n % i:
			i += 1
		else:
			n //= i
			f.append(i)
	if n > 1:
		f.append(n)
	
	fz = [(x, f.count(x)) for x in set(f)]
	
	return fz

		
def mystery2(a,b):
	f = 1
	for i in mystery(a):
		matches = [j for j in mystery(b) if j[0] == i[0]]
		if len(matches):
			match = matches[0]
			f *= i[0]**min(i[1],match[1])
			
	return f
	

