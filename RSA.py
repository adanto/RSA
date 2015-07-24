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

# Totient:
# Function that counts the positive integers less than n that are 
# relatively primes to n (coprimes)
def totient(n):
	return len([i for i in xrange(1, n) if coprimes(i, n)]) if n > 1 else 1


# Coprimes: 
# Two numbers are coprimes where the only divisor in common is 1
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
	return list(set(aDiv).intersection(set(bDiv))) == [1]

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
	#print coprimes(3,5)
	test(16)
	#mainRSA()

def test(digits = 16):
	print "---------- TEST TOTIENT ----------"
	testTotient()
	print "------- TEST TOTIENT ENDED -------\n"
	print "---------- TEST COPRIMES ----------"
	testCoprimes()
	print "------- TEST COPRIMES ENDED -------\n"
	print "---------- TEST DIGITS ----------"
	testDigits(digits)
	print "------- TEST DIGITS ENDED -------\n"
	print "---------- TEST DIG LEN ----------"
	testDigitsLen(digits)
	print "------- TEST DIG LEN ENDED -------\n"
	


def testTotient():
	print "CORRECT" if totient(1) == 1 else "INCORRECT", "TOTIENT"
	print "CORRECT" if totient(2) == 1 else "INCORRECT", "TOTIENT"
	print "CORRECT" if totient(3) == 2 else "INCORRECT", "TOTIENT"
	print "CORRECT" if totient(5) == 4 else "INCORRECT", "TOTIENT"
	print "CORRECT" if totient(9) == 6 else "INCORRECT", "TOTIENT"
	print "CORRECT" if totient(10) == 4 else "INCORRECT", "TOTIENT"
	print "CORRECT" if totient(11) == 10 else "INCORRECT", "TOTIENT"
	print "CORRECT" if totient(14) == 6 else "INCORRECT", "TOTIENT"
	print "CORRECT" if totient(19) == 18 else "INCORRECT", "TOTIENT"
	print "CORRECT" if totient(21) == 12 else "INCORRECT", "TOTIENT"
	print "CORRECT" if totient(24) == 8 else "INCORRECT", "TOTIENT"
	print "CORRECT" if totient(29) == 28 else "INCORRECT", "TOTIENT"
	print "CORRECT" if totient(30) == 8 else "INCORRECT", "TOTIENT"
	print "CORRECT" if totient(40) == 16 else "INCORRECT", "TOTIENT"
	print "CORRECT" if totient(45) == 24 else "INCORRECT", "TOTIENT"
	print "CORRECT" if totient(53) == 52 else "INCORRECT", "TOTIENT"
	print "CORRECT" if totient(56) == 24 else "INCORRECT", "TOTIENT"
	print "CORRECT" if totient(57) == 36 else "INCORRECT", "TOTIENT"
	print "CORRECT" if totient(80) == 32 else "INCORRECT", "TOTIENT"
	print "CORRECT" if totient(97) == 96 else "INCORRECT", "TOTIENT"
	print "CORRECT" if totient(99) ====  60 else "INCORRECT", "TOTIENT"

def testCoprimes():
	print "CORRECT" if coprimes(14, 15) == True else "INCORRECT"
	print "CORRECT" if coprimes(14, 21) == False else "INCORRECT"
	print "CORRECT" if coprimes(3, 5) == True else "INCORRECT"
	print "CORRECT" if coprimes(10, 5) == False else "INCORRECT"
	print "CORRECT" if coprimes(10, 9) == True else "INCORRECT"
	print "CORRECT" if coprimes(9, 9) == False else "INCORRECT"
	print "CORRECT" if coprimes(10, 11) == True else "INCORRECT"

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