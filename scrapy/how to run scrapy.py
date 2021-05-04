'''
scrapy crawl itunes -s LOG_ENABLED=False
'''

if __name__ == '__main__':
    from scrapy.utils.project import get_project_settings
    from scrapy.crawler import CrawlerProcess, CrawlerRunner

    settings = get_project_settings()
    process = CrawlerProcess(settings)
    process.crawl(ItunesSpider)
    process.start()
