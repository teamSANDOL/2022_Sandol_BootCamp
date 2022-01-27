import requests
from bs4 import BeautifulSoup
import re

url = r'https://movie.naver.com/movie/sdb/rank/rmovie.naver'
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')

table = soup.find('table', {'class': 'list_ranking'}).find('tbody')

# print(table.find('img')['alt']) # 순위
# print(table.find('td', {'class': 'title'}).text.strip()) # 영화 제목

movie_link = []
origin_url = r'https://movie.naver.com'


def no_space(text):
    text1 = re.sub('&nbsp;|\n|\t|\r', '', text)
    return text1


for content in table:
    try:
        movie_link.append(origin_url + content.find(
            'td', {'class': 'title'}).find('a')['href'])
    except Exception:
        continue

for mv_link in movie_link:

    req = requests.get(mv_link)
    soup = BeautifulSoup(req.text, 'html.parser')

    title = soup.find('div', {'class': 'mv_info'}).find('a').text.strip()

    info_spec = soup.find('dl', {'class': 'info_spec'}).find_all('dd')

    overview_list = []
    overview = info_spec[0].find_all('span')
    director = info_spec[1].find('a').text

    for ov in overview:
        overview_list.append(no_space(ov.text).strip())

    genre = overview_list[0]
    try:
        date = overview_list[3].split(' ')[0]
    except Exception:
        date = '-'
    print('-----------------------')
    print(f'\t{title}\n'
          f'장르 : {genre}\n'
          f'개봉일자 : {date}\n'
          f'감독 : {director}')
