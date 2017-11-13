# -*- coding:utf-8 -*-

import scrapy
from endpro.items import  MovieItem
from endpro.items import MovieCommentItem
import faker
from faker import Factory

f = Factory.create()


class NewMovieSpider(scrapy.Spider):
    name = 'duanpin'
    start_urls=['https://movie.douban.com/']

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Connection': 'keep-alive',
        'Host': 'movie.douban.com',
        'User-Agent': f.user_agent()
    }
    

    formdata = {
        'form_email': 'he__v5@163.com',
        'form_password': 'Glory05&',
        # 'captcha-solution': '',
        # 'captcha-id': '',
        'login': '登录',
        'redir': 'https://www.douban.com/',
        'source': 'None'
    }
    
    def start_requests(self):
        return [scrapy.Request(url='https://movie.douban.com/',
                               headers=self.headers,
                               meta={'cookiejar': 1},
                               callback=self.parse1)]
    
    

    def parse_login(self, response):
        print(response.url)
            
        return [scrapy.FormRequest.from_response(response,
                                                 formdata=self.formdata,
                                                 headers=self.headers,
                                                 meta={'cookiejar': response.meta['cookiejar']},
                                                 callback=self.after_login
                                                 )]
    def after_login(self, response):
        print (response.status)
        self.headers['Host']="www.douban.com"
        print(response.url)
        return scrapy.Request(url="https://movie.douban.com",
                              meta={'cookiejar': response.meta['cookiejar']},
                              headers=self.headers,
                              callback=self.parse2)
                                                
    
                                                
    def parse1(self,response):
        print(response.status)
        print(response.url)
        print(response.body[:2000])


        for href in  response.xpath('//*[@id="screening"]/div[2]/ul/li/ul/li[2]/a/@href'):
            full_url = response.urljoin(href.extract())
            print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
            yield scrapy.Request(full_url, callback=self.parse2)

    def parse2(self,response):
        print('***************************************')
        yield {
            'pubtime':response.xpath('//*[@id="content"]/h1/span[2]/text()').extract_(),
            'moname':response.xpath('//*[@id="content"]/h1/span[1]/text()').extract(),
            'totscore':response.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()').extract(),

        }



       
        print(count)


    def parse4(self,response):
        print(response.status)

        print(response.url)

        tiaoshu=response.xpath('//*[@id="comments-section"]/div[1]/h2/span/a/text()').extract()
        diyitiao=response.xpath('//*[@id="hot-comments"]/div[1]/div/p/text()').extract()
        diertiao=response.xpath('//*[@id="hot-comments"]/div[2]/div/p/text()').extract()

        print(tiaoshu)
        print(diyitiao)
        print(diertiao)



