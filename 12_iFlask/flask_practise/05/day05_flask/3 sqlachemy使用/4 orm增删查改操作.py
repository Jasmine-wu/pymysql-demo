from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import User,Person,Hobby
from sqlalchemy.orm import scoped_session
from sqlalchemy.sql import text
engine = create_engine("mysql+pymysql://root:123@127.0.0.1:3306/aaa", max_overflow=0, pool_size=5)

Session = sessionmaker(bind=engine)
session = scoped_session(Session)
# session=Session()

####1 新增多个对象
# obj=User(name='xxx')
# obj2=User(name='yyyy')
# obj3=User(name='zzz')
#新增同样对象
# session.add_all([obj,obj2,obj3])
#新增不同对象
# session.add_all([Person(name='lqz'),Hobby()])
####2 简单删除（查到删除）
# res=session.query(User).filter_by(name='2008').delete()
# res=session.query(User).filter(User.id>=2).delete()
# # 影响1行
# print(res)

#### 3 修改
# res=session.query(User).filter_by(id=1).update({User.name:'ccc'})
# res=session.query(User).filter_by(id=1).update({'name':'ccc'})

# session.query(User).filter(User.id > 0).update({User.name: User.name + "099"}, synchronize_session=False) # 如果要把它转成字符串相加
# session.query(User).filter(User.id > 0).update({"age": User.age + 1}, synchronize_session="evaluate")  ## 如果要把它转成数字相加


####4 基本查询操作

# res=session.query(User).all()
# print(type(res))
# res=session.query(User).first()
# print(res)

#filter传的是表达式，filter_by传的是参数
# res=session.query(User).filter(User.id==1).all()
# res=session.query(User).filter(User.id>=1).all()
# res=session.query(User).filter(User.id<1).all()

# res=session.query(User).filter_by(name='ccc099').all()


#了解
# res = session.query(User).from_statement(text("SELECT * FROM users where name=:name")).params(name='ccc099').all()
# print(res)


session.commit()
# 并没有真正关闭连接，而是放回池中
session.close()
