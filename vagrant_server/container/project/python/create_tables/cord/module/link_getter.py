# coding:UTF-8

import os
import json
import requests
from bs4 import BeautifulSoup

PATH = os.path.dirname(__file__)
SPLIT = "/"

with open("{}{}{}".format(PATH, SPLIT, "information.json"), encoding="UTF-8") as f:
    json = json.load(f)

domain = json["home"]


def get_links(_url: str):
    """
    :param _url:特定のカテゴリのパーツ一覧、だいたい100件くらい出てくる
    :return links:詳細ページへのリンクのリスト
    """
    links = []
    soup = requests.get(url=_url)
    soup = BeautifulSoup(soup.content, "lxml")
    soup = soup.find("ul", class_="ranking css-mtusop e3vi7o70").find_all("li")

    for s in soup:
        lk = "{}{}".format(domain, s.find("a")["href"])
        if "null" not in lk:
            links.append(lk)

    return links


categories = json["items"].items()

if __name__ == '__main__':
    links = get_links("https://jisaku.com/cpu-cooler/popular")
