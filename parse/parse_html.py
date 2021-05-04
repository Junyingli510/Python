import requests
from lxml import html

sess = requests.Session()
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
}

url = "https://stackoverflow.com/"
r = sess.get(url, headers=headers)
tree = html.fromstring(r.text)

links = tree.xpath('//div[@class="summary"]/h3/a/@href')

