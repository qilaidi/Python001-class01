# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import os
import sys

from spiders.DBOperator import DBOperation as db

print("当前的工作目录：" + os.getcwd())
print("python搜索模块的路径集合：", sys.path)


class SpidersPipeline:
    def process_item(self, item, spider):
        movie_name = item["movie_name"]
        movie_type = item["movie_type"]
        movie_date = item["movie_date"]
        movie_type_str = "/".join(movie_type)
        sql = f"""INSERT INTO movies (name, type, release_date) VALUES ('{movie_name}', '{movie_type_str}', '{movie_date}');"""
        db.run(sql)
        return item

