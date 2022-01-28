import requests
from bs4 import BeautifulSoup


class EclassEducationStatus:
    def __init__(self):
        # 1page start = 1 / 2page start = 11 / ...
        self.form_data = {
            'start': 1
        }
        self.url = r'https://eclass.kpu.ac.kr/ilos/st/main/course_ing_list.acl'

    def print_eduStatus(self):

        # 5페이지 정보출력을 위한 반복문
        for i in range(1, 6):
            req = requests.post(self.url, data=self.form_data)
            soup = BeautifulSoup(req.text, 'html.parser')

            tbody = soup.find('tbody')
            for content in tbody:
                try:
                    # 과목/교수
                    sub_prof = content.find('td', {'class': 'left'}).text
                    # 청강 가능 여부
                    audit_yn = content.find_all(
                        'td', {'class': 'name'})[1].text

                    print(f'과목/교수 : {sub_prof}  |  청강 가능 여부 : {audit_yn}')

                except Exception:
                    continue

            # 다음 페이지를 위한 form_data 설정
            self.form_data['start'] += 10


if __name__ == "__main__":
    EclassEducationStatus().print_eduStatus()
