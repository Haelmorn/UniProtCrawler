import scrapy


# Enter your uniprot FASTA id's here
upfastalist = [
"Q1LCD7",
"P0AC26",
]


class UniprotSpider(scrapy.Spider):
    name = "fastaspider"
    download_timeout = 3600

    def start_requests(self):
        urls = [
            f"https://www.uniprot.org/uniprot/{fasta_id}.fasta" for fasta_id in upfastalist]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        yield {"fasta": response.xpath("//body//text()").get()}
