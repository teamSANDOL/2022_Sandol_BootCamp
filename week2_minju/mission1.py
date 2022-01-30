import requests
from bs4 import BeautifulSoup

url = "https://movie.naver.com/movie/sdb/rank/rmovie.naver"
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')
movies = soup.select('td.title > div.tit3')

rank = 1
for movie in movies:
    try:
        movie_title = movie.select_one('a')['title']
        print(str(rank) + "위 : " + movie_title)
        rank += 1
    except Exception:
        continue