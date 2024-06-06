import scrapy


class RSF_Spider(scrapy.Spider):
    name = "RSF"
    start_urls = ["https://russwimming.ru/federations/"]

    def parse(self, response):
        region_links = response.css("ul.regions_list a")
        yield from response.follow_all(region_links, self.parse_region)

    def parse_region(self, response):
        counter = 0
        while response.css("td.table_row") is not None:
            counter += 1

        yield {
            "region": response.css("div.block_header::text").get(),
            "number-of-schools": counter
        }
