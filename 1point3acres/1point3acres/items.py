# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ForumItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    post_time = scrapy.Field()
    url = scrapy.Field()
    undergrad_school = scrapy.Field()
    undergrad_gpa = scrapy.Field()
    grad_school = scrapy.Field()
    grad_gpa = scrapy.Field()
    toefl = scrapy.Field()
    gre = scrapy.Field()
    submit_time = scrapy.Field()
    content = scrapy.Field()











