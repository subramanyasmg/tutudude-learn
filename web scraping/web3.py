import urllib

import requests

user = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
}

payload = {
    "title": 'Greetings',
    "content": 'Python Love',
}
url = "http://localhost:8000/post/"
response = requests.post(url, data=payload, headers=user)
html = response.text
print(html)
print(response.text)
