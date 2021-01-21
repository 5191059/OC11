from collections import OrderedDict

# lst = [{'product_id': 10001,
#         'product_name': 'AMD Ryzen 9 5900X BOX',
#         'image': 'https://cdn.jisaku.com//images/b7536204591e0028.jpg/720.jpg',
#         'clock': '3.7GHz',
#         'GEN': '4',
#         'multi_thread': '○',
#         'cache_2nd': '6',
#         'cache_3rd': '64',
#         'turbo_clock': '4.8GHz',
#         'cores': '12',
#         'thread': '24',
#         'socket': 'Socket AM4',
#         'TDP': '105W',
#         'price.product_id': 10001,
#         'web_id': 203,
#         'price': 0,
#         'status': '不明',
#         'url': 'https://kakaku.com/item/K0001299537/'},
#        {'product_id': 10002,
#         'product_name': 'AMD Ryzen 5 5600X BOX',
#         'image': 'https://cdn.jisaku.com//images/3b91dd1304a37036.jpg/720.jpg',
#         'clock': '3.7GHz',
#         'GEN': '4',
#         'multi_thread': '○',
#         'cache_2nd': '3',
#         'cache_3rd': '32',
#         'turbo_clock': '4.6GHz',
#         'cores': '6',
#         'thread': '12',
#         'socket': 'Socket AM4',
#         'TDP': '65W',
#         'price.product_id': 10002,
#         'web_id': 201,
#         'price': 39380,
#         'status': '在庫',
#         'url': 'https://www.dospara.co.jp/5shopping/detail_parts.php?ic=469252'},
#        {'product_id': 10002,
#         'product_name': 'AMD Ryzen 5 5600X BOX',
#         'image': 'https://cdn.jisaku.com//images/3b91dd1304a37036.jpg/720.jpg',
#         'clock': '3.7GHz',
#         'GEN': '4',
#         'multi_thread': '○',
#         'cache_2nd': '3',
#         'cache_3rd': '32',
#         'turbo_clock': '4.6GHz',
#         'cores': '6',
#         'thread': '12',
#         'socket': 'Socket AM4',
#         'TDP': '65W',
#         'price.product_id': 10002,
#         'web_id': 203,
#         'price': 39380,
#         'status': '不明',
#         'url': 'https://kakaku.com/item/K0001299539/'},
#        {'product_id': 10002,
#         'product_name': 'AMD Ryzen 5 5600X BOX',
#         'image': 'https://cdn.jisaku.com//images/3b91dd1304a37036.jpg/720.jpg',
#         'clock': '3.7GHz',
#         'GEN': '4', 'multi_thread': '○',
#         'cache_2nd': '3', 'cache_3rd': '32',
#         'turbo_clock': '4.6GHz',
#         'cores': '6',
#         'thread': '12',
#         'socket': 'Socket AM4',
#         'TDP': '65W',
#         'price.product_id': 10002,
#         'web_id': 204,
#         'price': 39380,
#         'status': '在庫',
#         'url': 'https://www.sofmap.com/product_detail/exec/?sku=21464382'},
#        {'product_id': 10003,
#         'product_name': 'AMD Ryzen 7 5800X BOX',
#         'image': 'https://cdn.jisaku.com//images/d28cd554d387261d.jpg/720.jpg',
#         'clock': '3.8GHz',
#         'GEN': '4',
#         'multi_thread': '○',
#         'cache_2nd': '4',
#         'cache_3rd': '32',
#         'turbo_clock': '4.7GHz',
#         'cores': '8',
#         'thread': '16',
#         'socket': 'Socket AM4',
#         'TDP': '105W',
#         'price.product_id': 10003,
#         'web_id': 201,
#         'price': 58828,
#         'status': '在庫',
#         'url': 'https://www.dospara.co.jp/5shopping/detail_parts.php?ic=469251'}
#        ]


def site_num(name):
    if 'amazon' in name:
        return 0
    elif 'dospara' in name:
        return 1
    elif 'kakaku' in name:
        return 2
    elif 'sofmap' in name:
        return 3


def check_website(parts_lst):
    for part in parts_lst:
        count = [0, 0, 0, 0]
        work_dict = {}
        for where_url in part['url']:
            idx = part['url'].index(where_url)
            if 'amazon' in where_url:
                work_dict.update({'amazon': part['price'][idx]})
                count[0] += 1
            elif 'dospara' in where_url:
                work_dict.update({'dospara': part['price'][idx]})
                count[1] += 1
            elif 'kakaku' in where_url:
                work_dict.update({'kakaku': part['price'][idx]})
                count[2] += 1
            elif 'sofmap' in where_url:
                work_dict.update({'sofmap': part['price'][idx]})
                count[3] += 1

        part['price'] = work_dict
        if sum(count) != 4:
            site_lst = ['amazon', 'dospara', 'kakaku', 'sofmap']
            if sum(count) == 3:
                part['price'].update({site_lst[count.index(0)]: '価格なし'})
            elif sum(count) == 2:
                for i in range(2):
                    part['price'].update({site_lst[count.index(0)]: '価格なし'})
                    count[count.index(0)] = 1
            elif sum(count) == 1:
                for i in range(3):
                    part['price'].update({site_lst[count.index(0)]: '価格なし'})
                    count[count.index(0)] = 1

        part['price'] = sorted(part['price'].items(), key=lambda x: x[0])

    for part in parts_lst:
        count = [0, 0, 0, 0]
        for url in part['url']:
            if 'amazon' in url:
                count[0] += 1
            elif 'dospara' in url:
                count[1] += 1
            elif 'kakaku' in url:
                count[2] += 1
            elif 'sofmap' in url:
                count[3] += 1
        if sum(count) != 4:
            site_lst = ['amazon', 'dospara', 'kakaku', 'sofmap']
            if sum(count) == 3:
                part['url'].insert(count.index(0), '')
            elif sum(count) == 2:
                for i in range(2):
                    part['url'].insert(count.index(0), '')
                    count[count.index(0)] = 1
            elif sum(count) == 1:
                for i in range(3):
                    part['url'].insert(count.index(0), '')
                    count[count.index(0)] = 1
    return parts_lst


def parts_info(name):
    summary = {
        'Cpu': ['socket', 'clock', 'thread', 'cores'],
        'cpuCooler': ['socket', 'height'],
        'Memory': ['mem_stndrd', 'capacity'],
        'Motherboard': ['Socket', 'chipset', 'formfactor'],
        'GPU': ['chip'],
        'SSD': ['interface', 'capacity'],
        'HDD': ['rpm', 'capacity', 'size'],
        'Cases': ['factor_available'],
        'caseCooler': ['size'],
        'Power': ['capacity', '80PLUS']
    }

    return summary[name]


def sort_lst(name, before_lst):
    product_dict = OrderedDict()
    for i in range(len(before_lst)):
        product = before_lst[i]['product_name']
        price = before_lst[i]['price']
        url = before_lst[i]['url']
        if product in product_dict:
            if price == 0:
                product_dict[product].append('価格なし')
            else:
                product_dict[product].append(price)
            product_dict[product + 'url'].append(url)
        else:
            work = OrderedDict()
            if price == 0:
                work[product] = ['価格なし']
            else:
                work[product] = [price]
            
            work[product + 'image'] = before_lst[i]['image']
            work[product + 'url'] = [url]

            information = []
            for info in parts_info(name):
                information.append(before_lst[i][info])
            work[product + 'info'] = information
            product_dict.update(work)

    product_return_lst = []
    index = 1
    for k, v in product_dict.items():
        if index % 4 == 1:
            work = {'product_name': k, 'price': v}
        elif index % 4 == 2:
            work2 = {'image': v}
            work.update(work2)
        elif index % 4 == 3:
            work3 = {'url': v}
            work.update(work3)
        else:
            work4 = {'info': v}
            work.update(work4)
            product_return_lst.append(work)
        index += 1
    return check_website(product_return_lst)
