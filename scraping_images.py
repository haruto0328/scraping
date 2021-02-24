import requests
from bs4 import BeautifulSoup
import os

try:
    os.mkdir("img")
except:
    pass

images = []

load_url = input('画像を入手したいサイトのURLを入力してください。')
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "lxml")

for link in soup.find_all("img"):
    if link.get("src").endswith(".jpg"):
        images.append(link.get("src"))
    elif link.get("src").endswith(".png"):
        images.append(link.get("src"))

for target in images:
    re = requests.get(target)
    with open('img/' + target.split('/')[-1], 'wb')as f:
        f.write(re.content)

print("ok")

