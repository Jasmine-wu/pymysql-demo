from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import User,Person,Hobby,Boy,Girl,Boy2Girl
from sqlalchemy.sql import text
engine = create_engine("mysql+pymysql://root:123@127.0.0.1:3306/aaa", max_overflow=0, pool_size=5)
Session = sessionmaker(bind=engine)
session=Session()



###  1 一对多插入数据
# obj=Hobby(caption='足球')
# session.add(obj)
# p=Person(name='张三',hobby_id=2)
# session.add(p)
### 2 方式二(默认情况传对象有问题)
###### Person表中要加 hobby = relationship('Hobby', backref='pers')
# p=Person(name='李四',hobby=Hobby(caption='美女'))
# 等同于
# p=Person(name='李四2')
# p.hobby=Hobby(caption='美女2')
# session.add(p)

## 3 方式三，通过反向操作
# hb = Hobby(caption='人妖')
# hb.pers = [Person(name='文飞'), Person(name='博雅')]
# session.add(hb)


#### 4 查询（查询：基于连表的查询，基于对象的跨表查询）
### 4.1 基于对象的跨表查询(子查询，两次查询)
# 正查
# p=session.query(Person).filter_by(name='张三').first()
# print(p)
# print(p.hobby.caption)
# 反查
# h=session.query(Hobby).filter_by(caption='人妖').first()
# print(h.pers)

### 4.2 基于连表的跨表查（查一次）
# 默认根据外键连表
# isouter=True 左外连，表示Person left join Hobby，没有右连接，反过来即可
# 不写 inner join
# person_list=session.query(Person,Hobby).join(Hobby,isouter=True).all()
# print(person_list)
# print(person_list)
# for row in person_list:
#     print(row[0].name,row[1].caption)

# '''
# select * from person left join hobby on person.hobby_id=hobby.id
# '''
#
# ret = session.query(Person, Hobby).filter(Person.hobby_id == Hobby.id)
# print(ret)
# '''
# select * from user,hobby where user.id=favor.nid;
#
# '''


#join表，默认是inner join
# ret = session.query(Person).join(Hobby)
# # ret = session.query(Hobby).join(Person,isouter=True)
# '''
# SELECT *
# FROM person INNER JOIN hobby ON hobby.id = person.hobby_id
# '''
# print(ret)


# 指定连表字段（从来没用过）
# ret = session.query(Person).join(Hobby,Person.nid==Hobby.id, isouter=True)
# # ret = session.query(Person).join(Hobby,Person.hobby_id==Hobby.id, isouter=True).all()
# print(ret)
'''
SELECT *
FROM person LEFT OUTER JOIN hobby ON person.nid = hobby.id

'''

# print(ret)




# 组合（了解）UNION 操作符用于合并两个或多个 SELECT 语句的结果集
# union和union all的区别？
# q1 = session.query(User.name).filter(User.id > 2)  # 6条数据
# q2 = session.query(User.name).filter(User.id < 8) # 2条数据


# q1 = session.query(User.id,User.name).filter(User.id > 2)  # 6条数据
# q2 = session.query(User.id,User.name).filter(User.id < 8) # 2条数据
# ret = q1.union_all(q2).all()
# ret1 = q1.union(q2).all()
# print(ret)
# print(ret1)
#
# q1 = session.query(User.name).filter(User.id > 2)
# q2 = session.query(Hobby.caption).filter(Hobby.nid < 2)
# ret = q1.union_all(q2).all()







#### 多对多

# session.add_all([
#     Boy(hostname='霍建华'),
#     Boy(hostname='胡歌'),
#     Girl(name='刘亦菲'),
#     Girl(name='林心如'),
# ])
# session.add_all([
#     Boy2Girl(girl_id=1, boy_id=1),
#     Boy2Girl(girl_id=2, boy_id=1)
# ])


##### 要有girls = relationship('Girl', secondary='boy2girl', backref='boys')
# girl = Girl(name='张娜拉')
# girl.boys = [Boy(hostname='张铁林'),Boy(hostname='费玉清')]
# session.add(girl)

# boy=Boy(hostname='蔡徐坤')
# boy.girls=[Girl(name='谢娜'),Girl(name='巧碧螺')]
# session.add(boy)
# session.commit()


# 基于对象的跨表查

# girl=session.query(Girl).filter_by(id=3).first()
# print(girl.boys)

#### 基于连表的跨表查询

# 查询蔡徐坤约过的所有妹子
'''
select girl.name from girl,boy,Boy2Girl where boy.id=Boy2Girl.boy_id and girl.id=Boy2Girl.girl_id where boy.name='蔡徐坤'

'''
# ret=session.query(Girl.name).filter(Boy.id==Boy2Girl.boy_id,Girl.id==Boy2Girl.girl_id,Boy.hostname=='蔡徐坤').all()

'''
select girl.name from girl inner join Boy2Girl on girl.id=Boy2Girl.girl_id inner join boy on boy.id=Boy2Girl.boy_id where boy.hostname='蔡徐坤'

'''
# ret=session.query(Girl.name).join(Boy2Girl).join(Boy).filter(Boy.hostname=='蔡徐坤').all()
ret=session.query(Girl.name).join(Boy2Girl).join(Boy).filter_by(hostname='蔡徐坤').all()
print(ret)


### 执行原生sql（用的最多的）
### django中orm如何执行原生sql
#
# cursor = session.execute('insert into users(name) values(:value)',params={"value":'xxx'})
# print(cursor.lastrowid)
# session.commit()

session.close()
