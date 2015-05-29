import scrapy

class HydraItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()

class HydraSpider(scrapy.Spider):
    name = "Hydra"
    allowed_domains = ["napaleagues.com"]
    start_urls = [
        "http://www.napaleagues.com/data/stats.php?playerSelected=Y&playerID=10027000&xTab=2#perform"
        ]
    