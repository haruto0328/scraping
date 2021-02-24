import requests#データを取得するモジュール
from bs4 import BeautifulSoup#取り出したデータを解析するモジュール
from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=R"C:\Users\User\chromedriver")
driver.implicitly_wait(10)

# 下記サイトにアクセス
driver.get("https://produce-web.net")

while True:
    try:
        url = driver.current_url #取得するサイトのURL
        html = requests.get(url)#指定したURLのサイトから情報を取得
        soup = BeautifulSoup(html.content, "html.parser") #取得した情報を解析、バイナリデータを取得

        for element in soup.select('.entry-title'): #指定したタグについて、そのタグ内のテキスト部分を取得
            print(element.text)

        # 次のページへの遷移ボタン(>>)を探す
        next = driver.find_element_by_xpath("//div[@class='nav-links']/ul[@class='page-numbers']/li[last()]/a[contains(@class,'next')]")
        # 見つかったらクリック
        next.click()
    except:
    	# 見つからなかったら終了(最終ページ)
        driver.close()

	# 3秒待つ
    time.sleep(3)

driver.close()

