import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

sess = requests.Session()
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
}

url = "https://neue-pressemitteilungen.de/post_part1.xml"
r = sess.get(url, headers=headers)

# root = ET.fromstring(r.text)
# links = root.findall('./loc')
# print(links)

soup = BeautifulSoup(r.text, 'lxml')
links = [elm.get_text() for elm in soup.find_all('loc')]

print(links)
