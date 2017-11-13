# -*- coding:utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    moname=scrapy.Field()  #电影名
    pubtime=scrapy.Field() #上映年份
    totscore=scrapy.Field()#总评分


class MovieCommentItem(scrapy.Item):
    useful_num = scrapy.Field()      # 多少人评论有用
    no_help_num = scrapy.Field()     # 多少人评论无用
    people = scrapy.Field()          # 评论者
    people_url = scrapy.Field()      # 评论者页面
    star = scrapy.Field()            # 评分
    comment = scrapy.Field()         # 评论
    title = scrapy.Field()           # 标题
    comment_page_url = scrapy.Field()# 当前页

class CommenterInfoItem(scrapy.Item):
    commenter_name=scrapy.Field()
    commenter_star=scrapy.Field()
    commenter_co=scrapy.Field()
    commenter_page=scrapy.Field()
    commenter_zan=scrapy.Field()
    commenter_movie=scrapy.Field()
    commenter_time=scrapy.Field()
    
