#! /bin/sh
# cron_smzdm.sh

source /etc/profile
cd /Users/Kernel/Documents/Documents_cc/ZhangQian/Study/Python/code/mycode/Python001-class01/venv/bin/
source activate
cd /Users/Kernel/Documents/Documents_cc/ZhangQian/Study/Python/code/mycode/Python001-class01/week10/product_analysis
PATH=$PATH:/usr/local/bin
export PATH
scrapy crawl smzdm
python3.7 product_data_clean.py