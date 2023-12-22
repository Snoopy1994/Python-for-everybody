import requests
from bs4 import BeautifulSoup

url = 'https://water.taiwanstat.com/'
web = requests.get(url)
# soup = BeautifulSoup(web.text, "html.parser")  # 使用 html.parser 解析器
soup = BeautifulSoup(web.text, "html5lib")       # 使用 html5lib 解析器
title = soup.title
print(title)
a = soup.a
print(a)
find_a = soup.find_all('a')
# print(find_a)
# for link in find_a:
# print(link.get('href'))

for tag in soup.find_all(True):
    print(tag.name)
