# -*- encoding: utf-8 -*-
# Create by zq
# Create on 2020/9/1
import pandas as pd
import numpy as np
from snownlp import SnowNLP
from sqlalchemy import create_engine
from product_analysis import settings


class ProductDataHandler:
    def __init__(self):
        host = settings.MYSQL_HOST
        port = settings.MYSQL_PORT
        username = settings.MYSQL_USERNAME
        password = settings.MYSQL_PASSWORD
        db = settings.MYSQL_DB

        self.conn = create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{db}')
        sql = 'SELECT * FROM product;'

        self.data = pd.read_sql(sql, self.conn)

    def handle_duplicate(self, data):
        """删除重复值"""
        # handle empty or blank string
        data['user_comment'] = data['user_comment'].str.strip()
        data.drop(data[data['user_comment'] == ''].index, inplace=True)
        # drop duplicate
        return data.drop_duplicates(subset=['product_name', 'user_name', 'user_comment'], keep='last')

    def handle_missing(self, data):
        """删除评论为空的，填充用户为空"""

        # data['isempty'] = data['user_comment'].apply(lambda x: np.nan if x.strip() == '' else 0)
        # print(data)
        return data.dropna(subset=['user_comment']).fillna(value={'user_name': '空用户'})

    def just_do_it(self):
        cleaned_data = self.handle_duplicate(self.data)
        cleaned_data = self.handle_missing(cleaned_data)
        cleaned_data = self.sentiment_analysis(cleaned_data)
        self.save_to_db(cleaned_data)

    def sentiment_analysis(self, data):
        data['sentiment'] = data['user_comment'].apply(lambda x: SnowNLP(x).sentiments)
        return data

    def save_to_db(self, data):
        with self.conn.begin() as connection:
            data.to_sql('product_cleaned', con=connection, if_exists='replace', index=False, index_label='id')
            connection.execute("""ALTER TABLE `product_cleaned` ADD PRIMARY KEY (`id`);""")


if __name__ == '__main__':
    test = ProductDataHandler()
    test.just_do_it()
    print("Data cleaning & analysis sentiments Done!")