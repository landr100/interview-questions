#!/usr/bin/python

'''
write a class Foo and a class Bar that inherits from Foo. when a Foo object is created it prints "foo". when a Bar object is created it prints "foo" using inheritance and "bar".
'''

class Foo(object):
	"""base class"""
	def __init__(self):
		print "foo"

class Bar(Foo):
	"""derived class"""
	def __init__(self):
		super(Bar, self).__init__() # call Foo's init
		print "bar"

j = Foo()
k = Bar()

