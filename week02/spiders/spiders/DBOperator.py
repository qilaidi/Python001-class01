import pymysql

from spiders import dbinfo

import os
import sys
print("当前的工作目录：" + os.getcwd())
print("python搜索模块的路径集合：", sys.path)


# 创建表
# mysql> CREATE TABLE movies
#     -> (
#     -> id INT(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,
#     -> name VARCHAR(100),
#     -> type VARCHAR(200),
#     -> release_date DATETIME
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
            print(cur.fetchall())
            cur.close()
            conn.commit()
        except:
            conn.rollback()
        conn.close()


if __name__ == "__main__":
    db = DBOperation()
    db.run()

