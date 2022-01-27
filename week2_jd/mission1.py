import requests
from bs4 import BeautifulSoup


def get_movieRanking():
    url = r'https://movie.naver.com/movie/sdb/rank/rmovie.naver'
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')

    table = soup.find('table', {'class': 'list_ranking'}).find('tbody')

    rank = 1
    for content in table:
        try:
            movie = content.find('td', {'class': 'title'}).text.strip()
            print(f'{rank}위 : {movie}')
            rank += 1
        except Exception:
            continue


get_movieRanking()
