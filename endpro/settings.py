# -*- coding: utf-8 -*-

# Scrapy settings for endpro project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#COOKIE={'ll':"108258", 'bid':'PAYxOcHJD2Y', '__yadk_uid':'6CWTjVDSR8sJCY7sFD1tpqkq7lIvbnJP', 'ps':'y', 'ct':'y', 'push_noty_num':'0', 'push_doumail_num':'0', '_pk_ref.100001.4cf6':'%5B%22%22%2C%22%22%2C1507188592%2C%22https%3A%2F%2Fwww.douban.com%2Faccounts%2Flogin%3Fsource%3Dmovie%22%5D', '_vwo_uuid_v2':'5E9A079D9148CE0FBA3A34BF6005CAE8|3cfe376ac1c885dd5b1b7655de713b22', '__utma':'30149280.1693210639.1500790445.1507182964.1507188592.134', '__utmb':'30149280.0.10.1507188592', '__utmc':'30149280', '__utmz':'30149280.1506746858.114.31.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/accounts/login', '__utmv':'30149280.16670', '__utma':'223695111.763107274.1500790445.1507182964.1507188592.132', '__utmb':'223695111.0.10.1507188592', '__utmc':'223695111','__utmz':'223695111.1506746858.112.29.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/accounts/login', 'ap':'1', '_pk_id.100001.4cf6':'432d15288c6875f3.1500790453.133.1507189745.1507185973.', '_pk_ses.100001.4cf6':'*', 'ue':"15000776293@163.com", 'dbcl2':"166709890:AcK6M5QihuI"}
BOT_NAME = 'endpro'

SPIDER_MODULES = ['endpro.spiders']
NEWSPIDER_MODULE = 'endpro.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'endpro (+http://www.yourdomain.com)'
from faker import Factory
f = Factory.create()
USER_AGENT = f.user_agent()

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}
DEFAULT_REQUEST_HEADERS = {
    'Host': 'book.douban.com',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'endpro.middlewares.EndproSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'endpro.middlewares.MyCustomDownloaderMiddleware': 543,
#'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware':5323,
#'endpro.middlewares.HTTPPROXY':123

#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'endpro.pipelines.EndproPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
IPPOOL=[  
    {"ipaddr":"121.232.145.247:9000"},  
    {"ipaddr":"59.62.27.129:808"},  
    {"ipaddr":"121.232.144.39:9000"},  
    {"ipaddr":"121.232.148.83:9000"},  
    {"ipaddr":"117.90.0.155:9000"},  
    {"ipaddr":"111.155.124.81:8123"},  
    {"ipaddr":"106.120.78.129:80"}  
]  