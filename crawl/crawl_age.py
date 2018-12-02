from bs4 import BeautifulSoup
import os
import requests
import time

def make_folder(folder_name) :
    if not os.path.isdir(folder_name) :
        os.mkdir(folder_name)

teen = './data/teen.txt'
twenty =  './data/twnety.txt'
thirty =  './data/thirty.txt'
fourty =  './data/fourty.txt'
fifty = './data/fifty.txt'

#URL = 'https://datalab.naver.com/keyword/realtimeList.naver?datetime=' + str(year) + '-' + str(month) + '-' + str(day) + 'T20:00:00'
##content > div > div.keyword_carousel > div > div.section_lst_area.carousel_area > div.keyword_rank.select_date > div > div > ul > li > a > span
#URL = 'https://datalab.naver.com/keyword/realtimeList.naver?datetime=' + str(year) + '-' + str(month) + '-' + str(day) + 'T20%3A00%3A00'
##content > div > div.keyword_carousel > div > div > div:nth-of-type(1) > div > div > ul > li > a > span

for year in range(2018, 2019):
    for month in range(10, 12):
        if (year == 2018 and month == 10) :
            for day in range (1, 32):
                if day < 10 :
                    page = ''
                    while page == '':
                        try:
                            URL = 'https://datalab.naver.com/keyword/realtimeList.naver?datetime=' + str(year) + '-' + str(month) + '-0' + str(day) + 'T20%3A00%3A00'
                            print(URL)
                            header = {'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"}
                            req = requests.get(URL, headers=header)
                            source = req.text
                            break
                        except:
                            print("Connection refused by the server..")
                            time.sleep(20)
                            continue
                    soup = BeautifulSoup(source,'html.parser')
                    for age in range(2, 7) :
                        top_list = soup.select("#content > div > div.keyword_carousel > div > div > div:nth-of-type(" + str(age) + ") > div > div > ul > li > a > span")
                        if age == 2 : new_file_name = teen
                        elif age == 3 : new_file_name = twenty
                        elif age == 4 : new_file_name = thirty
                        elif age == 5 : new_file_name = fourty
                        elif age == 6 : new_file_name = fifty

                        new_file = open(new_file_name, 'a+')
                        for top in top_list:
                            new_file.write(top.text)
                            new_file.write('\n')
                        new_file.close()
                
                elif day > 10 :
                    page = ''
                    while page == '':
                        try:
                            URL = 'https://datalab.naver.com/keyword/realtimeList.naver?datetime=' + str(year) + '-' + str(month) + '-' + str(day) + 'T20%3A00%3A00'
                            print(URL)
                            header = {'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"}
                            req = requests.get(URL, headers=header)
                            source = req.text
                            break
                        except:
                            print("Connection refused by the server..")
                            time.sleep(20)
                            continue
                    soup = BeautifulSoup(source,'html.parser')
                    for age in range(2, 7) :
                        top_list = soup.select("#content > div > div.keyword_carousel > div > div > div:nth-of-type(" + str(age) + ") > div > div > ul > li > a > span")
                        if age == 2 : new_file_name = teen
                        elif age == 3 : new_file_name = twenty
                        elif age == 4 : new_file_name = thirty
                        elif age == 5 : new_file_name = fourty
                        elif age == 6 : new_file_name = fifty
                        
                        new_file = open(new_file_name, 'a+')
                        for top in top_list:
                            new_file.write(top.text)
                            new_file.write('\n')
                        new_file.close()
                
                else : continue

        elif (year == 2018 and month == 11) :
            for day in range(1, 27):
                if day < 10 :
                    URL = 'https://datalab.naver.com/keyword/realtimeList.naver?datetime=' + str(year) + '-' + str(month) + '-0' + str(day) + 'T20%3A00%3A00'
                else :
                    URL = 'https://datalab.naver.com/keyword/realtimeList.naver?datetime=' + str(year) + '-' + str(month) + '-' + str(day) + 'T20%3A00%3A00'
                
                page = ''
                while page == '':
                    try:
                        print(URL) 
                        header = {'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"}
                        req = requests.get(URL, headers=header)
                        source = req.text
                        break
                    except:
                        print("Connection refused by the server..")
                        time.sleep(20)
                        continue
                    soup = BeautifulSoup(source,'html.parser')
                    for age in range(2, 7) :
                        top_list = soup.select("#content > div > div.keyword_carousel > div > div > div:nth-of-type(" + str(age) + ") > div > div > ul > li > a > span")
                        if age == 2 : new_file_name = teen
                        elif age == 3 : new_file_name = twenty
                        elif age == 4 : new_file_name = thirty
                        elif age == 5 : new_file_name = fourty
                        elif age == 6 : new_file_name = fifty
                        
                        new_file = open(new_file_name, 'a+')
                        for top in top_list:
                            new_file.write(top.text)
                            new_file.write('\n')
                        new_file.close()

        else : continue




                        
# header = {'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"}
# req = requests.get('https://datalab.naver.com/keyword/realtimeList.naver?datetime=2017-09-03T20:00:00', headers=header)
# source = req.text
# soup = BeautifulSoup(source,'html.parser')
# top_list = soup.select("#content > div > div.keyword_carousel > div > div.section_lst_area.carousel_area > div.keyword_rank.select_date > div > div > ul > li > a > span")
# new_file = open(new_file_name, 'a+')
# for top in top_list:
#     new_file.write(top.text)
#     new_file.write('\n')