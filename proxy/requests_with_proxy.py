import random
import requests

proxy_file_name = 'proxy_http_ip.txt'
PROXIES = []
with open(proxy_file_name, 'rb') as text:
    PROXIES = ["http://" + x.decode("utf-8").strip() for x in text.readlines()]


sess = requests.Session()
pxy = random.choice(PROXIES)
proxyDict = {
    'http': pxy,
    'https': pxy,
    'ftp': pxy,
    'SOCKS4': pxy
}
sess.proxies = proxyDict
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
}

url = "https://neue-pressemitteilungen.de/geg-erwirbt-eurotheum-in-frankfurt-von-commerz-real.html"
r = sess.get(url, headers=headers)