import traceback

import pymysql
import os
import sys

from pymysql import DatabaseError

from week06 import dbinfo

print("当前的工作目录：" + os.getcwd())
print("python搜索模块的路径集合：", sys.path)


# 创建表
# mysql> CREATE TABLE movie_hamilton
#     -> (
#     -> id INT(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,
#     -> shorts VARCHAR(500),
#     -> stars INT(4),
#     -> );

class DBOperation(object):
    @classmethod
    def run(cls, sql):
        conn = pymysql.connect(host=dbinfo.HOST,
                               port=dbinfo.PORT,
                               user=dbinfo.USERNAME,
                               password=dbinfo.PASSWORD,
                               db=dbinfo.DB)
        cur = conn.cursor()
        try:
            cur.execute(sql)
            cur.close()
            conn.commit()
            print("insert db !")
        except DatabaseError as e:
            print(e)
            conn.rollback()
        conn.close()


if __name__ == "__main__":
    stars_map = {
        "力荐": 5,
        "推荐": 4,
        "还行": 3,
        "较差": 2,
        "很差": 1
    }
    db = DBOperation()
    shorts = '如果你是个美国移民，你是民主党拥趸，我可以理解你看汉密尔顿的激动，黑人平权，支持同性恋……，用民主党政治正确重写了遍建国者故事，奥巴马夹带私货推崇它不是没有理由。但你是个土生土长的中国人，各种剧中建国历史代入感，意识形态你没有，也不用讲究与共和党不同的政治正确，实在没太理解一帮中国文艺青年在豆瓣把它狂吹成最好的音乐剧，到底为了啥'
    stars = stars_map["还行"]

    sql = f"""INSERT INTO movie_hamilton (shorts, stars) VALUES ('{shorts}', '{stars}');"""
    db.run(sql)

