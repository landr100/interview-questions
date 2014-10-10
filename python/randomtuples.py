#!/usr/bin/python

'''
randomtuples.py | write a function to generate a list of length 0-3 of the following tuple:
(an integer between 0-3, a float between -0.5 and 0.5, a random alphanumeric string of length 0-5 which may also be None)
'''

# ref: http://stackoverflow.com/a/2257449
import random
import string

list_size = random.randint(0, 3)
my_list = []
char_set = string.ascii_uppercase + string.digits

for tuple_no in range(list_size):
	my_size = random.randint(0, 6) # random number from 0 to 5; if 0 then pick None
	my_str = (None if my_size == 0 else ''.join(random.sample(char_set*my_size, my_size))) # generate a random string of length 0-5
	my_list += [(random.randint(0, 3), random.uniform(-0.5, 0.5), my_str)] # append this tuple to the list

print my_list

