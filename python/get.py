#!/usr/bin/env python
# vim: set ts=4 et:

import requests
import unittest

def get(url):
    try:
	    resp = requests.get(url)
	    return resp.status_code, resp.headers, resp.content
    except:
	print "get on url %s failed" % url
	return None

class TestURLS(unittest.TestCase):
    def test_google(self):
        r = get('http://www.google.com/')
        self.assertEqual(r[0], 200)
    def test_none(self):
        r = get(None) # fails due to invalid url
    def test_abc(self):
        r = get('abc') # fails due to invalid url
    def test_htp(self):
        r = get('htp://') # fails due to invalid url
    def test_htp(self):
        r = get('http://dns.failure') # fails due to invalid url

if __name__ == '__main__':
    import sys
    if sys.argv[1:]:
        url = sys.argv[1]
        print get(url)
    else:
        unittest.main()

