#!/usr/bin/python

'''
 write a program that prints the numbers from 1 to 100.
But for multiples of three print Fizz instead of the number and for the multiples of five print Buzz.
For numbers which are multiples of both three and five print FizzBuzz.
'''

for i in range(100):
	j = i + 1	
	if(j%2 == 0) or (j%3 == 0) or (j%5 == 0) or (j%7 == 0):
		next
	print j

