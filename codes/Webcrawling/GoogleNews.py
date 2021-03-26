import requests, urllib
from bs4 import BeautifulSoup

base_url = "https://news.google.com"
search_keyword = "파이썬"
search_url = base_url + '/search?hl=ko&gl=KR&q=' + urllib.parse.quote(search_keyword)

resp = requests.get(search_url)
html_src = resp.text
soup = BeautifulSoup(html_src, 'html.parser')

# 뉴스 아이템 블록 선택하기
news_items = soup.select('div[class="xrnccd"]')

# 10개 뉴스 날짜, 시각, 제목, 기관, 텍스트 불러오기
for item in news_items[:10]:
  link = item.find('a', attrs = {'class':'VDXfz'}).get('href')
  news_link = base_url + link[1:]
  print(news_link)
  print('\n')
  
  news_title = item.find('a', attrs = {'class':'DY5T1d'}).getText()
  print(news_title)
  print('\n')

  news_content = item.find('span', attrs = {'class':'xBbh9'}).text
  print(news_content)
  print('\n')  
  
  news_agency = item.find('a', attrs = {'class':'wEwyrc AVN2gc uQIVzc Sksgp'}).text
  print(news_agency)
  print('\n')
  
  news_reporting = item.find('time', attrs = {'class':'WW6dff uQIVzc Sksgp'})
  news_reporting_datetime = news_reporting.get('datetime').split('T')
  news_reporting_date = news_reporting_datetime[0]
  news_reporting_time = news_reporting_datetime[1][:-1]
  print(news_reporting_date, news_reporting_time)
  
# 뉴스 목록 함수로 정의하기
def google_news_clipping(url, limit= 10):
  
  resp = requests.get(url)
  html_src = resp.text
  soup = BeautifulSoup(html_src, 'html.parser')
  
  news_items = soup.select('div[class="xrnccd"]')
  
  links=[]; titles=[]; contents=[]; agencies=[]; reporting_dates=[]; reporting_times=[];
  
  for item in news_items[:limit]:
    link = item.find('a', attrs = {'class':'VDXfz'}).get('href')
    news_link = base_url + link[1:]
    links.append(news_link)
    
    news_title = item.find('a', attrs = {'class':'DY5T1d'}).getText()
    titles.append(news_title)
    
    news_content = item.find('span', attrs = {'class':'xBbh9'}).text
    contents.append(news_content)
    
    news_agency = item.find('a', attrs = {'class':'wEwyrc AVN2gc uQIVzc Sksgp'}).text
    agencies.append(news_agency)
    
    news_reporting = item.find('time', attrs = {'class':'WW6dff uQIVzc Sksgp'})
    news_reporting_datetime = news_reporting.get('datetime').split('T')
    news_reporting_date = news_reporting_datetime[0]
    news_reporting_time = news_reporting_datetime[1][:-1]
    reporting_dates.append(news_reporting_date)
    reporting_times.append(news_reporting_time)
    
    result = {'link':links, 'title':titles, 'contents':contents, 'agency':agencies, \
              'date':reporting_dates, 'time': reporting_times}
  return result

news = google_news_clipping(search_url, 10)
print(news)












