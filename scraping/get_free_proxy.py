from free_proxy import FreeProxy
import os
from proxyscrape import create_collector

from datetime import datetime

def get_now_str():
    now = datetime.now()
    return now.strftime("%Y-%m-%d")

from db_manager import DB

class ScrapeFreeProxies():
    def __init__(self):
        self.result_dir = os.path.join(os.getcwd(), "Result")
        if not os.path.exists(self.result_dir):
            os.makedirs(self.result_dir)

        self.collector = create_collector('my-collector', 'http')

        self.DB_Name = "proxies.db"
        self.tbl_name = "http"
        self.db_proxy = DB(dst_path=self.result_dir, dbname=self.DB_Name)

        self.fields = [
            "anonymous", "code", "country", "host", "port", "type", "date", "status"
        ]
        self.db_proxy.createTable(tbl_name=self.tbl_name, fields=self.fields)


    def get_proxies(self):
        # Retrieve only anonymous 'uk' or 'us' proxies
        proxies = self.collector.get_proxies({'anonymous': True})
        for proxy in proxies:
            result_row = {
                'anonymous': proxy.anonymous,
                'code': proxy.code,
                'country': proxy.country,
                'host': proxy.host,
                'port': proxy.port,
                'type': proxy.type,
                'date': get_now_str()
            }
            self.db_proxy.insert_row(tbl_name=self.tbl_name, result_row=result_row)
            print(result_row)


if __name__ == '__main__':
    app = ScrapeFreeProxies()
    app.get_proxies()