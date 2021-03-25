import re
import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
resp = requests.get(url)
html_src = resp.text

soup = BeautifulSoup(html_src, 'html.parser')
print(type(soup))
print("\n")

print(soup.head)
print('\n')
print(soup.body)
print('\n')

print('title 태그 요소: ', soup.title)
print('title 태그 이름: ', soup.title.name)
print('title 태그 문자열: ', soup.title.string)

# image
first_img = soup.find(name = 'img')
print(first_img)
print("\n")

target_img = soup.find(name = 'img', attrs =  {'alt':'Seoul-Metro-2004-20070722.jpg'})
print("HTML 요소: ", target_img)

target_img_src = target_img.get('src')
print("이미지 파일 경로: ", target_img_src)

target_img_resp = requests.get('http:' + target_img_src)
out_file_path = "../../dataset/download_image.jpg"

# 이미지 저장하기
with open(out_file_path, 'wb') as out_file:
  out_file.write(target_img_resp.content)
  print("이미지 저장 완료")
  
# 하이퍼링크 
links = soup.find_all("a")
print("하이퍼링크의 개수: ", len(links))
print("첫 3개의 원소: ", links[:3])

wiki_links = soup.find_all(name = "a", href=re.compile("/wiki/"), limit= 3)
print("/wiki/ 문자열이 포함된 하이퍼링크: ", wiki_links)

external_links = soup.find_all(name = "a", attrs={"class": "external text"}, limit = 3)
print("class 속성으로 추출한 하이퍼링크: ", external_links)

# css selector 
subway_image = soup.select("#mw-content-text > div > table:nth-child(3) > \
                           tbody > tr:nth-child(2) > td > a > img")
print(subway_image)

subway_image2 = soup.select("tr > td > a > img")

external_links = soup.select('a[class="external text"]')
print(external_links[:3])

id_selector = soup.select('#siteNotice')
print(id_selector)

id_selector2 = soup.select('div#siteNotice')
print(id_selector2)

id_selector3 = soup.select('p#siteNotice')
print(id_selector3)

class_selector4 = soup.select('.mw-headline')
print(class_selector)

class_selector2 = soup.select('span.mw-headline')
print(class_selector2)