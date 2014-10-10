#!/usr/bin/python

'''
perm2.py     | permutations of size 2 of a given list
'''

import itertools
import sys
my_str = (sys.argv[1] if sys.argv[1:] else 'a string') # provide a default string
print list(itertools.permutations(my_str, 2)) # print all iterations of size 2
