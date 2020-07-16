import requests
from bs4 import BeautifulSoup
import time

URL = "https://www.worldometers.info/coronavirus/country/poland/"

page = requests.get(URL)
### wchodzi na stronę

source = page.content
### pobiera zawartość f12

soup = BeautifulSoup(source, 'lxml')
### creates a subobject xd

### print(soup.prettify())
### formatuje kontent

### soup.find_all("div")
### wyszukuje konkretne tagi, np. div


tag1 = soup.find_all("span")[4]
tag2 = soup.find_all("span")[5]
tag3 = soup.find_all("span")[6]

s = tag1.string
p = tag2.string
r = tag3.string

print("przypadki:", s,"zmarli:", p,"ozdrowieńcy:", r)
time.sleep(10)
