#!/usr/bin/env python

# Key generation
# Select p,q both primes p != q
# n = p * q
# Calculate totient(n) = (p - 1)(q - 1)
# Select integer e -> gcd (totient(n), e) = 1; 1 < e < totient(n)
# Calculate d -> d = e^-1 (mod totient(n))

# Encryption 
# C = M^e mod n

# Decryption
# M = C^d mod n

from numpy import random
from math import sqrt

def coprimes(a, b):
	aDiv = [1]
	for i in xrange(2, a/2 + 1):
		if a % i == 0:
			aDiv.append(i)
	aDiv.append(a)
	bDiv = [1]
	for i in xrange(2, b/2 + 1):
		if b % i == 0:
			bDiv.append(i)
	bDiv.append(b)

	print a, aDiv
	print b, bDiv

def isPrime(num):
	if num % 2 == 0:
		return False
	for i in xrange(3, int(sqrt(num)) + 1, 2):
		if num % i == 0:
			return False
	return True

def primeGenerator(digits = 100):
	if digits <= 0:
		return 0
	num = 0

	for i in xrange(10, digits + 1, 10):
		num *= 10000000000
		num += random.randint(int("9" * 9), int("1" + "0" * 10))
	still = digits % 10
	if still > 0:
		num *= int("1" + "0" * still)
		num += random.randint(int("0" + "9" * (still - 1)), int("1" + "0" * still))

	while not isPrime(num):
		num += 1
		if len(str(num)) > digits:
			num -= int("1" + "0" * (digits))
	return num

def mainRSA(digits = 16):
	p = primeGenerator(digits)
	q = primeGenerator(digits)
	while p == q:
		q = primeGenerator(digits) 
	n = p * q
	coprimes = (p - 1) * (q - 1)
	print "p =", p
	print "q =", q
	print "n = p * q =", n
	print "coprimes(n) =", coprimes


def main():
	test(16)


def test(digits = 16):
	print "---------- TEST COPRIMES ----------"
	testCoprimes()
	print "------- TEST COPRIMES ENDED -------\n"
	print "---------- TEST DIGITS ----------"
	testDigits(digits)
	print "------- TEST DIGITS ENDED -------\n"
	print "---------- TEST DIG LEN ----------"
	testDigitsLen(digits)
	print "------- TEST DIG LEN ENDED -------\n"
	
def testCoprimes():
	print "CORRECT" if coprimes(10, 5) == True else "INCORRECT"

def testDigits(digits):
	for _ in xrange(5):
		a = primeGenerator(digits)
		print a, len(str(a)) == digits
		if len(str(a)) != digits:
			print "ERROR"

def testDigitsLen(digits = 20):
	for i in xrange(1, digits + 1):
		prime = primeGenerator(i)
		print i, "digits ->", prime, "PROBLEM" if not isPrime(prime) else ""
		if len(str(prime)) != i:
			print "incorrect len()" 


if __name__ == "__main__": 
	main()