# 라이브러리 설치
# 터미널 >
# pip install requests
# pip install beautifulsoup4
# pip install lxml
 
import requests
from bs4 import BeautifulSoup

# 특정 사이트의 html 가져오기
url = "https://n.news.naver.com/mnews/article/092/0002447111"
html = requests.get(url)

# print(html.text)

# html 분석
soup = BeautifulSoup(html.text, 'lxml')

# 뉴스 제목
h2 = soup.find('h2', id='title_area')
span = h2.find('span')
text = span.get_text()
print(text)