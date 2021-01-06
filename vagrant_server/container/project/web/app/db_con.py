import pymysql.cursors

conn = pymysql.connect(host='host',
                       user='user',
                       password='password',
                       db='db',
                       cursorclass=pymysql.cursors.DictCursor
                       )

cursor = conn.cursor()
def get_table():
    cursor.execute("show tables;")
    c = cursor.fetchall()
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

    for t in t_list:
        sql = "select * from Tables;"
        sql = sql.replace("Tables", t)
        cursor.execute(sql)
        info_list[str(t)] = cursor.fetchall()
    return info_list

# sqlalchemy参考ページ ＞ https://qiita.com/uokada/items/d81fd930402e3be4aa62
# Base = declarative_base()
# engine = create_engine('mysql+pymysql://masteruser:master#36711@pdb/p_sdb?charset=utf8',echo=True)
# metadata = MetaData(bind=engine)
#
# price = Table('Price', metadata, autoload=True)
# cases = Table('Cases', metadata, autoload=True)
# casecooler = Table('caseCooler', metadata, autoload=True)
# cpu = Table('Cpu', metadata, autoload=True)
# cpucooler = Table('cpuCooler', metadata, autoload=True)
# hdd = Table('HDD', metadata, autoload=True)
# memory = Table('Memory', metadata, autoload=True)
# mother = Table('Motherboard', metadata, autoload=True)
# power = Table('Power', metadata, autoload=True)
# ssd = Table('SSD', metadata, autoload=True)
#
# def get_info():
#     table = [cases, casecooler, cpu, cpucooler,
#              hdd, memory, mother, power, ssd]
#
#     info_list = {'cases': None, 'casecooler': None, 'cpu': None, 'cpucooler': None,
#                  'hdd': None, 'memory': None, 'mother': None, 'power': None, 'ssd': None}
#
#     for t in table:
#         #: 取得したいカラムのリストを作成
#         columns = [price.c.price, t]
#         q = join(price, t, price.c.product_id == t.c.product_id).select()
#         q = q.with_only_columns(columns)
#         qlist = q.execute()
#         info_list[str(t).lower()] = qlist
#     return info_list


    # columns = [cases, price.c.price]
    # cq = join(cases, price, cases.c.product_id == price.c.product_id).select()
    # # 条件を付ける場合この後ろに .where(テーブル名.c.カラム名=="条件")
    # cq = cq.with_only_columns(columns)