
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import User  # pycharm报错，不会影响我们


# 1 制作engine
engine = create_engine("mysql+pymysql://root:123@127.0.0.1:3306/aaa", max_overflow=0, pool_size=5)

# 2 制造一个 session 类（会话）
Session = sessionmaker(bind=engine)    # 得到一个类
# 3 得到一个session对象
session=Session()  # 得到一个session对象
# conn=Session()


# 4 创建一个对象
obj1 = User(name="lqz")
# 5 把对象通过add放入
session.add(obj1)
# 6 提交
session.commit()