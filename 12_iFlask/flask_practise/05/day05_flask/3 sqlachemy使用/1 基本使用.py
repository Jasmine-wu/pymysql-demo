
import time
import threading
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine

# 第一步生成一个engine对象
engine = create_engine(
    "mysql+pymysql://root:123@127.0.0.1:3306/flask?charset=utf8",
    max_overflow=0,  # 超过连接池大小外最多创建的连接
    pool_size=5,  # 连接池大小
    pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
    pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
)
# 第二步：创建连接（执行原生sql）
conn = engine.raw_connection()
# 第三步：获取游标对象
cursor = conn.cursor()

# 第四步：具体操作
cursor.execute('select * from boy')

res=cursor.fetchall()
print(res)

# 比pymysql优势在，有数据库连接池