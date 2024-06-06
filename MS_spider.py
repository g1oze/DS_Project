import scrapy


class MS_Spider(scrapy.Spider):
    name = "MS"
    start_urls = ["https://msrfinfo.ru/sports/64"]

    def parse(self, response):
        table = response.css("div.table-responsive.mb-3 tbody")
        rows = table.css("tr")
        for row in rows:
            yield {
                "region": row.css("a::text").get(),
                "ms_quant": int(row.css("td")[1].css("::text").get())
            }
