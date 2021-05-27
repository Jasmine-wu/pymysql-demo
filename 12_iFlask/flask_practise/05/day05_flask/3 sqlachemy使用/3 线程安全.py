


from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import User  # pycharm报错，不会影响我们
from sqlalchemy.orm import scoped_session

# 1 制作engine
engine = create_engine("mysql+pymysql://root:123@127.0.0.1:3306/aaa", max_overflow=0, pool_size=5)

# 2 制造一个 session 类（会话）
Session = sessionmaker(bind=engine)    # 得到一个类
# 3 得到一个session对象（线程安全的session）
#
#为什么线程安全，还是用的local
#线程安全：方案1:加锁 ，方案2：放到local里

# session是全局的，来一个请求开一个线程，1w个请求共用一个session对象，性能会更不上
# session放请求内，来一个请求创建一个session,1w个请求1w的session对象，也不好(单例多了，性能也不好)
# 解决方法：线程安全session:scoped_session, 现在的session已经不是session对象了,没有add，commit，close等方法，所有pycharm会报错
# 问题：那为什么可以调用add，commit,close等方法，这是如何实现的？
session = scoped_session(Session)

# session=Session()

# 4 创建一个对象
obj1 = User(name="2008")
# 5 把对象通过add放入
session.add(obj1)
# session.aaa()
# 6 提交
session.commit()
session.close()


# 类不继承Session类，但是有该类的所有方法（通过反射，一个个放进去）

# scoped_session.add------->instrument(name)--->do函数内存地址---》现在假设我要这么用：session.add()--->do()
# scoped_session.close----->instrument(name)--->do函数内存地址