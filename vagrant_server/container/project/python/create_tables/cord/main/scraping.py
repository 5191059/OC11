from cord.module import link_getter ,detail
from cord.cord.in_data import all_in, con_end
# detail, link_getter
# from .module import detail, link_getter

import time
import json
import os



def main():
    print("全件取得します")
    for k, v in link_getter.categories:
        print("{}を取得しています...".format(k))
        uri = link_getter.domain + v["link"]
        links = link_getter.get_links(uri)


        temp = []
        for l in links[:1]:
            print("取得リンク..{}".format(l))

            det = detail.get_detail(l)
            if det is not None:
                # temp.append(det)
                all_in(k, det)
            time.sleep(15)

            # with open("./output/{}/{}.json".format(k, l.split("/")[-1].replace("-", "_")), "w") as f:
            #     json.dump(temp, f)

        # fetched[k] = temp
        # all_in(k, temp)
    con_end()
