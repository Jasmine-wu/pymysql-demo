import pymysql
# 新增一条图书数据(id:4 title:西游记 pub_date:1986-01-01 )

try:
    cont = pymysql.connect(host="localhost", port=3306, user="root", password="12345678", database="Books",
                           autocommit=False)
    cursor = cont.cursor()
    sql = "insert into t_book(id,title,pub_date) values(4,'西游记','1986-01-01');"
    cursor.execute(sql)
    cont.commit()
except Exception as e:
    cont.rollback()
    print(e)
finally:
    if cursor:
        cursor.close()
    if cont:
        cont.close()

sql = "insert into t_book(id,title,pub_date) values(4,'西游记','1986-01-01');"

print(sql.split())