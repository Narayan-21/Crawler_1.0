import scrapy

class postSpider(scrapy.Spider):
    name = "posts"
    start_urls = [
        "https://www.zyte.com/blog/"
    ]

    def parse(self, response):
            for post in response.css('div.oxy-posts'):
                yield {
                    'title': post.css('.oxy-post-wrap div a::text').get(),
                    'date': post.css('.oxy-post-image div.oxy-post-image-date-overlay::text').get(),
                    'author': post.css('.oxy-post-wrap div.oxy-post-meta-author::text').get()
                }
            next_page = response.css('div.oxy-easy-posts-pages a.next.page-numbers::attr(href)').get()
            if next_page is not None:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse)