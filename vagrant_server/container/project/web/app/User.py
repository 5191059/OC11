
from flask_login import UserMixin

#データベースへの接続
from db import get_db

class User(UserMixin):
    def __init__(self, id_, name, email, profile_pic):
        self.id = id_
        self.name = name
        self.email = email
        self.profile_pic = profile_pic

    @staticmethod
    def get(user_id):
        con = get_db()
        db = con.cursor()
        sql = "SELECT * FROM Users WHERE user_id = %s"
        db.execute(sql, (user_id))
        user = db.fetchone()
        #fetchall()は多重　例 {{1:a},{2:b}}
        #fetchone()は１レコード　例 {1:a}
        if not user:
            return None

        
        user = User(
            id_=user['id'], name=user['name'], email=user['email'], profile_pic=user['profile_pic']
        )

        con.close()

        return user

    @staticmethod
    def create(id_, name, email, profile_pic):
        con = get_db()
        db = con.cursor()
        sql = "INSERT INTO Users (id, name, email, profile_pic) VALUES (%s, %s, %s, %s)"
        db.execute(sql, (id_, name, email, profile_pic))
        con.commit()
        con.close()