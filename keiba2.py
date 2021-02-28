import pandas as pd
import time
from tqdm import tqdm

#始め4桁:20xx年 今回は2020
#中2桁: 開催都市　01;札幌 02;函館 03;福島 04;新潟 05;東京 06;中山 07;中京 08;京都 09;阪神 10;小倉
#中2桁: x回(1~5)
#中2桁: x日目(1~9)
#最後2桁: xR(ラウンド(1~12))

def scrape_race_results(race_id_list):
    race_result = {}
    for race_id in tqdm(race_id_list):
        url = "https://db.netkeiba.com/race/"+ race_id
        race_result[race_id] = pd.read_html(url)[0]
        time.sleep(1)

    return race_result


#race_id_list = ["202001010101", "202001010102", "202001010103"]

#test = scrape_race_results(race_id_list)

#print(test)

##race_id_listをネットからとってきて全部scrape_race_results で表す

#race_list = []
#str_citeis = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
#times = 5

race_list = []
citeis = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
times = ["1", "2", "3", "4", "5"]
days = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
rounds = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]


def search_race_id():
    year = "2020"
    for city in citeis:
        #year = "2020" + city.zfill(2)
        #race_list.append(year)

        for time in times:
            #year = year + time.zfill(2)
            #race_list.append(year)
            year = year[:-2]

            for day in days:
                #year = "2020" + city.zfill(2) + time.zfill(2) + day.zfill(2)
                #race_list.append(year)
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
print(test)