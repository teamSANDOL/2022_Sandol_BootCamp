import requests
from bs4 import BeautifulSoup

class MovieInfo:
    def __init__(self):
        self.url = "https://movie.naver.com/movie/sdb/rank/rmovie.naver"

    # 랭킹에 존재하는 영화의 링크 수집
    def get_url(self):
        req = requests.get(self.url)
        soup = BeautifulSoup(req.text, "html.parser")
        
        movies = soup.find("tbody").find_all("div", "tit3")
        origin_url = "https://movie.naver.com"
        
        url_list = []
        index = 0
        for movie in movies:
            movie_url = movie.find("a")["href"]
            url_list.insert(index, origin_url + movie_url)
            index += 1
            
        return url_list

    # 정보(제목, 장르, 개봉일자, 감독) 수집
    def get_info(self):
        
        movie_url_list = self.get_url()
        index = 0
        
        for movie_link in movie_url_list:
            
            movie_link = movie_url_list[index]
            movie_req = requests.get(movie_link)
            movie_soup = BeautifulSoup(movie_req.text, "html.parser")
            index += 1
            info_spec = movie_soup.select_one("dl.info_spec")
            
            # 제목
            title = movie_soup.find("h3", "h_movie").find("a")
            # 장르
            genre = info_spec.select_one("span > a")
            # 연도
            year = info_spec.select_one("span:nth-child(4) > a:nth-child(1)")
            # 날짜
            date = info_spec.select_one("span:nth-child(4) > a:nth-child(2)")
            # 감독
            director = info_spec.select_one("dd:nth-child(4) > p > a") 
            
            # 영화 개봉일자 없는 경우(예외)
            try :
                # 개봉일자
                open_date = year.text + date.text
            except Exception:
                open_date = "정보 없음"
            
            # 정보 출력    
            print("-" * 50)
            print(f"<'{title.text}'의 정보>\n"
                f"장르: {genre.text}\n"
                f"개봉일자: {open_date}\n"
                f"감독: {director.text}")

MovieInfo().get_info()