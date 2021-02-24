import requests
from bs4 import BeautifulSoup
import csv

load_url = input('スクレイピングしたいサイトのURLを入力してください。')
html = requests.get(load_url, timeout=(9.0 , 12.0))
soup = BeautifulSoup(html.content, "html.parser")

csvlist = [["新着順", "投稿題名"]]
num = 1

for element in soup.select('.entry-title'):
    csvlist.append([num, element.text])
    num += 1

f = open('my_blog.csv', "w", encoding="utf-16")
writecsv = csv.writer(f, lineterminator="\n")

writecsv.writerows(csvlist)
f.close()