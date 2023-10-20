import requests

print('python language')

url = f'http://python.org'
r = requests.get(url)
print(r.status_code)

print(r.content)

print(b'Python is a programming language' in r.content)