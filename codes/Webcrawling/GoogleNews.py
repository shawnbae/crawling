import requests, urllib
from bs4 import BeautifulSoup

base_url = "https://news.google.com"
search_keyword = "파이썬"
search_url = base_url + '/search?q=' + urllib.parse.quote(search_keyword)

resp = requests.get(search_url)
html_src = resp.text
soup = BeautifulSoup(html_src, 'html.parser')

# 뉴스 아이템 블록 선택하기
news_items = soup.select('div[class="xrnccd"]')
print(news_items[:3])

