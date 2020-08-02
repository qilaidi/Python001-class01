import requests, re
from bs4 import BeautifulSoup as bs

from week06.DBOperator import DBOperation


def get_page_content():
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    header = {'user-agent':user_agent}
    url = 'https://movie.douban.com/subject/34961898/comments?status=P'
    response = requests.get(url, headers=header)
    soup = bs(response.text, "html.parser")
    return soup

def save_to_db(soup):
    comments = soup.find(id="comments")
    stars_map = {
        "力荐": 5,
        "推荐": 4,
        "还行": 3,
        "较差": 2,
        "很差": 1
    }
    for item in comments.find_all('div', attrs={'class': 'comment-item'}):
        short = item.find('span', attrs={'class': 'short'}).text
        star = item.find('span', attrs={'class': 'comment-info'}).find(class_=re.compile('rating'))['title']
        print(short, star)
        db = DBOperation()
        sql = f"""INSERT INTO movie_hamilton (shorts, stars) VALUES ('{short}', '{stars_map[star]}');"""
        db.run(sql)

if __name__ == '__main__':
    save_to_db(get_page_content())