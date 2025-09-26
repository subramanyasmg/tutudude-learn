import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup

url = urllib.request.urlopen('http://www.python.org')

for line in url:
    print(line.decode().strip())

