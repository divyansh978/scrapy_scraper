import scrapy


class BusinessProfilesSpider(scrapy.Spider):
    name = "business_profiles"
    allowed_domains = ["xxx"]
    start_urls = ["https://xxx"]

    def parse(self, response):
        pass
