# -*- coding: utf-8 -*-

import sys
import random
from random import randint

def main():
	print "Usage: python math-generator.py <amount-of-questions> <min-number> <max-number> <type:addition,subtraction,multiply,divide>"
	if len(sys.argv)<>5:
		print "Usage: python math-generator.py <amount-of-questions> <min-number> <max-number> <type:addition,subtraction,multiply,divide>"
		sys.exit(0)

	amount = int(sys.argv[1])
	min = int(sys.argv[2])
	max = int(sys.argv[3])
	type = str(sys.argv[4])

	i = 1
	while i <= amount:
		i += 1
		temp_min = randint(min,max)
		temp_max = randint(min,max)
		if temp_min>temp_max:
			temp = temp_min
			temp_min = temp_max
			temp_max = temp
		print temp_min,op_type(type),temp_max,"="


def op_type(t):
	return {
		"addition":"+",
		"subtraction":"-",
		"multiply":"x",
		"divide":"÷"
	}[t]

if __name__ == "__main__":
	main()
