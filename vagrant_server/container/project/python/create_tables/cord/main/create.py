# MySQLdbのインポート
import MySQLdb

# データベースへの接続とカーソルの生成
connection = MySQLdb.connect(
    host='host',
    user='root',
    passwd='root',
    db='p_sdb',
    # テーブル内部で日本語を扱うために追加
    charset='utf8'
)

def create_pdb():
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS Cpu")
    cursor.execute("DROP TABLE IF EXISTS Motherboard")
    cursor.execute("DROP TABLE IF EXISTS SSD")
    cursor.execute("DROP TABLE IF EXISTS Memory")
    cursor.execute("DROP TABLE IF EXISTS HDD")
    cursor.execute("DROP TABLE IF EXISTS Cases")
    cursor.execute("DROP TABLE IF EXISTS Power")
    cursor.execute("DROP TABLE IF EXISTS cpuCooler")
    cursor.execute("DROP TABLE IF EXISTS caseCooler")
    cursor.execute("DROP TABLE IF EXISTS Price")
    cursor.execute("DROP TABLE IF EXISTS Website")
    cursor.execute("DROP TABLE IF EXISTS Maker")
    cursor.execute("DROP TABLE IF EXISTS GPU")

    print("start create tables")

    # Maker table
    cursor.execute("""CREATE TABLE Maker(
                        maker_id       INT not null,
                        maker_name     VARCHAR(50),
                        primary key(maker_id)
                    )""")

    # Website table
    cursor.execute("""CREATE TABLE Website(
                        web_id       INT not null,
                        web_name     VARCHAR(50),
                        primary key(web_id)
                    )""")
    cursor.execute("""INSERT INTO Website (web_id, web_name)
                        VALUES (201, 'dospara'),
                               (202, 'amazon'),
                               (203, 'kakaku'),
                               (204, 'sofmap')
                    """)

    #外部参照　参考ページ https://qiita.com/SLEAZOIDS/items/d6fb9c2d131c3fdd1387



    # Price table
    cursor.execute("""CREATE TABLE Price(
                        product_id     INT,
                        web_id         INT,
                        price          int,
                        status         varchar(20),
                        url            varchar(300),
                        constraint pk_price_product
                        primary key (product_id,web_id),
                        constraint fk_web_id
                        foreign key (web_id)
                        references Website (web_id)
                        ON UPDATE CASCADE
                    )""")
    #外部キー削除　ALTER TABLE テーブル名 DROP FOREIGN KEY 制約の名前(fk_web_id);

    # Cpu table

    cursor.execute("""CREATE TABLE Cpu(
                        product_id       INT auto_increment,
                        product_name     VARCHAR(200),
                        image            VARCHAR(300),
                        clock            varchar(10),
                        GEN              varchar(10),
                        multi_thread     varchar(10),
                        cache_2nd        varchar(25),
                        cache_3rd        varchar(25),
                        turbo_clock      varchar(10),
                        cores            varchar(3),
                        thread           varchar(3),
                        socket           varchar(20),
                        TDP              varchar(10),
                        constraint pk_cpu_product
                        primary key (product_id)
                    )auto_increment=10001""")


    # Motherboard table

    cursor.execute("""CREATE TABLE Motherboard(
                        product_id       INT auto_increment,
                        product_name     VARCHAR(200),
                        image            VARCHAR(300),
                        audio            VARCHAR(30),
                        chipset          varchar(20),
                        crossfire        varchar(8),
                        formfactor       varchar(10),
                        max_memory       varchar(10),
                        lan_speed        varchar(30),
                        memory_slot      varchar(2),
                        sata_slot        varchar(10),
                        memory_type      varchar(20),
                        Socket           varchar(15),
                        constraint pk_mother_product
                        primary key (product_id)
                    )auto_increment=20001""")


    # SSD table

    cursor.execute("""CREATE TABLE SSD(
                        product_id       INT auto_increment,
                        product_name     VARCHAR(200),
                        image            VARCHAR(300),
                        capacity         varchar(20),
                        interface        varchar(100),
                        speed_read       varchar(30),
                        speed_write      varchar(30),
                        constraint pk_ssd_product
                        primary key (product_id)
                    )auto_increment=30001""")


    # Memory table

    cursor.execute("""CREATE TABLE Memory(
                        product_id       INT auto_increment,
                        product_name     VARCHAR(200),
                        image            VARCHAR(300),
                        capacity         varchar(5),
                        interface        varchar(100),
                        piece            varchar(5),
                        mem_stndrd       varchar(20),
                        constraint pk_memory_product
                        primary key (product_id)
                    )auto_increment=40001""")

    # HDD table

    cursor.execute("""CREATE TABLE HDD(
                        product_id       INT auto_increment,
                        product_name     VARCHAR(200),
                        image            VARCHAR(300),
                        size             varchar(15),
                        capacity         varchar(10),
                        interface        varchar(15),
                        rpm              varchar(10),
                        thickness        varchar(10),
                        constraint pk_hdd_product
                        primary key (product_id)
                    )auto_increment=50001""")

    # Case table

    cursor.execute("""CREATE TABLE Cases(
                        product_id       INT auto_increment,
                        product_name     VARCHAR(200),
                        image            VARCHAR(300),
                        bay_cnt2_5       varchar(3),
                        bay_cnt3_5       varchar(3),
                        bay_cnt5_25      varchar(3),
                        factor_available varchar(50),
                        interface        varchar(100),
                        height           varchar(15),
                        weight           varchar(10),
                        width            varchar(10), 
                        constraint pk_case_product
                        primary key (product_id)
                    )auto_increment=60001""")

    # Power table

    cursor.execute("""CREATE TABLE Power(
                        product_id       INT auto_increment,
                        product_name     VARCHAR(200),
                        image            VARCHAR(300),
                        80PLUS           varchar(10),
                        capacity         varchar(10),
                        plugin_available varchar(8),
                        standard         varchar(15),
                        constraint pk_power_product
                        primary key (product_id)
                    )auto_increment=70001""")

    #cpuCooler  table

    cursor.execute("""CREATE TABLE cpuCooler(
                        product_id       INT auto_increment,
                        product_name     VARCHAR(200),
                        image            VARCHAR(300),
                        type             varchar(20),
                        thickness        varchar(5),
                        height           varchar(15),
                        socket           varchar(200),
                        width            varchar(5),
                        constraint pk_air_product
                        primary key (product_id)
                    )auto_increment=80001""")

    #caseCooler  table

    cursor.execute("""CREATE TABLE caseCooler(
                        product_id       INT auto_increment,
                        product_name     VARCHAR(200),
                        image            VARCHAR(300),
                        connector        varchar(10),
                        size             varchar(6),
                        led_writing      varchar(8),
                        noise            varchar(6),
                        max_rpm          varchar(15),
                        PWM              varchar(8),
                        constraint pk_cco_product
                        primary key (product_id)
                    )auto_increment=90001""")

    #GPU table

    cursor.execute("""CREATE TABLE GPU(
                        product_id       INT auto_increment,
                        product_name     VARCHAR(200),
                        image            VARCHAR(300),
                        cuda             varchar(10),
                        chip             varchar(50),
                        bus_interface    varchar(20),
                        mem_bus          varchar(10),
                        memory           varchar(20),
                        constraint pk_cco_product
                        primary key (product_id)
                    )auto_increment=11001""")
    
    print("end create tables")

    # 保存を実行
    connection.commit()

    # 接続を閉じる
    connection.close()