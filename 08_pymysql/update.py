import pymysql
cont = pymysql.connect(host="localhost", port=3306, user="root", password="12345678", database="Books",autocommit=True)
# cont.cursor()
cursor = cont.cursor()
# 更新[西游记]图书名称为(title:东游记)
sql = "update t_book set title='东游记' where title='西游记';"

cursor.execute(sql)
cursor.close()
cont.close()