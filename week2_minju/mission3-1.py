import requests
from bs4 import BeautifulSoup

url = "http://eclass.kpu.ac.kr/ilos/st/main/course_ing_list.acl"
        
def get_list():
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
       
    # 교육진행과정 목록
    list = soup.select("tbody > tr")
    
    for subject in list:
        # 과목 / 교수
        sub_professor = subject.find("td", "left").text
        # 청강여부
        onclass = subject.select_one("td:nth-child(4)").text
        print ("-" * 50)
        print (f"과목 및 교수: {sub_professor}")
        print (f"청강 가능 여부: {onclass}")
        
get_list()