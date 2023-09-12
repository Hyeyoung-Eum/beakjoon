from bs4 import BeautifulSoup
import requests

base_url = "https://m.search.naver.com/search.naver?where=m_view&sm=tab_jum&query="
keyword = input("검색어를 입력하세요 : ")
search_url = base_url + keyword

r = requests.get(search_url) #url에 대해 서버에 요청하고 응답을 r에 저장, r.text가 html임
# print(r.text[:500]) #500자까지 테스트

soup = BeautifulSoup(r.text, "html.parser")
items = soup.select(".api_txt_lines.total_tit") #html내에 클래스명이 api_txt_lines total_tit 였는데, class는 . id는 #을 찍어줌
for e, item in enumerate(items, 1):
    print(f"{e} : {item.text}")

# #ssl 오류 처리 방지
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context
