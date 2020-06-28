# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class SpidersPipeline:
    def process_item(self, item, spider):
        movie_name = item["movie_name"]
        movie_type = item["movie_type"]
        movie_date = item["movie_date"]
        with open("./maoyan_movie.csv", "a+", encoding="utf-8") as movie_file:
            movie_type_str = "/".join(movie_type)
            movie_file.write(f"类型：{movie_type_str}\t片名：《{movie_name}》\t 上映日期：{movie_date}\n")
        return item
