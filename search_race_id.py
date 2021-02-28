race_list = []
citeis = ["1","2","3","4","5","6","7","8","9","10"]
times = ["1","2","3","4","5"]
days = ["1","2","3","4","5","6","7","8","9"]
rounds = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10","11","12"]
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
                    year = "2020" + city.zfill(2) + time.zfill(2) + day.zfill(2) + round.zfill(2)
                    race_list.append(year)
                    year = year[:-2]
                
                       
    race_id_list = list(map(int, race_list))
    
    return race_id_list

test = search_race_id()

print(test)
