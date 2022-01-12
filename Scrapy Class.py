import scrapy

class PracticeSpider(scrapy.Spider):
     name='practice'

     start_urls = ['https://www.olx.com.pk/mobile-phones_c1453',]


     def parse(self, response):
         title = response.xpath("//div[@class='_41d2b9f3']/a/@href")
         for i in title:
            myurl = "https://www.olx.com.pk" + i.extract()
            yield scrapy.Request(url=myurl, callback=self.parse_product)

     def parse_product(self, response):
        title = response.xpath("//h1[@class='a38b8112']/text()").get()
        price = response.xpath("//span[@class='_56dab877']/text()").get()

        yield{
            'Title' : title,
            'Price' : price
        }
