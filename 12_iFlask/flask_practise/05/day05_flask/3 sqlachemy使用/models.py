



# 创建一个个类（继承谁？字段怎么写）
import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
# 字段和字段属性
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, UniqueConstraint, Index
from sqlalchemy.orm import relationship
# 制造了一个类，作为所有模型类的基类
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'  # 数据库表名称(固定写法)，如果不写，默认以类名小写作为表的名字
    id = Column(Integer, primary_key=True)  # id 主键
    # mysql中主键自动建索引：聚簇索引
    # 其他建建的索引叫：辅助索引
    name = Column(String(32), index=True, nullable=False)  # name列，索引，不可为空
    # email = Column(String(32), unique=True)  # 唯一
    # #datetime.datetime.now不能加括号，加了括号，以后永远是当前时间
    # ctime = Column(DateTime, default=datetime.datetime.now) # default默认值
    # extra = Column(Text, nullable=True)

    #类似于djagno的 Meta
    # __table_args__ = (
    #     UniqueConstraint('id', 'name', name='uix_id_name'), #联合唯一
    #     Index('ix_id_name', 'name', 'email'), #索引
    # )
    def __str__(self):
        return self.name
    def __repr__(self):
        # python是强类型语言
        return self.name+str(self.id)




# 一对多关系

# 一个Hobby可以有很多人喜欢
# 一个人只能由一个Hobby
class Hobby(Base):
    __tablename__ = 'hobby'
    id = Column(Integer, primary_key=True)
    caption = Column(String(50), default='篮球')


class Person(Base):
    __tablename__ = 'person'
    nid = Column(Integer, primary_key=True)
    name = Column(String(32), index=True, nullable=True)
    # hobby指的是tablename而不是类名，uselist=False
    # 一对多的关系，关联字段写在多的一方
    hobby_id = Column(Integer, ForeignKey("hobby.id"))  # 默认可以为空

    # 跟数据库无关，不会新增字段，只用于快速链表操作
    # 类名，backref用于反向查询
    hobby = relationship('Hobby', backref='pers')


# 多对多关系
# 实实在在存在的表
class Boy2Girl(Base):
    __tablename__ = 'boy2girl'
    id = Column(Integer, primary_key=True, autoincrement=True) # autoincrement自增，默认是True
    girl_id = Column(Integer, ForeignKey('girl.id'))
    boy_id = Column(Integer, ForeignKey('boy.id'))



class Girl(Base):
    __tablename__ = 'girl'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True, nullable=False)


class Boy(Base):
    __tablename__ = 'boy'

    id = Column(Integer, primary_key=True, autoincrement=True)
    hostname = Column(String(64), unique=True, nullable=False)

    # 与生成表结构无关，仅用于查询方便,放在哪个单表中都可以
    # secondary 通过哪个表建关联，跟django中的through一模一样
    girls = relationship('Girl', secondary='boy2girl', backref='boys')

# 创建表
def create_table():
    # 创建engine对象
    engine = create_engine(
        "mysql+pymysql://root:123@127.0.0.1:3306/aaa?charset=utf8",
        max_overflow=0,  # 超过连接池大小外最多创建的连接
        pool_size=5,  # 连接池大小
        pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
        pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
    )
    # 通过engine对象创建表
    Base.metadata.create_all(engine)

# 删除表
def drop_table():
    # 创建engine对象
    engine = create_engine(
        "mysql+pymysql://root:123@127.0.0.1:3306/aaa?charset=utf8",
        max_overflow=0,  # 超过连接池大小外最多创建的连接
        pool_size=5,  # 连接池大小
        pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
        pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
    )
    # 通过engine对象删除所有表
    Base.metadata.drop_all(engine)

if __name__ == '__main__':
    create_table()  # 原来已经存在user表，再执行一次不会有问题
    # drop_table()

# 创建库？手动创建库
# 问题，sqlachemy支持修改字段吗？不支持