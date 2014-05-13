# Test for json post requests

import requests
import json

url = 'http://httpbin.org/post'

r = requests.post(url, json={'life': 42})

print r

print r.json()

print r.status_code

print r.content

print r.request


