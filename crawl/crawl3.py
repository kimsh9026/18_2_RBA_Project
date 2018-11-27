import requests
from bs4 import BeautifulSoup

req = requests.get('https://www.naver.com/keyword/realtimeList.naver')
source = req.text
soup = BeautifulSoup(source, 'html.parser')

top_list = soup.select("#content > div > div.keyword_carousel > div > div > div:nth-child(1) > div > div > ul > li > a > span")

for top in top_list :
	print(top.text)

