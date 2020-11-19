#!/usr/bin/python

import requests

r=requests.get('https://bell.ca')
print r.text
