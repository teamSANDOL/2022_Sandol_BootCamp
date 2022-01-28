import requests
import pprint
from bs4 import BeautifulSoup
import json


# url = f'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%BD%94%EB%A1%9C%EB%82%98'
# header = {
#     'referer': 'https://www.naver.com/',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
# }
# req = requests.get(url, headers=header)
# soup = BeautifulSoup(req.text, 'html.parser')

# box = soup.find('div', {'class': 'main_tab_area'})
# inner_box = box.find('div', {'class': 'status_info'})
# inform_data = box.find('div', {'class': 'status_info'}).find('ul')


# print(f"오늘의 일일 확진자 수는 {inform_data.find('li',{'class':'info_01'}).text.strip().split(' ')[2]}명 입니다! 건강에 유의하세요")


# url = r"https://m.search.naver.com/p/csearch/content/nqapirender.nhn?where=nexearch&pkid=9005&key=diffV2API"
# html = requests.get(url).text
# data = json.loads(html)
# # pprint.pprint(data)
# # print(data['result']['data']['dailyCnt'])
# # print(data['result']['baseDate'].split(' ')[0][:-1])
# date = data['result']['baseDate'].split(' ')[0][:-1]


# print(f"{date}일까지 코로나 발생현황이에요!\n"
#       f"확진자 수는 {data['result']['data']['dailyCnt'][6]}"
#       f"전일대비 { int(data['result']['data']['dailyCnt'][6].replace(',','')) - int(data['result']['data']['dailyCnt'][5].replace(',',''))} ")


# url = r"https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%B6%80%EC%B2%9C+%EB%82%A0%EC%94%A8"
# html = requests.get(url)
# soup = BeautifulSoup(html.text, 'html.parser')

# data = soup.find('div', {'class': 'status_wrap'})

# # 온도
# temperature = data.find(
#     'div', {'class': 'temperature_text'}).find('strong').text
# # 전날 온도와 비교
# temp_info = data.find('div', {'class': 'temperature_info'}).find('p').text

# # 차트 리스트
# chart_list = []
# today_chart_list = data.find(
#     'ul', {'class': 'today_chart_list'}).find_all('li')
# for lev in today_chart_list:
#     chart_list.append(lev.text.strip())

# print(temperature)
# print(temp_info.strip().split(' ')[-1])


# print(f"오늘 부천의 날씨.\n"
#       f"오늘 날씨는 {temp_info.strip().split(' ')[-1]}이고\n"
#       f"{temperature} 이며\n"
#       f"{chart_list[0]}이고,\n{chart_list[1]}이며,\n{chart_list[2]}입니다.")


# url = r"https://eclass.kpu.ac.kr/ilos/lo/login.acl"
# session = requests.Session()
# user_info = {
#     'usr_id': '2018158026',
#     'usr_pwd': 'wjdehd3985%'
# }
# session.post(url, data=user_info)


# USER_INFO_URL = r'http://eclass.kpu.ac.kr/ilos/mp/myinfo_form.acl'


# def getInfo():
#     try:
#         html = session.get(USER_INFO_URL)
#         soup = BeautifulSoup(html.text, 'html.parser')
#         user_email = soup.find("div", {'style': 'width: 200px; float: left; overflow: hidden;'}).get_text().replace(
#             u'\xa0', u'')
#         user_name = soup.select_one("#user").text
#         user_code = (soup.find("tr", {'style': 'height: 40px; vertical-align: middle;'}).
#                      find_all("td")[1].text)[(soup.find("tr", {'style': 'height: 40px; vertical-align: middle;'}).
#                                              find_all("td")[1].text).find('(') + 1:(
#                          soup.find("tr", {'style': 'height: 40px; vertical-align: middle;'}).
#                          find_all("td")[1].text).find(')')]  # 학번

#         return user_name, user_code, user_email

#     except Exception as e:
#         return False


# if getInfo() is False:
#     print("로그인 실패")
# else:
#     print(getInfo())


notice_list = r"http://eclass.kpu.ac.kr/ilos/community/notice_list.acl"
home_url = r"https://eclass.kpu.ac.kr"

html = requests.get(notice_list)
soup = BeautifulSoup(html.text, 'html.parser')
table = soup.find('tbody')
url_list = []
for lst in table.find_all('tr'):
    title = lst.find('td', {'class': 'left'})
    url_list.append(home_url + title.find('a')['href'])

for url in url_list:
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    print(soup.select(
        "#myform > table > tbody > tr:nth-child(5) > td > div:nth-child(1)")[0].text)
