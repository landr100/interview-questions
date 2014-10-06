#!/usr/bin/env python
# vim: set ts=4 et:

import requests
import unittest

def get(url):
    resp = requests.get(url)
    return resp.status_code, resp.headers, resp.content

class TestURLS(unittest.TestCase):
    def test_google(self):
        r = get('http://www.google.com/')
        self.assertEqual(r[0], 200)
    def test_none(self):
        r = get(None)
    def test_abc(self):
        r = get('abc')
    def test_htp(self):
        r = get('htp://')
    def test_htp(self):
        r = get('http://dns.failure')

if __name__ == '__main__':
    import sys
    if sys.argv[1:]:
        url = sys.arg[1]
        get(url)
    else:
        unittest.main()

