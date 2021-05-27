from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import User,Person,Hobby
from sqlalchemy.sql import text
engine = create_engine("mysql+pymysql://root:123@127.0.0.1:3306/aaa", max_overflow=0, pool_size=5)
Session = sessionmaker(bind=engine)
session=Session()


# 1 查询名字为lqz的所有user对象
# ret = session.query(User).filter_by(name='ccc099').all()
# 2 表达式，and条件连接
# ret = session.query(User).filter(User.id > 1, User.name == 'egon').all()
# 查找id在1和10之间，并且name=egon的对象
# ret = session.query(User).filter(User.id.between(1, 10), User.name == 'egon').all()

# in条件(class_,因为这是关键字，不能直接用)
# ret = session.query(User).filter(User.id.in_([1,3,4])).all()

# 取反 ~
ret = session.query(User).filter(~User.id.in_([1,3,4])).all()

#二次筛选
# select *
# ret = session.query(User).filter(User.id.in_(session.query(User.id).filter_by(name='egon'))).all()
# # select name，id 。。。。
# ret = session.query(User.id,User.name).filter(User.id.in_(session.query(User.id).filter_by(name='egon'))).all()

'''
SELECT users.id AS users_id, users.name AS users_name 
FROM users 
WHERE users.id IN (SELECT users.id AS users_id 
FROM users 
WHERE users.name = %(name_1)s)

'''


#
from sqlalchemy import and_, or_
#or_包裹的都是or条件，and_包裹的都是and条件
#查询id>3并且name=egon的人
# ret = session.query(User).filter(and_(User.id > 3, User.name == 'egon')).all()

# 查询id大于2或者name=ccc099的数据
# ret = session.query(User).filter(or_(User.id > 2, User.name == 'ccc099')).all()
# ret = session.query(User).filter(
#     or_(
#         User.id < 2,
#         and_(User.name == 'egon', User.id > 3),
#         User.extra != ""
#     )).all()
# print(ret)

'''
select *from user where id<2 or (name=egon and id >3) or extra !=''
'''


# 通配符，以e开头，不以e开头
# ret = session.query(User).filter(User.name.like('e%')).all()
# ret = session.query(User).filter(~User.name.like('e%')).all()

# 限制，用于分页，区间 limit
# 前闭后开区间，1能取到，3取不到
ret = session.query(User)[1:3]

'''
select * from users limit 1,2;
'''


# 排序，根据name降序排列（从大到小）
# ret = session.query(User).order_by(User.name.desc()).all()
# ret = session.query(User).order_by(User.name.asc()).all()
#第一个条件降序排序后，再按第二个条件升序排
# ret = session.query(User).order_by(User.id.asc(),User.name.desc()).all()
# ret = session.query(User).order_by(User.name.desc(),User.id.asc()).all()


# 分组
from sqlalchemy.sql import func

# ret = session.query(User).group_by(User.name).all()
#分组之后取最大id，id之和，最小id
# sql 分组之后，要查询的字段只能有分组字段和聚合函数
# ret = session.query(
#     func.max(User.id),
#     func.sum(User.id),
#     func.min(User.id),
#     User.name).group_by(User.name).all()
# '''
# select max(id),sum(id),min(id) from user group by name;
#
# '''
# for obj in ret:
#     print(obj[0],'----',obj[1],'-----',obj[2],'-----',obj[3])
# print(ret)

#haviing筛选
# ret = session.query(
#     func.max(User.id),
#     func.sum(User.id),
#     func.min(User.id)).group_by(User.name).having(func.min(User.id) >2).all()

'''
select max(id),sum(id),min(id) from user group by name having min(id)>2;

'''
print(ret)
session.commit()

session.close()
