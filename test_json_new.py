import requests

r = requests.post('http://httpbin.org/post', json={'life': 42})
print(r)
print(r.json())
print(r.encoding)
print(r.headers)
