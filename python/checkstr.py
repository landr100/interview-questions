#!/usr/bin/python

'''
checkstr.py | a string may contain alphanumeric characters. it may also contain dashes, but not begin or end with them or contain 2 or sequentially.
	write a function that checks for this format.
'''

import re # re.search(regex, string) is not None means the string matches the regex

Ok = 0
Bad = 1 # enables counting number of failed results

# TODO: what if string is empty; success or failure?
def checkstr(my_str):
	my_regex = "[a-zA-Z0-9\-]" # first pass
	first_pass = re.search(my_regex, my_str)
	if first_pass is None:
		print "checkstr did not find alphanumerics or dashes in %r" % my_str
		return Bad
	else:
		regex2 = "^\-|\-$|\-\-" # second pass
		second_pass = re.search(regex2, my_str)
		if second_pass is not None:
			print "checkstr: string %r begins or ends with dashes and/or has 2 or more consecutive dashes" % my_str
			return Bad

		return Ok

if __name__ == '__main__':
	import sys
	if sys.argv[1:]:
		my_str = sys.argv[1]
		check = checkstr(my_str)
		print "result of calling checkstr on %r is %r" % (my_str, ('Ok' if check == Ok else 'Bad'))
	else:
		num_fail = 0
		# contains alphanumeric characters (plus dot, pipe, comma) ; requirements are unclear; assume success
		should_pass = checkstr('checkstr.py | a string may contain alphanumeric characters. it may also contain dashes, but not begin or end with them or contain 2 or sequentially.')
		if should_pass == Bad:
			print "first test failed"
			num_fail += 1

		# should succeed because the only hyphens are in the middle and there are not two in a row
		should_succeed = checkstr('abcdefghijklmnopqrstuvwxyz-0123456789-x')
		if should_succeed == Bad:
			print "second test failed"
			num_fail += 1

		# all four should fail
		should_fail2 = checkstr('-abc') + checkstr('abc-') + checkstr('-abc012') + checkstr('a--b')
		if should_fail2 != 4*Bad:
			print "third test failed"
			num_fail += should_fail2

		print "%d tests failed" % num_fail

