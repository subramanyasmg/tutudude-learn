import requests
url = 'http://www.python.org'
response = requests.get(url)
html = response.text
print(html)
