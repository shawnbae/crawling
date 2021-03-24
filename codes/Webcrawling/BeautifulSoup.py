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
print(target_img)
