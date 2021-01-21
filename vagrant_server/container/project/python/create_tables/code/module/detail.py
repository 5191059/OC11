# coding:UTF-8

import os
import re
import requests
import urllib.parse
from bs4 import BeautifulSoup
import json

PATH = os.path.dirname(__file__)
SPLIT = "/"

with open("{}{}{}".format(PATH, SPLIT, "information.json"), encoding="UTF-8") as f:
    json = json.load(f)

STORES = json["stores"]


def get_detail(link: str, category="cpu"):
    # カテゴリを識別する
    print(link)

    # たまに空のリンクが交じるっぽい
    if "null" in link:
        return None

    cat = link.replace(json["home"] + "/", "")
    cat = cat.split("/")[0]

    schemes = json["items"][cat]["CNAME"]

    info = {k: "" for k in schemes.values()}

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
    }
    soup = requests.get(url=link, headers=headers)
    soup = BeautifulSoup(soup.content, "lxml")

    info["image_link"] = ""

    # 画像リンク
    try:
        images = soup.find_all("amp-img")
        image = [s["src"] for s in images if "https" in s["src"]][0]

        info["image_link"] = image
    except Exception as e:
        print("the page has no img")
        print(e)

    sections = soup.find_all("section")
    for sc in sections:
        title = sc.find("h2")

        if title is None:
            continue

        title = title.getText()

        if "価格情報" in title:
            item_name = title.replace("の価格情報", "")
            info["name"] = item_name

            prices = sc.find_all("tr")

            for pr in prices[1:]:
                res = pr.find_all("td")

                head = res[0].find("span")

                if head is not None:
                    res[0].find("span").extract()  # ヘッダ（不要）

                site = res[0].getText()[:-1]  # サイト名の末尾に謎の空白あり

                value = res[1].getText()  # ￥5,960 -> 5960
                value = re.sub("\\D", "", value)

                if value != "":
                    value = int(value)

                status = res[2].getText()

                # ドスパラのリダイレクト先urlだけなんか変問題
                link = json["home"] + res[3].find("a")["href"]  # 自作.comから当該サイトにリダイレクトされるっぽいので再帰的にBS4
                redirect = requests.get(url=link, headers=headers)
                redirect = BeautifulSoup(redirect.content, "lxml")
                link = redirect.find("a")["href"]

                if site == "ドスパラ":
                    link = link.split("vc_url=")[1]
                if site == "ソフマップ.com":
                    link = link.split("murl=")[1]

                link = urllib.parse.unquote(link)

                if site in STORES:
                    info[STORES[site]] = {
                        "value": value,
                        "status": status,
                        "link": link
                    }

            # req = urllib.request.Request(link,  headers=headers)
            # with urllib.request.urlopen(req) as response:
            #     the_page = response.read()
        if "スペック詳細" in title:
            item_name = title.replace("のスペック詳細", "")
            info["name"] = item_name

            records = sc.find_all("tr")
            import pdb

            for r in records:
                try:
                    name = r.find("th").getText()
                    value = r.find("td").getText()
                except AttributeError:
                    continue

                if name in schemes.keys():
                    info[schemes[name]] = value
    return info


# amazon
# 価格com
# dospara
# sofmap

if __name__ == '__main__':
    pt = get_detail("https://jisaku.com/cpu-cooler/h60(2018)-cw-9060036-ww")
    print(pt)
