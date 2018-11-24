import feedparser
from bs4 import BeautifulSoup
import requests
from urllib.request import *

try:
    while True:

        URL = "https://news.yahoo.co.jp/pickup/computer/rss.xml"

        urlopen(URL)

        news = feedparser.parse(URL)
        i = 1
        links = {}
        for entry in news.entries:
            title = entry.title
            link  = entry.link
            links[i] = link
            print (i,":",title)
            i+=1
        print("\n")
        s =int(input("Which article do you want to see?(1~8)"))
        try:
            url = links[s]

            s = requests.Session()
            r = s.get(url)
            soup = BeautifulSoup(r.text,"lxml")

            elems = soup.find_all('h2', class_="newsTitle")
            elems +=soup.find_all('p',class_="hbody")
            for elem in elems:
                print(elem.getText())
            break

        except:
            print("1~8で入力してください")
            print("もう一度表示します")
            print("\n")

except:
	print("インターネットに接続されていません")
