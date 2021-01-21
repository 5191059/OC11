from flask_login import UserMixin

#データベースへの接続
from db import get_db

def insert_product(product):
    print(product)
    con = get_db()
    db = con.cursor()
    sql = "INSERT INTO User_info (client, user_info) VALUES (%s, JSON_OBJECT(%s, JSON_OBJECT('product_name', %s, 'product_src', %s)))"
    db.execute(sql, (product[2] , product[2], product[0], product[1]))
    con.commit()
    con.close()


# def delete_product(product):
#     print(product)
#     con = get_db()
#     db = con.cursor()
#     sql = "UPDATE User_info SET user_info = json_merge( user_info,'{36711: %s }') where client = 36711;"
#     db.execute(sql, (36712 , product[0], product[1]))
#     con.commit()
#     con.close()