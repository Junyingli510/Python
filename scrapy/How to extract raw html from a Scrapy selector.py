import scrapy
import pandas as pd

tbl = response.xpath('(//div[contains(@class,"tabbertab tabbertabdefault")])[1]').get()
df = pd.read_html(tbl)