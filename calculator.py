#!/usr/bin/env python

import sys

def addition(a, b):
	return a + b

def main():
	# Parse the command line
	try:
		a, op, b = sys.argv[1].split()
		a, b = float(a), float(b)
	except:
		print 'Usage: calculator.py "A op B"'
		return -1

	print 'Unknown operator', op
	return -1

if __name__ == "__main__":
	main()
