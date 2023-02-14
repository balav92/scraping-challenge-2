import scrapy
from scrapy_splash import SplashRequest

class QuotesToScrapeSpider(scrapy.Spider):
	name = 'quotes'
	
	def start_requests(self):
		yield SplashRequest(
			url='http://quotes.toscrape.com/js/',
			callback=self.parse,
		)

	def parse(self, response):
		for quote in response.css("div.quote"):

			#Used to fetch quotes detail in text format
			text = quote.css("span.text::text").extract_first()
			
			#Used to fetch author name in text format
			author = quote.css("small.author::text").extract_first()

			#Used to fetch tags details and have used extract() since there are multiple tags
			tags = quote.css("div.tags > a.tag::text").extract()

			#Yield is used to map the values for output
			yield {
			'Quote': text,
			'Author': author,
			'Tags': tags,
			}
			
		#This function is to navigate to the next page
		next_page = response.css("li.next > a::attr(href)").extract_first()
		if next_page is not None:
			yield SplashRequest(response.urljoin(next_page))
