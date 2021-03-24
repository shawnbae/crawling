import requests

url = "https://www.python.org/"
resp = requests.get(url)
print(resp) # 성

url2 = "https://www.python.org/1"
resp2 = requests.get(url2)
print(resp2) # 실패

# 페이지의 text 출력하기
html = resp.text
print(html)

# robots.txt 확인하기
urls = ["https://www.naver.com/", "https://www.python.org/"]
filename = "robots.txt"

for url in urls:
  file_path = url + filename
  print(file_path)
  resp = requests.get(file_path)
  print(resp.text)
  print("\n")