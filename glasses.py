import scrapy

class GlassesSpider(scrapy.Spider):
    name = "glasses"
    allowed_domains = ["www.glassesshop.com"]
    start_urls = ["https://www.glassesshop.com/bestsellers"]

    def parse(self, response):
        products = response.xpath('//*[@id="product-lists"]/div/div/a[1]/@href').getall()

        for product in products:
            url = product
            yield response.follow(url=product, callback=self.parse_eachGlass, meta={'product_url': product})

    def parse_eachGlass(self, response):
        product_url = response.meta.get('product_url')
        name = response.xpath('//h1[@class]/text()').get()
        size = response.xpath('//div[@class="size-desc"]/span/text()').get()
        price = response.xpath('//div[@class="product-price"]/span/text()').get()
        color = response.xpath('//div[@class="productImg-list"]/div/span[2]/text()').get()
        frame = response.xpath('//div[@class="col-12 col-lg-3"]/div[2]/a/text()').get()
        shape = response.xpath('//div[@class="col-12 col-lg-3"]/div[3]/a/text()').get()
        weight = response.xpath('(//div[@class="col-12 col-lg-4"]/div[1] /text())[2]').get()
        gender = response.xpath('//div[@class="mt-4 mt-lg-0"]/a/text()').get()
        material = response.xpath('(//div/a[@class="col01 info-desc-link"])[4]/text()').get()
        
        yield {
            'Name': name.strip() if name else None,
            'Price': price.strip() if price else None,
            'Size': size.strip() if size else None,
            'Color': color.strip() if color else None,
            'Frame': frame.strip() if frame else None,
            'Shape': shape.strip() if shape else None,
            'Weight': weight.strip() if weight else None,
            'Gender': gender.strip() if gender else None,
            'Material': material.strip() if material else None,
            'Product_url': product_url
        }
