import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter -')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

reservoir = soup.select('.reservoir')
for i in reservoir:
    # print(i.find('div', class_='name').get_text(), end=' ')
    # print(i.find('div', class_='volumn').get_text(), end=' ')
    print(i.find('h3').get_text(), end=' ')
    print(i.find('h5').get_text(), end=' ')
    print()
