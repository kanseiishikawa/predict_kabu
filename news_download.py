import requests
import bs4
import pickle

data = {}

def news(year, month_name, day_name):
    host_url = "https://news.yahoo.co.jp/list/?c=economy&d="#確定のurl
    url = host_url + year + month_name + day_name
    res = requests.get(url)
    res.raise_for_status()
    #print(res.text)
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    name = soup.find_all("dl", class_="title") 
    name = str(name).split("\n")
    news_storage = []
    for i in range(1, len(name)):
        if i % 3 == 1:
            news_data = name[i].replace("<dt>", "")
            news_data = news_data.replace("</dt>", "")
            news_storage.append(news_data)
    data[year + month_name + day_name] = news_storage
    print(data)
    
def main():
    for year in range(2009 ,2019):
        for month in range(1, 13):   
            if month == 1 or month == 3\
               or month == 5 or month == 7\
               or month == 8 or month == 10\
               or month == 12:
                final_day = 31
            elif month == 4 or month == 6\
                 or month == 9 or month == 11:
                final_day = 30
            else:
                final_day = 28
                if year % 4 == 0:
                    final_day += 1
                    
            for day in range(1,final_day + 1):
                if month < 10:
                    month_name = "0" + str(month)
                else:
                    month_name = str(month)
                    
                if day < 10:
                    day_name = "0" + str(day)
                else:
                    day_name = str(day)
                news(str(year), month_name, day_name)
                
    f = open("ten_year_news_data", "wb")
    pickle.dump(data, f)
    f.close
main()
