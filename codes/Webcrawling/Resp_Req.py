import requests

url = "https://www.python.org/"
resp = requests.get(url)
print(resp) # 성

url2 = "https://www.python.org/1"
resp2 = requests.get(url2)
print(resp2) # 실패