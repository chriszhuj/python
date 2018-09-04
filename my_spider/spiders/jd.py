import requests
from bs4 import BeautifulSoup

r1 = requests.get('https://mall.jd.com/index-1000001760.html')
status_code = r1.status_code
if status_code == 200:
    soup = BeautifulSoup(r1.content, 'html.parser')
links = soup.find_all('a')
for link in links:
    tmpLink = str(link)
    if tmpLink.find('item.jd.com') > -1:
        href = tmpLink[tmpLink.index('href="') + 8:tmpLink.index('html"') + 4]
        r2 = requests.get('https://' + href)
        print(r2.content)
        break
