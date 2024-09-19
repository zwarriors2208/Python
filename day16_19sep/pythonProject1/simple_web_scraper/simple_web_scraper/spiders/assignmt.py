import scrapy
class BooksSpider(scrapy.Spider):
    name='assignment'
    start_urls=['https://books.toscrape.com/']
    def parse(self,response):
        #Extract the h1 title of the page

        #Print the page title for debugging purposes

        # Extract book information
        for book in response.css('article.product_pod'):

            url=book.css('h3 a::attr(href)').get()
            # Yield book data along with page title
            yield {

                'url':response.urljoin(url),
            }

        #
        next_page=response.css('a::attr(href)').getall()
        if next_page is not None:
            # Join the next page URL with the base URL
            next_page_url=response.urljoin(next_page)
            yield scrapy.Request(url=next_page_url, callback=self.parse)

