from nturl2path import url2pathname
from bs4 import BeautifulSoup
import requests
import pandas as pd
import openpyxl

search = input("검색할 키워드를 입력해주세요: ")
page = int(input("크롤링할 페이지를 입력해주세요. ex)1(숫자만입력): "))
print("크롤링할 페이지:", page, "페이지")

if page == 1:
    page_start = 1
else:
    page_start = page + 9*(page-1)

url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=" + \
    search + "&start=" + str(page_start)
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

results = soup.findAll('a', 'news_tit')

wb = openpyxl.Workbook()
ws1 = wb.active
ws1.title = "네이버 뉴스 검색어"

title = []
number = []
num = 1
for i in results:
    title.append(i.attrs["title"])
    number.append(num)
    num += 1

title_list = {"번호": number, "제목": title}

raw_data = pd.DataFrame(title_list)  # 데이터 프레임으로 전환
raw_data.to_excel('newstitle.xlsx', sheet_name="검색어")  # 엑셀로 저장

df = pd.read_excel('newstitle.xlsx', index_col=0)

print(df)
