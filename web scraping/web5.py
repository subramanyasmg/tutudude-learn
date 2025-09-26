import requests
from bs4 import BeautifulSoup
import csv

url = 'https://en.wikipedia.org/wiki/Main_Page'

user = {
    "User-Agent": "Mozilla/5cd .0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
}


def Extract(url):
    response = requests.get(url, headers=user).content
    soup = BeautifulSoup(response, 'lxml')
    tag = soup.find('div', attrs={'id': 'mp-right'})
    h = tag.find_all("h2")
    content = [content.text for content in h]
    print(content)
    with open("wiki.csv", "w") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(content)


Extract(url)