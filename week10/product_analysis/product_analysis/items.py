# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

# 创建表
# mysql> CREATE TABLE product
#     -> (
#     -> id BIGINT(20) PRIMARY KEY NOT NULL AUTO_INCREMENT,
#     -> product_name VARCHAR(128) COMMENT '产品名',
#     -> user_name VARCHAR(128) COMMENT '用户名',
#     -> user_comment VARCHAR(768) COMMENT '用户评论',
#     -> create_time DATETIME COMMENT '入库时间'
#     -> ) DEFAULT CHARSET=utf8mb4;

import scrapy


class ProductAnalysisItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    product_name = scrapy.Field()
    user_name = scrapy.Field()
    user_comment = scrapy.Field()
