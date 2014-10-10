#!/usr/bin/python

'''
primes100.py | print the primes between 1-100
this version uses a function to determine if a number is prime
'''

# ref: http://stackoverflow.com/a/15285590
# function that returns true if a number is prime, false otherwise
def isPrime(n):
	""""precondition n is a nonnegative integer
postcondition:  return True if n is prime and False otherwise."""
	if n < 2:
		 return False
	if n % 2 == 0:
		 # return False
		 return n == 2
	k = 3
	while k*k <= n:
		 if n % k == 0:
			 return False
		 k += 2
	return True

for j in range(2, 100):
	if(isPrime(j)):
		print j
