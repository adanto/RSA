#!/usr/bin/env python

from numpy import random
import time 

# Returns n ** exp 
def expF(n, exp):
	if n == 0:
		return 0
	if exp == 1:
		return n
	while exp > 1:
		if exp % 2 == 0:
			return expF(n * n, exp / 2)
		else:
			return n * expF(n, exp - 1)
 
def expModF(n, exp, mod):
	n = n % mod
	if n == 0:
		return 0
	if exp == 1:
		return n
	while exp > 1:
		if exp % 2 == 0:
			return expModF(n * n % mod, exp / 2, mod)
		else:
			return (n * expModF(n, exp - 1, mod)) % mod


def test(times = 100):
	start_time = time.time()

	# a = expModF(5784672865487267586478326578463782657843628, 999999, 50)

	a = 5784672865487267586478326578463782657843628 ** 999999 % 50
	
	print a
	print time.time()-start_time
	# for i in xrange(times + 1):
	# 	n = random.randint(-1000, 100000)
	# 	exp = random.randint(1, 10000)
	# 	alg = expF(n, exp)
	# 	print n ** exp == alg, str(100 * (i + 0.0)/times) + "%"
	# 	if n ** exp!= alg:
	# 		print "ERROR"
	# 		break



if __name__ == "__main__":
	test(10000)

