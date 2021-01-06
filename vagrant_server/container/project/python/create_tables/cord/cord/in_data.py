import pymysql.cursors

conn = pymysql.connect(host='host',
                       user='user',
                       password='user',
                       db='p_sdb',
                       cursorclass=pymysql.cursors.DictCursor
                       )
cur = conn.cursor()


def price(item_list,tablename):
    insert_sql = 'insert into Price(product_id,web_id,price,status,url) Values(%s,%s,%s,%s,%s)'
    select_sql = 'select product_id from Table where product_name = %s'
    select_sql = select_sql.replace('Table',tablename)
    web_list = {"dospara":201,"amazon":202,"kakaku":203,"sofmap":204} 
    item = []
    item = item_list
    param = []

    for data in item:
        cur.execute(select_sql,data['name'])
        proid = cur.fetchone()
        for web in web_list:
            if web in data:
                if data[web]['value'] == '':
                    data[web]['value'] = 0
                param.append([proid["product_id"],web_list[web],data[web]['value'],data[web]['status'],data[web]['link']])
    cur.executemany(insert_sql,param)
    conn.commit()
    

    

def cpu(item_list):
    sql = 'insert into Cpu(product_name,image,\
                                clock,GEN,multi_thread,cache_2nd,cache_3rd,\
                                turbo_clock,cores,thread,socket,TDP)\
                            Values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    item = []
    item.append(item_list)
    param = []

    for data in item:
        param.append( [ data['name'], data['image_link'], data['clock'], data['GEN'], data['multi_thread'], data['cache_2nd'],
                  data['cache_3rd'], data['turbo_clock'], data['cores'], data['thread'], data['socket'], data['TDP']
                ] )
    cur.executemany(sql,param)
    conn.commit()
    price(item,'Cpu')

def memory(item_list):
    sql = 'insert into Memory(product_name,image,\
                                capacity,interface,piece,mem_stndrd)\
                            Values(%s,%s,%s,%s,%s,%s)'
    item = []
    item.append(item_list)
    param = []

    for data in item:
        param.append([
            data['name'], data['image_link'], data['capacity'],
            data['interface'], data['piece'], data['mem_stndrd']
        ])
    cur.executemany(sql,param)
    conn.commit()
    price(item,'Memory')

def gpu(item_list):
    sql = 'insert into GPU(product_name,image,\
                                cuda, chip, bus_interface, mem_bus, memory)\
                            Values(%s,%s,%s,%s,%s,%s,%s)'
    item = []
    item.append(item_list)
    param = []

    for data in item:
        param.append([
            data['name'], data['image_link'], data['cuda'], data['chip'],
            data['bus_interface'], data['mem_bus'], data['memory']
        ])
    cur.executemany(sql,param)
    conn.commit()
    price(item,'GPU')

def cpucooler(item_list):
    sql = 'insert into cpuCooler(product_name,image,\
                                type, thickness, height, socket, width)\
                            Values(%s,%s,%s,%s,%s,%s,%s)'
    item = []
    item.append(item_list)
    param = []
    for data in item:
        param.append([
            data['name'], data['image_link'], data['type'], data['thickness'],
            data['height'], data['socket'], data['width']
        ])
    cur.executemany(sql,param)
    conn.commit()
    price(item,'cpuCooler')

def motherboard(item_list):
    sql = 'insert into Motherboard(product_name,image,\
                                audio, chipset, crossfire, formfactor, max_memory, lan_speed,\
                                memory_slot, sata_slot, memory_type, Socket)\
                            Values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    item = []
    item.append(item_list)
    param = []

    for data in item:
        param.append([
            data['name'], data['image_link'], data['audio'], data['chipset'], data['crossfire'], data['formfactor'],
            data['max_memory'], data['lan_speed'], data['memory_slot'], data['sata_slot'], data['memory_type'], data['Socket']
        ])
    cur.executemany(sql,param)
    conn.commit()
    price(item,'Motherboard')

def ssd(item_list):
    sql = 'insert into SSD(product_name,image,\
                                capacity, interface, speed_read, speed_write)\
                            Values(%s,%s,%s,%s,%s,%s)'
    item = []
    item.append(item_list)
    param = []

    for data in item:
        param.append([
            data['name'], data['image_link'], data['capacity'],
            data['interface'], data['speed-read'], data['speed-write']
        ])
    cur.executemany(sql,param)
    conn.commit()
    price(item,'SSD')

def hdd(item_list):
    sql = 'insert into HDD(product_name,image,\
                                size, capacity, interface, rpm, thickness)\
                            Values(%s,%s,%s,%s,%s,%s,%s)'
    item = []
    item.append(item_list)
    param = []

    for data in item:
        param.append([
            data['name'], data['image_link'], data['size'], data['capacity'],
            data['interface'], data['rpm'], data['thickness']
        ])
    cur.executemany(sql,param)
    conn.commit()
    price(item,'HDD')

def power(item_list):
    sql = 'insert into Power(product_name,image,\
                                80PLUS, capacity, plugin_available, standard)\
                            Values(%s,%s,%s,%s,%s,%s)'
    item = []
    item.append(item_list)
    param = []

    for data in item:
        param.append([
            data['name'], data['image_link'], data['80PLUS'], 
            data['capacity'], data['plugin_available'], data['standard']
        ])
    cur.executemany(sql,param)
    conn.commit()
    price(item,'Power')

def casecooler(item_list):
    sql = 'insert into caseCooler(product_name,image,\
                                connector, size, led_writing, noise, max_rpm, PWM)\
                            Values(%s,%s,%s,%s,%s,%s,%s,%s)'
    item = []
    item.append(item_list)
    param = []

    for data in item:
        param.append([
            data['name'], data['image_link'], data['connector'], data['size'],
            data['led_writing'], data['noise'], data['max_rpm'], data['PWM']
        ])
    cur.executemany(sql,param)
    conn.commit()
    price(item,'caseCooler')

def case(item_list):
    sql = 'insert into Cases(product_name,image,\
                                bay_cnt2_5, bay_cnt3_5, bay_cnt5_25, factor_available, interface, height, weight, width)\
                            Values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    item = []
    item.append(item_list)
    param = []

    for data in item:
        param.append([
            data['name'], data['image_link'], data['bay_cnt2.5'], data['bay_cnt3.5'], data['bay_cnt5.25'], 
            data['factor_available'], data['interface'], data['height'], data['weight'], data['width']
        ])
    cur.executemany(sql,param)
    conn.commit()
    price(item,'Cases')

def con_end():
    conn.close()

def all_in(k, item_list):
    print("データを挿入します...")
    i = item_list
    print("in data", k)
    if k == 'cpu':
        cpu(i)
    if k == 'memory':
        memory(i)
    if k == 'gpu':
        gpu(i)
    if k == 'cpu-cooler':
        cpucooler(i)
    if k == 'motherboard':
        motherboard(i)
    if k == 'ssd':
        ssd(i)
    if k == 'hdd':
        hdd(i)
    if k == 'power-supply':
        power(i)
    if k == 'case-fan':
        casecooler(i)
    if k == 'pc-case':
        case(i)
    