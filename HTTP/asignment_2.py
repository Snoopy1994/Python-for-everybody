import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url -')
count = int(input('Enter count -'))
position = int(input('Enter position -'))

for i in range(count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')

    s = []
    for tag in tags:
        x = tag.get('href', None)
        s.append(x)
    print(s[position-1])
    url = s[position-1]
