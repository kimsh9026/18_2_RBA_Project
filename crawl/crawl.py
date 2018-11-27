# #######################크롤링 코드
URL = 'https://datalab.naver.com/keyword/realtimeList.naver?datetime=2018-11-26T22%3A54%3A00&period=now'
header = {
   'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"
}
req = requests.get(URL, headers=header)
source = req.text
soup = BeautifulSoup(source, 'html.parser')
top_list = soup.select("#content > div > div.keyword_carousel > div > div > div:nth-of-type(1) > div > div > ul > li > a > span")
time.sleep(1)
for top in top_list:
	print(top.text)
time.sleep(1)