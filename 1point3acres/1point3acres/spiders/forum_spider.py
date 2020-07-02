"""
一亩三分地论坛录取数据爬取
"""
import scrapy
from webscraping.items import ForumItem
from selenium import webdriver
driver = webdriver.PhantomJS()

class ForumSpider(scrapy.Spider):
    name = 'forum_spider'
    start_urls = ['http://www.1point3acres.com/bbs/forum-82-1.html', ]
    cookies = {
        'sc_is_visitor_unique': 'rx4760979.1523002139.8B27B8B423C44F7391FAE0E1E64FBA4B.55.50.48.46.44.41.36.30.21-4806808.1523000009.23.20.19.18.18.18.15.14.10',
        '4Oaf_61d6_lastact': '1523002378%09forum.php%09misc',
        '4Oaf_61d6_lip': '80.211.209.160%2C1523002368',
        '4Oaf_61d6_sid': 'UlY6rR',
        '4Oaf_61d6_noticeTitle': '1',
        '4Oaf_61d6_forum_lastvisit': 'D_82_1523002137',
        '4Oaf_61d6_lastcheckfeed': '342897%7C1523002138',
        '4Oaf_61d6_sendmail': '1',
        '4Oaf_61d6_smile': '4D1',
        '__utma': '142000562.755013681.1489155651.1522986460.1522997706.56',
        '__utmb': '142000562.34.10.1522997706',
        '__utmc': '142000562',
        '__utmz': '142000562.1522986460.55.47.utmcsr=baidu|utmccn=(organic)|utmcmd=organic',
        '4Oaf_61d6_viewid': 'tid_386170',
        '4Oaf_61d6_visitedfid': '82D27',
        '4Oaf_61d6_groupviewed': '156',
        '4Oaf_61d6_home_diymode': '1',
        '_ga': 'GA1.2.755013681.1489155651',
        '_gid': 'GA1.2.323093966.1522997564',
        '4Oaf_61d6_atarget': '1',
        '4Oaf_61d6_nofavfid': '1',
        '4Oaf_61d6_auth': 'cca5FIzyQIJIgYjyW8gin%2BGK8J%2FJhVNk1H1RMr7dkRNrjb99KT0hUu%2BL%2BFhjogExcJTLAsMfQQIMsCRRf4He8FbRScI',
        '4Oaf_61d6_ulastactivity': 'f4f860MAZgz3malsoEMUg4ugAP%2BWWS0Oj4ato9nW1AcBIWfvV1K7',
        '4Oaf_61d6_lastvisit': '1522996261',
        '4Oaf_61d6_saltkey': 'yf8vEAg5',
        'sc_is_visitor_unique': 'rx4760979.1494162944.73730E2750F84F71E07A1B4670DE6DB5.4.4.4.4.4.4.4.3.2',
    }

    def parse(self, response):
        posts = response.xpath("//tbody[contains(@id, 'normalthread')]//a[@class='s xst']/@href").extract()
        for post in posts:
            yield scrapy.Request(url=post, cookies=self.cookies, callback=self.parse_detail)

        next_page = response.xpath("//a[contains(text(), '下一页']/@href").extract_first()
        if next_page:
            yield scrapy.Request(url=next_page, cookies=self.cookies, callback=self.parse)

    def parse_detail(self, response):
        driver.get(response.url)
        driver.add_cookie(self.cookies)
        driver.refresh()
        hidden = driver.find_elements_by_link_text('点击查看')
        if hidden:
            for hidden_items in hidden:
                hidden_items.click()
        item = ForumItem()
        item['title'] = driver.find_elements_by_xpath("//span[@id='thread_subject']").text
        item['author'] = driver.find_elements_by_xpath("//div[@class='authi']/a[@class='xi2']").text
        item['post_time'] = driver.find_elements_by_xpath("//em[contains(@id, 'authorposton')]").text
        item['url'] = response.url
        metrics = ''.join(driver.find_elements_by_xpath("//div[@class='pcb']").text)
        item['undergrad_school'] = ''