import scrapy
class BooksSpider(scrapy.Spider):
    name='singlePageSpider'
    start_urls=['https://books.toscrape.com/catalogue/category/books/mystery_3/index.html']
    def parse(self,response):
        #Extract the h1 title of the page
        page_title=response.css('h1::text').get()
        #Print the page title for debugging purposes
        print(f'Page Title: {page_title}')
        # Extract book information
        for book in response.css('article.product_pod'):
            title=book.css('h3 a::attr(title)').get()
            url=book.css('h3 a::attr(href)').get()
            # Yield book data along with page title
            yield {
                'page_title':page_title, #Add the page title to each
                'title': title,
                'url':response.urljoin(url),
            }
