import scrapy


# Enter embl id here
embl_list = [
    "AAB02268.1",
    "CAB15355.2",
    "AAL19452.1",
]


class UniprotSpider(scrapy.Spider):
    name = "emblspider"
    download_timeout = 3600

    def start_requests(self):
        urls = [f"https://www.ebi.ac.uk/ena/data/view/{embl_id}&display=fasta" for embl_id in embl_list]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        yield {"Nuc_sequence": response.xpath("//body//text()").get()}
