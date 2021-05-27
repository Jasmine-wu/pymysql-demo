
# pip install DBUtils
# import pymysql
# 数据库连接池的作用：maxconnections=6,不会一致性创建所有的连接，每次只创建6个
# from DBUtils.PooledDB import PooledDB
# import time
# from threading import Thread
# POOL = PooledDB(
#     creator=pymysql,  # 使用链接数据库的模块
#     maxconnections=6,  # 连接池允许的最大连接数，0和None表示不限制连接数
#     mincached=2,  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
#     maxcached=5,  # 链接池中最多闲置的链接，0和None不限制
#     maxshared=3,  # 链接池中最多共享的链接数量，0和None表示全部共享。PS: 无用，因为pymysql和MySQLdb等模块的 threadsafety都为1，所有值无论设置为多少，_maxcached永远为0，所以永远是所有链接都共享。
#     blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
#     maxusage=None,  # 一个链接最多被重复使用的次数，None表示无限制
#     setsession=[],  # 开始会话前执行的命令列表。
#     ping=0,
#     # ping MySQL服务端，检查是否服务可用。
#     host='127.0.0.1',
#     port=3306,
#     user='root',
#     password='123',
#     database='flask',
#     charset='utf8'
# )
#
#
# def func():
#     # 检测当前正在运行连接数的是否小于最大链接数，如果不小于则：等待或报raise TooManyConnections异常
#     # 否则
#     # 则优先去初始化时创建的链接中获取链接 SteadyDBConnection。
#     # 然后将SteadyDBConnection对象封装到PooledDedicatedDBConnection中并返回。
#     # 如果最开始创建的链接没有链接，则去创建一个SteadyDBConnection对象，再封装到PooledDedicatedDBConnection中并返回。
#     # 一旦关闭链接后，连接就返回到连接池让后续线程继续使用。
#     conn = POOL.connection()
#
#     # print(th, '链接被拿走了', conn1._con)
#     # print(th, '池子里目前有', pool._idle_cache, '\r\n')
#
#     cursor = conn.cursor()
#     cursor.execute('select * from boy')
#     result = cursor.fetchall()
#     time.sleep(2)
#     print(result)
#     conn.close()

# 数据库连接池的作用：maxconnections=6,不会一致性创建所有的连接，每次只创建6个
# if __name__ == '__main__':
#     for i in range(10):
#         t=Thread(target=func)
#         t.start()



# import pymysql
# from settings import Config
# class SQLHelper(object):
#
#     @staticmethod
#     def open(cursor):
#         POOL = Config.PYMYSQL_POOL
#         conn = POOL.connection()
#         cursor = conn.cursor(cursor=cursor)
#         return conn,cursor
#
#     @staticmethod
#     def close(conn,cursor):
#         conn.commit()
#         cursor.close()
#         conn.close()
#
#     @classmethod
#     def fetch_one(cls,sql,args,cursor =pymysql.cursors.DictCursor):
#         conn,cursor = cls.open(cursor)
#         cursor.execute(sql, args)
#         obj = cursor.fetchone()
#         cls.close(conn,cursor)
#         return obj
#
#     @classmethod
#     def fetch_all(cls,sql, args,cursor =pymysql.cursors.DictCursor):
#         conn, cursor = cls.open(cursor)
#         cursor.execute(sql, args)
#         obj = cursor.fetchall()
#         cls.close(conn, cursor)
#         return obj
#     @classmethod
#     def execute(cls,sql, args,cursor =pymysql.cursors.DictCursor):
#         conn, cursor = cls.open(cursor)
#         cursor.execute(sql, args)
#         cls.close(conn, cursor)