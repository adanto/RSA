#!/usr/bin/env python

def egcd(a, b):
	x, y, u, v = 0, 1, 1, 0
	while a != 0:
		q, r = b // a, b % a
		m, n = x - u * q, y - v * q
		b, a, x, y, u, v = a, r, u, v, m, n
	gcd = b
	return gcd, x, y

def test():
	# d * e = 1 (mod totient(n))
	e = 65537

	tot = 4624
	print "egcd(", e, tot,")", egcd(e, tot)
	tot = 5148
	print "egcd(", e, tot,")", egcd(e, tot)
	tot = 480
	print "egcd(", e, tot,")", egcd(e, tot)


if __name__ == "__main__":
	test()