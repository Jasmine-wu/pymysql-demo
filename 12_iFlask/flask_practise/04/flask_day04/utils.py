import pymysql
from pool import POOL


class SQLHelper(object):

    @staticmethod
    def open(cursor):
        conn = POOL.connection()
        # conn = pymysql.connect(host='127.0.0.1',
        #                        port=3306,
        #                        user='root',
        #                        password='123',
        #                        database='flask',
        #                        charset='utf8')
        cursor = conn.cursor(cursor=cursor)
        return conn, cursor

    @staticmethod
    def close(conn, cursor):
        conn.commit()
        cursor.close()
        conn.close()

    @classmethod
    def fetch_one(cls, sql, args, cursor=pymysql.cursors.DictCursor):
        conn, cursor = cls.open(cursor)
        cursor.execute(sql, args)
        obj = cursor.fetchone()
        cls.close(conn, cursor)
        return obj

    @classmethod
    def fetch_all(cls, sql, args, cursor=pymysql.cursors.DictCursor):
        conn, cursor = cls.open(cursor)
        cursor.execute(sql, args)
        obj = cursor.fetchall()
        cls.close(conn, cursor)
        return obj

    @classmethod
    def execute(cls, sql, args, cursor=pymysql.cursors.DictCursor):
        conn, cursor = cls.open(cursor)
        cursor.execute(sql, args)
        cls.close(conn, cursor)
