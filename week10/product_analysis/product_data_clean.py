# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/9/1
import pandas as pd
from sqlalchemy import create_engine

from week10.product_analysis.product_analysis import settings


class ProductDataHandler:
    def __init__(self):
        host = settings.MYSQL_HOST
        port = settings.MYSQL_PORT
        username = settings.MYSQL_USERNAME
        password = settings.MYSQL_PASSWORD
        db = settings.MYSQL_DB

        conn = create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{db}')
        sql = 'SELECT * FROM product;'

        self.data = pd.read_sql(sql, conn)

    def handle_duplicate(self, data):
        """删除重复值"""
        return data.drop_duplicates(subset=['product_name', 'user_name', 'user_comment'], keep='last')

    def handle_missing(self, data):
        """删除评论为空的，填充用户为空"""
        return data.dropna(subset=['user_comment']).fillna(value={'user_name': '空用户'})

    def just_do_it(self):
       return self.handle_missing(self.handle_duplicate(self.data))

    def save_to_db(self, data):
        pass

if __name__ == '__main__':
    test = ProductDataHandler()
    print(test.just_do_it().iloc[0])