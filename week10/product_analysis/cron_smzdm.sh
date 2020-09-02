#! /bin/sh
# cron_smzdm.sh

source /etc/profile
cd /Users/zhangqian/Python/mycode/Python001-class01/week10/product_analysis
PATH=$PATH:/usr/local/bin
export PATH
scrapy crawl smzdm
python3.7 product_data_clean.py