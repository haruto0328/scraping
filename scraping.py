import requests#データを取得するモジュール
from bs4 import BeautifulSoup#取り出したデータを解析するモジュール

load_url = 'https://produce-web.net' #取得するサイトのURL
html = requests.get(load_url)#指定したURLのサイトから情報を取得
soup = BeautifulSoup(html.content, "html.parser") #取得した情報を解析、バイナリデータを取得

for element in soup.select('.entry-title'): #指定したタグについて、そのタグ内のテキスト部分を取得
    print(element.text)