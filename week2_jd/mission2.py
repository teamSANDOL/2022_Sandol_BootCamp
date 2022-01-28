import requests
from bs4 import BeautifulSoup
import re


class MovieInformation:
    def __init__(self):
        self.url = r'https://movie.naver.com/movie/sdb/rank/rmovie.naver'

    # 영화 개요에 있는 <span> 태그 내에 ", "를 제거하기 위함
    def no_space(self, text):
        #text1 = re.sub('&nbsp;|\n|\t|\r', '', text)
        text1 = re.sub('\t|\r|\n', '', text)
        return text1

    # 1~50위 영화 링크 리스트를 받아옴
    def get_movieLink(self) -> list:
        req = requests.get(self.url)
        soup = BeautifulSoup(req.text, 'html.parser')

        table = soup.find('table', {'class': 'list_ranking'}).find('tbody')

        movie_link = []
        origin_url = r'https://movie.naver.com'

        for content in table:
            try:
                movie_link.append(origin_url + content.find(
                    'td', {'class': 'title'}).find('a')['href'])
            except Exception:
                continue

        return movie_link

    # 각 영화 정보 출력
    def print_movieInfo(self):

        movie_link = self.get_movieLink()
        for mv_link in movie_link:

            req = requests.get(mv_link)
            soup = BeautifulSoup(req.text, 'html.parser')

            title = soup.find('div', {'class': 'mv_info'}).find(
                'a').text.strip()

            info_spec = soup.find('dl', {'class': 'info_spec'}).find_all('dd')

            # 개요 태그
            overview = info_spec[0].find_all('span')
            # 감독
            director = info_spec[1].find('a').text

            # 개요 (장르/국가/상영시간/개봉일자)
            overview_list = []
            for ov in overview:
                overview_list.append(self.no_space(ov.text).strip())

            # 장르
            genre = overview_list[0]

            # 개봉일자가 없는 영화가 존재하므로 예외처리
            try:
                date = overview_list[3].split(' ')[0]
            except Exception:
                date = '-'

            print('-----------------------')
            print(f'\t{title}\n'
                  f'장르 : {genre}\n'
                  f'개봉일자 : {date}\n'
                  f'감독 : {director}')


if __name__ == "__main__":
    MovieInformation().print_movieInfo()
