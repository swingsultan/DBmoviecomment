# -*- coding:utf-8 -*-
import scrapy
from endpro.items import  MovieItem
from faker import Factory
from urllib.parse import urlparse
f = Factory.create()


class NewMovieSpider(scrapy.Spider):
    name = 'newmovie'
    start_urls=['https://movie.douban.com']
    
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Connection': 'keep-alive',
        'Host': 'movie.douban.com',
        'User-Agent': f.user_agent()
    }
    
    
    def start_requests(self):
        return [scrapy.Request(url='https://movie.douban.com/',
                               headers=self.headers,
                               meta={'cookiejar': 1},
                               callback=self.parse2)]
    
    
    
                                                


    def parse2(self,response):
        print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
        
        print(response.url)
        

        

        

        count=0


        for item in response.xpath('//*[@id="screening"]/div[2]/ul//li'):
            
            newmovie=MovieItem()
            newmovie['moname']=item.xpath('@data-title').extract()
            if newmovie['moname']:
                count +=1
                newmovie['pubtime']=item.xpath('@data-release').extract()
                newmovie['totscore']=item.xpath('@data-rate').extract()
                yield newmovie

        print(count)


