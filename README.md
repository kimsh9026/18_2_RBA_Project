# 18_2_RBA_Project
### 프로젝트 설명
 - Naver data lab 분석을 통해 2017~2018년에 꾸준히 인기가 있었던 키워드를 분석
 - 연령별 검색어순위 분석

### 프로젝트 진행
1. python을 이용한 crawling
	- Naver Data Lab 웹페이지에서 제공하는 10월 10일 이후의 시간대별, 연령별 검색순위
	- Naver Data Lab 웹페이지에서 제공하는 2017년 3월 29일부터 2018년 11월 26일까지의 20시 기준 실시간 검색순위
	- *crawl directory의 python code는 crawling 구현 code이고, craw/data와 craw/data directory에 있는 txt file들이 crawling한 data입니다*

2. R-programming을 이용하여 wordcloud 작성하기
	- 검색어의 공백을 삭제하여 검색어 자체를 분석
	- 검색어의 공백을 기준으로 검색어를 단어 단위로 자르고, 가장 꾸준히 검색된 단어가 무엇인지를 분석
	- 연령별 검색어 순위를 분석

