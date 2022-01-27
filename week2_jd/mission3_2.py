import requests
from bs4 import BeautifulSoup

form_data = {
    'start': 1
}
url = r'https://eclass.kpu.ac.kr/ilos/st/main/course_ing_list.acl'

for i in range(1, 6):
    req = requests.post(url, data=form_data)
    soup = BeautifulSoup(req.text, 'html.parser')

    tbody = soup.find('tbody')
    for content in tbody:
        try:
            sub_prof = content.find('td', {'class': 'left'}).text
            audit_yn = content.find_all('td', {'class': 'name'})[1].text
            print(f'과목/교수 : {sub_prof}  |  청강 가능 여부 : {audit_yn}')
        except Exception:
            continue

    form_data['start'] += 10
