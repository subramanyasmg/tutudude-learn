import requests
from bs4 import BeautifulSoup



class PriceTracer:
    def __init__(self, url):
        self.url = url
        self.user_agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"}
        self.response = requests.get(url= self.url, headers=self.user_agent)
        self.soup = BeautifulSoup(self.response.text, "lxml")

    def product_title(self):
        title = self.soup.find('span', attrs={'id': 'productTitle'})
        if title is not None:
            return title.text.strip()
        else:
            return "Tag not found"


    def product_price(self):
        price = self.soup.find('span', attrs={'class': 'a-price-whole'})
        if price is not None:
            return price.text.strip()
        else:
            return "No price"

url = 'https://www.amazon.in/dp/B0FDL3VZR8/ref=sspa_dk_detail_0?psc=1&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWwy'
device = PriceTracer(url)
print(device.product_title())
print(device.product_price())