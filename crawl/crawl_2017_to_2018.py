from bs4 import BeautifulSoup
import os
import requests
import time

def make_folder(folder_name) :
    if not os.path.isdir(folder_name) :
        os.mkdir(folder_name)

path = './data'
util_path = './data/utilization/'

#crawling
for year in range(2017, 2019):
    if year == 2017:
        for month in range(29, 31):
            if month == 3 :
                for day in range (10, 28):
                    for hour in range(0, 24) :
                        time.sleep(1)
                        if hour < 10:
                            page = ''
                            while page == '':
                                try:
                                    URL = 'https://datalab.naver.com/keyword/realtimeList.naver?datetime=2018-'+ str(month)'- ' + str(day) + 'T0' + str(hour) + ':00:00'
                                    print(URL)
                                    header = {
                                    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"
                                    }
                                    req = requests.get(URL, headers=header)
                                    source = req.text
                                    break
                                except:
                                    print("Connection refused by the server..")
                                    print("Let me sleep for 5 seconds")
                                    print("ZZzzzz...")
                                    time.sleep(5)
                                    print("Was a nice sleep, now let me continue...")
                                    continue
                            soup = BeautifulSoup(source,'html.parser')
                            top_list = soup.select("#content > div > div.keyword_carousel > div > div > div:nth-of-type(1) > div > div > ul > li > a > span")
                            new_file_name = new_folder_name + '/' + str(hour) +'.txt'
                            new_file = open(new_file_name, 'w')
                            for top in top_list:
                                new_file.write(top.text)
                                new_file.write('\n')
                        else:
                            page = ''
                            while page == '':
                                try:
                                    URL = 'https://datalab.naver.com/keyword/realtimeList.naver?datetime=2018-'+ str(month)'- ' + str(day) + 'T0' + str(hour) + ':00:00'
                                    URL = 'https://datalab.naver.com/keyword/realtimeList.naver?datetime=2018-' + str(month) +'-' + str(day) + 'T0' + str(hour) + '%3A00%3A00'
                                    print(URL)
                                    header = {
                                    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"
                                    }
                                    req = requests.get(URL, headers=header)
                                    source = req.text
                                    break
                                except:
                                    print("Connection refused by the server..")
                                    print("Let me sleep for 5 seconds")
                                    print("ZZzzzz...")
                                    time.sleep(5)
                                    print("Was a nice sleep, now let me continue...")
                                    continue
                            soup = BeautifulSoup(source,'html.parser')
                            top_list = soup.select("#content > div > div.keyword_carousel > div > div > div:nth-of-type(1) > div > div > ul > li > a > span")
                            new_file_name = new_folder_name + '/' + str(hour) +'.txt'
                            new_file = open(new_file_name, 'w')
                            for top in top_list:
                                new_file.write(top.text)
                                new_file.write('\n')
                
            else :
                for day in range (1, 28):
                    if(day < 10) :
                        new_folder_name = util_path + str(month) + '_0' + str(day)
                        make_folder(new_folder_name)
                    else :
                        new_folder_name = util_path + str(month) + '_' + str(day)
                        make_folder(new_folder_name)
                    for hour in range(0, 24) :
                        time.sleep(1)
                        
                        if hour < 10:
                            page = ''
                            while page == '':
                                try:
                                    URL = 'https://datalab.naver.com/keyword/realtimeList.naver?datetime=2018-' + str(month) +'-' + str(day) + 'T0' + str(hour) + '%3A00%3A00'
                                    print(URL)
                                    header = {
                                    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"
                                    }
                                    req = requests.get(URL, headers=header)
                                    source = req.text
                                    break
                                except:
                                    print("Connection refused by the server..")
                                    print("Let me sleep for 5 seconds")
                                    print("ZZzzzz...")
                                    time.sleep(5)
                                    print("Was a nice sleep, now let me continue...")
                                    continue
                            soup = BeautifulSoup(source,'html.parser')
                            top_list = soup.select("#content > div > div.keyword_carousel > div > div > div:nth-of-type(1) > div > div > ul > li > a > span")
                            new_file_name = new_folder_name + '/' + str(hour) +'.txt'
                            new_file = open(new_file_name, 'w')
                            for top in top_list:
                                new_file.write(top.text)
                                new_file.write('\n')
                        else:
                            page = ''
                            while page == '':
                                try:
                                    URL = 'https://datalab.naver.com/keyword/realtimeList.naver?datetime=2018-' + str(month) +'-' + str(day) + 'T0' + str(hour) + '%3A00%3A00'
                                    print(URL)
                                    header = {
                                    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"
                                    }
                                    req = requests.get(URL, headers=header)
                                    source = req.text
                                    break
                                except:
                                    print("Connection refused by the server..")
                                    print("Let me sleep for 5 seconds")
                                    print("ZZzzzz...")
                                    time.sleep(5)
                                    print("Was a nice sleep, now let me continue...")
                                    continue
                            soup = BeautifulSoup(source,'html.parser')
                            top_list = soup.select("#content > div > div.keyword_carousel > div > div > div:nth-of-type(1) > div > div > ul > li > a > span")
                            new_file_name = new_folder_name + '/' + str(hour) +'.txt'
                            new_file = open(new_file_name, 'w')
                            for top in top_list:
                                new_file.write(top.text)
                                new_file.write('\n')
