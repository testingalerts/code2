#!/usr/bin/python

import requests

r=requests.get('https://outlook.office.com')
print r.text
