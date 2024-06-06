import scrapy
import re


class OldPoolsSpider(scrapy.Spider):
    name = "pools-2019"
    start_urls = ["https://old.russwimming.ru/regional_federations"]

    def parse(self, response):
        region_links = response.css("ul.fo li a::attr(href)")
        yield from response.follow_all(region_links, self.parse_region)

    def parse_region(self, response):
        table = response.css(
            'table:contains("КОЛИЧЕСТВО"), table:contains("СТАТИСТИКА") tbody')
        rows = table.css('tr')
        row_2019 = rows[len(rows) - 1]

        def extract_with_re(query):
            return int(re.sub(r'[\t\n]+', '', row_2019.css('td::text')[query].get()).strip())

        yield {
            "region": response.css("h1.title::text").get(),
            "50m": extract_with_re(1),
            "25m": extract_with_re(2),
            "total": extract_with_re(3),
        }
