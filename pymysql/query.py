import pymysql

# connect = pymysql.connect(host="localhost",
#                        port=3306,
#                        user="root",
#                        password="12345678",
#                        database="Books")
# cursor = connect.cursor()
#
# cursor.execute("select version()")
#
# result = cursor.fetchall()
# print(result)
#
# cursor.close()
# connect.close()

connect = pymysql.connect(host="localhost",port=3306,user="root",password="12345678",database="Books")
cursor = connect.cursor()
cursor.execute("select id,title,`read`,`comment` from t_book;")
print(cursor.rownumber)
print(cursor.fetchone())
print(cursor.rownumber)
result = cursor.fetchall()
print(result)
print(cursor.rownumber)

result2 = cursor.fetchall()
print(result2)
# cursor.rownumber = 0
# result2 = cursor.fetchall()
print(cursor.rownumber)
print(result2)

# 1).连接到数据库(host:localhost user:root password:root database:books)
# 2).查询图书表的数据(包括:图书id、图书名称、阅读量、评论量) 3).获取查询结果的总记录数
# 4).获取查询结果的第一条数据
# 5).获取全部的查询结果

cursor.close()
connect.close()
