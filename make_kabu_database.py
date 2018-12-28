import os
import database

def kabu_main():
    base_path = "/Users/kansei.ishikawa/Desktop/kabu/kabu_data/"
    number_list = os.listdir(base_path)
    dp = database.database_python("/Users/kansei/Desktop/kabu/database/predict_kabu.db")
    dp.cleatetable("kabu_value", ["number","year", "month", "day", "start", "max", "min", "finish", "yield"])
    number_list.sort()
    for i in range(0, len(number_list)):
        print(number_list[i])
        if os.path.isfile(base_path + number_list[i]):
            continue
        
        file_name_list = os.listdir(base_path + number_list[i] + "/")
        for r in range(0, len(file_name_list)):
            
            if file_name_list[r] == ".DS_Store":
                continue
            
            with open(base_path + number_list[i] + "/" + file_name_list[r], encoding="shift-jis") as f:
                data = f.readlines()
                for t in range(2 , len(data)):
                    kabu = [number_list[i]]
                    data[t] = data[t].replace('"', '')
                    data[t] = data[t].replace('\n', '')
                    data[t] = data[t].split(',')
                    time = data[t][0].split("-")
                                        
                    for s in range(0, len(time)):
                        kabu.append(int(time[s]))

                    for s in range(1, len(data[t]) - 1):
                        kabu.append(float(data[t][s]))

                    dp.add("kabu_value", kabu)
                    
def test():                    
    dp = database.database_python("/Users/kansei/Desktop/kabu/database/predict_kabu.db")
    print(dp.take_out(["start", "max"], ["year=2010", "aa"]))
