import pandas as pd
import time
from tqdm import tqdm
from bs4 import BeautifulSoup
import csv

######小規模テスト用######

#始め4桁:20xx年 今回は2020
#中2桁: 開催都市　01;札幌 02;函館 03;福島 04;新潟 05;東京 06;中山 07;中京 08;京都 09;阪神 10;小倉
#中2桁: x回(1~5)
#中2桁: x日目(1~9)
#最後2桁: xR(ラウンド(1~12))


def scrape_race_results(race_id_list):
    race_result = {}
    for race_id in tqdm(race_id_list):
        url = "https://db.netkeiba.com/race/" + race_id
        race_result[race_id] = pd.read_html(url)[0]
        time.sleep(1)
    
    #with open('/Users/taro/beginner_python/keiba/attempt.csv', 'w') as file:
        #f = csv.DictWriter(file, ['202002010102', '202001010102', '202001010101', '202002010101'])
        #f.writerow(race_result)
    
    #dict型をjson_normalze()でDatarame型へ
    df = pd.json_normalize(race_result)
    
    #attempt.csv
    df.to_csv('/Users/taro/beginner_python/keiba/attempt.csv',index=False)

    return race_result


##race_id_listをネットからとってきて全部scrape_race_results で表す

race_list = []
citeis = ["1", "2"]
times = ["1"]
days = ["1"]
rounds = ["1", "2",]


def search_race_id():
    year = "2020"
    for city in citeis:
        for time in times:
            year = year[:-2]
            for day in days:
                year = year[:-2]
                for round in rounds:
                    year = "2020" + \
                        city.zfill(2) + time.zfill(2) + \
                        day.zfill(2) + round.zfill(2)
                    race_list.append(year)
                    year = year[:-2]

    #race_id_list = list(map(int, race_list))

    return race_list


test = scrape_race_results(search_race_id())
#print(test)
