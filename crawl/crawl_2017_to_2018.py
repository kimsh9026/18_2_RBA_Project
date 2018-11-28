from bs4 import BeautifulSoup
import os
import requests
import time

def make_folder(folder_name) :
    if not os.path.isdir(folder_name) :
        os.mkdir(folder_name)

new_file_name = './data/all_rank.txt'
#2017년 3월 29일부터 2018년 10월 9일까지..
#2018 10월 10일부터 2018 11월 27일까지!

#18/ 2
#18/ 10 11

#URL = 'https://datalab.naver.com/keyword/realtimeList.naver?datetime=' + str(year) + '-' + str(month) + '-' + str(day) + 'T20:00:00'
##content > div > div.keyword_carousel > div > div.section_lst_area.carousel_area > div.keyword_rank.select_date > div > div > ul > li > a > span
#URL = 'https://datalab.naver.com/keyword/realtimeList.naver?datetime=' + str(year) + '-' + str(month) + '-' + str(day) + 'T20%3A00%3A00'
##content > div > div.keyword_carousel > div > div > div:nth-of-type(1) > div > div > ul > li > a > span

for year in range(2017, 2019):
    for month in range(1, 13):

        if (year==2017 and (month == 5 or month == 7 or month == 8 or month == 10 or month == 12)) or (year==2018 and (month == 1 or month == 3 or month == 5 or month == 7 or month==8)) :
            for day in range(1, 32):
                if month < 10 :
                    if day < 10 :
                        URL = 'https://datalab.naver.com/keyword/realtimeList.naver?datetime=' + str(year) + '-0' + str(month) + '-0' + str(day) + 'T20:00:00'
                    else :
                        URL = 'https://datalab.naver.com/keyword/realtimeList.naver?datetime=' + str(year) + '-0' + str(month) + '-' + str(day) + 'T20:00:00'
                else :
                    if day < 10 :
                        URL = 'https://datalab.naver.com/keyword/realtimeList.naver?datetime=' + str(year) + '-' + str(month) + '-0' + str(day) + 'T20:00:00'
                    else :
                        URL = 'https://datalab.naver.com/keyword/realtimeList.naver?datetime=' + str(year) + '-' + str(month) + '-' + str(day) + 'T20:00:00'
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
                top_list = soup.select("#content > div > div.keyword_carousel > div > div.section_lst_area.carousel_area > div.keyword_rank.select_date > div > div > ul > li > a > span")
                new_file = open(new_file_name, 'w')
                for top in top_list:
                    new_file.write(top.text)
                    new_file.write('\n')
                new_file.close()

        elif (year==2017 and (month == 4 or month == 6 or month == 9 or month == 11)) or (year==2018 and (month == 4 or month == 6 or month == 9)) :
            for day in range(1, 31) :    
                if month < 10 :
                    if day < 10 :
                        URL = 'https://datalab.naver.com/keyword/realtimeList.naver?datetime=' + str(year) + '-0' + str(month) + '-0' + str(day) + 'T20:00:00'
                    else :
                        URL = 'https://datalab.naver.com/keyword/realtimeList.naver?datetime=' + str(year) + '-0' + str(month) + '-' + str(day) + 'T20:00:00'
                else :
                    if day < 10 :
                        URL = 'https://datalab.naver.com/keyword/realtimeList.naver?datetime=' + str(year) + '-' + str(month) + '-0' + str(day) + 'T20:00:00'
                    else :
                        URL = 'https://datalab.naver.com/keyword/realtimeList.naver?datetime=' + str(year) + '-' + str(month) + '-' + str(day) + 'T20:00:00'
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
                top_list = soup.select("#content > div > div.keyword_carousel > div > div.section_lst_area.carousel_area > div.keyword_rank.select_date > div > div > ul > li > a > span")
                new_file = open(new_file_name, 'w')
                for top in top_list:
                    new_file.write(top.text)
                    new_file.write('\n')
                new_file.close()

        elif (year == 2017 and month == 3) :
            for day in range (29, 32):
                if month < 10 :
                    if day < 10 :
                        URL = 'https://datalab.naver.com/keyword/realtimeList.naver?datetime=' + str(year) + '-0' + str(month) + '-0' + str(day) + 'T20:00:00'
                    else :
                        URL = 'https://datalab.naver.com/keyword/realtimeList.naver?datetime=' + str(year) + '-0' + str(month) + '-' + str(day) + 'T20:00:00'
                else :
                    if day < 10 :
                        URL = 'https://datalab.naver.com/keyword/realtimeList.naver?datetime=' + str(year) + '-' + str(month) + '-0' + str(day) + 'T20:00:00'
                    else :
                        URL = 'https://datalab.naver.com/keyword/realtimeList.naver?datetime=' + str(year) + '-' + str(month) + '-' + str(day) + 'T20:00:00'
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
            top_list = soup.select("#content > div > div.keyword_carousel > div > div.section_lst_area.carousel_area > div.keyword_rank.select_date > div > div > ul > li > a > span")
            new_file = open(new_file_name, 'w')
            for top in top_list:
                new_file.write(top.text)
                new_file.write('\n')
            new_file.close()

        elif (year == 2018 and month == 2) :
            for day in range (1, 29) :
                if month < 10 :
                    if day < 10 :
                        URL = 'https://datalab.naver.com/keyword/realtimeList.naver?datetime=' + str(year) + '-0' + str(month) + '-0' + str(day) + 'T20:00:00'
                    else :
                        URL = 'https://datalab.naver.com/keyword/realtimeList.naver?datetime=' + str(year) + '-0' + str(month) + '-' + str(day) + 'T20:00:00'
                else :
                    if day < 10 :
                        URL = 'https://datalab.naver.com/keyword/realtimeList.naver?datetime=' + str(year) + '-' + str(month) + '-0' + str(day) + 'T20:00:00'
                    else :
                        URL = 'https://datalab.naver.com/keyword/realtimeList.naver?datetime=' + str(year) + '-' + str(month) + '-' + str(day) + 'T20:00:00'
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
                top_list = soup.select("#content > div > div.keyword_carousel > div > div.section_lst_area.carousel_area > div.keyword_rank.select_date > div > div > ul > li > a > span")
                new_file = open(new_file_name, 'w')
                for top in top_list:
                    new_file.write(top.text)
                    new_file.write('\n')
                new_file.close()
        
        elif (year == 2018 and month == 10) :
            for day in range (1, 32):
                if day < 10 :
                    page = ''
                    while page == '':
                        try:
                            URL = 'https://datalab.naver.com/keyword/realtimeList.naver?datetime=' + str(year) + '-' + str(month) + '-0' + str(day) + 'T20:00:00'
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
                    top_list = soup.select("#content > div > div.keyword_carousel > div > div.section_lst_area.carousel_area > div.keyword_rank.select_date > div > div > ul > li > a > span")
                    new_file = open(new_file_name, 'w')
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
                    top_list = soup.select("#content > div > div.keyword_carousel > div > div > div:nth-of-type(1) > div > div > ul > li > a > span")
                    new_file = open(new_file_name, 'w')
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
                top_list = soup.select("#content > div > div.keyword_carousel > div > div > div:nth-of-type(1) > div > div > ul > li > a > span")
                new_file = open(new_file_name, 'w')
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
# new_file = open(new_file_name, 'w')
# for top in top_list:
#     new_file.write(top.text)
#     new_file.write('\n')