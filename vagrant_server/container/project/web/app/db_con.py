import pymysql.cursors
from db import get_prodb

def get_table():
    conn = get_prodb()
    cursor = conn.cursor()
    cursor.execute("show tables;")
    c = cursor.fetchall()
    cursor.close()
    t_list = []
    for i in c:
        for l in i.values():
            t_list.append(l)
            
    del_tables = ['Maker', 'Website', 'Price']
    [t_list.remove(i) for i in del_tables]
    return t_list

def get_info():
    t_list = get_table()
    info_list = dict(zip(t_list, [None] * len(t_list)))
    conn = get_prodb()
    cursor = conn.cursor()

    for t in t_list:
        sql = "select * from Tables as t, Price as p where t.product_id = p.product_id;"
        sql = sql.replace("Tables", t)
        cursor.execute(sql)
        info_list[str(t)] = cursor.fetchall()
    cursor.close()
    return info_list


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


def get_summary(name):
    p_list = parts_info(name)
    summary_list = dict(zip(p_list, [None] * len(p_list)))
    conn = get_prodb()
    cursor = conn.cursor()

    for info in parts_info(name):
        sql = "SELECT DISTINCT info FROM Tables WHERE info is not null and info != '' ORDER BY LENGTH(info), info;"
        sql = sql.replace("Tables", name)
        sql = sql.replace("info", info)
        cursor.execute(sql)
        summary_list[str(info)] = cursor.fetchall()
    cursor.close()
    return summary_list