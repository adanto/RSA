#!/usr/bin/env python

# Key generation
# Select p,q both primes p != q
# n = p * q
# Calculate totient(n) = (p - 1)(q - 1)
# Select integer e -> gcd (totient(n), e) = 1; 1 < e < totient(n)
# In this case e = 2^16 + 1
# Calculate d -> d * e = 1 (mod totient(n))

from numpy import random

def strToInt(txt, n):
	l = []
	v = 0
	for i in txt:
		v *= 27
		v += translate(i)
		if (v * 27) + 27 > n:
			l.append(v)
			v = 0
	l.append(v)
	return l


def intToStr(li):
	txt = ""
	while li > 0:
		txt = reTranslate(li % 27) + txt
		li -= li % 27
		li /= 27
	return  txt

# Makes n ** exp % mod more quick. Tested in exponentAlgTest.py
def expModF(n, exp, mod):
	n = n % mod
	if n == 0:
		return 0
	if exp == 1:
		return n % mod
	while exp > 1:
		if exp % 2 == 0:
			return expModF(n * n, exp / 2, mod) % mod
		else:
			return (n * expModF(n, exp - 1, mod)) % mod


# Extended Euclidean Algorithm 
# from: https://en.m.wikibooks.org/wiki/Algorithm_Implementation/Matematics/Extended_Euclidean_algorithm
# This function takes two different integers a, b and return a triple (g, x, y) such that
# ax + by = gcd(a, b)
def egcd(a, b):
	x, y, u, v = 0, 1, 1, 0
	while a != 0:
		q, r = b // a, b % a
		m, n = x - u * q, y - v * q
		b, a, x, y, u, v = a, r, u, v, m, n
	gcd = b
	return gcd, x, y

# Last method that has to be correctly implemented
# with the EXTENDED EUCLIDEAN ALGORITHM
def calculateD(e, module):
	d = 0
	while True:
		if d * e % module == 1:
			return d
		d += 1

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
	if num == 1:
		return False
	if num % 2 == 0:
		return False
	for i in xrange(3, int(pow(num, 0.5)) + 1, 2):
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


# Encryption 
# C = M^e mod n
def encrypt(plain, e, n):
	#return expModF(plain, e, n)
	return pow(plain, e) % n

# Decryption
# M = C^d mod n
def decrypt(enc, d, n):
	return (enc ** d % n)

def mainRSA(digits = 16, plain = "2"):
	# prime p
	p = primeGenerator(digits)
	print "p =", p

	# prime q
	q = primeGenerator(digits)
	while p == q:
		q = primeGenerator(digits) 
	print "q =", q
	
	# n = p * q (this is the future module)
	n = p * q
	print "n = p * q =", n
	
	# lets calcule the totient 
	# must be the sabe as totient(n = p * q)
	totient = (p - 1) * (q - 1)
	print "totient(n) =", totient

	e = pow(2, 16) + 1
	print "e = 2 ^ 16 + 1 =", e

	# calculate d
	d = egcd(e, totient)[1]
	
	# if negative d, we can obtain another d = totient + (negative d)
	d = totient + d if d < 0 else d

	print "d =", d


	plain = strToInt(plain, n)

	encryption = []
	for block in plain:

		enc = encrypt(block, d, n)
		encryption.append(enc)
		dec = decrypt(enc, e, n)

		print "'" + intToStr(block) + "'", "-> encrypted ->", enc, "-> decrypted again ->", "'" + intToStr(dec) + "'"
	return [intToStr(i) for i in encryption], n, totient, d

def translate(letter):
	dic = {
		"a": 1,
		"b": 2,
		"c": 3, 
		"d": 4,
		"e": 5,
		"f": 6,
		"g": 7,
		"h": 8,
		"i": 9,
		"j": 10,
		"k": 11,
		"l": 12,
		"m": 13,
		"n": 14,
		"o": 15,
		"p": 16,
		"q": 17,
		"r": 18,
		"s": 19,
		"t": 20,
		"u": 21,
		"v": 22,
		"w": 23,
		"x": 24,
		"y": 25,
		"z": 26,
		" ": 0
	}
	return dic[letter] if letter in dic else -1

def reTranslate(letter):
	dic = {
		1 : "a",
		2 : "b",
		3 : "c", 
		4 : "d",
		5 : "e",
		6 : "f",
		7 : "g",
		8 : "h",
		9 : "i",
		10 : "j",
		11 : "k",
		12 : "l",
		13 : "m",
		14 : "n",
		15 : "o",
		16 : "p",
		17 : "q",
		18 : "r",
		19 : "s",
		20 : "t",
		21 : "u",
		22 : "v",
		23 : "w",
		24 : "x",
		25 : "y",
		26 : "z",
		0 : " "
	}
	return dic[letter] if letter in dic else -1

def main():
	
	plain = "hello world this is a test to see of we can encrypt any len text with letters and spaces"
	
	for i in xrange(1):
	#while True:
		dig = 2
		a = mainRSA(dig, plain)
		print a,"\n\n"
		
	# test(10, 10, 277)


def test(digits = 16, times = 10, plain = 277):
	print "---------- TEST ENC DEC ----------"
	testEncDec(digits, times)
	print "------- TEST ENC DEC ENDED -------\n"
	print "---------- TEST EGCD ----------"
	testEGCD(digits)
	print "------- TEST EGCD ENDED -------\n"
	print "---------- TEST TOTIENT ----------"
	testTotient()
	print "------- TEST TOTIENT ENDED -------\n"
	print "---------- TEST COPRIMES ----------"
	testCoprimes()
	print "------- TEST COPRIMES ENDED -------\n"
	print "---------- TEST DIGITS ----------"
	testDigits(digits)
	print "------- TEST DIGITS ENDED -------\n"
	print "---------- TEST DIGITS LEN ----------"
	testDigitsLen(digits)
	print "------- TEST DIGITS LEN ENDED -------\n"
	
def testEncDec(digits = 10, times = 10):
	for i in xrange(times):
		plain = random.randint(0, 10000000000000000)
		print "plain text ->", plain
		p = primeGenerator(digits)
		q = primeGenerator(digits)
		while p == q:
			q = primeGenerator(digits) 
		n = p * q
		totient = (p - 1) * (q - 1)
		e = pow(2, 16) + 1
		d = egcd(e, totient)[1]
		d = totient + d if d < 0 else d
		enc = encrypt(plain, d, n)
		dec = decrypt(enc, e, n)
		if dec == plain:
			print plain, "->", enc, "->", dec, "\n", "CORRECT", str(100.0 * (1 + i)/times) + "%\n"
		else:
			print "ERROR"
			break

def testEGCD(digits = 4, times = 10):	# prime p
	for i in xrange(times ):
		p = primeGenerator(digits)
		# prime q
		q = primeGenerator(digits)
		while p == q:
			q = primeGenerator(digits) 
		
		# n = p * q (this is the future module)
		n = p * q		
		# lets calcule the totient 
		# must be the sabe as totient(n = p * q)
		totient = (p - 1) * (q - 1)
		e = pow(2, 16) + 1
		# calculate d
		d = egcd(e, totient)[1]
		d = totient + d if d < 0 else d
		print "d * e = 1 mod tot --->", d, e, totient
		if d * e % totient == 1:
			print "CORRECT", str(100.0 * (1 + i) / times) + "%"
		else:
			print "ERROR" 
			break
		
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
	print "CORRECT" if totient(99) ==  60 else "INCORRECT", "TOTIENT"

def testCoprimes():
	print "CORRECT" if coprimes(14, 15) == True else "INCORRECT"
	print "CORRECT" if coprimes(14, 21) == False else "INCORRECT"
	print "CORRECT" if coprimes(3, 5) == True else "INCORRECT"
	print "CORRECT" if coprimes(10, 5) == False else "INCORRECT"
	print "CORRECT" if coprimes(10, 9) == True else "INCORRECT"
	print "CORRECT" if coprimes(9, 9) == False else "INCORRECT"
	print "CORRECT" if coprimes(10, 11) == True else "INCORRECT"

def testDigits(digits, times = 10):
	for _ in xrange(times):
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