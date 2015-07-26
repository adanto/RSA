#!/usr/bin/env python

from numpy import random

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


def test(times = 100):
	print expF(2, 5)
	for i in xrange(times + 1):
		n = random.randint(-1000, 100000)
		exp = random.randint(1, 10000)
		alg = expF(n, exp)
		print n ** exp == alg, str(100 * (i + 0.0)/times) + "%"
		if n ** exp!= alg:
			print "ERROR"
			break



if __name__ == "__main__":
	test(10000)

