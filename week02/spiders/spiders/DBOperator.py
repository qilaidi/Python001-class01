import traceback

import pymysql

from spiders import dbinfo

import os
import sys

from pymysql import DatabaseError

print("当前的工作目录：" + os.getcwd())
print("python搜索模块的路径集合：", sys.path)


# 创建表
# mysql> CREATE TABLE movies
#     -> (
#     -> id INT(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,
#     -> name VARCHAR(100),
#     -> type VARCHAR(200),
#     -> release_date DATE
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
    db = DBOperation()
    movie_name = '天气之子'
    movie_type = [' 爱情 ', ' 动画 ', ' 奇幻 ']
    movie_type_str = "/".join(movie_type)
    movie_date = '2019-11-01'
    sql = f"""INSERT INTO movies (name, type, release_date) VALUES ({movie_name}, '{movie_type_str}', '{movie_date}');"""
    db.run(sql)

