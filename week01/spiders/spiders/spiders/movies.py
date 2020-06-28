import re

import scrapy
from scrapy.selector import Selector
from ..items import MaoYanMovieItem


class MoviesSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']
    base_url = "https://maoyan.com"

    def start_requests(self):
        uri = "/films?showType=3"
        yield scrapy.Request(url=self.base_url+uri, callback=self.parse)

    def parse(self, response):
        Cookie = response.headers.getlist('Set-Cookie')
        print(Cookie)

        movies = Selector(response).xpath('//div[@class="movie-item film-channel"]')[:10]
        for movie in movies:
            uri = movie.xpath("./a/@href").extract_first()
            print(uri)
            yield scrapy.Request(url=self.base_url+uri, callback=self.parse_details)


    def parse_details(self, response):
        item = MaoYanMovieItem()
        movie_name = Selector(response).xpath("//h1/text()").extract_first()
        movie_type = Selector(response).xpath("//div[@class='movie-brief-container']//li[1]//a/text()").extract()
        movie_date = re.search("\d{4}-\d{2}-\d{2}", Selector(response).xpath("//div[@class='movie-brief-container']//li[3]/text()").extract_first()).group()
        print("-"*50)
        print(f"movie_name = {movie_name}")
        print(f"movie_type = {movie_type}")
        print(f"movie_date = {movie_date}")
        print("-"*50)
        item["movie_name"] = movie_name
        item["movie_type"] = movie_type
        item["movie_date"] = movie_date
        yield item
