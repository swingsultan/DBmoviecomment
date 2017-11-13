# -*- coding:utf-8 -*-
import scrapy
from endpro.items import  MovieItem
from endpro.items import CommenterInfoItem
from faker import Factory
import urllib.request
import urllib
import re
from scrapy.conf import settings
from urllib.parse import urlparse
f = Factory.create()


class CommentSpider(scrapy.Spider):
    name = 'moviecomment'
    allowed_domains = ['douban.com','accounts.douban.com']
    start_urls = [
        'https://movie.douban.com/'
    ]

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'Host': 'accounts.douban.com',
        #'Referer':'https://movie.douban.com/',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent': f.user_agent()
        
    }

    cookies = settings['COOKIE']

    
    
    
    def start_requests(self):

        

        return [scrapy.Request(url='https://accounts.douban.com/login',
                               headers=self.headers,
                               #cookies=self.cookies,
                               
                               meta={'cookiejar': 1,
                               'dont_redirect': True,  # 禁止网页重定向
                               'handle_httpstatus_list': [301, 302]  # 对哪些异常返回进行处理
                               },
                               callback=self.post_login)]


    def post_login(self, response):
        print ('Preparing login====', response.url)
        # s = 'index_nav'
        #html = urllib.request.urlopen(response.url).read()
        #html=response.body
        # print 'htnl:', html
        # 验证码图片地址
        #imgurl = re.search('<img id="captcha_image" src="(.+?)" alt="captcha" class="captcha_image"/>', html)
        imgurl=False
        if imgurl:
            url = imgurl.group(1)
            # 将图片保存至同目录下
            res = urllib.urlretrieve(url, 'v.jpg')
            # 获取captcha-id参数
            captcha = re.search('<input type="hidden" name="captcha-id" value="(.+?)"/>', html)
            if captcha:
                vcode = raw_input('请输入图片上的验证码：')
                return [scrapy.FormRequest.from_response(response,
                                                  meta={'cookiejar': response.meta['cookiejar']},
                                                  formdata={
                                                      'source': 'index_nav',
                                                      # 'source': s,
                                                      'form_email': '15000776293@163.com',
                                                      'form_password': 'lsypcdb913',
                                                      'captcha-solution': vcode,
                                                      'captcha-id': captcha.group(1),
                                                      'user_login': '登录'
                                                  },
                                                  callback=self.after_login,
                                                  dont_filter=True)
                        ]
        return [scrapy.FormRequest.from_response(response,
                                          meta={'cookiejar': response.meta['cookiejar']},
                                          formdata={
                                              'source': 'index_nav',
                                              # 'source': s,
                                              'form_email': '15000776293@163.com',
                                              'form_password': '319bdcpysl'
                                              },
                                          headers=self.headers,
                                          callback=self.after_login
                                          )
                ]



    def after_login(self, response):
        print (response.status)
        self.headers['Host'] = "movie.douban.com"
        return scrapy.Request(url='https://movie.douban.com/',
                              meta={'cookiejar': response.meta['cookiejar']},
                              headers=self.headers,
                              callback=self.parse1)

    def parse1(self,response):
        print(response.status)
        print(response.url)
        print(response.body[:2000])

        i=0
        #self.headers['Host']='www.douban.com'

        #cookie={'ll': '"108258"', 'bid': 'PAYxOcHJD2Y', '__yadk_uid': '6CWTjVDSR8sJCY7sFD1tpqkq7lIvbnJP', 'ct': 'y', 'ps': 'y', 'ue': '"15000776293@163.com"', '_pk_ref.100001.4cf6': '%5B%22%22%2C%22%22%2C1506746858%2C%22https%3A%2F%2Fwww.douban.com%2Faccounts%2Flogin%3Fsource%3Dmovie%22%5D', 'as': '"https://movie.douban.com/"', 'push_noty_num': '0', 'push_doumail_num': '0', 'ap': '1', '_pk_id.100001.4cf6': '432d15288c6875f3.1500790453.113.1506747366.1506702572.', '__utma': '223695111.763107274.1500790445.1506701062.1506746858.112', '__utmc': '223695111', '__utmz': '223695111.1506746858.112.29.utmcsr', '__utmv': '30149280.16670', '_vwo_uuid_v2': '5E9A079D9148CE0FBA3A34BF6005CAE8|3cfe376ac1c885dd5b1b7655de713b22'}
        


        for item in  response.xpath('//*[@id="screening"]/div[2]/ul/li/ul/li[2]/a'):
            full_url = item.xpath('@href').extract_first()
            
            i +=1
            
            yield scrapy.Request(full_url,headers=self.headers,callback=self.parse2)
        print('&&&&&&&&&热门电影 %f 部$$$$$$$$$$$$$$$$$$'%i)

    def parse2(self,response):
        print(response.status)
        print(response.url)
        
        commentpage=response.xpath('//*[@id="comments-section"]/div[1]/h2/span/a/@href').extract_first()
        
        print('********************************')
        yield scrapy.Request(commentpage,headers=self.headers,callback=self.parse3)


    pagecount=1

    def parse3(self,response):
        print(response.status)
        print(response.url)
        
        for item in response.xpath('//*[@id="comments"]/div'):
            
            
            
            commentinfo=CommenterInfoItem()
            commentinfo['commenter_movie']=response.xpath('//*[@id="content"]/h1/text()').extract_first()
            commentinfo['commenter_name']=item.xpath('./div[2]/h3/span[2]/a/text()').extract_first()
            commentinfo['commenter_star']=item.xpath('div[2]/h3/span[2]/span[2]/@title').extract_first()
            commentinfo['commenter_co']=item.xpath('./div[2]/p/text()').extract_first()
            commentinfo['commenter_zan']=item.xpath('./div[2]/h3/span[1]/span/text()').extract_first()
            commentinfo['commenter_time']=item.xpath('./div[2]/h3/span[2]/span[3]/text()').extract_first()
            commentinfo['commenter_page']=item.xpath('div[2]/h3/span[2]/a/@href').extract_first()
            
            yield commentinfo

        if self.pagecount==1:
           next_page=response.xpath('//*[@id="paginator"]/a/@href').extract_first()
           if next_page is not None:
              next_page=re.sub(r'\?status=P',next_page,response.url)
              print(next_page)
              self.pagecount +=1
           else:
              print('共 %i 页短评'%self.pagecount)
              self.pagecount=1





        else:
           next_page=response.xpath('//*[@id="paginator"]/a[3]/@href').extract_first()
           if next_page is not None:
              next_page=re.sub(r'\?[\w\W]+',next_page,response.url)
              
              print(next_page)
              self.pagecount +=1
           else:
              print('共 %i 页短评'%self.pagecount)
              self.pagecount=1
           

        yield scrapy.Request(next_page,headers=self.headers,callback=self.parse3)




    def _requests_to_follow(self, response):  
        """重写加入cookiejar的更新"""  
        if not isinstance(response, HtmlResponse):  
           return  
        seen = set()  
        for n, rule in enumerate(self._rules):  
            links = [l for l in rule.link_extractor.extract_links(response) if l not in seen]  
            if links and rule.process_links:  
               links = rule.process_links(links)  
            for link in links:  
                seen.add(link)  
                r = Request(url=link.url, callback=self._response_downloaded)  
                # 下面这句是我重写的  
                r.meta.update(rule=n, link_text=link.text, cookiejar=response.meta['cookiejar'])  
                yield rule.process_request(r)  





        





    

        









