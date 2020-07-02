# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import numpy as np
import pandas as pd


class WebscrapingPipeline(object):
    def __init__(self):
        self.data = []

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        self.data.append(dict(item))
        return item

    def close_spider(self, spider):
        df = pd.DataFrame(self.data)
        order = []
        df = df.reindex_axis(order, axis=1)
        df.to_excel('/Users/francis/Desktop/forum_data.xlsx', index=False)


