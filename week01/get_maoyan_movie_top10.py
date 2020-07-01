# -*- encoding:utf-8 -*-
# maoyan前 10 个电影名称、电影类型和上映时间
import requests, re
from bs4 import BeautifulSoup as bs
import pandas as pd


def get_page_content(url):
    user_agent = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3"
    cookie = """__mta=213278251.1593049911044.1593049911044.1593054624349.2; 
    _lxsdk_cuid=16875b6977fc8-086c7fc103e92b-10336653-13c680-16875b697803d; uuid_n_v=v1; 
    uuid=6E0CD8B0B68611EA909D9FF2C00A78C340B6EBDA9F494CD8BB5F998EE90EA231; 
    _csrf=0f3467195309731aed35390fb3c08afc4cbd26d1307822a8b3bcec889fb88a78; 
    mojo-uuid=6a4490e41a669a78f6e37fc37c9166ca; 
    _lxsdk=6E0CD8B0B68611EA909D9FF2C00A78C340B6EBDA9F494CD8BB5F998EE90EA231; mojo-session-id={
    "id":"11c3d8dda668ae87ce796bbb71286b5d","time":1593078166684}; mojo-trace-id=2; 
    Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593049911,1593078172; 
    Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593078172; __mta=213278251.1593049911044.1593054624349.1593078171692.3; 
    _lxsdk_s=172eadba0e8-18c-267-0ca%7C%7C5 """  # 换行
    headers = {"user-agent": user_agent, "cookie": cookie}
    response = requests.get(url, headers=headers)
    soup = bs(response.text, "html.parser")
    return soup


# 获取前10个电影的名称、电影类型和上映时间
base_url = "https://maoyan.com"
uri = "/films?showType=3"
soup = get_page_content(base_url + uri)
items = soup.find_all(attrs={"class": "movie-item film-channel"})
soup = get_page_content(base_url + items[i].find('a')['href'])  # 将请求挪到循环外
contents = []

for i in range(10):
    movie_name = soup.find('h1').text
    print(f"电影名称：{movie_name}")
    movie_type = soup.find(attrs={"class": "movie-brief-container"}).find_all('li')[0].text.strip("\n").replace("\n",
                                                                                                                "/")
    print(f"电影类型：{movie_type}")
    movie_date = re.search("\d{4}-\d{2}-\d{2}",
                           soup.find(attrs={"class": "movie-brief-container"}).find_all('li')[2].text).group()
    print(f"上映时间：{movie_date}")
    contents.append((movie_name, movie_type, movie_date))
# 保存

pd.DataFrame(data=contents).to_csv("./movie.csv", encoding='utf-8', index=False, header=False)
