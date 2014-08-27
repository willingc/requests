import requests
import json

r = requests.post('http://httpbin.org/post', data=json.dumps({'life': 42}))
print(r.status_code)
print(r.json())
print(r.encoding)
print(r.headers)
